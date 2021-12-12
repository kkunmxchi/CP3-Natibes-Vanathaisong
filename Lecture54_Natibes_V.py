def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "kkunmxchi" and passwordInput == "Pack_123":
        print("Success")
        return showMenu()
    else:
        print("Username or Password wrong")
        print("Login Try again")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input("Please select the menu >>"))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return priceCalculator()

def vatCalculator():
    price = int(input("Price(THB) : "))
    vat = 7
    result = price + (price * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    vat = 7
    totalprice = price1+price2
    result = totalprice + (totalprice * vat/100)
    return result

print(login())