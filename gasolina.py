# código de geração do gráfico
import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', palette='pastel')
  grafico.set(title='Preço da gasolina', xlabel='Dia', ylabel='Preço')
  grafico.figure.savefig('gasolina.png')