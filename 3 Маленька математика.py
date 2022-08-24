def function(x, y):
    a = x - y
    b = x + y
    c = x / y
    d = x * y
    print( a, b, c, d)
x = int(input())
y = int(input())
print('x =', x)
print('y =', y)
print('a = x - y', '=', x, '-', y, '=', x - y)
print('b = x + y', '=', x, '+', y, '=', x + y)
print('c = x / y', '=', x, '/', y, '=', x / y)
print('d = x * y', '=', x, '*', y, '=', x * y)