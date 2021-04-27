food = ['rice', 'beans']

food.append('brocolli')

more_food = ['bread', 'pizza']

food.extend(more_food)

print(food[:2])

print(food[-1])

breakfast_string = "eggs,fruit,orange juice"

breakfast = breakfast_string.split(",")

print(breakfast)

print(len(breakfast))

float_list = []

while True:
    inp = input('Enter a floating-point number or "stop" to quit: ')

    if inp == 'stop':
        break
    value = float(inp)
    float_list.append(value)

average = sum(float_list) / len(float_list)
print(f'Average: {average}')

float_list_min = min(float_list)
print(f'Min: {float_list_min}')

float_list_max = max(float_list)
print(f'Max: {float_list_max}')