VENV = venv
PYTHON = $(VENV)/bin/python
SCRIPTS = scripts/

.PHONY: help install clean webscraping transformacao

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

clean:
	rm -rf $(VENV)
	rm -f *.zip *.pdf *.csv *.xlsx
	rm -rf __pycache__