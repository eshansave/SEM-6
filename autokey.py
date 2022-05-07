from email import message
import re

def AutoKeyEncrypt(msg,key):
    index=0;
    cText=''
    for letter in msg:
        num=ord(letter)-65
        newno=(num+(ord(key[index%len(key)])-65))%26
        cText+=chr(newno+65)
        index+=1
    print (cText)
    return cText
def AutoKeyDecrypt(cText,key):
    index=0;
    dText=''
    for letter in cText:
        num=ord(letter)-65
        newno=(num-(ord(key[index%len(key)])-65))%26
        dText+=chr(newno+65)
        index+=1
    print (dText)
    return dText

msg="hello world"
key="jash"
msg=re.sub(r'[^A-Z]','',msg.upper())
key=re.sub(r'[^A-Z]','',key.upper())
keysize=len(key)
msgindex=0
while keysize<len(msg):
    key+=msg[msgindex]
    keysize+=1
    msgindex+=1
print(msg)
print(key)
cText=AutoKeyEncrypt(msg,key)
AutoKeyDecrypt(cText,key)
