def suma(a,b):
    return a+b

def login (username: str) -> str:
    if username == "admin":
        return " logged"
    else:
        return " not logged"



if __name__=="__main__":
    print(suma(2,3))
    print(login(username="admin"))

