import math

# for checking a number is floating point or integer
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False 

# solves the inside bracket content and returns
def insideBracket(lst,i):
    global status
    j=i+1 
    brackets=1
    while j<len(lst):
        if lst[j]=='(':
            brackets+=1
        elif lst[j]==')':
            brackets-=1

        if brackets==0:
            ret_number,status=calculation(lst[i+1:j])
            if status!='Successful':
                return lst,status
            lst[i:j+1]=ret_number
            break
        j+=1
    #print 'Inside InsideBracket'
    return lst,status

def substitute(lst):
    # Replacing the constants with their values
    for i in range(len(lst)):
        if lst[i]=='R':
            lst[i]=8.314
        elif lst[i]=='k':
            lst[i]=1.38e-23
        elif lst[i]=='pi':
            lst[i]=math.pi
        elif lst[i]=='e':
            lst[i]=math.e
        elif lst[i]=='h':
            lst[i]=6.626e-34
        elif lst[i]=='t':
            lst[i]=2
    return lst

def calculation(lst):
    global status

    # for sin ,cos , tan , log, ln , exp calculation
    i=0
    while i<len(lst)-1:
        if lst[i]=='sin':
            if lst[i+1]=='(':
                lst,status=insideBracket(lst,i+1)
                if status!='Successful':
                    return lst,status

            sin_result=math.sin(lst[i+1])
            lst[i:i+2]=[sin_result]

        elif lst[i]=='cos':
            if lst[i+1]=='(':
                lst,status=insideBracket(lst,i+1)
                if status!='Successful':
                    return lst,status
            
            cos_result=math.cos(lst[i+1])
            lst[i:i+2]=[cos_result]

        elif lst[i]=='tan':
            if lst[i+1]=='(':
                lst,status=insideBracket(lst,i+1)
                if status!='Successful':
                    return lst,status

            tan_result=math.tan(lst[i+1])
            lst[i:i+2]=[tan_result]

        elif lst[i]=='log':
            if lst[i+1]=='(':
                lst,status=insideBracket(lst,i+1)
                if status!='Successful':
                    return lst,status

            if lst[i+1]>0:
                log_result=math.log10(lst[i+1])
                lst[i:i+2]=[log_result]
            else:
                status+= 'Argument of log10 cannot be negative'
                return lst,status

        elif lst[i]=='exp':
            if lst[i+1]=='(':
                lst,status=insideBracket(lst,i+1)
                if status!='Successful':
                    return lst,status

            exp_result=math.exp(lst[i+1])
            lst[i:i+2]=[exp_result]

        elif lst[i]=='ln':
            if lst[i+1]=='(':
                lst,status=insideBracket(lst,i+1)
                if status!='Successful':
                    return lst,status

            if lst[i+1]>0:
                ln_result=math.log1p(lst[i+1])
                lst[i:i+2]=[ln_result]
            else:
                status+= '\nArgument of ln cannot be negative'
                return lst,status

        elif lst[i]=='sqrt':
            if lst[i+1]=='(':
                lst,status=insideBracket(lst,i+1)
                if status!='Successful':
                    return lst,status

            if lst[i+1]>=0:
                sqrt_result=pow(lst[i+1],0.5)
                lst[i:i+2]=[sqrt_result]
            else:
                status+='\nsquare root of negative number not possible'
                return lst,status
        elif lst[i]=='(':
            lst,status=insideBracket(lst,i)
            if status!='Successful':
                return lst,status
        i+=1

    # for power x^n
    i=0
    while i<len(lst)-1:
        if lst[i]=='^':
            if lst[i-1]<0 and lst[i+1]>-1 and lst[i+1]<1:
                status='Negative numbers cannot be raised to fractional powers'
                return lst,status
            else:
                power_result=pow(lst[i-1],lst[i+1])
                lst[i-1:i+2]=[power_result]
                i-=1
        i+=1

    # for percentage calculation
    i=0
    while i<len(lst)-1:
        if lst[i]=='%':
            if lst[i+1]!=0:
                percentage_result=(lst[i-1]/lst[i+1])*100
                lst[i-1:i+2]=[percentage_result]
                i-=1
            else:
                status+='\ndivide by zero error'
                return lst,status
        i+=1

    # for dividion of two numbers
    i=0
    while i<len(lst)-1:
        if lst[i]=='/':
            if lst[i+1]!=0:                               #97*100/5
                divide_result=lst[i-1]/lst[i+1]
                lst[i-1:i+2]=[divide_result]
                i-=1
            else:
                status+='\ndivide by zero error'
                return lst,status
        i+=1

    # for multiplication of two numbers
    i=0
    while i<len(lst)-1:
        if lst[i]=='x':
            multiply_result=lst[i-1]*lst[i+1]
            lst[i-1:i+2]=[multiply_result]
            i-=1
        i+=1  

    # Error handling cases when user types something arbitrarily
    if lst[0]=='-' and len(lst)>=2:
        lst[0:2]=[lst[1]*(-1)] 
    elif lst[0]=='+' and len(lst)>=2:
        lst[0:2]=[lst[1]]

    # for subtraction
    i=0
    while i<len(lst)-1:
        if lst[i]=='-':
            subtract_result=lst[i-1]-lst[i+1]
            lst[i-1:i+2]=[subtract_result]
            i-=1
        i+=1
    
    # for addition
    i=0
    while i<len(lst)-1:
        if lst[i]=='+':
            if isNumber(lst[i-1]) and isNumber(lst[i+1]):
                add_result=lst[i-1]+lst[i+1]
                lst[i-1:i+2]=[add_result]
                i-=1
            else:
                return lst,status
        i+=1
    return lst,'Successful'  
  
