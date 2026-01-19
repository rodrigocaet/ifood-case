

# Case iFood – Recomendação de Ofertas

Este projeto apresenta uma abordagem orientada a dados para apoiar a decisão
de qual oferta enviar para cada cliente, maximizando conversão e impacto financeiro.


## Estrutura
```
ifood-case/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 1_data_processing.ipynb
│   └── 2_modeling.ipynb
├── presentation/
├── src/
│   └── pre_process_transactions.py
├── README.md
└── requirements.txt
```

## Abordagem

- Modelo preditivo de probabilidade de conversão

- Simulação contrafactual para priorização de ofertas

- Estimativa de uplift vs estratégia baseline

## Execução

- Antes da execução dos notebooks, é necessário rodar o script armazenado em src/pre_process_transactions.py.

Este script faz um tratamento dos dados do dataset de transactions, para que se possa fazer o upload no site do databricks.

- Subir os datasets no server do Databricks

- Rodar primeiramente o notebook 1_data_processing.ipynb, que vai gerar o dataset df_model

- Rodar o notebook 2_modeling.ipynb, que consiste do treinamento, avaliação e análise de impacto do modelo.

## Limitações do estudo

- O estudo foi feito informação offer_id para os eventos de transações. Foi feito uma aproximação com a offer_id do evento mais próximo temporalmente.

- Algumas parte do código devem ser melhor trabalhadas em futuras versões, como a importância das features e testes de outros algoritmos que podem apresentar melhor performance.

- O impacto deve ser medido também em valor financeiro, para uma melhor avaliação do ponto de vista de negócios.

