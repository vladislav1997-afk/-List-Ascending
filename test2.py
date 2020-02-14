from random import randint

xs = [randint(-100, 100) for i in range(20)];
#xs = [-94,-94,-94,-94, -93, -82, -65, -65, -58, -34, -30, -13, -7, -5, -1, 5, 22, 22, 42, 48, 50, 67, 77, 87, 88, 99 ,99 ,99 ,99]
xs = [-1,-1,0,0]
xs.sort()
new_xs = xs
print(xs)
xs.sort()
new_ls = []
lst = []
f = []

def result(xs):
    for j, k in enumerate(xs):
        try:
            if (xs[j + 1] - xs[j]) != 1:
                new_xs.insert(j + 1, '|')
        except:
            k = 0
    for index, l in enumerate(new_xs):
        number = index
    for num, i in enumerate(new_xs):
        f.append(i)
        if num == number:
            new_ls.clear()
            if (str(f[0]) == str(f[-1])) and (len(f) == 1):
                ls = f[0]
                lst.append(ls)
            else:
                new_ls.append(str(f[0]))
                new_ls.append(str(f[-1]))
                ls = "-".join(new_ls)
                lst.append(ls)
        elif i == '|' and num != number:
            del f[-1]
            new_ls.clear()
            if (str(f[0]) == str(f[-1])) and (len(f) == 1):
                ls = f[0]
                lst.append(ls)
            else:
                new_ls.append(str(f[0]))
                new_ls.append(str(f[-1]))
                ls = "-".join(new_ls)
                lst.append(ls)
            f.clear()
    return(lst)

#while(1):
print(result(xs))



