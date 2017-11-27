people = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person():
    while True:
        user_say = input("Name please: ")
        name = people.pop()
        if user_say == name:
            print('нашелся')
            
        else: 
            print("Not")

find_person()