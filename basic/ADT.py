
lit = ['nihao','weisha','shenme']
print(lit[1])
lit.append("qunimade")
lit.insert(2,"wojiuxihuan zheyang shuidedezhaoya ")
print(lit)
lit.pop()
lit.pop(1)
tuple1=("nihao?",lit)#有意思的是这个东西，本身不可以改变但是他的里面的列表可以。
print(tuple1)
for i in lit:
    print(i)
