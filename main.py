import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  #charts.generate_pie_chart(countries, percentages)
  print('Welcome to the World Population App')
  country = input('Type Country => ')
  '''
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart1(countries, percentages)
  
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)

  
 
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
    charts.generate_pie_chart(country['Country/Territory'], countries, percentages)

  print(result)
  
if __name__ == '__main__':
  run()
  