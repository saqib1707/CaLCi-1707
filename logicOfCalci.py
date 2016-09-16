import math

def insideBracket(exp,i):
    global status
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
                ret_number,status=calculation(exp[j+1:k])
                exp[j+1:k]=ret_number
                break
            k+=1 
    return exp,status

def calculation(lst):
    global status
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

    # for sin ,cos , tan , log, ln , exp calculation
    i=0
    while i<len(lst)-1:
        if lst[i]=='sin':
            lst,status=insideBracket(lst,i)

            if status!='':
                return lst,status

            sin_result=math.sin(lst[i+2])
            lst[i:i+4]=[sin_result]
        elif lst[i]=='cos':
            lst,status=insideBracket(lst,i)

            if status!='':
                return lst,status

            cos_result=math.cos(lst[i+2])
            lst[i:i+4]=[cos_result]
        elif lst[i]=='tan':
            lst,status=insideBracket(lst,i)

            if status!='':
                return lst,status

            tan_result=math.tan(lst[i+2])
            lst[i:i+4]=[tan_result]
        elif lst[i]=='log':
            lst,status=insideBracket(lst,i)

            if status!='':
                return lst,status

            if lst[i+2]>0:
                log_result=math.log10(lst[i+2])
                lst[i:i+4]=[log_result]
            else:
                status+= '\nArgument of log10 cannot be negative'
                return lst,status

        elif lst[i]=='exp':
            lst,status=insideBracket(lst,i)

            if status!='':
                return lst,status

            exp_result=math.exp(lst[i+2])
            lst[i:i+4]=[exp_result]

        elif lst[i]=='ln':
            lst,status=insideBracket(lst,i)
            #print lst

            if status!='':
                return lst,status

            if lst[i+2]>0:
                ln_result=math.log1p(lst[i+2])
                lst[i:i+4]=[ln_result]
            else:
                status+='\nArgument of ln cannot be negative'
                return lst,status
                #answer_label.setText('Argument of ln cannot be negative')

        i+=1
    # for sqrt
    i=0
    while i<len(lst)-1:
        if lst[i]=='sqrt':
            lst,status=insideBracket(lst,i)

            if status!='':
                return lst,status

            if lst[i+2]>=0:
                sqrt_result=pow(lst[i+2],0.5)
                lst[i:i+4]=[sqrt_result]
            else:
                status+='\nsquare root of negative number not possible'
                return lst,status
        i+=1

    # for solving inside brackets
    brackets=0
    i=0
    while i<len(lst)-1:
        if lst[i]=='(':
            brackets+=1
            j=i+1
            while j<len(lst):
                if lst[j]=='(':
                    brackets+=1
                elif lst[j]==')':
                    brackets-=1

                if brackets==0:
                    ret_number,status=calculation(lst[i+1:j])
                    if status!='':
                        return lst,status
                    lst[i:j+1]=ret_number
                    break
                j+=1
        i+=1

    # for power x^n
    i=0
    while i<len(lst)-1:
        #print lst
        if lst[i]=='^':
            if lst[i-1]<0 and lst[i+1]>-1 and lst[i+1]<1:
                status='Negative numbers cannot be raised to fractional powers'
                return lst,status
            else:
                power_result=pow(lst[i-1],lst[i+1])
                lst[i-1:i+2]=[power_result]
                i-=1
        i+=1

    i=0
    while i<len(lst)-1:
        #print lst
        if lst[i]=='%':
            if lst[i+1]!=0:
                percentage_result=(lst[i-1]/lst[i+1])*100
                lst[i-1:i+2]=[percentage_result]
                i-=1
            else:
                status+='\ndivide by zero error'
                return lst,status

        i+=1


    # for divide
    i=0
    while i<len(lst)-1:
        #print lst
        if lst[i]=='/':
            if lst[i+1]!=0:                               #97*100/5
                divide_result=lst[i-1]/lst[i+1]
                lst[i-1:i+2]=[divide_result]
                i-=1
            else:
                status+='\ndivide by zero error'
                return lst,status
        i+=1

    # for multiplication
    i=0
    while i<len(lst)-1:
        #print lst
        if lst[i]=='x':
            print lst[i-1]
            multiply_result=lst[i-1]*lst[i+1]
            lst[i-1:i+2]=[multiply_result]
            #print 'hey'+str(lst)
            i-=1
        i+=1  

    if lst[0]=='-':
        lst[0:2]=[lst[1]*(-1)] 

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
        #print lst
        if lst[i]=='+':
            if isNumber(lst[i-1]) and isNumber(lst[i+1]):
                add_result=lst[i-1]+lst[i+1]
                lst[i-1:i+2]=[add_result]
                i-=1
            else:
                return lst,'Bad Expression'
        i+=1
    return lst,status

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False    
                    
def main(txt):
    #print txt
    #print math.log(math.sin(math.pi))
    global status
    status=''
    lst=[]

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
        elif txt[i:i+2] in ['pi','ln'] and i<len(txt)-1:
            lst.append(txt[i:i+2])
            i+=1
        else:
            lst.append(txt[i])
        i+=1

    # for extra space removal
    i=0
    while i<len(lst):
        if lst[i]==' ':
            lst.pop(i)
            i-=1
        if lst[i]==')' and i<len(lst)-1:
            if lst[i+1]=='(':
                lst.insert(i+1,'x')
            elif lst[i+1] in ['sin','cos','tan','sqrt','log','ln','exp']:
                lst.insert(i+1,'x')
        if isNumber(lst[i]) and i<len(lst)-1:
            if lst[i+1] in ['sin','cos','tan','log','ln','exp','sqrt']:
                lst.insert(i+1,'x')
        i+=1
    #print lst
    return calculation(lst)

