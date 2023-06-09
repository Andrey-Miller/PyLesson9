# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import csv

data = 'sample_data/california_housing_train.csv'
total_value = 0
houses_count = 0

with open(data) as file:
    dict = csv.DictReader(file)
    for row in dict:
        population = float(row['population'])
        median_value = float(row['median_house_value'])

        if population >= 0 and population <= 500:
            total_value += median_value
            houses_count += 1


average_value = total_value / houses_count
print(f"Средняя стоимость дома, где кол-во людей от 0 до 500: {round(average_value, 2)}")
