import hashlib
S="i am kuldeep"
inp=S.encode()

result=hashlib.md5(inp)

print(result.digest())
print(result.hexdigest())

result=hashlib.sha1(inp)

print(result.digest())
print(result.hexdigest())