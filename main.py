import pandas as pd
import numpy as np

# passo 1 - importar a base de dados
tabela = pd.read_csv('dados_baguncados.csv')

# passo 2 - padronização de colunas

tabela.columns = tabela.columns.str.lower().str.strip()

# passo 3 - remover linhas duplicadas
tabela = tabela.drop_duplicates()

# passo 4 - remover colunas vazias
tabela = tabela.dropna(how='all', axis=1)

# passo 5 - tratar os tipos de dados
tabela['data_venda'] = pd.to_datetime(tabela['data_venda'], errors='coerce')

# passo 6 - tratar linhas com valores vazios
tabela['quantidade'] = pd.to_numeric(tabela['quantidade'], errors='coerce')
tabela['quantidade'] = tabela['quantidade'].fillna(tabela['quantidade'].median())
tabela['quantidade'] = tabela['quantidade'].round().astype(int)

# passo 7 - padronizar valores de texto
tabela['uf'] = tabela['uf'].str.upper().str.strip()
tabela['cliente_email'] = tabela['cliente_email'].str.lower()

# passo 8 - criar colunas auxiliares 
tabela['faturamento'] = tabela['quantidade'] * tabela['preco_unitario']

# tabela.info()
tabela.to_excel('Dados_tratados.xlsx')

# ===============================
# Tabela por cliente + filtro
# ===============================

# 1) Agregar por cliente_email
clientes_faturamento = (
    tabela
        .groupby("cliente_email", as_index=False)
        .agg(
            pedidos=("faturamento", "count"),
            quantidade_total=("quantidade", "sum"),
            faturamento_total=("faturamento", "sum")
        )
        .sort_values("faturamento_total", ascending=False)
)

print("Tabela por cliente (top 10):")
print(clientes_faturamento.head(10))

# 2) Função de filtro por faixa de faturamento
def filtrar_por_faturamento(df, min_faturamento=None, max_faturamento=None):
    out = df.copy()
    if min_faturamento is not None:
        out = out[out["faturamento_total"] >= min_faturamento]
    if max_faturamento is not None:
        out = out[out["faturamento_total"] <= max_faturamento]
    return out.sort_values("faturamento_total", ascending=False)

clientes_faturamento.to_excel("Clientes_Faturamento.xlsx", index=False)