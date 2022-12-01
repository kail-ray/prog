from argparse import *
from random import *
from string import *
class Password():
    def __init__(self,kol,dlin,one):
        self.kol=kol
        self.dlin=dlin
        self.one=one
    def ggg(self):
        z=[]
        pas=''
        alf=ascii_lowercase+ascii_uppercase+digits 
        if args.kol==0 and  args.ctr==0 and args.prop==0 and args.num==0 and args.one!=0 and args.dlin==0:        #работает если задан параметр -о
            return (''.join(choices(alf,k=args.one)))
        elif args.kol==0 and  args.ctr==0 and args.prop==0 and args.num==0 and args.one==0 and args.dlin==0:
            return('введите -h для получения справки по работе программы')
        else:
            if args.kol==0:
                if args.ctr!=0:
                    pas+=''.join(choices(ascii_lowercase,k=args.ctr))
                if args.prop!=0:
                    pas+=''.join(choices(ascii_uppercase,k=args.prop))
                if args.num!=0:
                    pas+=''.join(choices(digits,k=args.num))
                return(''.join(sample(pas,len(pas))))
            elif self.kol!=0 and (args.ctr!=0 or args.prop!=0 or args.num!=0)and self.dlin==0:
                for i in range (args.kol):
                    if args.ctr!=0:
                        pas=''.join(choices(ascii_lowercase,k=args.ctr))
                    if args.prop!=0:
                        pas+=''.join(choices(ascii_uppercase,k=args.prop))
                    if args.num!=0:
                        pas+=''.join(choices(digits,k=args.num))
                    z.append(''.join(sample(pas,len(pas))))
                return(z)
            elif self.kol!=0 and (args.ctr==0 and args.prop==0 and args.num==0) and self.dlin==0:
                for i in range (args.kol):
                    z.append(''.join(choices(alf,k=5)))
                return(z)
            elif self.kol!=0 and (args.ctr==0 and args.prop==0 and args.num==0) and self.dlin!=0:
                for i in range (args.kol):
                    z.append(''.join(choices(alf,k=args.dlin)))
                return(z)
parser=ArgumentParser( prog='Password Generator.',description='Generate any number of passwords with this tool.')
parser.add_argument('-k','--kol', type=int, help='введите кол-во генерируемых паролей. команда используется как одна так и всвязке с "-d", "-с", "-p", "-n" ',default=0)
parser.add_argument('-d','--dlin',type=int, help='введите длины генерируемых паролей. Команда не может использоваться одна, только совместно с "-k"', default=0)
parser.add_argument('-o','--one',type=int, help='если срочно нужно сгенерировать 1 пароль введи "-o" и количество символов в пароле, команда "-o" не работает с остальными командами',default=0)
parser.add_argument('-c','--ctr', type=int, help='введите "-c" для использовния в алфавите строчных символов и их кол-во. Команда работает как одна, так и с "-k", "-p", "-n"',default=0)
parser.add_argument('-p','--prop', type=int,help='введите "-p" для использовния в алфавите прописных символов и их кол-во. Команда работает как одна, так и с "-k", "-c", "-n"', default=0)
parser.add_argument('-n','--num', type=int,help='введите "-n" для использовния в алфавите цифр и их кол-во. Команда работает как одна, так и с "-k", "-c", "-p"', default=0)
args=parser.parse_args()
str_pas=(Password(args.kol,args.dlin,args.one).ggg())
print(str_pas)
f1=open('Password.txt','w')
f1.write(str(str_pas))
f1.close()