largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    
    try:
        n=int(num)
    except:
        n=-1
    
    if n==-1:
        print('Invalid input')
        continue
        
    if largest is None:
        largest=n
    elif largest<n:
        largest=n
        
        
    if smallest is None:
        smallest=n
    elif smallest>n:
        smallest=n
        
        
        
        
        
print("Maximum", largest)
print("Minimum", smallest)


