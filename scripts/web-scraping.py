import requests
from bs4 import BeautifulSoup
import zipfile
import os

def get_pdf_links(url):
    """Obtém os links dos Anexos I e II da página"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica erros HTTP
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

def create_zip(downloaded_files, zip_name='Anexos_ANS.zip'):
    """Compacta os arquivos em um ZIP e remove os originais"""
    try:
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            for file in downloaded_files:
                zipf.write(file)
                os.remove(file)
        print(f"Arquivo compactado criado: {zip_name}")
        return True
    
    except Exception as e:
        print(f"Erro ao criar arquivo ZIP: {e}")
        return False

def main():
    # URL a ser acessada
    target_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    
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
    
    print("\n3. Criando arquivo compactado...")
    success = create_zip(downloaded_files)
    
    if success:
        print("\nProcesso concluído com sucesso!")
    else:
        print("\nOcorreu um erro na compactação.")

if __name__ == "__main__":
    main()