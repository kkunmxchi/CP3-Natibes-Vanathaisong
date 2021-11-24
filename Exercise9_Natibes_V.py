usernameinput = input("Username : ")
passwordinput = input("Password : ")

while usernameinput != "kkunmxchi" or passwordinput != "Pack_123":
    print("Username or Password is wrong Please try agian")
    print("")
    usernameinput = input("Username : ")
    passwordinput = input("Password : ")

print("Login Success")
print("")

print("---Welcome To Mxchi Shop---")
print("1.Nike Kyrie 7 5500THB ")
print("2.Nike Air Force 1 5400THB ")
print("3.Vans old skool 2400THB ")
print("4.Adidas stan smith 3200THB ")
print("5.Balenciaga triple s 33000THB ")
print("----------------------------")

quantity = int(input("Please select the quantity you wish to purchase : "))
while quantity > 5:
    print("Limited selection of products")
    print("")
    quantity = int(input("Please select the quantity you wish to purchase : "))

if quantity >= 1 and quantity <= 5:
    if quantity == 1:
        price1 = int(input("Enter price1 amount : "))
        print("Total :", price1, "THB")
    elif quantity == 2:
        price1 = int(input("Enter price1 amount : "))
        price2 = int(input("Enter price2 amount : "))
        print("Total :", price1 + price2, "THB")
    elif quantity == 3:
        price1 = int(input("Enter price1 amount : "))
        price2 = int(input("Enter price2 amount : "))
        price3 = int(input("Enter price3 amount : "))
        print("Total :", price1 + price2 + price3, "THB")
    elif quantity == 4:
        price1 = int(input("Enter price1 amount : "))
        price2 = int(input("Enter price2 amount : "))
        price3 = int(input("Enter price3 amount : "))
        price4 = int(input("Enter price4 amount : "))
        print("Total :", price1 + price2 + price3 + price4, "THB")
    elif quantity == 5:
        price1 = int(input("Enter price1 amount : "))
        price2 = int(input("Enter price2 amount : "))
        price3 = int(input("Enter price3 amount : "))
        price4 = int(input("Enter price4 amount : "))
        price5 = int(input("Enter price5 amount : "))
        print("Total :", price1 + price2 + price3 + price4 + price5, "THB")
else:
    print("Thank you")
print("See you again")
