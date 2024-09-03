### https://onecompiler.com/python/42r4tyx8n
def outer():
     num=20
     
     def inner():
            num=30
            print(num)
     print(num)
     inner()
     print(num)

num=10
outer()
print(num)
