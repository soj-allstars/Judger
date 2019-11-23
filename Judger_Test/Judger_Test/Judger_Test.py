import json
import subprocess
import os
import sys
from multiprocessing import Process

fileName = "test.cpp"
CpfileName = r".\test.exe"

def forprint(temp):
    for i in temp:
        print(i)


def CompileCode():
    subprocess.call(["g++","-g",fileName,"-o",CpfileName])
    print("cp over ---")

    with open('output.txt','w') as Out_f: 
        p = subprocess.Popen([CpfileName],stdout=Out_f)   
        p.communicate() 
    print("run over --")


def ComparedWithAnswer():
    with open('output.txt','r') as Out_f:
        with open('answer.txt','r') as Ans_f:
            Out = Out_f.read()
            Ans = Ans_f.read()
            if(Out == Ans): 
                print("true")
            else:
                print("false")
def Init():
    InitByOS()

def InitByOS():
    global CpfileName
    MyOs = sys.platform
    if(MyOs =="linux"):
        CpfileName = r"./test.out"
   




if __name__ == '__main__':
    


    with open("testjson.json",'r') as load_f:
        load_dict = json.load(load_f)
        #print(load_dict)
        fo = open(fileName, "w")
        fo.write( load_dict["submitted_code"])
        fo.close()
    Init()
    CompileCode()
    ComparedWithAnswer()
    print(CpfileName)
    
    
    pass

