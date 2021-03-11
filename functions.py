def customFunction():
    pass

def func_1(*args):
    print(args);

def func_2(**kwargs):
    print(kwargs);


func_1('hello', 'world')
func_2(s1='hello', s2='world')
