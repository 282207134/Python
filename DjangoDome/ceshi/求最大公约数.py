def gcd(num1,num2):
    x=num1
    y=num2
    while(x!=y):
        if(x>y):
            x=x-y
        else:
            y=y-x
    return print('最大公约数为:',x)

if __name__ == '__main__':
    print('----- -求最大公约数------')
    a=int(input('请输入第一个数字'))
    b=int(input('请输入第二个数字'))
    gcd(a,b)