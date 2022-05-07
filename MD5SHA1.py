import hashlib
def runthehash(str1):
    print(str1.encode())
    resultmd5 = hashlib.md5(str1.encode())
    resultsha1 = hashlib.sha1(str1.encode())
    print(f'String:{str1}\n\nMD5 Hashed:\nbyteformat:     {resultmd5.digest()}\nhexadecimalFormat:     {resultmd5.hexdigest()} \n\n SHA1 Hashed:\nbyteformat:     {resultsha1.digest()}\nhexadecimalFormat:     {resultsha1.hexdigest()} \n\n')

string1='Hii Shreyas'
string2="Hiii Shreyas"
str2resulthex=hashlib.md5(string2.encode()).hexdigest()
string3="Hiii Shrayas"
str3resulthex=hashlib.md5(string3.encode()).hexdigest()
runthehash(string1)
runthehash(string2)
runthehash(string3)

index=0
matched=0
unmatched=0
for i in string2:
    if(string2[index]==string3[index]):
        print(f"{index}: Matched ")
        matched+=1
    else:
        print(f"{index}: unMatched ")
        unmatched+=1
    index+=1
print(f'matched% ={matched*100/index}\nunmatched% ={unmatched*100/index}\n')


print("\n\nRESULT:")

matched=0
unmatched=0
index=0
for i in str2resulthex:
    if(str2resulthex[index]==str3resulthex[index]):
        print(f"{index}: Matched ")
        matched+=1
    else:
        print(f"{index}: unMatched ")
        unmatched+=1
    index+=1
print(f'matched% ={matched*100/index}\nunmatched% ={unmatched*100/index}\n')
