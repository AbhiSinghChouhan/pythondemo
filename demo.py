def div(x,y):
    print(x/y)


def smart_div(func):    
    def inner(x,y):
        if x<y:
            x,y = y,x
        return func(x,y)
    return inner

div = smart_div(div) 
div(2,4)
