from random import randint

xs = [randint(-100, 100) for i in range(20)];
#xs = [1,2,3,8,9,10]
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
    number = new_xs.index(new_xs[-1])
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

print(result(xs))

