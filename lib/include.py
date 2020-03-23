func=['put','putln','input','if','while']
opes=['+','-','*','/','(',')','^']
logs=['==','<','<=','>','>=','!=']
var=[['PI',3.1415926]]
iflag2=0

def isfunc(line):
    ret=[]
    if line[line.__len__()-1:line.__len__()]==')':
        try:
            line=line[0:line.__len__()-1]
            pendis=line.split('(')[1]
            line=line.split('(')[0]
            each=''
            for each in func:
                if line==each:
                    break
                else:
                    each=''
            if each!='':
                ret.append(each)
                ret.append(pendis)
                return ret
            else:
                return 0
        except:
            return 0
    else:
        if line[line.__len__() - 1:line.__len__()] == '{':
            try:
                line = line[0:line.__len__() - 2]
                pendis = line.split('(')[1]
                line = line.split('(')[0]
                each = ''
                for each in func:
                    if line == each:
                        break
                    else:
                        each = ''
                if each != '':
                    ret.append(each)
                    ret.append(pendis)
                    return ret
                else:
                    return 0
            except:
                return 0
        else:
            return 0

def isdef(line):
    if line[0:4]=='var ':
        try:
            vs = line[4:line.__len__()].split('|')
            ret=0
            for v in vs:
                try:
                    if v.split('=')[1].split('\n')[0][0:1] == "'" and v.split('=')[1].split('\n')[0][
                                                                         v.split('=')[1].split('\n')[0].__len__() - 1:
                                                                         v.split('=')[1].split('\n')[
                                                                             0].__len__()] == "'":
                        var.append([v.split('=')[0].split('\n')[0],
                                    v.split('=')[1].split('\n')[0][1:v.split('=')[1].split('\n')[0].__len__() - 1]])
                    else:
                        var.append([v.split('=')[0].split('\n')[0], v.split('=')[1].split('\n')[0]])
                    ret=1
                except:
                    var.append([v.split('\n')[0], '[Undefined]'])
                    ret=1
            return ret
        except:
            line=line[4:line.__len__()]
            try:
                if line.split('=')[1].split('\n')[0][0:1]=="'" and line.split('=')[1].split('\n')[0][
                                                                   line.split('=')[1].split('\n')[0].__len__()-1:
                                                                   line.split('=')[1].split('\n')[
                                                                       0].__len__()]=="'":
                    var.append([line.split('=')[0].split('\n')[0],
                                line.split('=')[1].split('\n')[0][1:line.split('=')[1].split('\n')[0].__len__()-1]])
                else:
                    var.append([line.split('=')[0].split('\n')[0],line.split('=')[1].split('\n')[0]])
                return 1
            except:
                var.append([line.split('\n')[0],'[Undefined]'])
                return 1
    else:
        return 0

def isass(line):
    fb=line.split('=')
    try:
        fb[1]=fb[1].split("'")[1]
    except:
        pass
    flag = 0
    for i in range(var.__len__()):
        if var[i][0] == fb[0]:
            if fb[1].isdigit()!=True:
                retu=op(fb[1])
                if retu!='bad':
                    ret=eval(retu)
                    if ret!='bad':
                        var[i][1] = ret
                        flag = 1
                    else:
                        flag = 0
                else:
                    flag = 0
            else:
                var[i][1] = fb[1].split('\n')[0]
                flag = 1
            break
    if flag != 0:
        return 1
    else:
        return 0

def op(line):
    l=line.split(' ')
    bflag=0
    for i in range(l.__len__()):
        if l[i] not in opes:
            if l[i].isdigit()!=True:
                flag=0
                for j in range(var.__len__()):
                    if var[j][0]==l[i]:
                        l[i]=var[j][1]
                        flag=1
                        break
                if flag==1:
                    bflag=1
                else:
                    bflag=0
            else:
                bflag=1
        else:
            pass
    if bflag==1:
        return ''.join(map(str,l))
    else:
        return 'bad'

def log(line):
    l=line.split(' ')
    bflag=0
    for i in range(l.__len__()):
        if l[i].isdigit()!=True and l[i] not in logs and l[i][0:1]!="'" and l[i][l[i].__len__()-1:l[i].__len__()]!="'":
            flag=0
            for j in range(var.__len__()):
                if var[j][0]==l[i]:
                    try:
                        if var[j][1].isdigit()==True:
                            l[i] = var[j][1]
                            flag = 1
                            break
                        else:
                            l[i] = "'"+var[j][1]+"'"
                            flag = 1
                            break
                    except:
                        l[i] = str(var[j][1])
                        flag = 1
                        break
            if flag==1:
                bflag=1
            else:
                try:
                    test=list(l[i])
                    l2=' '.join(test)
                    ret=op(l2)
                    if ret=='bad':
                        return 'bad'
                    else:
                        l[i]=str(eval(ret))
                except:
                    return 'bad'
        else:
            bflag=1
    if bflag==1:
        return ''.join(l)
    else:
        return 'bad'

