VENV = venv
PYTHON = $(VENV)/bin/python
SCRIPTS = scripts/
DB-TEST = db-test/
SERVER = api/

.PHONY: help install clean webscraping transformacao prep-bd run-flask

help:
	@echo "Comandos disponíveis:"
	@echo "  make install       - Instala dependências"
	@echo "  make webscraping   - Executa web scraping"
	@echo "  make transformacao - Processa dados"
	@echo "  make clean         - Limpa ambiente"

install:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

webscraping:
	@echo "Executando web scraping..."
	$(PYTHON) $(SCRIPTS)web-scraping.py

transformacao:
	@echo "Executando transformação de dados..."
	$(PYTHON) $(SCRIPTS)data-transformacao.py

prep-bd:
	@echo "Preparando dados"
	$(PYTHON) $(DB-TEST)prep-task.py 

run-flask:
	@echo "Rodando Server flask"
	$(PYTHON) $(SERVER)server.py

clean:
	rm -rf $(VENV)
	rm -rf downloads
	rm -f *.zip *.pdf *.csv *.xlsx
	rm -rf __pycache__