### Bill APP

import random

### Variables
number_guests = 0
list_guest = []
sum_bill = 0
individual_pay = 0
flag = False
iflucky = False
lucky_person_name = ''
final_dict = {}

def intro():
    global flag
    try:
        number_guests = int(input('Hello! How many guest will be here? '))
        if number_guests < 1:
           print('No one joing the party')
           flag = False

        else:
           flag = True
        return number_guests
    except ValueError:
        print('You can print only int here')
        flag = False


def guestlist (number_guests):
    counter = 1
    for i in range(number_guests):
        name = input(f'name of the guest {counter}: ')
        counter +=1
        list_guest.append(name)
    return list_guest

def billing():
    global flag
    global sum_bill
    try:
        sum_bill = int(input('How much is the bill? '))
        if sum_bill > 0:
            flag = True
        else:
            print('party was free')
            flag = False
    except ValueError:
        print("Sorry ! the input should be int")
        flag = False
    return sum_bill

def lucky_fun (list_guest):
    global flag
    global lucky_person
    global iflucky
    if len(list_guest) > 1:
            activating = input('do you want to use lucky function: y/n ')
            paying_guests = 0
            if activating == 'y':
                paying_guests = len(list_guest)-1
                lucky_person_num = random.randint(1,len(list_guest))
                lucky_person = list_guest[lucky_person_num-1]
                print(f'{lucky_person} is the lucky person')
                iflucky = True
            elif activating == 'n':
                paying_guests = len(list_guest)
            else:
                print('sorry, the input can be only "y" or "n"')
                flag = False
    else:
        print('Sorry, no lucky function for one client')
        paying_guests = len(list_guest)
    return paying_guests

def paying_calc(bill, number_payer):
    summ = round(bill/number_payer, 2)
    return summ
def creating_dict(names,sums):
    global final_dict
    final_dict = final_dict.fromkeys(names, sums)
    if iflucky:
        final_dict[lucky_person] = 0
    return final_dict


def party():
   step_one = intro()
   if flag:
       list_guest = guestlist(step_one)
       sum_bill = billing()
       if flag:
           payers = lucky_fun(list_guest)
           if flag:
               calc_results = paying_calc(sum_bill, payers)
               finals = creating_dict(list_guest, calc_results)
               print(finals)



party()



