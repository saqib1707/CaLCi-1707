def function(lst):
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
        print lst
        if lst[i]=='/':
            divide_result=lst[i-1]/lst[i+1]
            lst[i-1:i+2]=[divide_result]
            i-=1
        i+=1

    i=0
    while i<len(lst):
        print lst
        if lst[i]=='x':
            multiply_result=lst[i-1]*lst[i+1]
            lst[i-1:i+2]=[multiply_result]
            i-=1
        i+=1   

    i=0
    while i<len(lst):
        print lst
        if lst[i]=='+':
            add_result=lst[i-1]+lst[i+1]
            lst[i-1:i+2]=[add_result]
            i-=1
        i+=1

    i=0
    while i<len(lst):
        print lst
        if lst[i]=='-':
            subtract_result=lst[i-1]-lst[i+1]
            lst[i-1:i+2]=[subtract_result]
            i-=1
        i+=1
    return lst
                    

if __name__=='__main__':
    txt=raw_input("Enter the text::")   # 456+897-534====   [456.0, '+', 897.0, '-', 534.0]
    lst=[]
    i=0
    while i<len(txt):
        #print 'i after i in range'+str(i)
        if txt[i] in ['0','1','2','3','4','5','6','7','8','9','.']:
            j=i+1
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
        else:
            lst.append(txt[i])
        i+=1
    print lst
    print(function(lst))

