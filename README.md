# LangGraph-Memory-Tools

Este projeto implementa um chatbot inteligente com memória, utilizando a biblioteca LangGraph, integração com ferramentas de busca (Tavily e YouTube) e suporte a modelos de linguagem OpenAI.

## Funcionalidades
- Chatbot com memória curta e local de conversas.
- Busca na web via Tavily.
- Busca de vídeos no YouTube.
- Integração com modelos OpenAI (ex: GPT-4.1).
- Estrutura baseada em grafo de estados para controle do fluxo conversacional.

## Como funciona
O chatbot utiliza um grafo de estados para alternar entre respostas do modelo de linguagem e uso de ferramentas externas. A memória é persistida para manter o contexto da conversa.

### Principais componentes
- `Main_tool_memory.py`: Script principal do chatbot.
- `requirements.txt`: Dependências do projeto.

### Fluxo básico
1. O usuário envia uma mensagem.
2. O grafo decide se a resposta será do modelo ou de uma ferramenta (busca web/YouTube).
3. O resultado é retornado ao usuário e armazenado na memória.

## Instalação
1. Clone o repositório.
2. Crie um ambiente virtual e ative-o:
   ```sh
   python3 -m venv env
   source env/bin/activate
   ```
3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
4. Crie um arquivo `.env` com suas chaves de API necessárias (ex: OpenAI, Tavily).

## Variáveis de ambiente necessárias (.env)

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

- `OPENAI_API_KEY`: chave de API da OpenAI para uso dos modelos GPT.
- `TAVILY_API_KEY`: chave de API do Tavily para buscas na web.

Certifique-se de obter essas chaves nos respectivos sites oficiais.

## Uso
Execute o chatbot:
```sh
python Main_tool_memory.py
```
Digite sua mensagem e interaja. Para sair, digite `quit`, `exit` ou `q`.

## Dependências principais
- langgraph
- langchain-openai
- langchain-tavily
- youtube_search
- python-dotenv

## Observações
- Certifique-se de ter as chaves de API válidas no arquivo `.env`.
- O projeto pode ser expandido com novas ferramentas e fluxos conversacionais.

---

Desenvolvido por Leonardo.