# this function takes the string and parses it into a list of numbers , operands and expressions                  
def main(txt):
    global status
    status=''
    lst=[]
    decimal=['0','1','2','3','4','5','6','7','8','9','.']

    i=0
    while i<len(txt):
        if txt[i] in decimal:
            countDot=0
            if txt[i] =='.':
                countDot+=1
            j=i+1
            if j==len(txt):
                lst.append(float(txt[i]))
            while j<len(txt):
                if txt[j] in decimal:
                    if txt[j]=='.':
                        countDot+=1
                        if countDot>1:
                            return [],status
                    j+=1
                    if j==len(txt):
                        lst.append(float(txt[i:j]))
                        i=j-1
                else:
                    lst.append(float(txt[i:j]))
                    i=j-1
                    break

        elif txt[i:i+4] in ['sqrt','asin','acos'] and i<len(txt)-4:
            lst.append(txt[i:i+4])
            i+=3
        elif txt[i:i+3] in ['sin','cos','tan','log','exp'] and i<len(txt)-3:
            lst.append(txt[i:i+3])
            i+=2
        elif txt[i:i+2] in ['pi','ln'] and i<len(txt)-1:
            lst.append(txt[i:i+2])
            i+=1
        else:
            lst.append(txt[i])
        i+=1

    # substituting the constants with their values
    #print lst
    lst=substitute(lst)
    #print lst

    # check if list is empty
    if lst==[]:
        return lst,'Empty Expression'

    # for last element checking 
    if not (isNumber(lst[len(lst)-1]) or lst[len(lst)-1]==')'):
        return lst,status

    # for correct brackets check
    i=0
    brackets=0
    while i<len(lst):
        if lst[i]=='(':
            brackets+=1
        elif lst[i]==')':
            brackets-=1
    
        if brackets<0:
            return lst,status
        i+=1
    if brackets!=0:
        return lst,status

    # for extra space removal and incorrect syntax checking
    i=0
    while i<len(lst):
        if lst[i]==' ':
            lst.pop(i)
            i-=1
        elif lst[i] in ['+','-','x','/','^','%'] and i<len(lst)-1 and lst[i+1] in ['+','-','x','/','^','%']:
            return lst,status

        elif lst[i] in ['(','+','-','x','/','^','%'] and i<len(lst)-1 and lst[i+1] in [')','x','/','^','%']:
            return lst,status

        elif lst[i] in ['sin','cos','tan','log','ln','exp','sqrt'] and i<len(lst)-1:
            if not (isNumber(lst[i+1]) or lst[i+1]=='('):
                return lst,status

        elif (lst[i]==')' or isNumber(lst[i])) and i<len(lst)-1 and (lst[i+1] in ['sin','cos','tan','sqrt','log','ln','exp','('] or isNumber(lst[i+1])):
                lst.insert(i+1,'x')

        i+=1
    #print lst   
    return calculation(lst)