def email(x):
    l = [{"name":"omar","pass":"123"},{"name":"mohamed","pass":"555"}]
    for i in l:
        if i["name"] == x:
            p = input("your pass")
            if i["pass"] == p:
                print("welcome")
                break
            else:
                print("unauth")
                break
        else:
            continue
    else :
        print("not found")
        exit()
y = input("enter your name :" )
email(y) 