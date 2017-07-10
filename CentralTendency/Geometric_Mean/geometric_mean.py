while True:
     
    try: #validates the input to make sure its numbers only.
        user_input = input("Enter numbers (exponentials accepted i.e 1e2 for 100) separated by commas: ")
        input_list = user_input.split(',')
        numbers = [float(x.strip()) for x in input_list]
           
    except ValueError:
        print("Sorry enter numbers only, separated by commas.")
        
        continue
    else:
        break

#calculating the  geometric mean

def Geometric_mean(numbers):
    
    product = 1
    
    for i in numbers:
        product *= i
    
    geometric_mean = (product)**(1/(len(numbers)))
        
    if product == 0:
        print(" Your data contains a value of zero. Please remove the zero or add a constant to all numbers.\nIf you intend to keep the zero, the geometric mean (complex number) of your data is", geometric_mean)
        
    
    if product < 0:
        print("Your data contains a negative number, please process your data further.\nIf you intend to keep the negative number, the geometric mean (complex number) of your data is", geometric_mean)
       
    
    else:    
        print('The geometeric mean of your data is', geometric_mean)
    
    return 


print(Geometric_mean(numbers))