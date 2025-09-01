# 🧹 Data Cleaning & Analysis – Vendas

Este projeto realiza **tratamento e análise de dados de vendas** a partir de um arquivo CSV desorganizado (`dados_baguncados.csv`).  
O script usa **pandas** e **numpy** para limpeza, padronização e geração de relatórios em Excel.  

---

## 📌 Funcionalidades
O código executa as seguintes etapas:

1. **Importação da base de dados** (`pandas.read_csv`)  
2. **Padronização dos nomes das colunas** (minúsculas, sem espaços extras)  
3. **Remoção de linhas duplicadas**  
4. **Remoção de colunas vazias**  
5. **Tratamento de tipos de dados**  
   - Datas convertidas com `pd.to_datetime`  
   - Coluna `quantidade` convertida para inteiro  
6. **Preenchimento de valores ausentes** (usando a mediana de `quantidade`)  
7. **Padronização de valores de texto** (`UF` em maiúsculo, `cliente_email` em minúsculo)  
8. **Criação da coluna `faturamento`** (`quantidade * preco_unitario`)  
9. **Exportação dos dados tratados** para `Dados_tratados.xlsx`  
10. **Agregação por cliente**:  
    - Total de pedidos  
    - Quantidade total comprada  
    - Faturamento total  
11. **Exportação do relatório de clientes** para `Clientes_Faturamento.xlsx`  
12. **Função de filtro por faixa de faturamento** para análises personalizadas  

---

## 📂 Estrutura de saída
Após rodar o script, serão gerados dois arquivos:

- `Dados_tratados.xlsx` → Base original limpa e padronizada  
- `Clientes_Faturamento.xlsx` → Resumo agregado por cliente  

---

## 🚀 Como usar
1. Coloque seu arquivo de dados no mesmo diretório do script com o nome **`dados_baguncados.csv`**.  
2. Instale as dependências:  
   ```bash
   pip install pandas numpy openpyxl
3. Rode o script:
   ```bash
   python script.py
4. Confira os arquivos Excel gerados no diretório do projeto.

## 🛠️ Tecnologias usadas
* Python 3
* pandas
* numpy
* openpyxl
