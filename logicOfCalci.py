def function(lst):

    # Replacing the constants with their values
    for i in range(len(lst)):
        if lst[i]=='R':
            lst[i]=8.314
        elif lst[i]=='k':
            lst[i]=1.38e-23
        elif lst[i]=='pi':
            lst[i]=float(22/7)
        elif lst[i]=='e':
            lst[i]=2.727

    # for power
    i=0
    while i<len(lst):
        if lst[i]=='pow':
            j=i+1
            while lst[j]!=',':
                j+=1
            lst[i+2:j]=function(lst[i+2:j])
            j=i+1
            while lst[j]!=')':
                j+=1
            lst[i+4:j]=function(lst[i+4:j])

            power_result=pow(lst[i+2],lst[i+4])
            lst[i:i+6]=[power_result]
        i+=1

    # for sqrt
    i=0
    while i<len(lst):
        if lst[i]=='sqrt':
            j=i+1 
            brackets=0
            if lst[j]=='(':
                brackets+=1
                k=j+1
                while k<len(lst):
                    if lst[k]=='(':
                        brackets+=1
                    elif lst[k]==')':
                        brackets-=1

                    if brackets==0:
                        ret_number=function(lst[j+1:k])
                        lst[j+1:k]=ret_number
                        break
                    k+=1
            sqrt_result=pow(lst[i+2],0.5)
            lst[i:i+4]=[sqrt_result]
        i+=1

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
                    ret_number=function(lst[i+1:j])
                    lst[i:j+1]=ret_number
                    break
                j+=1
        i+=1

    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='p':
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


    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='/':
            if lst[i+1]!='0':                               #97*100/5
                divide_result=lst[i-1]/lst[i+1]
                lst[i-1:i+2]=[divide_result]
                i-=1
            else:
                print 'divide by zero error'
                return lst
        i+=1

    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='x':
            multiply_result=lst[i-1]*lst[i+1]
            lst[i-1:i+2]=[multiply_result]
            i-=1
        i+=1   

    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='+':
            add_result=lst[i-1]+lst[i+1]
            lst[i-1:i+2]=[add_result]
            i-=1
        i+=1

    i=0
    while i<len(lst):
        #print lst
        if lst[i]=='-':
            subtract_result=lst[i-1]-lst[i+1]
            lst[i-1:i+2]=[subtract_result]
            i-=1
        i+=1
    return lst
                    

#if __name__=='__main__':
    #txt=raw_input("Enter the text::")   # 456+897-534====   [456.0, '+', 897.0, '-', 534.0]
def main(txt):
    print txt
    lst=[]
    i=0
    while i<len(txt):
        #print 'i after i in range'+str(i)
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
                    #print 'i after i=j-1'+str(i) 
                    break

        elif txt[i:i+4] in ['sqrt','asin','acos'] and i<len(txt)-4:
            lst.append(txt[i:i+4])
            i+=3
        elif txt[i:i+3] in ['pow','sin','cos','tan'] and i<len(txt)-3:
            lst.append(txt[i:i+3])
            i+=2
        elif txt[i:i+2] in ['pi'] and i<len(txt)-2:
            lst.append(txt[i:i+2])
            i+=1

        else:
            lst.append(txt[i])
        i+=1
    print lst
    return function(lst)

