\# Case iFood – Recomendação de Ofertas



Este projeto apresenta uma abordagem orientada a dados para apoiar a decisão

de qual oferta enviar para cada cliente, maximizando conversão e impacto financeiro.



\## Estrutura

```

ifood-case/

├── data/

│   ├── raw/

│   └── processed/

├── notebooks/

│   ├── 1\_data\_processing.ipynb

│   └── 2\_modeling.ipynb

├── presentation/

├── src/

├── README.md

└── requirements.txt

```



\## Abordagem

\- Modelo preditivo de probabilidade de conversão

\- Simulação contrafactual para priorização de ofertas

\- Estimativa de uplift vs estratégia baseline



\## Execução

\- Antes da execução dos notebooks, é necessário rodar o script armazenado em src/pre\_process\_transactions.py

Este script faz um tratamento dos dados do dataset de transactions, para que se possa fazer o upload no site do databricks.

\- Subir os datasets no server do Databricks

\- Rodar primeiramente o notebook 1\_data\_processing.ipynb, que vai gerar o dataset df\_model

\- Rodar o notebook 2\_modeling.ipynb, que consiste do treinamento, avaliação e análise de impacto do modelo.

