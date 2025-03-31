import os
import requests
from bs4 import BeautifulSoup

def get_latest_files(base_url, keyword, years=2):
    """Obtém os links dos arquivos dos últimos anos com base em uma palavra-chave."""
    response = requests.get(base_url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [base_url + '/' + a['href'] for a in soup.find_all('a', href=True) if keyword in a['href']]
    
    # Filtrar pelos últimos anos
    links = sorted(links, reverse=True)[:years]
    return links

def download_files(file_links, download_dir):
    """Faz o download dos arquivos."""
    os.makedirs(download_dir, exist_ok=True)
    
    for file_url in file_links:
        file_name = os.path.join(download_dir, file_url.split('/')[-1])
        response = requests.get(file_url)
        
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Download concluído: {file_name}")

# URLs base
base_url_demonstracoes = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis"
base_url_operadoras = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas"

demonstracoes_links = get_latest_files(base_url_demonstracoes, "zip", years=2)
operadoras_links = get_latest_files(base_url_operadoras, "csv", years=1)

download_files(demonstracoes_links, "downloads/demonstracoes_contabeis")
download_files(operadoras_links, "downloads/operadoras")
