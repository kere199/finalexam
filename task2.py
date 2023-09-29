def rec_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + rec_sum(lst[1:])


print(rec_sum([1,2,5]))