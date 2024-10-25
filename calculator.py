
input_1 = (input("What is your first number? "))
try:
    val_1=int(input_1)
    input_2 = (input("What is your second number? "))
    try:
        val_2=int(input_2)
        input_3 = input("What is your third number? Type Done if you have only inputted those numbers. ")
        if input_3 == ("Done"):
            select = int(input("Select one of these operations:\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division \n"))
            if select == 1:
                number = val_1 + val_2
                print(number)
            elif select == 2:
                number = val_1 - val_2
                print(number)
            elif select == 3:
                number = val_1 * val_2
                print(number)
            elif select == 4:
                number = val_1 / val_2
                print(number)
        else:
            try:
                val_3=int(input_3)
                input_4 = input("What is your fourth number? Type Done if you have only inputted those numbers. ")
                if input_4 == ("Done"):
                    select = int(input("Select one of these operations:\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division \n"))
                    if select == 1:
                        number = val_1 + val_2 + val_3
                        print(number)
                    elif select == 2:
                        number = val_1 - val_2 - val_3
                        print(number)
                    elif select == 3:
                        number = val_1 * val_2 * val_3
                        print(number)
                    elif select == 4:
                        number = val_1 / val_2 / val_3
                        print(number)
                else:
                    try:
                        val_4=int(input_4)
                        input_5 = input("What is your fifth number? Type Done if you have only inputted those numbers. ")
                        if input_5 == ("Done"):
                            select = int(input("Select one of these operations:\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division \n"))
                            if select == 1:
                                number = val_1 + val_2 + val_3 + val_4
                                print(number)
                            elif select == 2:
                                number = val_1 - val_2 - val_3 - val_4
                                print(number)
                            elif select == 3:
                                number = val_1 * val_2 * val_3 * val_4
                                print(number)
                            elif select == 4:
                                number = val_1 / val_2 / val_3 / val_4
                                print(number)
                        else:
                            try:
                                val_5=int(input_5)
                                select = int(input("Select one of these operations:\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division \n"))
                                if select == 1:
                                    number = val_1 + val_2 + val_3 + val_4 + val_5
                                    print(number)
                                elif select == 2:
                                    number = val_1 - val_2 - val_3 - val_4 - val_5
                                    print(number)
                                elif select == 3:
                                    number = val_1 * val_2 * val_3 * val_4 * val_5
                                    print(number)
                                elif select == 4:
                                    number = val_1 / val_2 / val_3 / val_4 / val_5
                                    print(number)
                            except ValueError:
                                print("Invalid Input")
                    except ValueError:
                        print("Invalid Input")
            except ValueError:
                print("Invalid Input")
    except ValueError:
        print("Invalid Input")
except ValueError:
    print("Invalid Input")

