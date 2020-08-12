# -*- coding: utf-8 -*-
import urllib
import json

while True:
    content = input("input : ")
    if content == 'q': 
        break
    
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_ENTER'
    
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url);
    response = urllib.request.urlopen(req, data);
    res = response.read().decode('utf-8')
    
    target = json.loads(res)
    
    print("output: " + target['translateResult'][0][0]['tgt'])
    
    