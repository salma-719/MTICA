def div(a,b):
    assert( isinstance(a,int) or isinstance(a,float)), \
            'Argument should be either Integer or Flost'
    assert (b!=0),"Divisiion by zero is not defined"
    return a/b

try:
    print(div(55,0))
except AssertionError as obj:
    print(obj)
try:
    print(div(20,3))
except AssertionError as obj:
    print(obj)
try:
    print(div(100,20))
except AssertionError as obj:
    print(obj)

