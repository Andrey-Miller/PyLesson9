# Задача 42: Узнать какая максимальная households в зоне минимального значения population


import csv

data = 'sample_data/california_housing_train.csv'
min_population = float("inf")
max_households = 0

with open(data) as file:
    dict = csv.DictReader(file)
    for row in dict:
        population = int(float(row['population']))
        households = int(float(row['households']))

        if population < min_population:
            min_population = population
            max_households = households

print(f"Максимальное количество households в зоне с минимальной популяцией населения ({min_population} человек): {max_households}")