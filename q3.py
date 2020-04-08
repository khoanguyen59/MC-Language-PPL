#Q3.a
def lessThan_a(n, lst):
    list1 = []
    for x in lst:
        if x < n:
            list1.append(x)
    return list1

print(lessThan_a(50, [1,55,6,2]))

#Q3.b
def lessThan_b(n, lst):
    if lst == []:
        return []
    if lst[0] < n:
        return [lst[0]] + lessThan_b(n, lst[1:])
    return lessThan_b(n, lst[1:])

print(lessThan_b(50, [1,55,6,2]))

#Q3.c
def lessThan_c(n, lst):
    return list(filter(lambda x: x < n, lst))

print(lessThan_c(50, [1,55,6,2]))