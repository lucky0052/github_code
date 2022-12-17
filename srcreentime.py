import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

file = pd.read_csv("screentime.csv")
print(file.columns)


is_null = file.isnull().sum()
print(is_null)

print(file.describe())

figure = px.bar(file,x='Date',y='Usage',color='App',title='Usage')
figure.show()


new_file = file.groupby(['App'])
print(new_file.size())
