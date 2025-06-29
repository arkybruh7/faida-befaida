import func
from dev import max_num, max_dataset
topic1_val = [None]*max_dataset
topic1_adv = [None]*max_dataset
topic1_dis_val = [None]*max_dataset
topic1_dis_adv = [None]*max_dataset
topic2_val = [None]*max_dataset
topic2_adv = [None]*max_dataset
topic2_dis_val = [None]*max_dataset
topic2_dis_adv = [None]*max_dataset
topic1 = input('Whats the first topic you wanna discuss? ')
topic2 = input("thats spicy! nextt what you wanna compare it to? ")

#TOPIC 1
#ADVANTAGE
print(f'''okay cool! Now you have to enter the like advantage of {topic1} and assign a certain value
      eg: {topic1} is too cool assign 10 points 
      max you can assign 100 points''' )
topic1_adv[0] = input(f'Whats the first advantage you can think for {topic1}? ')
topic1_val[0] = int(input("Assign its value! Like how big of a deal it is?"))
topic1_val[0] = func.max_input_length(topic1_val[0], max_num)
c= 0
ask = input("Anymore advantages y/n  :")
if ask == "y" or "Y":
    choice = "y"
    while choice == "Y" or choice=="y":
        c = c +1
        topic1_adv[c],topic1_val[c]= func.advantage()
        print(f'Advantage is {topic1_adv[c]} and value is {topic1_val[c]}')
        print()
        choice = input("any more advantages y/n ")
print(f'SN   |  advantage   | value')
for i in range (c+1):
        print(f'{i+1} |  {topic1_adv[i]}    | {topic1_val[i]}')

#DISADVANTAGE

print(f"okay now time for disadvantage of {topic1}")
topic1_dis_adv[0] = input(f'Whats the first disadvantage you can think for {topic1}? ')
topic1_dis_val[0] = int(input("""Assign its value! Like how big of a bad thing  it is? 
                      100--> veryy bad 0---> not bad at all
                     """))
topic1_dis_val[0] = func.max_input_length(topic1_dis_val[0], max_num)
c= 0
ask = input("""Anymore disadvantages y/n  :""")
if ask == "y" or "Y":
    choice = "y"
    while choice == "Y" or choice=="y":
        c = c +1
        topic1_dis_adv[c],topic1_dis_val[c]= func.disadvantage()
        print(f'''disadvantage is {topic1_adv[c]} and value is {topic1_val[c]}
              ''')
        print()
        choice = input("any more disadvantages y/n ")
print(f'SN |  disadvantage   | value')
for i in range (c+1):
        print(f'{i+1} |  {topic1_dis_adv[i]}    | {topic1_dis_val[i]}')
print()

#TOPIC 2
#ADVANTAGE

print(f'''okay cool! Now you have to enter the like advantage of {topic2} and assign a certain value
      eg: {topic2} is too cool assign 10 points 
      max you can assign 100 points''' )
topic2_adv[0] = input(f'Whats the first advantage you can think for {topic2}? ')
topic2_val[0] = int(input("Assign its value! Like how big of a deal it is? :"))
topic2_val[0] = func.max_input_length(topic2_val[0], max_num)
c= 0
ask = input("Anymore advantages y/n")
if ask == "y" or "Y":
    choice = "y"
    while choice == "Y" or choice=="y":
        c = c +1
        topic1_adv[c],topic2_val[c]= func.advantage()
        print(f'Advantage is {topic1_adv[c]} and value is {topic2_val[c]}')
        choice = input("any more advantages y/n ")
print(f'SN   |  advantage   | value')
for i in range (c+1):
        print(f'{i+1} |  {topic1_adv[i]}    | {topic2_val[i]}')
print()
#DISADVANTAGE

print(f"okay now time for disadvantage of {topic2}")
topic2_dis_adv[0] = input(f'Whats the first disadvantage you can think for {topic2}? ')
topic2_dis_val[0] = int(input("""Assign its value! Like how big of a bad thing  it is? 
                      (100--> veryy bad 0---> not bad at all) :"""))
topic2_dis_val[0] = func.max_input_length(topic2_dis_val[0], max_num)
c= 0
ask = input("""Anymore disadvantages y/n   :""")
print()
if ask == "y" or "Y":
    choice = "y"
    while choice == "Y" or choice=="y":
        c = c +1
        topic2_dis_adv[c],topic2_dis_val[c]= func.disadvantage()
        print(f'''disadvantage is {topic1_adv[c]} and value is {topic2_val[c]}
              ''')
        choice = input("any more disadvantages y/n ")
print(f'SN |  disadvantage   | value')
for i in range (c+1):
        print(f'{i+1} |  {topic2_dis_adv[i]}    | {topic2_dis_val[i]}')
print(f'''

     ------------- FINAL RESULTSSS ----------
      ''')
#Calculations
a = sum(1 if item is not None else 0 for item in topic1_adv)
b = sum(1 if item is not None else 0 for item in topic1_dis_adv)
c = sum(1 if item is not None else 0 for item in topic2_adv)
d = sum(1 if item is not None else 0 for item in topic2_dis_adv)
#FINDING IF TOPIC HAS MORE ADVANTAGES OR DISADVANTAGES FOR PROPER DISPLAY
if a>=b :
      x = a
else:
        x = b
if c>=d :
      y = c
else:
        y = d
print(f""" 
_________________{topic1}_________________
""")
print(f'SN |  advantage   | value |  disadvantage   | value ')
for i in range (x):
        print(f'{i+1} |  {topic1_adv[i]}    | {topic1_val[i]} |  {topic1_dis_adv[i]}    | {topic1_dis_val[i]}')
print(f""" 
___________________________________________

      """)
print(f""" 
_________________{topic2}_________________
""")
print(f'SN |  advantage   | value |  disadvantage   | value ')
for i in range (y):
        print(f'{i+1} |  {topic2_adv[i]}    | {topic2_val[i]} |  {topic2_dis_adv[i]}    | {topic2_dis_val[i]}')
print(f""" 
__________________________________________

      """)
score1, score2 = func.calculate(topic1_val, topic1_dis_val, topic2_val, topic2_dis_val)

#TO AVOID DIVIDE BY ZERO ERROR
if score1 == 0:
      score1==1
if score2 == 0:
      score2==1
print(f""" 
___________________________________________________
""")
print(f'''so the overall score
                         for {topic1} is {score1}
                         for {topic2} is {score2}''')
print(f""" 
____________________________________________________

      """)
print(f""" 
_____________________________________________________
""")
if score1>score2:
     percent = func.percentage(score1,score2)
     print(f'{topic1} is better than {topic2} by {round(abs(percent), 2)}%')
else:
     percent = func.percentage(score2,score1)
     print(f'{topic2} is better than {topic1} by {round (abs(percent), 2)}%')
print("""
_________________by rahul shrestha____________________
""")
temp = input("press any key to exit")
