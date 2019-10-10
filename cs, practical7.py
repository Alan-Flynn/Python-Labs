'''
CS102 Programming Semester 2
Example Code - David Smyth
'''

def multMatrices(m1,m2):
    '''look up Python's numpy module for a proper implementation. Assuming that no. of elements per row 
    and no. of elements per column is consistent for matrix 1 and matrix 2, will return the product
    of matrix 1 and matrix 2'''

    if(len(m1[0])!=len(m2)):
        print("Matrix dimensions do not match")
        return

    else:
        #read a book on the basics of multiplying matrices if not sure what's going on here
        #mxn matrix multiplied by nxk matrix results in mxk matrix
        returnMatrix=[[0 for x in range(len(m2[0]))] for y in range(len(m1))]
        print(returnMatrix)
        #for each row in matrix 1 (m)

        for i in range(len(m1)):
            #for each column in matrix 2 (k)
            for j in range(len(m2[0])):
                # for each column in the return Matrix (n)
                for k in range(len(m2)):
                    #update the i, j posision in the return matrix
                    returnMatrix[i][j]+=m1[i][k]*m2[k][j]

        return returnMatrix
        
def binaryPowerMatrixPositive(matrix,powerValue,iteration=0):
    '''A function that will find a matrix raised to a power (powerValue). The key thing to notice is that this
    function determines the order in which the operations are carried out. Note that replacing * with + gives an
    algorithm that will now multiply number by powerValue. In an abstract sense, * can be replaced with any 
    associative binary operator. (Associativity essentially means that (ab)c=a(bc) e.g. multiplication, addition.)
    This function makes use of the fact that any number has a unique binary expansion. 
    '''
    #any number raised to the power zero is 1 (because number^0=number^x-x=number^x*number^-x=number^x*(1/number^x)=1)
    #base case

    if (powerValue==0):
        print('Completed in ', iteration, 'iterations.')
        return [[1,0,0],[0,1,0],[0,0,1]]
    #if the powerValue is divisible by two, then rewrite number*powerValue as (number^2)^(powerValue/2) = (number*number)^(powerValue/2) e.g. 2^6=(2^2)^3

    elif (powerValue%2==0):
        return binaryPowerMatrixPositive(multMatrices(matrix,matrix),powerValue/2,iteration+1)
    #if the powerValue is odd, then rewrite as number*(number*number)^(powerValue-1)/2 e.g. 3^5=3*((3^2)^2)=3*(3*3)^2

    else:
        return multMatrices(matrix,binaryPowerMatrixPositive(multMatrices(matrix,matrix),(powerValue-1)/2,iteration+1))

#first fibonacci number is zero
#second fibonacci number is one
#then we get recurrence relation:
#f_i+1=f_i+f_i-1
#f_i=f_i+0
#write this as a linear system

fibolucciMatrix=[[1,1,1],[1,0,0],[0,1,0]]

#i.e.                     (1 1 1) * (f_i)    =(f_i+f_i-1) =(f_i+1)
#  fibolucciMatrix:       (1 0 0)   (f_i-1)  =(f_i)       =(f_i)
#                         (0 1 0)   (f_i-2)  =(f_i-1)     =(f_i-1)

#To get the 3rd, 2nd & 1st fibolucci number, we now just need to apply fibolucciMatrix to the vecor(1,0,0),
#representing the 1st and 0th fibonacci numbers.
#Then to get the 3rd & 2nd fibonacci numbers, apply fibonacci matrix the the previous result to move i along by one value (as seen above)

#Since matrix multiplication is associative, finding the i_th fibolucci number corresponds to finding  
#fibolucciMatrix(fibolucciMatrix(fibolucciMatrix(..i times ..fibolucciMatrix * (1))))
#                                                                              (1)
#                                                                              (0)
#which is the same as fibolucciMatrix^i 
#Matrix multiplication is associative, so we can use the binary powering alogrithm to do this for us efficiently

#(challenge: how much more efficienly than an iterative version?)

#EXAMPLE: FINDING THE 5TH fibolucci NUMBER, 57th fibolucci NUMBER and the 93rd fibolcci NUMBER

