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
		
		
		
#calculating harmonic mean of data

def Harmonic_Mean(numbers):
    for x in numbers:
        if x < 0:
            print('One of your numbers is negative. Negative numbers not allowed for harmonic mean')
            return False
    
    sumOfnumbers = 0
    
    for i in numbers:
        sumOfnumbers += (1/i)
        
    harmonic_mean = (len(numbers)/sumOfnumbers)
    
    print("The harmonic mean of your data is ", harmonic_mean)

print(Harmonic_Mean(numbers))