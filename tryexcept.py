try: 
    #k = 5//0 # raises divide by zero exception. 
    #print(k) 
    h = "i" + 3
    print(h)
    
# handles zerodivision exception     
except ZeroDivisionError:    
    print("Can't divide by zero") 
except TypeError:
    print("Invalid Types")
        
finally: 
    # this block is always executed  
    # regardless of exception generation. 
    print('This is always executed')  

#output: Invalid Types
#        This is always executed

try: 
    k = 5//0 # raises divide by zero exception. 
    print(k) 
    #h = "i" + 3
    #print(h)
    
# handles zerodivision exception     
except ZeroDivisionError:    
    print("Can't divide by zero") 
except TypeError:
    print("Invalid Types")
        
finally: 
    # this block is always executed  
    # regardless of exception generation. 
    print('This is always executed')  

#output: Can't divide by zero
#        This is always executed 

from time import sleep
while True:
    try:
        print("Try and stop me")
        sleep(1)
    except:
        print("Don't stop me now, I'm having such a good time!")

#output: Try and stop me : over and over again every second
