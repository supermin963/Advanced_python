
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 调用的时候扔进去一个数组的话，请也使用*。
