
class Dog:

    breed = ''
    age = 0
    color=''
    weight = 0
    height = 0
    gender = ''

    def  bark(self):
        print('🐶bow'* 3)

    def wag(self):
        print('wags tails')

    def eat(self, food):
        print(f'dog{food} kha raha h')




tommy = Dog()  # u are calliing the constructor
tommy.age = 3
tommy.breed = 'street dog'
tommy.color = ' black'
tommy.gender = 'male'
tommy.height = 1.1
tommy.weight = 8






charle = Dog()
charle.age = 4
charle.breed = 'bull dog'
charle.color = ' gray '
charle.gender = 'female'
charle.height = 1.2
charle.weight = 6
 
 
jimmy = Dog()
jimmy.age = 4
jimmy.breed = 'husky'
jimmy.color = ' yellow '
jimmy.gender = 'male'
jimmy.height = .8
jimmy.weight = 9


jimmy.bark()
jimmy.eat('fish')
jimmy.eat('dog-food')
tommy.eat('bachi hui roti')
tommy.eat('bachi hui roti')
tommy.bark()
jimmy.bark()





print(tommy.age)


print(charlie.age)

print(jimmy.age)
