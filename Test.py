from lib.include import *
import sys

lines=[]
iflag=0
eflag=0
wflag=0
wlog=[]
wf2=0
li=0
i=1
try:
    if len(sys.argv)<=1: f=open('test.tst','r')
    else: f=open(sys.argv[1],'r')
except:
    print('Error when opening sourse file.')
    exit(0)
for l in f:
    if iflag==0 and eflag==0 and wflag==0:
        ret=syntax(l.split('\n')[0])
        if ret=='Error1234567890' or ret=='Break1234567890' or ret=='Continue1234567890':
            print('[Error]Line',i,',syntax error!')
        elif ret=='New1234567890':
            iflag+=1
        elif ret=='Newelse1234567890':
            eflag+=1
        elif ret=='Newwhile1234567890':
            wflag+=1
            wlog.append(isfunc(l.split('\n')[0])[1])
        elif ret!='Pass1234567890' and ret!='Input1234567890':
            if type(ret)!=list:
                if ret!=None:
                    print(ret,end='')
            else:
                if ret[0]=='Input':
                    if '0' in ret:
                        print('[Error]Line', i, ',syntax error!')
                elif ret[0]=='Put':
                    if 'Error1234567890' in ret:
                        print('[Error]Line', i, ',syntax error!')
                    else:
                        for each in ret[1:]:
                            print(each,end='')
                elif ret[0] == 'Putln':
                    if 'Error1234567890' in ret:
                        print('[Error]Line', i, ',syntax error!')
                    else:
                        for each in ret[1:]:
                            print(each)
    elif iflag>=1:
        if l.split('\n')[0]=='}' and iflag-1==blanks(l.split('\n')[0])/4:
            iflag-=1
            print(iflag)
            continue
        elif l.split('\n')[0]=='}else{' and iflag-1==blanks(l.split('\n')[0])/4:
            iflag-=1
            continue
        if iflag==blanks(l)/4:
            ret = syntax(l.split('\n')[0].strip())
            if ret == 'Error1234567890' or ret=='Break1234567890' or ret=='Continue1234567890':
                print('[Error]Line', i, ',syntax error!')
            elif ret == 'New1234567890':
                iflag +=1
            elif ret=='Newelse1234567890':
                eflag+=1
            elif ret == 'Newwhile1234567890':
                wflag += 1
                wlog.append(isfunc(l.split('\n')[0])[1])
            elif ret != 'Pass1234567890' and ret != 'Input1234567890':
                if type(ret) != list:
                    if ret != None:
                        print(ret,end='')
                else:
                    if ret[0] == 'Input':
                        if '0' in ret:
                            print('[Error]Line', i, ',syntax error!')
                    elif ret[0] == 'Put':
                        if 'Error1234567890' in ret:
                            print('[Error]Line', i, ',syntax error!')
                        else:
                            for each in ret[1:]:
                                print(each,end='')
                    elif ret[0] == 'Putln':
                        if 'Error1234567890' in ret:
                            print('[Error]Line', i, ',syntax error!')
                        else:
                            for each in ret[1:]:
                                print(each)
    elif eflag>=1:
        if l.split('\n')[0]=='}' and eflag-1==blanks(l.split('\n')[0])/4:
            eflag-=1
            continue
        if eflag==blanks(l)/4:
            ret = syntax(l.split('\n')[0].strip())
            if ret == 'Error1234567890' or ret=='Break1234567890' or ret=='Continue1234567890':
                print('[Error]Line', i, ',syntax error!')
            elif ret == 'New1234567890':
                iflag +=1
            elif ret=='Newelse1234567890':
                eflag+=1
            elif ret == 'Newwhile1234567890':
                wflag += 1
                wlog.append(isfunc(l.split('\n')[0])[1])
            elif ret != 'Pass1234567890' and ret != 'Input1234567890':
                if type(ret) != list:
                    if ret != None:
                        print(ret,end='')
                else:
                    if ret[0] == 'Input':
                        if '0' in ret:
                            print('[Error]Line', i, ',syntax error!')
                    elif ret[0] == 'Put':
                        if 'Error1234567890' in ret:
                            print('[Error]Line', i, ',syntax error!')
                        else:
                            for each in ret[1:]:
                                print(each,end='')
                    elif ret[0] == 'Putln':
                        if 'Error1234567890' in ret:
                            print('[Error]Line', i, ',syntax error!')
                        else:
                            for each in ret[1:]:
                                print(each)
    elif wflag>=1:
        if wflag==blanks(l.split('\n')[0])/4:
            lines.append(l)
            ret = syntax(l.split('\n')[0].strip())
            if ret == 'Error1234567890':
                print('[Error]Line', i, ',syntax error!')
            elif ret == 'New1234567890':
                iflag +=1
            elif ret=='Newelse1234567890':
                eflag+=1
            elif ret == 'Newwhile1234567890':
                wflag += 1
                wlog.append(isfunc(l.split('\n')[0])[1])
            elif ret=='Break1234567890' or ret=='Continue1234567890':
                continue
            elif ret != 'Pass1234567890' and ret != 'Input1234567890':
                if type(ret) != list:
                    if ret != None:
                        print(ret,end='')
                else:
                    if ret[0] == 'Input':
                        if '0' in ret:
                            print('[Error]Line', i, ',syntax error!')
                    elif ret[0] == 'Put':
                        if 'Error1234567890' in ret:
                            print('[Error]Line', i, ',syntax error!')
                        else:
                            for each in ret[1:]:
                                print(each,end='')
                    elif ret[0] == 'Putln':
                        if 'Error1234567890' in ret:
                            print('[Error]Line', i, ',syntax error!')
                        else:
                            for each in ret[1:]:
                                print(each)
        else:
            if l.split('\n')[0] == '}':
                while True:
                    if eval(log(wlog[wflag - 1])) == False:
                        wf2 -= 1
                        break
                    else:
                        l2 = lines[li]
                        if wflag == blanks(l2.split('\n')[0]) / 4:
                            ret = syntax(l2.split('\n')[0].strip())
                            if ret == 'Error1234567890':
                                print('[Error]Line', i, ',syntax error!')
                            elif ret == 'New1234567890':
                                iflag += 1
                            elif ret == 'Newelse1234567890':
                                eflag += 1
                            elif ret == 'Newwhile1234567890':
                                wflag += 1
                                wlog.append(isfunc(l.split('\n')[0])[1])
                            elif ret == 'Break1234567890':
                                break
                            elif ret=='Continue1234567890':
                                continue
                            elif ret != 'Pass1234567890' and ret != 'Input1234567890':
                                if type(ret) != list:
                                    if ret != None:
                                        print(ret,end='')
                                else:
                                    if ret[0] == 'Input':
                                        if '0' in ret:
                                            print('[Error]Line', i, ',syntax error!')
                                    elif ret[0] == 'Put':
                                        if 'Error1234567890' in ret:
                                            print('[Error]Line', i, ',syntax error!')
                                        else:
                                            for each in ret[1:]:
                                                print(each,end='')
                                    elif ret[0] == 'Putln':
                                        if 'Error1234567890' in ret:
                                            print('[Error]Line', i, ',syntax error!')
                                        else:
                                            for each in ret[1:]:
                                                print(each)
                        li += 1
                        if li >= lines.__len__():
                            li = 0

    i=i+1