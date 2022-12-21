code = ""

def lock(passw):
    global code
    code = passw
    print("locked")

def open(passw):
    if  code == passw:
        print ("open")
    else:
        print ("wrong code")

if __name__ == "__main__":
    while True:
        print("set your password to lock:")
        passw = input()
        lock(passw)
        print("Enter your password open:")
        passw = input()
        open(passw)



