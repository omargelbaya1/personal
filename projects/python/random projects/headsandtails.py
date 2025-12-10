import random

def heads_or_tails(number_of_times):
    tails_counter=0
    heads_counter=0
    while number_of_times>0:
        number_of_times-=1
        zero_or_one=random.randint(0,1)
        if zero_or_one==0:
            heads_counter+=1
        else:
            tails_counter+=1
    return print(f"heads: {heads_counter} tails: {tails_counter}")


heads_or_tails(10)
