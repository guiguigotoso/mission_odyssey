

# 🐍 Configuração do Projeto

Este repositório utiliza o **[uv](https://docs.astral.sh/uv/)** para gerenciar o ambiente Python e as dependências do projeto.

## 🚀 Pré-requisitos

Antes de começar, instale o **uv** (se ainda não tiver):

```bash
pip install uv
````

Verifique se foi instalado corretamente:

```bash
uv --version
```

## ⚙️ Configuração do ambiente
Crie o ambiente virtual e instale as dependências:

```bash
uv sync
```

Isso cria automaticamente o ambiente virtual e instala os pacotes definidos em `pyproject.toml`.

## ▶️ Executando o projeto

Ative o ambiente virtual:

```bash
.venv\Scripts\activate      # Windows
                            # ou 
source .venv/bin/activate   # Linux/macOS
```

Depois, execute o projeto normalmente, por exemplo:

```bash
python nome-do-arquivo.py
```

💡 *Dica:* você também pode rodar comandos dentro do ambiente sem ativá-lo manualmente:

```bash
uv run python nome-do-arquivo.py
```