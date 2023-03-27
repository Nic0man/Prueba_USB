x=5

def funcion1():
    global x
    x=x+10
    print("variable funcion 1 = ",x )

def main():
    global x
    x=x+2
    print('variable main = ',x)
    funcion1()
    

main()
