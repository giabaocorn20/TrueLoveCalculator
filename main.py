
name1 = input('What is your name?\n')
name2 = input('what is their name?\n')

bothNames = name1.lower() +name2.lower()

t = bothNames.count('t')
r = bothNames.count('r')
u = bothNames.count('u')
e = bothNames.count('e')

true = t + r + u + e

l = bothNames.count('r')
o = bothNames.count('o')
v = bothNames.count('v')
e = bothNames.count('e')

love = l + o + v + e 

trueLove = int(str(true) + str(love))

if (trueLove < 10) or (trueLove > 90): 
    print(f"Your love scrore is {trueLove} you go toghether like coke and mentos")
elif (trueLove >= 40) and (trueLove <=50):
    print(f"Your love score is {trueLove}, you are alright toghether")
else: 
    print(f"Your score is {trueLove}")
