import sys
import matplotlib.pyplot as plt
print("Enter at least three variables separated by a space")

if __name__ == '__main__':
    input = sys.stdin.read()
    
    n= list(map(int, input.split()))
    
import numpy


from scipy import stats as st


#n=(33,29,32,55,54,46,45)

SL=sorted(n)
fvalues=[]

for i in range(1,len(SL)+1):

    f= (i-0.375)/((len(SL) + 0.25))
    fvalues.append(f)

zvalue=st.norm.ppf(fvalues)

#calculate the r coefficient by using the sorted data and their z scores and use that table to determine
print("your variables in ascending order are", SL)
print("expected z scores for your variables are", zvalue) 
print ("the correlation coefficeint is", numpy.corrcoef(SL,zvalue)[0,1])

#compare with the table and suggest to the person if there's a linear relationship or not.
x = SL
y = zvalue
plt.scatter(x,y, label='Scatterplot', color='k')
plt.xlabel('x variables')
plt.ylabel('expected z scores')
plt.legend()
plt.show()

print("More references on this website. http://www.unco.edu/nhs/mathsci/facstaff/powers/m550/ContinuousDistributions/pdf/7.4.1%20Assessing%20Normality.pdf")
