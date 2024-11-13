# Creating variables for each type of data
name = "pranab"
my_int = 18         
my_float = 3.14     
my_boolean = True

# Arithmetic operations and string concatenation
int_calc = my_int * 5
float_calc = my_float + 35
string_calc = name + " has submitted assignment" 

# Creating a dictionary to store the results
calc_dict = {
    "Integer Calculation": int_calc,
    "Float Calculation": float_calc,
    "String Calculation": string_calc
}

# Displaying the output
print(calc_dict)
for data_type, values in calc_dict.items():  
    print(f"{data_type}: {values}")
    input("")
