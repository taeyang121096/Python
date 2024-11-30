
animals = ['cat', 'dog', 'monkey']

for animal in animals:
    print(animal)



range(3)
print(range(3))

for n in range(0, 3):
    print(n)

for j in range(2, 10):
    for i in range(1,10):
        print('{} x {} = {}'.format(j, i, j*i))


numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []

# comprehension
print([number for number in numbers if number % 2 == 1])
