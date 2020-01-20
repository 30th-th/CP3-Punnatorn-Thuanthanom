usernameinput = input("Usermane: ")
passwordinput = input("Password: ")
if usernameinput == "admin" and passwordinput == "1234" :
    print("Log in Success")
    print("Hello customer ")
    print("Should Product")
    print("1. Hamburgur = 5$")
    print("2. Sanwich = 3$")
    print("3. Hotdog = 2$")
    hamburgur = 5
    sanwich = 3
    hotdog = 2
    product = int(input(">>"))
    if product == 1:
        amout = int(input("Amout: "))
        print("Hamburgur ",hamburgur,"amout ",amout,"Total",hamburgur*amout,"$")
    elif product == 2:
        amout = int(input("Amout: "))
        print("Sanwich ",sanwich,"amout ",amout,"Total",sanwich*amout,"$")
    elif product == 3:
        amout = int(input("Amout: "))
        print("Hotdog ",hotdog,"amout ",amout,"Total",hotdog*amout,"$")
