# código de geração do gráfico
import pandas as pd
import seaborn as sns

gasolina_df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda', marker="o", palette='pastel')
  grafico.set(title='Preço Médio da Gasolina em SP', xlabel='Dias', ylabel='Moeda Real R$')
  grafico.legend("Sobe" , loc='upper right')
  grafico.figure.savefig('gasolina.png')