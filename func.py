from dev import max_num
def max_input_length(number, max_num):
    if int(number)> max_num or int(number)<0:
        print(f'''Bro {number}?? thats beyond rules!! number should be 0<N<=100
              Tryy Again!! ''')
        val1 = input('Enter again lil bro')
        return max_input_length(val1 , max_num )
    else:
        print(f'okay!!{number} thats solid')
        print()
        return number
    
def advantage():
    adv= input("other advantage : ")
    val = int(input(f"Enter advantage value for {adv} :  "))
    val= max_input_length(val, max_num)
    print()
    return adv, val

def disadvantage():
    dis_adv= input("other disadvantage : ")
    dis_val = int(input(f"Enter disadvantage value for {dis_adv} :"))
    dis_val= max_input_length(dis_val, max_num)
    print()
    return dis_adv, dis_val

def calculate(val1,disval1,val2,disval2):
    sum1 = 0
    for i in range (10):
        sum1 = sum(x if x is not None else 0 for x in val1 )
        dif1 = sum(x if x is not None else 0 for x in disval1 )
        sum2 = sum(x if x is not None else 0 for x in val2 )
        dif2 = sum(x if x is not None else 0 for x in disval2 )
        score1 = sum1 - dif1
        score2 = sum2 - dif2
        return score1, score2
    
def percentage (val1,val2):
    per= ((val1-val2)/val2)*100
    return per