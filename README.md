# 📊 AI Solutions First Agent

Este projeto é um **Agente Autônomo de Análise de Notas Fiscais** que responde perguntas quantitativas e qualitativas com base em arquivos CSV de notas fiscais. Ele foi desenvolvido usando **CrewAI**, **Python**, **Pandas** e conta com uma interface web simples feita em **Streamlit**.

---

## 🚀 Objetivo

O projeto tem como principal objetivo:

- ✅ Ler e processar múltiplos arquivos CSV de notas fiscais  
- ✅ Realizar limpeza, normalização e mesclagem de dados  
- ✅ Permitir ao usuário fazer perguntas em linguagem natural (ex.: "Qual fornecedor teve maior faturamento?")  
- ✅ Gerar respostas quantitativas e qualitativas baseadas em análise de dados com Python + Pandas  
- ✅ Exibir os resultados de forma interativa através do Streamlit  

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Python** (>=3.10, <3.14)
- **CrewAI** (>=0.126.0) - Framework para orquestração de agentes de IA
- **Streamlit** (>=1.45.1) - Framework para criação de interfaces web
- **Pandas** (>=2.3.0) - Biblioteca para manipulação e análise de dados
- **UV** - Gerenciador de dependências Python
- **OpenAI GPT-4** (para interpretação de linguagem natural e geração de código)
- **Custom Tools** (`CSVCleanerMergerTool`)

---

## 📋 Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git

---

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/ai_solutions.git
cd ai_solutions
```

2. Instale o UV (gerenciador de dependências):
```bash
pip install uv
```

3. Instale as dependências do projeto:
```bash
crewai install
```

---

## ⚙️ Configuração

1. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API OpenAI:
```bash
OPENAI_API_KEY=sua_chave_aqui
```

---

## 🏃‍♂️ Executando o Projeto

Para iniciar a interface web com Streamlit:

```bash
streamlit run src/web/app.py
```

Para executar o crew de agentes de IA:

```bash
crewai run
```

---

## 💻 Uso

1. Acesse a interface web através do navegador (geralmente em `http://localhost:8501`)
2. Interaja com os agentes através da interface Streamlit
3. Configure e execute tarefas conforme necessário
4. Visualize os resultados e relatórios gerados

---

## 🧠 Como Funciona por Trás dos Panos

1. **Upload dos arquivos CSV pelo usuário**  
   O usuário faz o upload dos arquivos CSV contendo os dados de notas fiscais diretamente na interface do Streamlit.

2. **Limpeza e normalização dos dados via `CSVCleanerMergerTool`**  
   Os arquivos são automaticamente tratados para corrigir problemas comuns como:  
   - Codificação de caracteres  
   - Colunas mal formatadas  
   - Dados duplicados  
   - Padronização de nomes de colunas  
   Além disso, se possível, os arquivos são mesclados em um único CSV integrado.

3. **Execução de tasks específicas baseadas na pergunta feita**  
   A pergunta do usuário é analisada para definir quais tasks serão executadas (exemplo: análise de fornecedores, cálculo de montantes, identificação de itens com maior volume).

4. **Geração de código Python dinâmico usando o LLM da OpenAI**  
   O agente utiliza um modelo da OpenAI para gerar automaticamente o código Python necessário para responder à pergunta.  
   Exemplo: geração de um código com `pd.DataFrame.groupby()` para agrupar e somar os dados relevantes.

5. **Execução segura do código usando o Code Interpreter do CrewAI**  
   O código gerado é executado de forma controlada e segura através do Code Interpreter interno do CrewAI, garantindo que só sejam realizadas operações seguras sobre os dados.

6. **Retorno da resposta direto na interface do Streamlit**  
   Por fim, a resposta final é exibida ao usuário de forma clara e detalhada na interface Streamlit, junto com o raciocínio utilizado e, quando relevante, o código Python gerado.

---

## 💬 Exemplo de Perguntas que o Agente Responde

### 📊 Perguntas Quantitativas:

- **Qual o fornecedor que mais faturou?**
- **Qual produto foi mais vendido em quantidade?**
- **Qual o valor total de notas fiscais emitidas em um determinado mês?**

### 📝 Perguntas Qualitativas:

- **Quais os principais itens comercializados por um fornecedor específico?**
- **Há concentração de vendas em algum período do ano?**
- **Existem padrões de compra por região?**

---

## 📂 Estrutura do Projeto

ai_solutions_first_agent/

├── src/

│ ├── ai_solutions/

│ │ ├── config/ # Configurações dos agentes e tarefas

│ │ ├── tools/ # Ferramentas personalizadas

│ │ ├── crew.py # Configuração dos agentes

│ │ └── main.py # Ponto de entrada principal

│ └── web/ # Interface Streamlit

├── data/ # Dados do projeto

├── knowledge/ # Base de conhecimento

└── pyproject.toml # Configuração do projeto