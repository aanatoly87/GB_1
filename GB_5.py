
#1

my_file = open("lesson5.txt", "w")
while True:
    text = input("Введите текст: ")
    if text =="":
        break
    my_file.write(text + "\n")
my_file.close()


#2

my_file = open("gb5.txt", "r")
content = list(my_file.readlines())
line = len(content)
print("Количество строк: ", line)
c = 1
for i in content:
    line_str = i.split(" ")
    print("Количество слов в " + str(c) + " строке равно: " + str(len(line_str)))
    c = c + 1
my_file.close()


#3

my_file = open("salary.txt", "r")
a = my_file.readlines()
my_list = []
for i in a:
    b = i.split(" ")
    my_list.append(b)
my_dict = dict(my_list)
print(my_dict)
sum = 0
emp = 0
for k,v in my_dict.items():
    sum+=int(v)
    emp+=1
    if int(v) > 15000:
        print(k)
print(sum/emp)
my_file.close()

#5

my_file = open("slovo.txt", "w")
text = map(int,input("Введите числа через пробел: ").split())
my_list = list(text)
sum = 0
for i in my_list:
    sum += i
print(sum)
my_file.write(str(sum))
my_file.close()



