def card_func(i):
    mylist = []
    for x in str(i):
        mylist.append(int(x))

    mylist.reverse()
    # print(mylist)

    final_list = []
    for x in range(len(mylist)):
        if x % 2 == 0:
            final_list.append(mylist[x] * 2)
        else:
            final_list.append(mylist[x])
    # print(final_list)


    sum_digits = []
    for num in final_list:
        if num > 10:
            sum_digits.append(num - 9)
        else:
            sum_digits.append(num)
    # print(sum_digits)

    sum = 0
    for x in sum_digits:
        sum = sum + x
    
    if sum % 10 == 0 :
        return 0
    else:
        return 10 - (sum % 10)
    

print(card_func(431571900679177))