print (multMatrices(binaryPowerMatrixPositive(fibolucciMatrix,5),[[1],[1],[0]]))
print ("The 57th, 58th and 59th fibolucci numbers are", multMatrices(binaryPowerMatrixPositive(fibolucciMatrix,57),[[1],[1],[0]]), "\n")
print ("The 93rd 94th and 95th fibolucci numbers are", multMatrices(binaryPowerMatrixPositive(fibolucciMatrix,93),[[1],[1],[0]]))

def power(number, powerValue, method='binary'):
    '''number is the desired number to power. (real number)
    powerValue is the amount of times number will be multiplied with itself (integer)
    method is the method by which the the powered number is found (binary, iterative or recursive)
    '''
    method=method.lower()
    availableMethods={'binary': binaryPowerPositive, 'iterative':powerIterative, 'recursive': powerRecursive}
    #ensure that method is valid

    if (method not in ['binary', 'iterative', 'recursive']):
        print('Method must be one of binary, iterative, recursive.')
        return

    #check that powerValue is an integer, currently can't deal with non-integer power values
    if (int(powerValue)!=powerValue):
        print('This function can only use integer values of powerValue')
        return

    #if the powerValue is less than zero, then 1/(number^powerValue) needs to be returned. Use the method requested by the user
    elif (powerValue<0):

        return 1/availableMethods[method](number, abs(powerValue))

    else:
        return availableMethods[method](number, powerValue)

def binaryPowerPositive(number,powerValue,iteration=0):
    '''A function that will find a number raised to a power (powerValue). The key thing to notice is that this
    function determines the order in which the operations are carried out. Note that replacing * with + gives an
    algorithm that will now multiply number by powerValue. In an abstract sense, * can be replaced with any 
    associative binary operator. (Associativity essentially means that (ab)c=a(bc) e.g. multiplication, addition.)
    This function makes use of the fact that any number has a unique binary expansion. 
    '''
    #any number raised to the power zero is 1 (because number^0=number^x-x=number^x*number^-x=number^x*(1/number^x)=1)
    #base case

    if (powerValue==0):
        print('Completed in %d iterations'%iteration) # print('Completed in ', iteration, 'iterations.')
        return 1

    #if the powerValue is divisible by two, then rewrite number*powerValue as (number^2)^(powerValue/2) = (number*number)^(powerValue/2) e.g. 2^6=(2^2)^3

    elif (powerValue%2==0):
        return binaryPowerPositive(number*number,powerValue/2,iteration+1)
    #if the powerValue is odd, then rewrite as number*(number*number)^(powerValue-1)/2 e.g. 3^5=3*((3^2)^2)=3*(3*3)^2

    else:
        return number*binaryPowerPositive(number*number,(powerValue-1)/2,iteration+1)
        
def powerIterative(number, powerValue, iteration=0):

    returnValue=1

    for i in range(0,powerValue):
        returnValue=returnValue*number
        iteration+=1

    print('Completed in %d iterations'%iteration) #print('Completed in ', iteration, 'iterations.')
    return returnValue    

def powerRecursive(number, powerValue, iteration=0):

    if powerValue==0:

        print('Completed in %d iterations'%iteration) # print('Completed in ', iteration, 'iterations.')
        return 1
    else:
        return number*powerRecursive(number,powerValue-1, iteration+1)

numberToPower=100
import time

p=900

for method in ['binary', 'iterative', 'recursive']:
    t1=time.time()
    power(numberToPower, p, method)
#    print('Using method', method,' to calculate ', numberToPower,'^',p,' took ', round(time.time()-t1,5), 'seconds.')
    print('Using method: %s to calculate: %d ^ %d took %5f seconds\n'%(method,numberToPower,p,round(time.time()-t1,5))) 
#Stack overflow answer on why the stack overflows!:

#==============================================================================
# #Question: What is the maximum recursion depth in Python, and how to increase it?
#==============================================================================

#==============================================================================
# Answer: It is a guard against a stack overflow, yes. Python (or rather, the CPython implementation) doesn't
#  optimize tail recursion, and unbridled recursion causes stack overflows. You can change the recursion
#  limit with sys.setrecursionlimit, but doing so is dangerous -- the standard limit is a little conservative,
#  but Python stackframes can be quite big. Python isn't a functional language and tail recursion is not a
#  particularly efficient technique. Rewriting the algorithm iteratively, if possible, is generally a better idea.
#==============================================================================












