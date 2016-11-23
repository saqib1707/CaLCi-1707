def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False 


def main(txt):
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
        elif lst[i]==')' and i<len(lst)-1 and lst[i+1] in ['sin','cos','tan','sqrt','log','ln','exp','(']:
                lst.insert(i+1,'x')

        elif isNumber(lst[i]) and i<len(lst)-1 and lst[i+1] in ['sin','cos','tan','log','ln','exp','sqrt']:
                lst.insert(i+1,'x')

        elif lst[i]=='(' and lst[i+1]==')' and i<len(lst)-1:
            return lst,status
        i+=1
    print lst




    # for empty brackets having no arguments
    i=0
    while i<len(lst):
        if lst[i]=='(' and lst[i+1]==')':
            return lst,status
        elif lst[i]=='(':
            #lst,status=insideBracket(lst,i-1)
            if status=='Bad Expression':
                return lst,status
        elif lst[i] in ['+','-','x','/','%','^',')'] and i!=len(lst)-1:
            if lst[i+1] in ['+','-','x','/','%','^',')']:
                return lst,status
        i+=1

    if lst==[]:
        return lst,status
    
    print 'Successful'

if __name__=='__main__':
    txt=raw_input('Enter text:')
    lst,status=main(txt)
    #print lst