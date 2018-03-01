lis = ['1','100','111','2']

def my_func(x):
    var = int(x)
    return var % 2

print (max(lis, key=lambda x:int(x)))

print (min(lis, key=lambda x:my_func(x)))
