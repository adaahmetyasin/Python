cars = ["bmw","mercedes","opel","mazda"]
#print(len(cars))
#print(cars[-1])
#cars[-1] = 'toyota'
#print(cars)
#result = 'mercedes' in cars
#result = cars[:3]
cars[-2:] = ['toyota','renault']
result = cars + ['ferrari','bugatti']

print(result)
print(result[::-1])