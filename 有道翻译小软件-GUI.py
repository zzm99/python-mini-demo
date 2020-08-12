# -*- coding: utf-8 -*-
from tkinter import *
import urllib
import json

root = Tk()
root.title("翻译软件")
root.geometry()
Label_root = Label(root)

def translate(content):
    
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {}  
    data['type'] = 'AUTO'
    data['i']=content
    data['doctype'] = 'json' 
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_ENTER'
    
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url) 
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    response = urllib.request.urlopen(req, data)   
    res = response.read().decode('utf-8')
    target = json.loads(res)  
    return target['translateResult'][0][0]['tgt']

def Answ():# 规则函数
    
    if var_first.get() == "" : return;
    Ans.insert(END,"翻译 "+ var_first.get() + ": " + translate(var_first.get()))
    
def Clea():#清空函数
    input_num_first.delete(0,END)
    Ans.delete(0,END)
    
#----------------------输入选择框架--------------------
frame_input = Frame(root)
Label_input=Label(frame_input, text='请输入需要翻译的内容', font=('',15))
var_first = StringVar()
input_num_first = Entry(frame_input, textvariable=var_first)


#---------------------计算结果框架---------------------
frame_output = Frame(root)
Label_output=Label(frame_output, font=('',15))
Ans = Listbox(frame_output, height=5,width=30) 

#-----------------------Button-----------------------

calc = Button(frame_output,text='翻译', command=Answ)
cle = Button(frame_output,text='清空', command=Clea)

Label_root.pack(side=TOP)
frame_input.pack(side=TOP)
Label_input.pack(side=LEFT)

input_num_first.pack(side=LEFT)

frame_output.pack(side=TOP)
Label_output.pack(side=LEFT)
calc.pack(side=LEFT)
cle.pack(side=LEFT)
Ans.pack(side=LEFT)

#-------------------root.mainloop()------------------

root.mainloop()

