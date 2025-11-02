# Desafio MBA Engenharia de Software com IA - Full Cycle

## Sobre o Projeto

Este projeto implementa um sistema de RAG (Retrieval Augmented Generation) que permite fazer perguntas sobre o conteúdo de documentos PDF. O sistema utiliza tecnologias modernas como OpenAI para processamento de linguagem natural, LangChain para orquestração, e pgvector para armazenamento eficiente de embeddings vetoriais.

### Principais Funcionalidades

1. Ingestão de documentos PDF com processamento de texto
2. Geração e armazenamento de embeddings usando OpenAI
3. Interface CLI para consultas em linguagem natural
4. Respostas contextualizadas baseadas no conteúdo do documento

## Pré-requisitos

- Python 3.8 ou superior
- Docker e Docker Compose
- Chave de API da OpenAI
- Um arquivo PDF para análise

## Configuração

1. Clone o repositório
2. Crie um ambiente virtual Python:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   .\venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`
   - Preencha as variáveis necessárias:
     - `OPENAI_API_KEY`: Sua chave de API da OpenAI
     - `PDF_PATH`: Caminho completo para o arquivo PDF a ser analisado
     - Demais variáveis já estão configuradas para uso local

5. Inicie o banco de dados PostgreSQL com pgvector:
   ```bash
   docker-compose up -d
   ```

## Executando o Projeto

1. Primeiro, processe o documento PDF:
   ```bash
   python src/ingest.py
   ```

2. Para fazer perguntas sobre o documento:
   ```bash
   python src/chat.py
   ```

O sistema irá solicitar sua pergunta e retornará uma resposta baseada no conteúdo do documento processado.

## Estrutura do Projeto

- `src/ingest.py`: Processamento e ingestão de documentos PDF
- `src/search.py`: Lógica de busca e processamento de consultas
- `src/chat.py`: Interface CLI para interação com o usuário
- `docker-compose.yml`: Configuração do banco de dados com pgvector

## Tecnologias Utilizadas

- OpenAI API (embeddings e chat)
- LangChain (framework de orquestração)
- PostgreSQL com pgvector (armazenamento de embeddings)
- Python (linguagem principal)
- Docker (containerização)