def islogic(line):
    ret=log(line)
    if ret!='bad':
        try:
            if eval(ret)==True:
                return 'New1234567890'
            else:
                return 'bad'
        except:
            return 'bad'
    else:
        return 'bad'

def blanks(line):
    s=0
    for each in line:
        if each==' ':
            s=s+1
        else:
            break
    return s

def syntax(line):
    global iflag2
    if iflag2>=1 and (line=='{' or line=='}else{'):
        iflag2=0
    if line=='}else{' and iflag2==0:
        return 'Newelse1234567890'
    ret=isfunc(line)
    if ret!=0:
        if ret[0]=='put':
            try:
                puts=ret[1].split(';')
                retus=['Put']
                for each in puts:
                    if each[0:1] == "'" and each[each.__len__() - 1:each.__len__()] == "'":
                        retus.append(each[1:each.__len__() - 1])
                    else:
                        flag = ''
                        for each2 in var:
                            if each2[0] == each:
                                flag = each2[1]
                                break
                        if flag != '':
                            if flag == '[Undefined]':
                                retus.append('')
                            else:
                                retus.append(flag)
                        else:
                            retu=op(each)
                            if retu!='bad':
                                retus.append(eval(retu))
                            else:
                                retus.append('Error1234567890')
                return retus
            except:
                if ret[1][0:1]=="'" and ret[1][ret[1].__len__()-1:ret[1].__len__()]=="'":
                    return ret[1][1:ret[1].__len__()-1]
                else:
                    flag=''
                    for each in var:
                        if each[0]==ret[1]:
                            flag=each[1]
                            break
                    if flag!='':
                        if flag=='[Undefined]':
                            return ''
                        else:
                            return flag
                    else:
                        retu = op(ret[1])
                        print(retu)
                        if retu != 'bad':
                            return eval(retu)
                        else:
                            return 'Error1234567890'
        elif ret[0]=='putln':
            try:
                puts=ret[1].split(';')
                retus=['Putln']
                for each in puts:
                    if each[0:1] == "'" and each[each.__len__() - 1:each.__len__()] == "'":
                        retus.append(each[1:each.__len__() - 1])
                    else:
                        flag = ''
                        for each2 in var:
                            if each2[0] == each:
                                flag = each2[1]
                                break
                        if flag != '':
                            if flag == '[Undefined]':
                                retus.append('')
                            else:
                                retus.append(flag)
                        else:
                            retu=op(each)
                            if retu!='bad':
                                retus.append(eval(retu))
                            else:
                                retus.append('Error1234567890')
                return retus
            except:
                if ret[1][0:1]=="'" and ret[1][ret[1].__len__()-1:ret[1].__len__()]=="'":
                    return ret[1][1:ret[1].__len__()-1]
                else:
                    flag=''
                    for each in var:
                        if each[0]==ret[1]:
                            flag=each[1]
                            break
                    if flag!='':
                        if flag=='[Undefined]':
                            return ''
                        else:
                            return flag
                    else:
                        retu = op(ret[1])
                        print(retu)
                        if retu != 'bad':
                            return eval(retu)
                        else:
                            return 'Error1234567890'
        elif ret[0]=='input':
            try:
                inps=ret[1].split(',')
                retus=['Input']
                for each in inps:
                    flag = 0
                    i = 0
                    for i in range(var.__len__()):
                        if var[i][0] == each:
                            var[i][1] = input().split('\n')[0]
                            flag = 1
                            break
                    if flag == 1:
                        retus.append('1')
                    else:
                        retus.append('0')
                return retus
            except:
                flag = 0
                i = 0
                for i in range(var.__len__()):
                    if var[i][0] == ret[1]:
                        var[i][1]=input().split('\n')[0]
                        flag=1
                        break
                if flag == 1:
                    return 'Input1234567890'
                else:
                    return 'Error1234567890'
        elif ret[0]=='if':
            if islogic(ret[1])=='New1234567890':
                iflag2=1
                return 'New1234567890'
            else:
                return 'Pass1234567890'
        elif ret[0]=='while':
            if islogic(ret[1])=='New1234567890':
                return 'Newwhile1234567890'
            else:
                return 'Pass1234567890'
    elif isdef(line)==1:
        return 'Pass1234567890'
    elif isass(line)==0:
        return 'Pass1234567890'
    elif line=='break':
        return 'Break1234567890'
    elif line=='continue':
        return 'Continue1234567890'