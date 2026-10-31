# Credit Card Analyzer

Aplicação desenvolvida em Python e Streamlit para análise detalhada de faturas de cartão de crédito a partir de arquivos CSV.

O sistema transforma os lançamentos da fatura em informações gerenciais, permitindo visualizar padrões de consumo, identificar despesas recorrentes e acompanhar compromissos financeiros futuros.

## Funcionalidades

- Importação e processamento de faturas em CSV.
- Análise de despesas por categoria.
- Identificação de compras recorrentes.
- Detecção de assinaturas e serviços recorrentes.
- Identificação e acompanhamento de compras parceladas.
- Projeção de compromissos financeiros futuros.
- Indicadores e score financeiro.
- Dashboard interativo com gráficos e indicadores.

## Tecnologias utilizadas

- Python
- Streamlit
- Pandas
- Plotly
- Unidecode

## Instalação local

Clone o repositório:

```bash
git clone https://github.com/alexpereira82log-ui/credit_card_analyzer.git
cd credit_card_analyzer
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Execução

Inicie a aplicação:

```bash
python -m streamlit run run.py
```

O Streamlit disponibilizará o endereço local para acesso ao dashboard.

## Utilização

1. Acesse a aplicação.
2. Envie um arquivo CSV de fatura de cartão de crédito.
3. Aguarde o processamento.
4. Explore os indicadores, gráficos e análises apresentados no dashboard.

---

Projeto desenvolvido para estudo e aplicação prática de Python, análise de dados e desenvolvimento de aplicações interativas.