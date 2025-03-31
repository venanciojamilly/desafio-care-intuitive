from flask import Flask, request, jsonify
import pandas as pd
from fuzzywuzzy import fuzz, process

app = Flask(__name__)

# Carregar os dados do CSV com tratamento adequado
try:
    # Tentar detectar automaticamente o encoding e separador
    df = pd.read_csv('downloads/operadoras/Relatorio_cadop.csv', 
                    sep=';', 
                    encoding='ISO-8859-1',
                    on_bad_lines='skip')
    
    # Normalizar nomes de colunas (remove espaços e acentos)
    df.columns = df.columns.str.strip().str.upper()
    df.columns = df.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    
    # Verificar colunas necessárias
    required_columns = {'REGISTRO ANS', 'CNPJ', 'RAZAO SOCIAL', 'NOME FANTASIA'}
    if not required_columns.issubset(df.columns):
        missing = required_columns - set(df.columns)
        raise ValueError(f"Colunas faltando no CSV: {missing}")

except Exception as e:
    print(f"Erro ao carregar CSV: {str(e)}")
    df = pd.DataFrame()  # DataFrame vazio para evitar erros

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    if df.empty:
        return jsonify({"error": "Dados não carregados corretamente"}), 500

    query = request.args.get('q', '').strip()
    limit = int(request.args.get('limit', 10))
    
    if not query:
        return jsonify({"error": "Parâmetro 'q' é obrigatório"}), 400
    
    try:
        # Função para calcular similaridade
        def calculate_similarity(row):
            text = f"{row['RAZAO SOCIAL']} {row['NOME FANTASIA']}"
            return fuzz.partial_ratio(query.lower(), text.lower())
        
        # Aplicar a função e ordenar
        df['similarity'] = df.apply(calculate_similarity, axis=1)
        results = df.sort_values('similarity', ascending=False).head(limit)
        
        # Converter para formato JSON
        return jsonify({
            "query": query,
            "results": results.drop('similarity', axis=1).rename(columns={
                'REGISTRO ANS': 'registro_ans',
                'RAZAO SOCIAL': 'razao_social',
                'NOME FANTASIA': 'nome_fantasia'
            }).to_dict(orient='records')
        })
    
    except Exception as e:
        return jsonify({
            "error": f"Erro ao processar busca: {str(e)}",
            "available_columns": list(df.columns)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)