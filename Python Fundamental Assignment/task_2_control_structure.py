def classify_number():
    while True:  
        user_value = input("Enter a number (or type 'end'): ")  
        if user_value.lower() == 'end':  
            print("over and out ")  
            break  
        
        user_value=float(user_value)

        if user_value > 0:
            print("The number is positive.")
        elif user_value < 0:
            print("The number is negative.")
        else:
            print("The number is zero.")
classify_number()
input("")