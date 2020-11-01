def hello_world():
    while True:
        exit_1 = "exit"
        kaki = input("Please Print strings only : ").casefold()
        if kaki == exit_1:
                break
        print("This is Your print:>>>>>>>>>>> {0} ".format(kaki))
        with open("koko.txt", 'a') as k:
                k.write(kaki)


hello_world()
