while True:
    try:
        
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            continue
            
        print(f"{num1} / {num2} = {num1 / num2:.3f}")
        break
        
    except ValueError:
        print("Error: Enter valid numbers.")