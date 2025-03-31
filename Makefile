# Configurações
VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MAIN_SCRIPT = src/main.py

.PHONY: help venv install run clean

help:
	@echo "Comandos disponíveis:"
	@echo "  make venv      - Cria o ambiente virtual"
	@echo "  make install   - Instala as dependências"
	@echo "  make run       - Executa o script principal"
	@echo "  make clean     - Remove o ambiente virtual"
	@echo "  make all       - Configura tudo (venv + instalação)"
all: setup run

setup:
	@echo "🛠️ Criando ambiente virtual..."
	python3 -m venv $(VENV)
	@echo "⚙️ Instalando dependências..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Configuração completa!"

# Apenas instala dependências
install:
	@echo "📦 Instalando/atualizando dependências..."
	$(PIP) install -r requirements.txt

# Executa o programa principal
run:
	@echo "🚀 Executando script principal..."
	$(PYTHON) $(MAIN_SCRIPT)

# Limpeza
clean:
	@echo "🧹 Limpando ambiente..."
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -f *.zip *.pdf
	@echo "⚠️  Use 'make nuke' para remover o venv também"

# Limpeza completa (incluindo venv)
nuke: clean
	@echo "💥 Removendo ambiente virtual..."
	rm -rf $(VENV)
