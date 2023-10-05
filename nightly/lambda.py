#result = (lambda x: "Even" if x%2 ==0 else "odd")(3)

numType = lambda x: "Even" if x%2==0 else "odd"
num = input()
num = int(num)
print(numType(num))