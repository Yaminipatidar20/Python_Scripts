# Simple game in python

print("Hi, welcome to Yamini's quiz!")
print("Try to get as many questions correct as possible...")

totalQuestions = 4
score = 0

ans = input('1. Who is the developer of python language ? ')

if ans.lower() == 'guido van rossum':
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('2. What is my age? ')

if ans == "21":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('3.Which is the World best country? ')

if ans.lower() == "india":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


ans = input('4.Which is the best version of python ? ')

if ans.lower() == "python 3":
    print('Correct!')
    score += 1
else:
    print('Incorrect')


print("Thank you for playing, you got " + str(score) + ' questions correct!' )
percent = (score/totalQuestions) * 100
print("Mark: " + str(int(percent)) + '%')

if percent >= 50:
    print('Nice! You passed!')
else:
    print('Better luck next time')