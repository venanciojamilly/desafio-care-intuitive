-- criar tabela para armazenar os dados das operadoras
CREATE TABLE operadoras_ativas (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(10) UNIQUE NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(50),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_de_comercializacao TEXT,
    data_registro DATE
);

-- criar tabela para armazenar demonstrações contábeis
CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(10) REFERENCES operadoras_ativas(registro_ans),
    ano INT NOT NULL,
    trimestre INT NOT NULL,
    receita_total NUMERIC(18,2),
    despesas_eventos_saude NUMERIC(18,2),
    despesas_administrativas NUMERIC(18,2)
);

-- carregar os dados do CSV das operadoras ativas
COPY operadoras_ativas(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, uf, data_registro)
FROM 'downloads/operadoras/Relatorio_cadop.csv'
DELIMITER ',' CSV HEADER ENCODING 'UTF8';

-- carregar os dados do CSV de demonstrações contábeis
COPY demonstracoes_contabeis(registro_ans, ano, trimestre, receita_total, despesas_eventos_saude, despesas_administrativas)
FROM 'downloads/operadoras/Relatorio_cadop.csv'
DELIMITER ',' CSV HEADER ENCODING 'UTF8';

-- Top 10 operadoras com maiores despesas em eventos de saúde no último trimestre
SELECT o.razao_social, d.ano, d.trimestre, d.despesas_eventos_saude
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE (d.ano, d.trimestre) = (
    SELECT ano, MAX(trimestre)
    FROM demonstracoes_contabeis
    WHERE ano = (SELECT MAX(ano) FROM demonstracoes_contabeis)
)
ORDER BY d.despesas_eventos_saude DESC
LIMIT 10;

-- Top 10 operadoras com maiores despesas em eventos de saúde no último ano
SELECT o.razao_social, d.ano, SUM(d.despesas_eventos_saude) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras_ativas o ON d.registro_ans = o.registro_ans
WHERE d.ano = (SELECT MAX(ano) FROM demonstracoes_contabeis)
GROUP BY o.razao_social, d.ano
ORDER BY total_despesas DESC
LIMIT 10;
