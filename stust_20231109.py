#建立函數
def nameage(name,age):
    print(name,age)

#建立可變長度參數的函數
def func1(*args):
    for i in args:
        print(i)

#從函數傳回多個值
def calculation(a, b):
    add = a+b
    reduce = a-b
    return add,reduce

#建立帶有預設參數的函數
def show_employee(name,money):
    print("姓名:",name," 薪水:",money)

#建立內部函數計​​算加法
def outer(a,b):
    def add(a,b):
        sum=a+b
        return sum
    result=add(a,b)
    return result+5

#建立遞歸函數
def addition(num):
    if num:
        return num+addition(num - 1)
    else:
        return 0

def display_student(name, age):
    print(name, age)


#呼叫函式
nameage("Ting",20)

func1(20,40,60)
func1(80,100)

res = calculation(40, 10)
print(res)

show_employee("Ben", 12000)

result = outer(5, 10)
print(result)

res =addition(10)
print(res)

showStudent = display_student
showStudent("Emma", 26)


#產生 4 到 30 之間所有偶數
print(list(range(4,30,2)))

#找出最大的項目
x = [4, 6, 8, 24, 12, 2]
print(max(x))