import math
#from calci import *

def insideBracket(exp,i):
    j=i+1 
    brackets=0
    if exp[j]=='(':
        brackets+=1
        k=j+1
        while k<len(exp):
            if exp[k]=='(':
                brackets+=1
            elif exp[k]==')':
                brackets-=1

            if brackets==0:
                ret_number=calculation(exp[j+1:k])
                exp[j+1:k]=ret_number
                break
            k+=1 
    return exp 

def calculation(lst):

    # Replacing the constants with their values
    for i in range(len(lst)):
        if lst[i]=='R':
            lst[i]=8.314
        elif lst[i]=='k':
            lst[i]=1.38e-23
        elif lst[i]=='pi':
            lst[i]=math.pi
        elif lst[i]=='e':
            lst[i]=math.exp
        elif lst[i]=='h':
            lst[i]=6.626e-34

    # for sin ,cos , tan , log, ln , exp calculation
    i=0
    while i<len(lst):
        if lst[i]=='sin':
            lst=insideBracket(lst,i)
            sin_result=math.sin(lst[i+2])
            lst[i:i+4]=[sin_result]
        elif lst[i]=='cos':
            lst=insideBracket(lst,i)
            cos_result=math.cos(lst[i+2])
            lst[i:i+4]=[cos_result]
        elif lst[i]=='tan':
            lst=insideBracket(lst,i)
            tan_result=math.tan(lst[i+2])
            lst[i:i+4]=[tan_result]
        elif lst[i]=='log':
            lst=insideBracket(lst,i)
            if lst[i+2]>0:
                log_result=math.log10(lst[i+2])
                #print log_result
                lst[i:i+4]=[log_result]
                #print lst
            else:
                status= 'Argument of log10 cannot be negative'
                return [status]
                #answer_label.setText('Argument of log10 cannot be negative')
        elif lst[i]=='exp':
            lst=insideBracket(lst,i)
            exp_result=math.exp(lst[i+2])
            lst[i:i+4]=[exp_result]

        elif lst[i]=='ln':
            lst=insideBracket(lst,i)
            if lst[i+2]>0:
                ln_result=math.log1p(lst[i+2])
                lst[i:i+4]=[ln_result]
            else:
                status='Argument of ln cannot be negative'
                return [status]
                #answer_label.setText('Argument of ln cannot be negative')

        i+=1

    """
    # for power
    i=0
    while i<len(lst):
        if lst[i]=='pow':
            j=i+1
            while lst[j]!=',':
                j+=1
            lst[i+2:j]=calculation(lst[i+2:j])
            j=i+1
            while lst[j]!=')':
                j+=1
            lst[i+4:j]=calculation(lst[i+4:j])

            power_result=pow(lst[i+2],lst[i+4])
            lst[i:i+6]=[power_result]
        i+=1
    """

    # for sqrt
    i=0
    while i<len(lst):
        if lst[i]=='sqrt':
            lst=insideBracket(lst,i)
            if lst[i+2]>0:
                sqrt_result=pow(lst[i+2],0.5)
                lst[i:i+4]=[sqrt_result]
        i+=1

    # for solving inside brackets
    brackets=0
    i=0
    while i<len(lst):
        if lst[i]=='(':
            brackets+=1
            j=i+1
            while j<len(lst):
                if lst[j]=='(':
                    brackets+=1
                elif lst[j]==')':
                    brackets-=1

                if brackets==0:
                    ret_number=calculation(lst[i+1:j])
                    lst[i:j+1]=ret_number
                    break
                j+=1
        i+=1

    # for power x^n
    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='^':
            power_result=pow(lst[i-1],lst[i+1])
            lst[i-1:i+2]=[power_result]
            i-=1
        i+=1

    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='%':
            percentage_result=(lst[i-1]/lst[i+1])*100
            lst[i-1:i+2]=[percentage_result]
            i-=1
        i+=1


    # for divide
    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='/':
            if lst[i+1]!=0:                               #97*100/5
                divide_result=lst[i-1]/lst[i+1]
                lst[i-1:i+2]=[divide_result]
                i-=1
            else:
                status='divide by zero error'
                return [status]
        i+=1

    # for multiplication
    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='x':
            multiply_result=lst[i-1]*lst[i+1]
            lst[i-1:i+2]=[multiply_result]
            #print 'hey'+str(lst)
            i-=1
        i+=1  

    if lst[0]=='-':
        lst[0:2]=[lst[1]*(-1)] 

    # for subtraction
    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='-':
            subtract_result=lst[i-1]-lst[i+1]
            lst[i-1:i+2]=[subtract_result]
            #print 'yo'+str(lst)
            i-=1
        i+=1
    

    # for addition
    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='+':
            add_result=lst[i-1]+lst[i+1]
            lst[i-1:i+2]=[add_result]
            i-=1
        i+=1
    return lst

    
                    
def main(txt):
    #print txt
    global status
    status = 'good'
    lst=[]
    """
    i=1
    if txt[0]=='-' and txt[1] in ['0','1','2','3','4','5','6','7','8','9','.']:
        while txt[i] in ['0','1','2','3','4','5','6','7','8','9','.']:
            i+=1
        lst.append(txt[0:i])
    elif txt[0]=='-' and txt[1:4] in ['pow','sin','cos','tan','exp']:
    """

    i=0
    while i<len(txt):
        if txt[i] in ['0','1','2','3','4','5','6','7','8','9','.']:
            j=i+1
            if j==len(txt):
                lst.append(float(txt[i]))
            while j<len(txt):
                if txt[j] in ['0','1','2','3','4','5','6','7','8','9','.']:
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
        elif txt[i:i+2] in ['pi','ln'] and i<len(txt)-2:
            lst.append(txt[i:i+2])
            i+=1

        else:
            lst.append(txt[i])
        i+=1
    print lst
    return calculation(lst)

