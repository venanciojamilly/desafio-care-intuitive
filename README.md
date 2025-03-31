# README - Sistema de Processamento de Dados ANS

## Visão Geral

Este projeto contém um conjunto de scripts Python para coleta, processamento e análise de dados da Agência Nacional de Saúde Suplementar (ANS), com automação via Makefile.

## Estrutura do Projeto

```
DESAFIO-CARE-INTUITIVE/
├── scripts/
│   ├── web-scraping.py         # Coleta de dados
│   └── data-transformacao.py   # Processamento de dados
├── venv/                       # Ambiente virtual Python
├── Makefile                    # Automação de tarefas
├── requirements.txt            # Dependências do projeto
└── README.md                   # Documentação
```

## Funcionamento dos Scripts

### 1. Web Scraping (`web-scraping.py`)

**Objetivo**: Coletar automaticamente os arquivos PDF da ANS.

**Fluxo de execução**:
1. Acessa o portal da ANS
2. Identifica os links dos Anexos I e II
3. Faz download dos arquivos PDF
4. Compacta os arquivos em um ZIP único

**Como executar**:
```bash
make webscraping
```

**Saída esperada**:
- Arquivos PDF baixados na pasta raiz
- Arquivo `Anexos_ANS.zip` contendo os PDFs

### 2. Transformação de Dados (`data-transformacao.py`)

**Objetivo**: Processar os arquivos coletados e gerar saídas estruturadas.

**Fluxo de execução**:
1. Lê o arquivo PDF do Anexo I
2. Extrai as tabelas de procedimentos
3. Transforma os dados em formato estruturado (CSV)
4. Substitui abreviações pelos valores completos
5. Gera arquivo compactado com os resultados

**Como executar**:
```bash
make transformacao
```

**Saída esperada**:
- Arquivo `Rol_Procedimentos.csv` com os dados estruturados
- Arquivo `Teste_[Nome].zip` contendo o CSV

## Makefile - Automação de Tarefas

O Makefile fornece atalhos para todas as operações:

| Comando          | Função                                                                 |
|------------------|-----------------------------------------------------------------------|
| `make install`   | Cria ambiente virtual e instala dependências                          |
| `make webscraping` | Executa apenas o script de web scraping                              |
| `make transformacao` | Executa apenas o script de transformação de dados                   |
| `make clean`     | Remove arquivos temporários, downloads e o ambiente virtual          |

**Fluxo completo recomendado**:
```bash
make install       # Primeira vez
make webscraping   # Coletar dados
make transformacao # Processar dados
```

## Configuração do Ambiente

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd DESAFIO-CARE-INTUITIVE
```

2. Configure o ambiente:
```bash
make install
```

3. Ative o ambiente virtual (quando necessário):
```bash
source venv/bin/activate
```

## Dependências

Todas as dependências estão listadas em `requirements.txt` e incluem:
- requests (para downloads)
- beautifulsoup4 (para parsing HTML)
- pandas (para manipulação de dados)
- pdfplumber (para extração de PDFs)

## Limpeza

Para remover todos os arquivos gerados e o ambiente virtual:
```bash
make clean
```

## Observações Importantes

1. Verifique se os arquivos PDF estão presentes antes de executar a transformação
2. O script de transformação espera o arquivo exato "Anexo_I_Rol_*.pdf"
3. Para problemas de encoding, verifique o arquivo PDF original