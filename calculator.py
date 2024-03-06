
while True:
    t = int(input("Choose ( + = 0, - = 1, * = 2, / = 3 ): "))
    if t == 55:
        print("Thanks")
        break
    num1 = int(input("Num 1: "))
    num2 = int(input("Num 2: "))

    if t == 0:
        result = int(num1 + num2)
        print(str(num1) + "+" + str(num2) + " = " + str(result))
    elif t == 1:
        result = int(num1 - num2)
        print(str(num1) + "-" + str(num2) + " = " + str(result))
    elif t == 2:
        result = int(num1 * num2)
        print(str(num1) + "*" + str(num2) + " = " + str(result))
    elif t == 3:
        result = float(num1 / num2)
        if result.is_integer():
            result = int(result)
        print(str(num1) + "/" + str(num2) + " = " + str(result))
    else:
        print("Wrong")

        Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5").place(x=10,
                                                                                                                   y=100)


