name = "Nguyen Van An"
print(name)
age = 18
print(age)
age = 3.5
max = 100
print(max-age)
x = 10
y = 3
print(x/y)
print(x//y)
print(x%y)

if age >= 18:
    print("Đủ 18 tuổi")
else:
    print("Chưa đủ 18 tuổi")

# tương đương i=0; i<10; i++
# range tạo mảng từ 0 đến 9
for i in range(10):
    print(i)

i=0
while i<5:
    print(i)
    i+=1

def hello():
    print("Hello word")
hello()

def total(a,b):
    return a+b
c = total(5,10)
print(c)
numbers = [1,2,3,4]
print(numbers[3]) #4
numbers.append(9)
print(numbers[4])

for n in numbers:
    print(n)

arr = range(100)
for n in arr:
    print(n)

# viết hàm kiểm tra có phải số nguyên tố hay không

def sont(a):
    if a < 2:
        print("a không phải số nguyên tố")
        return
    
    for i in range(2, a//2):
        if a % i == 0:
            print("a không phải số nguyên tố")
            return
    
    print("a là số nguyên tố")

def iPrime(p):
    if p<2:
        return False
    else: 
        if p<5:
            return True
        else:
            for i in range(2,p//2):
                if p%i==0:
                    return False
            return True

b = sont(3)
print(b)

def demo(x="Good morning"): #default param
    print(x)

demo("Hello")
demo()


def sub(a, b=1):
    print(a/b)

sub(5)
sub(5, b=5)
sub(b=6,a=12)

user = {#dictionary
    "name":"Nguyễn Văn A",
    "age" : 20
}
print(user["name"])

user= [
    {"name":"A","age":17},
    {"name":"B","age":20},
    {"name":"C","age":15}
]

#Viết hàm tính trung bình tuổi
def TBT(t):
    tong = 0
    for i in t:
        tong += i["age"]
    return (tong/len(t))
print("TBT {TBT:}",TBT(user))
