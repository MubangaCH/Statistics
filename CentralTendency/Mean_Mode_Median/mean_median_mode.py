# simple code to calculate mean, median, and mode of data


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

#calculating the mean

print('You entered ', len(numbers), 'numbers')
 

def mean_of_numbers(numbers):
    sumOfnumbers = 0      
    
    for i in numbers: 
        
        sumOfnumbers += i     
    
    Mean = sumOfnumbers / len(numbers)
    
    print('The mean of your data is', Mean)
    return
    

sorted_numbers = sorted(numbers)

#calculating the median
def middle_number(sorted_numbers):
    
    
    if len(sorted_numbers) % 2 == 1:
        Median = sorted_numbers[int((len(sorted_numbers)-1)/2)]
    else:
        Median = (sorted_numbers[int((len(sorted_numbers)/2))] + sorted_numbers[int((len(sorted_numbers)/2)-1)])/2
    print('The median of your data is ', Median)
    return 


#calculating the mode
def most_frequent(sorted_numbers):
    most = max(list(map(sorted_numbers.count, sorted_numbers)))
    mode = list(set(filter(lambda x: sorted_numbers.count(x) == most, sorted_numbers)))
    
    if len(mode) == len(sorted_numbers):
        return " Your data has no mode"
        
    if len(mode) >= 2:
        print("Your data does not have a unique mode. The following numbers appear with the same frequency;", mode)
        
        return 
        
    if len(mode) == 1:
        print('The mode of your data is;', mode)
        return 
    
print(mean_of_numbers(numbers)) 
print(middle_number(sorted_numbers))
print(most_frequent(sorted_numbers))
      
