from random import randint
import time
import os

class typing_speed:
    path = ""
    content = None
    lencontent = 0;

    def __init__(self):
        self.path = "/usr/share/dict/words"
        try:
            filetoread = open(self.path,"r")
        except:
            print("file:",self.path,"does not exist.")
        if(filetoread==None):
            print("file:",self.path,"does not exist.")
        self.content = filetoread.read().split('\n')
        self.lencontent = len(self.content)
    
    
        
    def getwordramdoly(self):
        if(self.content == None):
            print("the content can not be accessed because its value equal None")
        else:
            r = randint(0,self.lencontent-1)
            return self.content[r]

    def check(self,word):
        timestart = time.time()
        wordinput = input()
        timeclose = time.time()
        list = wordinput.split('\n')
        
        if(len(list)>=1):
            list = list[0].split(' ')
        else:
            check(word)
        if(len(list)>=1):
            return (list[0]==word,timeclose-timestart)
        else:
            check(word)
            
    def printlist(self,l):
        os.system('clear')
        str=""
        for i in range(len(l)):
            str+=l[i]+" "
        print(str)
    
    def update_list(self,l):
        for i in range(len(l)-1):
            l[i]=l[i+1]
        l[len(l)-1]= self.getwordramdoly()
        return l
    
    def create_list(self,size):
        l = [""]*size
        for i in range(size):
            l[i]= self.getwordramdoly()
        return l

def main(limitime):
    time = 0.0
    nb_word = 0
    nb_char = 0
    nb_correct = 0
    typsped = typing_speed()
    l = typsped.create_list(10)
    while time < float(limitime):
        typsped.printlist(l)
        bool,time_chk = typsped.check(l[0])
        if(bool):
            nb_correct+=1
            nb_char+=len(l[0])
            time+=time_chk
        nb_word+=1
        l = typsped.update_list(l)

    os.system('clear')
    print("char per minute:",float(nb_char)/float(time)*60)
    print("word per minute:",float(nb_correct)/float(time)*60)
    print("correctness:",(float(nb_correct)/float(nb_word))*100,"%")

main(120)


