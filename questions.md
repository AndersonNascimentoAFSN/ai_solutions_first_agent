# Perguntas para Análise de Notas Fiscais (CSV)

## Perguntas Quantitativas

1. Qual foi o fornecedor que mais faturou (maior valor total de notas)?
2. Qual foi o produto mais vendido em termos de quantidade?
3. Qual o valor total das notas emitidas durante o mês de janeiro de 2024?
4. Qual UF de destino recebeu o maior montante de vendas?
5. Qual foi a média de valor das notas fiscais emitidas?

## Perguntas Qualitativas

1. Quais os principais tipos de operações realizadas no período?
2. Quais os principais produtos comercializados (em variedade)?
3. Existe algum padrão de venda por tipo de destinatário (ex: Governo, Pessoa Jurídica, etc)?
4. Existe alguma concentração de vendas em determinados dias do mês?
5. Existe alguma correlação entre o tipo de operação e o estado de destino?

# ✅ Perguntas Quantitativas e Qualitativas com Respostas Detalhadas

## 1. Perguntas Quantitativas e Respostas Detalhadas

### 1.1 Qual foi o fornecedor que mais faturou (maior valor total de notas)?

- 📊 **Resposta:** CHEMYUNION LTDA com R$ 1.292.418,75.  
- 🔎 **Lógica:** Agrupei o DataFrame de cabeçalho pelo campo **"RAZÃO SOCIAL EMITENTE"**, depois somei o campo **"VALOR NOTA FISCAL"**.

---

### 1.2 Qual foi o produto mais vendido em quantidade?

- 📊 **Resposta:** DIPIFARMA INJETAVEL (DIPIRONA MONOIDR 500MG/ML) 2ML, com **51.000 unidades vendidas**.  
- 🔎 **Lógica:** Agrupei o DataFrame de itens pela **descrição do produto** e somei a coluna **"QUANTIDADE"**.

---

### 1.3 Qual o valor total das notas emitidas em Janeiro/2024?

- 📊 **Resposta:** R$ 3.371.754,84  
- 🔎 **Lógica:** Convertemos o campo **"VALOR NOTA FISCAL"** para numérico e somamos todos os registros do período.

---

### 1.4 Qual UF de destino recebeu o maior montante de vendas?

- 📊 **Resposta:** **Rio de Janeiro (RJ)** com R$ 1.423.297,97.  
- 🔎 **Lógica:** Agrupei o DataFrame pelo campo **"UF DESTINATÁRIO"** e somei o **valor total das notas**.

---

### 1.5 Qual foi a média de valor das notas fiscais emitidas?

- 📊 **Resposta:** R$ 33.717,55 por nota  
- 🔎 **Lógica:** Cálculo da média utilizando o método `.mean()` na coluna **"VALOR NOTA FISCAL"**.

---

## 2. Perguntas Qualitativas e Análises Profundas

### 2.1 Quais os principais tipos de operações realizadas no período?

- 📋 **Resposta:**
  - VENDA
  - RETORNO DE MATERIAL DEPOSITADO EM ARMAZEM GERAL
  - Venda
  - Venda de mercadoria adquirida ou recebida de terceiros
  - Venda Fora do Estado  

- 🔎 **Lógica:** Contagem por frequência na coluna **"NATUREZA DA OPERAÇÃO"**.

---

### 2.2 Quais os principais produtos comercializados (em variedade)?

- 📋 **Resposta:** Produtos mais recorrentes por variedade de notas:
  - 2023-O ANIVERSARIO DO DINOSSAURO-2020
  - 2023-A PINTA FUJONA-2020
  - 2023-CACHORROS NAO DANCAM BALE-2020
  - 2023-RIMARINHAS-2020
  - 2023-PACA TATU CUTIA SIM-2020  

- 🔎 **Lógica:** Contagem de ocorrência por **nome de produto**.

---

### 2.3 Existe padrão de venda por tipo de destinatário?

- 📋 **Resposta:**  
  Os maiores destinatários foram órgãos públicos federais, como:
  - Fundo Nacional de Desenvolvimento da Educação
  - Comando da Aeronáutica
  - Comando da Marinha
  - Ministério da Saúde
  - Ministério do Desenvolvimento Social  

- 🔎 **Lógica:** Contagem de frequência na coluna **"NOME DESTINATÁRIO"**, indicando padrão forte de vendas para **órgãos governamentais**.

---

### 2.4 Existe concentração de vendas em determinados dias do mês?

- 📋 **Resposta:**  
  Sim, os dias com maiores volumes foram:
  - Dia 29: R$ 1.304.009,06
  - Dia 16: R$ 794.000,91
  - Dia 17: R$ 352.902,36
  - Dia 24: R$ 320.677,53
  - Dia 30: R$ 147.022,77  

- 🔎 **Lógica:** Agrupei os dados por **dia (campo DATA EMISSÃO)**, somando o **valor das notas por dia**.

---

### 2.5 Existe correlação entre o tipo de operação e a UF de destino?

- 📋 **Resposta:**  
  Os maiores volumes por tipo de operação e estado foram:

| UF | Tipo de Operação | Quantidade de Notas |
|---|---|---|
| DF | Retorno de material de armazém geral | 7 |
| DF | VENDA | 4 |
| RJ | Venda de mercadoria adquirida ou recebida de terceiros | 3 |
| AM | Produção do estabelecimento | 2 |
| DF | Remessa - Entrega futura | 2 |

- 🔎 **Lógica:** Agrupei por **UF** e **Natureza da Operação**, contando a **quantidade de notas por combinação**.

---
