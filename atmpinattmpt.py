actual=2387
tries=3
for i in range(3):
    atmpin=int(input())
    print(atmpin)
    if actual==atmpin:
        print("successfully logged in")
        break
    else:
        if tries==1:
            print("your account got blocked,try after 24 hr")
        else:
            print("Incorrect password,you are left with",tries,"attempt")
    tries=tries-1
