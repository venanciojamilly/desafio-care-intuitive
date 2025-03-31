# README - Testes de Nivelamento v.250321

Este documento descreve uma série de testes de nivelamento divididos em quatro categorias principais: Web Scraping, Transformação de Dados, Banco de Dados e API. Cada teste possui requisitos específicos e deve ser realizado utilizando as tecnologias indicadas.

---

## **1. Teste de Web Scraping**
**Objetivo:** Acessar um site, baixar arquivos PDF e compactá-los.  
**Linguagens:** Python ou Java.  

### Tarefas:
1. Acessar o site:  
   [https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)  
2. Fazer o download dos Anexos I e II em formato PDF.  
3. Compactar todos os anexos em um único arquivo (ZIP, RAR, etc.).  

---

## **2. Teste de Transformação de Dados**
**Objetivo:** Extrair dados de um PDF, salvá-los em formato CSV e realizar transformações.  
**Linguagens:** Python ou Java.  

### Tarefas:
1. Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do Anexo I (todas as páginas).  
2. Salvar os dados em uma tabela estruturada no formato CSV.  
3. Compactar o CSV em um arquivo denominado `Teste_(seu_nome).zip`.  
4. Substituir as abreviações das colunas OD e AMB pelas descrições completas (conforme legenda no rodapé).  

---

## **3. Teste de Banco de Dados**
**Objetivo:** Criar scripts SQL para estruturar e analisar dados de operadoras de saúde.  
**Bancos de Dados:** MySQL 8 ou PostgreSQL >10.0.  

### Tarefas de Preparação:
1. Baixar os arquivos dos últimos 2 anos do repositório público:  
   [https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)  
2. Baixar os dados cadastrais das operadoras ativas em CSV:  
   [https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)  

### Tarefas de Código:
1. Criar queries para estruturar tabelas necessárias para o arquivo CSV.  
2. Elaborar queries para importar o conteúdo dos arquivos, considerando o encoding correto.  
3. Desenvolver queries analíticas para responder:  
   - Quais são as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?  
   - Quais são as 10 operadoras com maiores despesas nessa categoria no último ano?  

---

## **4. Teste de API**
**Objetivo:** Desenvolver uma interface web com Vue.js e um servidor em Python para busca textual.  

### Tarefas de Preparação:
1. Utilizar o CSV do item 3.2 (dados cadastrais das operadoras ativas).  

### Tarefas de Código:
1. Criar um servidor com uma rota que realize uma busca textual na lista de cadastros de operadoras e retorne os registros mais relevantes.  
2. Elaborar uma coleção no Postman para demonstrar o resultado.  

---

## **Instruções Gerais**
- Para cada teste, siga as especificações de linguagem e formato de saída.  
- Certifique-se de que os arquivos gerados estejam corretamente nomeados e compactados.  
- No caso do Teste de Banco de Dados, atente-se ao encoding dos arquivos durante a importação.  
- Para o Teste de API, utilize Vue.js para o frontend e Python para o backend.  

**Boa sorte!** 🚀
