import os
import zipfile
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pdfplumber

def get_pdf_links(url):
    """Obtém os links dos Anexos I e II da página"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        pdf_links = []
        for link in soup.find_all('a', href=True):
            if 'Anexo I' in link.text or 'Anexo II' in link.text:
                pdf_links.append(link['href'])
        
        return pdf_links
    
    except requests.RequestException as e:
        print(f"Erro ao acessar a página: {e}")
        return []

def download_pdfs(pdf_links):
    """Faz o download dos arquivos PDF"""
    downloaded_files = []
    
    for pdf_url in pdf_links:
        try:
            file_name = pdf_url.split('/')[-1]
            response = requests.get(pdf_url)
            response.raise_for_status()
            
            with open(file_name, 'wb') as file:
                file.write(response.content)
            downloaded_files.append(file_name)
            print(f"Download concluído: {file_name}")
            
        except requests.RequestException as e:
            print(f"Erro ao baixar {pdf_url}: {e}")
    
    return downloaded_files

def extract_table_from_pdf(pdf_path):
    """Extrai tabelas do PDF e retorna um DataFrame."""
    all_tables = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    if table:  # Verifica se a tabela não está vazia
                        df = pd.DataFrame(table[1:], columns=table[0])  # Usa primeira linha como cabeçalho
                        all_tables.append(df)
        
        if not all_tables:
            print("Nenhuma tabela encontrada no PDF.")
            return None
        
        return pd.concat(all_tables, ignore_index=True)
    
    except Exception as e:
        print(f"Erro ao extrair tabelas do PDF: {e}")
        return None

def clean_and_save_csv(df, csv_filename):
    """Limpa os dados e salva em um arquivo CSV."""
    try:
        # Substitui abreviações nas colunas
        df = df.rename(columns={
            "OD": "Odontologia",
            "AMB": "Ambulatorial"
        })
        
        # Remove linhas vazias ou inválidas
        df = df.dropna(how='all')
        
        df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
        print(f"Arquivo CSV salvo: {csv_filename}")
        return True
    except Exception as e:
        print(f"Erro ao salvar CSV: {e}")
        return False

def zip_file(file_name, zip_name):
    """Compacta o arquivo CSV em um ZIP."""
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            zipf.write(file_name)
        print(f"Arquivo ZIP criado: {zip_name}")
        return True
    except Exception as e:
        print(f"Erro ao criar arquivo ZIP: {e}")
        return False

def main():
    # Configurações
    target_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    your_name = "Anexo_I"  # Substitua pelo seu nome
    
    print("1. Obtendo links dos PDFs...")
    pdf_links = get_pdf_links(target_url)
    
    if not pdf_links:
        print("Nenhum link válido encontrado. Verifique a página.")
        return
    
    print("\n2. Baixando arquivos PDF...")
    downloaded_files = download_pdfs(pdf_links)
    
    if not downloaded_files:
        print("Nenhum arquivo foi baixado.")
        return
    
    # Encontra o arquivo do Anexo I (assumindo que contém "Anexo I" no nome)
    anexo_i_pdf = next((f for f in downloaded_files if "Anexo_I" in f), None)
    
    if not anexo_i_pdf:
        print("Arquivo do Anexo I não encontrado nos downloads.")
        return
    
    print(f"\n3. Extraindo dados do PDF: {anexo_i_pdf}")
    df = extract_table_from_pdf(anexo_i_pdf)
    
    if df is None:
        print("Falha ao extrair dados do PDF.")
        return
    
    csv_filename = "Rol_Procedimentos.csv"
    zip_filename = f"Teste_{your_name}.zip"
    
    print("\n4. Salvando dados em CSV...")
    if not clean_and_save_csv(df, csv_filename):
        return
    
    print("\n5. Compactando CSV...")
    if zip_file(csv_filename, zip_filename):
        # Remove o CSV após compactar (opcional)
        try:
            os.remove(csv_filename)
        except:
            pass
        
        print("\nProcesso concluído com sucesso!")

if __name__ == "__main__":
    main()