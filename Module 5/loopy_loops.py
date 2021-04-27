pokemon = ('picachu', 'charmander', 'bulbasaur')

print(pokemon[1])

starter1 = pokemon[0]
starter2 = pokemon[1]
starter3 = pokemon[2]

my_name = ('m', 'a', 't', 't')

if 'i' in my_name:
    print("My name has an 'i' in it.")
else:
    print("My name does not have an 'i' in it.")

for j in range(2, 11):
    print(j)

k = 2
while k in range(2,11):
    print(k)
    k += 1

simple_string = 'This is a simple string' 
for l in simple_string:
    print(l, end = "")

print('\n')
simple_set = ('this', 'is', 'a', 'simple', 'set')
for m in simple_set:
    for n in range(3):
        print(m, end = "")
    print('\n')