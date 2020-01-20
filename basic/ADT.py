lit = ['nihao', 'weisha', 'shenme']
print(lit[1])
lit.append("qunimade")
lit.insert(2, "wojiuxihuan zheyang shuidedezhaoya ")
print(lit)
lit.pop()
lit.pop(1)
tuple1 = ("nihao?", lit)  # 有意思的是这个东西，本身不可以改变但是他的里面的列表可以。
print(tuple1)
for i in lit:
    print(i)
a = 1
age = 20
# age = input('你好你几岁了呀\n')  # input返回的类型是
if a >= 1:
    print("nihao", age)
elif a > 0:
    print('啥玩意呀')

sum1 = 0
for i in range(100):
    sum1 = sum1 + i
print(sum1)

dic1 = {'nihao': 1, 'age': 2, 'shenmedx': 1280}
dic1.pop('nihao')
dic1['tianjia'] = 820849
print(dic1)
for i in dic1:
    print(dic1[i])


def niubi(x):
    if x > 0:
        x = 1
    return a


niubi(3)


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


