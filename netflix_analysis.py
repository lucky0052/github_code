import pandas as pd

file = pd.read_csv("netflixData.csv")
print(file.head())

print(file.columns)

print(file.isnull().sum())

new_file = file.drop(columns = ['Show Id', 'Director','Cast',
       'Production Country', 'Release Date', 'Rating', 'Duration',
       'Imdb Score', 'Date Added'])

print(new_file)
new_file = new_file.dropna()
file_group = new_file.groupby(['Genres','Content Type'])
print(file_group.size())