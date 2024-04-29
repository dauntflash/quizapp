
import random


question1='''.General Knowledge:
What is the capital of France?
A) London
B) Paris
C) Berlin
D) Rome
'''

question2='''.Science:
What is the chemical symbol for water?
A) Wt
B) H2O
C) O2
D) CO2
'''
question3='''.Geography:
Which of the following is the longest river in the world?
A) Nile
B) Amazon
C) Yangtze
D) Mississippi
'''
question4='''.History:
Who was the first President of the United States?
A) Thomas Jefferson
B) George Washington
C) Abraham Lincoln
D) John Adams
'''

question5='''.Mathematics:
What is the square of 9?
A) 72
B) 81
C) 64
D) 49
'''
question6='''.Literature:

Who wrote the play "Romeo and Juliet"?
A) William Shakespeare
B) Jane Austen
C) Charles Dickens
D) Mark Twain
'''
question7='''.Technology:

What does HTML stand for in web development?
A) HyperText Markup Language
B) High-Level Text Management Language
C) Hyperlink and Text Markup Language
D) Home Tool Markup Language
'''
question8='''.Movies:

In which movie did Leonardo DiCaprio win his first Academy Award for Best Actor?
A) Inception
B) The Wolf of Wall Street
C) Titanic
D) The Revenant
'''
question9='''.Sports:

What is the national sport of Japan?
A) Baseball
B) Sumo wrestling
C) Judo
D) Soccer
'''
question10='''.Music:

Who is known as the "Queen of Pop"?
A) Madonna
B) Beyoncé
C) Lady Gaga
D) Rihanna
'''

questions=[question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,]
answers=['B','B','B','B','B','A','A','D','B','A']

length=len(questions)

x=1

guess=[]


def limits():
    max_num=length-1
    min_num=0
    question=random.randint(min_num,max_num)
    return question

def choice(value,choose):
    print(value,questions[choose])
k=0
j=0
r=0
def checker(right):
    correct_answer=answers[right].upper()
    user_answer=input("Enter your answer: ").upper()
    while True:
        if user_answer in ('A','B','C','D'):
            if user_answer!=correct_answer:
                print("You are wrong,, the correct answer is",correct_answer)
                return False
            else:
                print("You are right.")
                return True
            break
        else:
            user_answer=input("Invalid input, try again(A,B,C,D): ").upper()
while x<=length:
    number=limits()
    while number not in guess:
        choice(x,number,)
        if checker(number):
            r+=1
        guess.append(number)
        x+=1

print("Game over! you had a total of",r,"correct guesses.")
