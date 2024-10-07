Claro! Aqui está uma versão reformulada do seu README:

```markdown
# Mini Sistema de Análise de Balanço Patrimonial

Este projeto é uma aplicação web simples que permite aos usuários inserir dados básicos de um balanço patrimonial e realizar análises fundamentais.

## Estrutura do Projeto

```
mini_sistema_analise_balanco/
│
├── app/                  # Código da aplicação
│   ├── __init__.py      # Inicialização do Flask
│   ├── routes.py        # Definição das rotas
│   ├── models.py        # Modelos de dados e interação com o banco
│   ├── forms.py         # Formulários (se usar WTForms)
│   └── static/          # Arquivos estáticos (CSS, JS, imagens)
│       └── style.css
│
├── templates/           # Templates HTML
│   ├── base.html        # Template base
│   └── index.html       # Página principal
│
├── data/                # Arquivos de dados (como o banco SQLite)
│   └── balanco.db
│
├── requirements.txt     # Dependências do projeto
└── run.py               # Script para rodar a aplicação
```

## Como Executar

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd mini_sistema_analise_balanco
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**

   ```bash
   python run.py
   ```

4. **Acesse no navegador:**

   Vá para `http://127.0.0.1:5000/` para utilizar a aplicação.

## Funcionalidades

- Inserir dados de despesas.
- Visualizar e analisar informações do balanço patrimonial.
- Interface simples e intuitiva.

## Contribuições

Sinta-se à vontade para contribuir! Abra uma issue ou um pull request com melhorias e sugestões.

```

Sinta-se à vontade para ajustar qualquer parte conforme necessário! Se precisar de mais ajuda, estou aqui!