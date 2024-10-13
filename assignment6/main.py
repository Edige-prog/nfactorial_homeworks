# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def Exercise_1():
    num1 = 15
    num2 = 25
    print(num1+num2)

def Exercise_2():
    s = "Some Words"
    s = s[::-1]
    print(s)

def Exercise_3():
    s = "Hello World!"
    print(len(s))

def Exercise_4():
    s = "First part!"
    s2 = "Second part!"
    result = s + s2
    print(result)

def Exercise_5():
    character1 = 'a'

    if(character1 in 'aeiou'):
        print(f"Charecter {character1} is a vowel")
    else:
        print(f"Charecter '{character1}' is a consonant")

def Exercise_6():
    title = "BestSeries"
    modified_title = title[len(title) - 1] + title[1:len(title) - 1] + title[0]
    print(modified_title)

def Exercise_7():
    word = "melody"
    print(word.upper())

def Exercise_8():
    x = 5
    y = 10
    area = x * y
    print(area)

def Exercise_9():
    number = 29
    print(bool(number % 2 == 0))

def Exercise_10():
    phrase = 'hellohellohello'
    print(phrase[:3])

def Exercise_11():
    first_name = 'Alexander'
    last_name = 'Hamilton'
    print(f'{first_name} {last_name}')

def Exercise_12():
    text = 'Interesting'
    print(text[2:6])

def Exercise_13():
    numeric_string = '283'
    print(int(numeric_string))

def Exercise_14():
    sound = 'beep'
    sound = sound * 3
    print(sound)

def Exercise_15():
    dividend = 80
    divisor = 7

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f'quotient: {quotient} and remainder: {remainder}')

def Exercise_16():
    num1 = 120
    num2 = 8
    print(f'division: {num1 / num2}')

def Exercise_17():
    name = "Christopher"
    print(f"Occurrences of r = {name.count('r')}")

def Exercise_18():
    statement = 'He said "I am the best"'
    print(statement)

def Exercise_19():
    lyrics = """In the end
it doesn't even matter
(Lost to the echo)"""
    print(lyrics)

import math
def Exercise_20():
    base = 3
    exponent = 5
    result = math.pow(base, exponent)
    print(int(result))

def Exercise_21():
    palindrome_test = "deified"
    print(str(palindrome_test == palindrome_test[::-1]))

def Exercise_22():
    word1 = "dust"
    word2 = 'stud'
    print(str(sorted(word1) == sorted(word2)))





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Exercise_1()
    Exercise_2()
    Exercise_3()
    Exercise_4()
    Exercise_5()
    Exercise_6()
    Exercise_7()
    Exercise_8()
    Exercise_9()
    Exercise_10()
    Exercise_11()
    Exercise_12()
    Exercise_13()
    Exercise_14()
    Exercise_15()
    Exercise_16()
    Exercise_17()
    Exercise_18()
    Exercise_19()
    Exercise_20()
    Exercise_21()
    Exercise_22()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
