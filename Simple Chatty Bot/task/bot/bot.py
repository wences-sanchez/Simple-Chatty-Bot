def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    ask_question()
    answer = input()
    while answer != 1:  # 1. is the correct answer
        print('Please, try again.')
        answer = input()

    print('Completed, have a nice day!')


def ask_question():
    print("Which is the world's longest river?")
    print('1. The Amazon River')
    print('2. The Danube River')
    print('3. The Nile River')
    print('4. The Mississippi River')


def end():
    print('Congratulations, have a nice day!')


greet('Christopher', '2021')
remind_name()
guess_age()
count()
# ...
end()
