import math
import time
#print("Hello World")
#print("elo")
name = "siema"
#print(type(name))
##print(name+"byniu")
human = False
##print(type(human))
#elo=input("input \n")
##print(elo)
#pwoer
##print(pow(3,2)) 9
part=name[2:5] #ema

par=name[0:5:2] #sea

reverse=name[::-1] #ameis
website="http://google.com"
slice=slice(7,-4)
sl=website[slice] #google
#num=int(input())
num =19
if num>=18 and num <=30:
    num+=1
elif num==0 or num==1:
    num-=1
else:
    num-=2
xd=""
# while len(xd)==0:
#     xd+="a"
# for i in range(5,0,-1): #leci do 1, trzecia opcja step
#     print(i)
#     time.sleep(1)
# print("bum")
# while True:
#     name=input()
#     if name != "":
#         break
phone="123-456-789"
for i in phone:
    if i=="-":
        continue
    print(i,end="")
food=["pizza","curry","milkshake","pasta"]
print (food[0])
food[0]="sushi"
print(food[0])
for x in food:
    print(x)
food.append("lody")
food.remove("sushi")
food.pop()
food.insert(0,"cake")
food.sort()
#food.clear
print(food)
drinks=["coffee","czai","chinka"]
deser=["lody","ciastka"]
wszystko=[food,drinks,deser]
print(wszystko)
print(wszystko[1][1])
student=("Camille",19,"fem")
print(student.count("Camille"))
print(student.index(19))
for x in student:
    print(x)
sztucc={"widelec","noz","lyzka","lyzka"}
for x in sztucc:
    print(x)
sztucc.add(1)
sztucc.remove("noz")
dish={"talerz","miska"}
dish.update(sztucc)
for x in dish:
    print(x)
    #.union jak do czegos innego bez zmieniania
#/difference zeby porownac
