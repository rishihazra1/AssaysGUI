def get_float(input_prompt):
    while True:
        input_holder = input(input_prompt)
        try:
            input_holder = float(input_holder)
            return input_holder
        except:
            ValueError
            if input_holder == "no":  # enables user to exit loops
                return input_holder
            print("Invalid input. Enter valid input of type: " + "float") 

def get_int(input_prompt):
    while True:
        input_holder = input(input_prompt)
        try:
            input_holder = int(input_holder)
            return input_holder
        except:
            ValueError
            print("Invalid input. Enter valid input of type: " + "int")
            
def get_y_or_no(input_prompt):
    while True:
        inupt_holder = input(input_prompt + " (y/n)\n")
        if inupt_holder == "y" or inupt_holder == "n":
            break
        else:
            print("Invalid input. Enter y or n.")
    return inupt_holder

