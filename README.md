# AI Solutions - Sistema de Análise de Dados Fiscais

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45.1%2B-FF4B4B)](https://streamlit.io/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.126.0%2B-00A67E)](https://crewai.com/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.0%2B-130654)](https://pandas.pydata.org/)

Sistema inteligente de análise de dados fiscais brasileiros utilizando CrewAI para orquestração de agentes especializados e Streamlit para interface web interativa.

## 📋 Índice

- [AI Solutions - Sistema de Análise de Dados Fiscais](#ai-solutions---sistema-de-análise-de-dados-fiscais)
  - [📋 Índice](#-índice)
  - [🎯 Visão Geral](#-visão-geral)
  - [✨ Funcionalidades](#-funcionalidades)
    - [🔧 Processamento de Dados](#-processamento-de-dados)
    - [🤖 Análise Inteligente](#-análise-inteligente)
    - [🌐 Interface Web](#-interface-web)
  - [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
  - [📋 Pré-requisitos](#-pré-requisitos)
  - [🚀 Instalação](#-instalação)
  - [⚙️ Configuração](#️-configuração)
  - [🏃‍♂️ Executando o Projeto](#️-executando-o-projeto)
    - [Interface Web (Recomendado)](#interface-web-recomendado)
    - [Linha de Comando](#linha-de-comando)
  - [📁 Estrutura do Projeto](#-estrutura-do-projeto)
  - [💻 Uso](#-uso)
    - [1. Upload de Arquivos](#1-upload-de-arquivos)
    - [2. Processamento Automático](#2-processamento-automático)
    - [3. Análise de Dados](#3-análise-de-dados)
    - [4. Visualização de Resultados](#4-visualização-de-resultados)
  - [🔌 API e Scripts](#-api-e-scripts)
    - [Scripts Disponíveis](#scripts-disponíveis)
    - [Funções Principais](#funções-principais)
  - [👨‍💻 Desenvolvimento](#-desenvolvimento)
    - [Adicionando Novos Agentes](#adicionando-novos-agentes)
    - [Criando Novas Ferramentas](#criando-novas-ferramentas)
    - [Estrutura de Contribuição](#estrutura-de-contribuição)
  - [🤖 Agentes, Tarefas e Ferramentas](#-agentes-tarefas-e-ferramentas)
    - [🎯 Visão Geral dos Agentes](#-visão-geral-dos-agentes)
    - [🔧 Agent ETL (Engenheiro de Dados)](#-agent-etl-engenheiro-de-dados)
    - [�� Agent QA (Analista de Dados)](#-agent-qa-analista-de-dados)
    - [📋 Tarefas do Sistema](#-tarefas-do-sistema)
      - [1. Cleaner Merger Task (Tarefa de Limpeza e Mesclagem)](#1-cleaner-merger-task-tarefa-de-limpeza-e-mesclagem)
      - [2. Answer Question Task (Tarefa de Resposta a Perguntas)](#2-answer-question-task-tarefa-de-resposta-a-perguntas)
    - [🛠️ Ferramentas Disponíveis](#️-ferramentas-disponíveis)
      - [CSVCleanerMergerToJSONConverterTool](#csvcleanermergertojsonconvertertool)
      - [JSONSearchTool (CrewAI)](#jsonsearchtool-crewai)
    - [🔄 Fluxo de Execução](#-fluxo-de-execução)
    - [📊 Exemplos de Perguntas e Respostas](#-exemplos-de-perguntas-e-respostas)
      - [Pergunta Quantitativa](#pergunta-quantitativa)
      - [Pergunta Qualitativa](#pergunta-qualitativa)
    - [🔍 Monitoramento e Logs](#-monitoramento-e-logs)
  - [🆘 Suporte](#-suporte)
    - [Documentação](#documentação)
    - [Comunidade](#comunidade)
    - [Problemas Comuns](#problemas-comuns)
  - [📝 Licença](#-licença)
  - [🤝 Contribuição](#-contribuição)

## 🎯 Visão Geral

O AI Solutions é um sistema avançado de análise de dados fiscais que combina:

- **Agente ETL**: Especializado em processamento, limpeza e integração de arquivos CSV de notas fiscais
- **Agente QA**: Analista de dados com expertise em Pandas para responder perguntas em linguagem natural
- **Interface Web**: Aplicação Streamlit para upload de arquivos e interação com o sistema
- **Orquestração**: Framework CrewAI para coordenação inteligente dos agentes

## ✨ Funcionalidades

### 🔧 Processamento de Dados
- Upload de arquivos ZIP contendo múltiplos CSVs
- Limpeza automática de dados (encoding, valores nulos, duplicatas)
- Padronização de nomes de colunas e tipos de dados
- Mesclagem inteligente de arquivos via colunas-chave
- Conversão para formato JSON estruturado

### 🤖 Análise Inteligente
- Perguntas em linguagem natural sobre os dados
- Análises quantitativas (somas, médias, agrupamentos)
- Análises qualitativas (tendências, padrões, insights)
- Execução de código Python com Pandas
- Respostas didáticas com explicação do processo

### 🌐 Interface Web
- Upload seguro de arquivos ZIP
- Validação automática de arquivos CSV
- Interface intuitiva para perguntas
- Visualização de resultados em tempo real


## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|------------|--------|-----------|
| **Python** | >=3.10, <3.14 | Linguagem principal |
| **CrewAI** | >=0.126.0 | Orquestração de agentes de IA |
| **Streamlit** | >=1.45.1 | Interface web interativa |
| **Pandas** | >=2.3.0 | Manipulação e análise de dados |
| **AgentOps** | >=0.4.16 | Monitoramento de agentes |
| **UV** | - | Gerenciador de dependências |

## 📋 Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Chave de API OpenAI válida

## 🚀 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/ai_solutions.git
cd ai_solutions
```

2. **Instale o UV (gerenciador de dependências):**
```bash
pip install uv
```

3. **Instale as dependências do projeto:**
```bash
crewai install
```

## ⚙️ Configuração

1. **Configure as variáveis de ambiente:**
```bash
# Crie o arquivo .env na raiz do projeto
OPENAI_API_KEY=sua_chave_aqui
```

2. **Personalize os agentes (opcional):**
   - Edite `src/ai_solutions/config/agents.yaml` para modificar roles e objetivos
   - Ajuste `src/ai_solutions/config/tasks.yaml` para customizar tarefas

3. **Configure ferramentas customizadas (opcional):**
   - Adicione novas ferramentas em `src/ai_solutions/tools/`
   - Modifique `src/ai_solutions/crew.py` para integrar novas funcionalidades

## 🏃‍♂️ Executando o Projeto

### Interface Web (Recomendado)
```bash
streamlit run src/web/app.py
```
Acesse `http://localhost:8501` no seu navegador.

### Linha de Comando
```bash
# Execução básica
crewai run

# Treinamento do crew
crewai train <iterações> <arquivo_saída>

# Replay de execução
crewai replay <task_id>

# Teste do sistema
crewai test <iterações> <modelo_llm>
```

## 📁 Estrutura do Projeto

ai_solutions/
├── src/
│ ├── ai_solutions/
│ │ ├── config/
│ │ │ ├── agents.yaml # Configuração dos agentes
│ │ │ └── tasks.yaml # Definição das tarefas
│ │ ├── tools/
│ │ │ ├── csv_cleaner_merger_to_json_converter_tool.py
│ │ │ └── custom_tool.py
│ │ ├── crew.py # Orquestração dos agentes
│ │ └── main.py # Ponto de entrada principal
│ └── web/
│ └── app.py # Interface Streamlit
├── data/
│ ├── uploads/ # Arquivos temporários
│ └── merged_cleaned.json # Dados processados
├── knowledge/ # Base de conhecimento
├── docs_ai/ # Documentação de IA
├── pyproject.toml # Configuração do projeto
└── README.md # Este arquivo


## 💻 Uso

### 1. Upload de Arquivos
- Acesse a interface web
- Faça upload de um arquivo ZIP contendo arquivos CSV
- O sistema validará automaticamente os arquivos

### 2. Processamento Automático
- O Agente ETL processará automaticamente os dados
- Limpeza, padronização e mesclagem serão executadas
- Resultado salvo em formato JSON estruturado

### 3. Análise de Dados
- Digite perguntas em linguagem natural
- Exemplos de perguntas:
  - "Qual foi o total de vendas por mês?"
  - "Quais são os 5 produtos mais vendidos?"
  - "Há alguma tendência nos dados de entrega?"

### 4. Visualização de Resultados
- Respostas detalhadas com explicação do processo
- Código Python executado para transparência
- Amostras de dados quando relevante

## 🔌 API e Scripts

### Scripts Disponíveis
```bash
# Execução principal
ai_solutions run

# Treinamento
ai_solutions train

# Replay
ai_solutions replay

# Testes
ai_solutions test
```

### Funções Principais
- `run(question: str)`: Executa análise para uma pergunta específica
- `train()`: Treina o crew com dados de exemplo
- `replay(task_id)`: Reexecuta uma tarefa específica
- `test()`: Executa testes de validação

## 👨‍💻 Desenvolvimento

### Adicionando Novos Agentes
1. Defina o agente em `config/agents.yaml`
2. Implemente a lógica em `crew.py`
3. Configure as tarefas em `config/tasks.yaml`

### Criando Novas Ferramentas
1. Crie uma nova classe em `tools/`
2. Herde de `BaseTool`
3. Implemente o método `_run()`
4. Registre na configuração do crew

### Estrutura de Contribuição
1. Fork do repositório
2. Crie uma branch para sua feature
3. Implemente as mudanças
4. Execute testes
5. Abra um Pull Request

## 🤖 Agentes, Tarefas e Ferramentas

### 🎯 Visão Geral dos Agentes

O sistema utiliza dois agentes especializados que trabalham em sequência para processar e analisar dados fiscais:
┌─────────────────┐ ┌─────────────────┐
│ Agent ETL │───►│ Agent QA │
│ (Processador) │ │ (Analista) │
└─────────────────┘ └─────────────────┘


### 🔧 Agent ETL (Engenheiro de Dados)

**Role:** Engenheiro de Dados especializado em ETL de documentos fiscais

**Goal:** Processar arquivos CSV brutos de notas fiscais, realizando limpeza, padronização, integração e transformação dos dados em um JSON confiável e estruturado.

**Responsabilidades:**
- ✅ Corrigir encoding, remover nulos, padronizar nomes e tipos de colunas
- ✅ Verificar e realizar mesclagem (merge) entre arquivos via chaves comuns
- ✅ Salvar o resultado limpo/mesclado como um JSON
- ✅ Relatar possíveis problemas de inconsistência, duplicidade ou impossibilidade de mescla
- ✅ Garantir que o output seja sempre um JSON pronto para análise

**Backstory:** Especialista com vasta experiência em ETL para dados fiscais brasileiros, focado em entregar dados limpos, integrados e prontos para uso analítico. Detecta automaticamente encoding incorreto, formatação regional e inconsistência de schemas.

**Ferramentas Utilizadas:**
- `CSVCleanerMergerToJSONConverterTool`

### �� Agent QA (Analista de Dados)

**Role:** Analista de Dados especialista em Pandas e interpretação de perguntas em linguagem natural

**Goal:** Responder perguntas qualitativas e quantitativas feitas pelo usuário com base no JSON limpo entregue pelo agente ETL.

**Responsabilidades:**
- ✅ Carregar o JSON processado
- ✅ Identificar colunas relevantes para a pergunta
- ✅ Realizar filtros, agrupamentos, cálculos e sumarizações usando Python (pandas)
- ✅ Gerar resposta didática, mostrando o código executado e explicando cada passo
- ✅ Comunicar claramente quando a resposta não for possível

**Backstory:** Analista com domínio de pandas, Python e compreensão de perguntas em português. Missão de responder com precisão, didática e transparência, sempre exibindo o raciocínio, código e resultado de cada análise.

**Ferramentas Utilizadas:**
- `JSONSearchTool` (do CrewAI Tools)

### 📋 Tarefas do Sistema

#### 1. Cleaner Merger Task (Tarefa de Limpeza e Mesclagem)

**Descrição:** Processa uma lista de arquivos CSV brutos, realizando limpeza, normalização e mesclagem dos dados.

**Entrada:** Lista de caminhos de arquivos CSV (`file_paths`)

**Processo:**
1. **Validação Inicial**
   - Verifica se há arquivos CSV para processamento
   - Retorna erro se lista estiver vazia

2. **Limpeza dos Dados Individuais**
   - Correção de problemas de codificação
   - Remoção de valores ausentes e registros duplicados
   - Padronização de nomes de colunas (lowercase, sem acentos, underscores)
   - Uniformização de formatos de dados (datas, números, textos)

3. **Verificação e Integração**
   - Análise de colunas-chave comuns entre arquivos
   - Mesclagem via inner join quando viável
   - Criação de CSV consolidado

4. **Conversão para JSON**
   - Transformação do resultado em arquivo JSON estruturado

**Saída:** Caminho do arquivo JSON resultante (`json_path`) ou mensagem de erro

**Agente Responsável:** Agent ETL

#### 2. Answer Question Task (Tarefa de Resposta a Perguntas)

**Descrição:** Responde perguntas em linguagem natural sobre os dados processados.

**Entrada:** Pergunta do usuário (`question`) e caminho do JSON (`json_path`)

**Processo:**
1. **Verificação do JSON**
   - Valida se o arquivo JSON existe e é acessível
   - Retorna erro se arquivo não for encontrado

2. **Carregamento e Inspeção**
   - Leitura do JSON em DataFrame pandas
   - Validação de dados e colunas disponíveis

3. **Classificação da Pergunta**
   - **Quantitativa:** Envolve cálculos, somas, médias, agrupamentos
   - **Qualitativa:** Análise descritiva, tendências, insights

4. **Execução da Análise**
   - Identificação de colunas relevantes
   - Execução de operações pandas apropriadas
   - Geração de código Python transparente

**Saída:** Resposta detalhada com explicação do processo e resultados

**Agente Responsável:** Agent QA

### 🛠️ Ferramentas Disponíveis

#### CSVCleanerMergerToJSONConverterTool

**Propósito:** Limpeza, normalização e mesclagem de arquivos CSV com conversão para JSON.

**Funcionalidades:**
- ✅ Remoção de linhas completamente vazias
- ✅ Padronização de nomes de colunas (lowercase, sem acentos, underscores)
- ✅ Conversão automática de tipos de dados
- ✅ Mesclagem inteligente via colunas comuns
- ✅ Salvamento em formato JSON estruturado

**Parâmetros de Entrada:**
```python
paths: List[str]  # Lista de caminhos dos arquivos CSV
```

**Exemplo de Uso:**
```python
tool = CSVCleanerMergerToJSONConverterTool()
result = tool._run(['arquivo1.csv', 'arquivo2.csv'])
# Retorna: "/caminho/para/merged_cleaned.json"
```

**Processo Interno:**
1. **Leitura de Arquivos:** Carrega cada CSV com detecção automática de encoding
2. **Limpeza:** Remove linhas vazias e padroniza colunas
3. **Normalização:** Converte tipos de dados quando possível
4. **Mesclagem:** Identifica colunas comuns e realiza inner join
5. **Persistência:** Salva resultado em JSON com formatação legível

#### JSONSearchTool (CrewAI)

**Propósito:** Ferramenta nativa do CrewAI para busca e análise de dados em arquivos JSON.

**Funcionalidades:**
- ✅ Carregamento automático de arquivos JSON
- ✅ Busca e filtragem de dados
- ✅ Execução de queries complexas
- ✅ Integração com pandas para análise

**Configuração:**
```python
JSONSearchTool(json_path="/caminho/para/merged_cleaned.json")
```

### 🔄 Fluxo de Execução
1. Upload de Arquivos ZIP
↓
2. Extração de CSVs
↓
3. Agent ETL + Cleaner Merger Task
├── Limpeza de dados
├── Padronização de colunas
├── Mesclagem de arquivos
└── Conversão para JSON
↓
4. Agent QA + Answer Question Task
├── Carregamento do JSON
├── Análise da pergunta
├── Execução de código pandas
└── Geração da resposta
↓
5. Apresentação do Resultado


### 📊 Exemplos de Perguntas e Respostas

#### Pergunta Quantitativa
**Pergunta:** "Qual foi o total de vendas por mês?"

**Processo do Agent QA:**
```python
import pandas as pd
df = pd.read_json('merged_cleaned.json')

# Agrupamento por mês e soma de vendas
resultado = df.groupby('mes')['valor_total'].sum().reset_index()
```

**Resposta:** "O total de vendas por mês foi: Janeiro - R$ 150.000, Fevereiro - R$ 180.000..."

#### Pergunta Qualitativa
**Pergunta:** "Quais são as principais tendências nos dados?"

**Processo do Agent QA:**
```python
# Análise de padrões e distribuições
tendencias = df.describe()
categorias_principais = df['categoria'].value_counts().head(5)
```

**Resposta:** "Identificamos que as vendas crescem 15% mensalmente, com destaque para a categoria 'Medicamentos'..."

### 🔍 Monitoramento e Logs

O sistema utiliza **AgentOps** para monitoramento:
- Logs de execução em `agentops.log`
- Métricas de performance dos agentes
- Rastreamento de erros e falhas
- Análise de eficiência das tarefas

## 🆘 Suporte

### Documentação
- [CrewAI Documentation](https://docs.crewai.com)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

### Comunidade
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [Discord CrewAI](https://discord.com/invite/X4JWnZnxPb)
- [Chat com Documentação](https://chatg.pt/DWjSBZn)

### Problemas Comuns
- **Erro de API Key**: Verifique se `OPENAI_API_KEY` está configurada no `.env`
- **Arquivo não encontrado**: Certifique-se de que o ZIP contém arquivos CSV válidos
- **Erro de encoding**: O sistema detecta e corrige automaticamente problemas de encoding

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia o [CONTRIBUTING.md](CONTRIBUTING.md) antes de submeter suas mudanças.

---
