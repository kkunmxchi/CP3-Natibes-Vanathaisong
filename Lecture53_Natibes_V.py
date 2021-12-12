def vatCal(totalPrice):
    result = totalPrice+(totalPrice*7/100)
    return result

x = int(input("Input your x : "))
print("Vat :",vatCal(x))