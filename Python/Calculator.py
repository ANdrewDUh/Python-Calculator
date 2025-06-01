import math

class Calculator():
    def calculate():
        while True:
            while True:    
                num_a = input("ENTER THE FIRST NUMBER:")
                num_b = input("ENTER THE SECOND NUMBER:")
                if num_a.isnumeric() and num_b.isnumeric():
                    num_a = int(num_a)
                    num_b = int(num_b)
                    break
                print("SYNTAX ERROR")
                    
            calc = input("ENTER THE ARITHMETIC OPERATION THAT YOU WANT(+ - x /):")

            if calc == "+":
                results = num_a + num_b
            elif calc == "-":
                results = num_a - num_b
            elif calc == "x":
                results = num_a * num_b
            elif calc == "/":
                results = num_a / num_b

            print(results)

            repeat = input("DO YOU WANT TO CALCULATE AGAIN?")
            if repeat.lower() == "no":
                print("CALCULATOR SHUTDOWN")
                break
            elif repeat.lower() == "yes":
                continue
            else:
                print("SYNTAX ERROR")
                break
        
Calculator.calculate()