import itertools

n=int(input("Enter number of men: "))
men_pref_list=[]
women_pref_list=[]
list=[]
count=[]

print("Enter preference list of men: ")
for i in range(n):
    p=input()
    men_pref_list.append([int(j) for j in p.split()])

print("Enter preference list of women: ")
for i in range(n):
    p=input()
    women_pref_list.append([int(j) for j in p.split()])

a=[]
for i in range(n):
    a.append(i)
s=itertools.combinations(a,2)