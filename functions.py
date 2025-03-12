#function to return sum of numbers in a nested loop
def nestsum(input_num1,input_num2):
    sum=0
    for i in input_num1:
        for j in input_num2:
            sum+=j
        return sum
        break
num1=2,3,5,6,3
num2=5,6,3,6,3
print(nestsum(num1,num2))
#function to print max min values in nested loop    
def function_max(n,n1):
    for i in n:
        for j in range(len(n1)):
            max=n1[j]
            if j>max:
                max=j
        return max
num1=2,3,6,3
num2=8,5,3,4,6,9
print(function_max(num1,num2))


def function_min(n,n1):
    min_value=9
    for i in n:
        for j in range(len(n1)):
            if n1[j]<min_value:
                min_value=n1[j]
        return min_value
num1=2,3,6,3
num2=8,5,3,4,6,9
print(function_min(num1,num2))        
       
        