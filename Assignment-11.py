#TCS,Sai,Rohit,Satya,Dhoni,Sarath,Saroj,Venkat,Sas
#INFOSYS,Kohli,Santosh,Venkat,Koti,Prabha,Soumya,Mishra
#WIPRO,Satya,Kohli,Ram,Chinna,Pop,Amelia,Suresh,Arjuna
#CTS,Prabha,Subha,Debha,Rabha,Venkat,Dhoni,Surya,Saroj
#NTH,Narayana,Akhil,Arha,Venkat,Sravya,Ananya,Revanth,Aha
#ABC,Arha,Chinna,Satya,Dhoni,Venkat,Rohit,Yash,Nikhilesh

#nthdata.txt
'''
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt','w')
x.write('TCS,Sai,Rohit,Satya,Dhoni,Sarath,Saroj,Venkat,Sas\nINFOSYS,Kohli,Santosh,Venkat,Koti,Prabha,Soumya,Mishra\nWIPRO,Satya,Kohli,Ram,Chinna,Pop,Amelia,Suresh,Arjuna\nCTS,Prabha,Subha,Debha,Rabha,Venkat,Dhoni,Surya,Saroj\nNTH,Narayana,Akhil,Arha,Venkat,Sravya,Ananya,Revanth,Aha\nABC,Arha,Chinna,Satya,Dhoni,Venkat,Rohit,Yash,Nikhilesh')
x.close()

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt','r')
y=x.read()
print(y)
'''
'''
#1. Write a program to fetch all data from the file.
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')
y=x.read()
print(y)

#2. Write a program to read the first line from the file.
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt','r')   #TCS,Sai,Rohit,Satya,Dhoni,Sarath,Saroj,Venkat,Sas
y=x.readline()
print(y)

#3. Write a program to read the last line from the file.
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt','r')   #ABC,Arha,Chinna,Satya,Dhoni,Venkat,Rohit,Yash,Nikhilesh
y=x.readlines()
print(y[-1])

#4. Write a program to read the 3rd line from file
                      #WIPRO,Satya,Kohli,Ram,Chinna,Pop,Amelia,Suresh,Arjuna
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt','r')
y=x.readlines()
print(y[2])

#5. Write a program to count total number of characters in the file?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')   #325
y=x.read()
lst=[]
for i in y:
    lst.append(i)
print(len(lst))

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')    #273(with out ,)
y=x.read().replace('\n',',')
z=y.split(',')
l=[]
for i in z:
    l.append(len(i))
print(sum(l))


#6. Write a program to count total number of commas in the file?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')    #47
y=x.read()
z=y.count(',')
print(z)
#7. Write a program to count total number of words in the first line?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')   #9
y=x.readline().split(',')
print(len(y))

#8. Write a program to count total number of lines in the file?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')    #6
y=x.readlines()
print(len(y))

#9. Write a program to count total number of 'Sai' name in the file?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')    #1
w=x.read()
y=w.replace('\n',',')
z=y.split(',')
lst=[]
for i in z:
    if i=='Sai':
        lst.append(i)
print(len(lst))

#10. Write a program to fetch the first word from each line in the file?
     #['TCS', 'INFOSYS', 'WIPRO', 'CTS', 'NTH', 'ABC']
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')
y=x.readlines()
lst=[]
for i in y:
    lst.append(i.split(',')[0])
print(lst)

#11. Write a program to fetch the last word from each line?

print([i.split(',')[-1].replace('\n','') for i in open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()])

#12. Write a program to fetch all words which starts with 'a' Character?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt','r')
y=x.read()
for i in y.replace('\n',',').split(','):
    if i.startswith('a'):
        print(i)

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')
y=x.read()
w=y.replace('\n',',')
z=w.split(',')
lst=[]
for i in z:
    if i[0]=='a':
        lst.append(i)
print(lst)
#13. Write a program to fetch all words which ends with an vowel?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')
y=x.read()
w=y.replace('\n',',')
z=w.split(',')
lst=[]
for i in z:
    if i[-1]in 'aeiou':
        lst.append(i)
print(lst)

print([i for i in open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read().replace('\n',',').split(',') if i[-1] in 'aeiou'])

#14. Write a program to fetch all words which has either 'a' or 'i' characters in the file?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')
y=x.read()
w=y.replace('\n',',')
z=w.split(',')
lst=[]
for i in z:
    if 'i'in i or  'a' in i:
        lst.append(i)
print(lst)

#15. Write a program to fetch all words which contains only 5 characters in the file?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')
y=x.read().replace('\n',',')
z=y.split(',')

lst=[]
for i in z:
    if len(i)==5:
        lst.append(i)
print(lst)

#16. Write a program to fetch all words which does not contains vowels except i in the file?
print([i for i in open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read().replace('\n',',').split(',')if 'a' not in i and 'e' not in i and 'o' not in i and 'u' not in i])

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read().replace('\n',',')
v=('a','e','o','u','A','E','O','U')
lst=''
for i in x:
    if i not in v:
        lst=lst+i
s1=lst.split(',')
for m in x.split(','):
    for n in s1:
        if m==n:
            print(m)


#17. Write a program to fetch all words which ends with uppercase character in the file?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')
y=x.read().replace('\n',',')
z=y.split(',')
for i in z:
    if i[-1].isupper():
        print(x)

#18. Write a program to count total number of characters in the file excluding commas and \ns?
print(len([i for i in open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()if i !=',' and i !='\n' ]))

#19. Write a program to count total number of words in the entire file?
print(len([i for i in open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read().replace('\n',',').split(',')]))
'''
#20. Write a program to fetch all even number words from from every line the file?
print([i for i in open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read().replace('\n',',').split(',') if len(i)%2==0])
'''

#21. Write a program to fetch all words which ends with 'bha' in the file?
print([i for i in open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read().replace('\n',',').split(',') if i.endswith('bha')])

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()
for i in x:
    if len(i.split(','))%2==0:
        print(i)

#22. Write a program to display all TCS employees?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')
y=x.readlines()
lst=[]
for i in y:
    for j in i.split(','):
        if j=='TCS':
            print(i.split(',')[1:-1])

#23. Write a program to display the company name of Chinna Employee?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')    #WIPRO ABC
y=x.readlines()
lst=[]
for i in y:
    if 'Chinna' in i:
        lst.append(i.replace('\n','').split(','))
for m in lst:
    print(m[0])

#24. Write a program to fetch the 2nd from 3rd line in the file?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')
y=x.readlines()[1:3]
print(y)

#25. Write a program to fetch the first character from each word in the 3rd line?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')     #['W', 'S', 'K', 'R', 'C', 'P', 'A', 'S', 'A']
y=x.readlines()[2]
z=y.split(',')
lst=[]
for i in z:
    lst.append(i[0])
print(lst)

#26. Write a program to fetch first and last character of each word in the last line?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')    #['AC', 'Aa', 'Ca', 'Sa', 'Di', 'Vt', 'Rt', 'Yh', 'Nh']
y=x.readlines()[-1]
#w=y.replace('\n','')
z=y.split(',')
lst=[]
for i in z:
    lst.append(i[0]+i[-1])
print(lst)

#27. Write a program to fetch all characters(except 1st and last chars) of each word in the 2nd line?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')    #['NFOSY', 'ohl', 'antos', 'enka', 'ot', 'rabh', 'oumy', 'ishr']
y=x.readlines()[1]
z=y.replace('\n','')
w=z.split(',')
lst=[]
for i in w:
    lst.append(i[1:-1])
print(lst)
            
#28. Write a program to count total number of words which starts with 'S' character?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt')  #14
y=x.read()
z=y.replace('\n',',')
w=z.split(',')
lst=[]
for i in w:
    if i[0]=='S':
        lst.append(i)
print(len(lst))

#29. Write a program to fetch all duplicate names in the file?
#{'Dhoni', 'Venkat', 'Rohit', 'Prabha', 'Saroj', 'Satya', 'Arha', 'Chinna', 'Kohli'}

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()
y=x.replace('\n',',').split(',')
lst=[]
for i in y:
    if y.count(i)>1:
        lst.append(i)
s=set(lst)
print(s)

#30. Write a program to count all vowels in the file? (Note: output must be in dict)
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()
v='aeiouAEIOU'
d= {}.fromkeys(v,0)
for i in x:
    if i in v:
        d[i]=d[i]+1
print(d)  
#{'a': 47, 'e': 10, 'i': 16, 'o': 13, 'u': 5, 'A': 8, 'E': 0, 'I': 2, 'O': 2, 'U': 0}

#31. Write a program to reverse all words in the file?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read().replace('\n',',').split(',')
lst=[]
for i in x:
    lst.append(i[-1::-1])
print(lst)

def reverse_str(x):
    y=""
    for i in x:
        y=i+y
    return y
print(reverse_str(x))

#32. Write a program to fetch all words which contains two or more then 'a' characters?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()
y=x.replace('\n',',').split(',')
lst=[]
for i in y:
    if i.count('a')>=2:
        lst.append(i)
print(lst)
    
#33. Write a program to fetch all words which starts and ends with 'a' character?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()    #[]
y=x.replace('\n',',').split(',')
lst=[]
for i in y:
    if i[0]=='a' and i[-1]=='a':
        lst.append(i)
print(lst)

#34. Write a program to fetch word which has more number of 'a' characters?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()
y=x.replace('\n',',').split(',')
z=[]
for i in y:
    z.append(i.count('a'))
more_a=max(z)
for i in y:
    if i.count('a')==more_a:
        print(i)

#35. Write a program to fetch all company names which starts with vowel?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()  #INFOSYS,ABC
y=x.replace('\n',',').split(',')
for i in y:
    if i.isupper() and i[0] in 'AEIOU':
        print(i)

#36. Write a program to display company name which contains Saroj Employee?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()   #TCS,CTS
for i in x:
    if 'Saroj'in i :
            print(i.split(',')[0])

#37. Write a program to count all words which starts and ends with consonants?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()
y=x.replace('\n',',').split(',')
lst=[]
for i in y:
    if i[0] not in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU':
        lst.append(i)
print(lst)

#38. Write a program to fetch all company names which does not contain Venkat employee?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines() #WIPRO
for i in x:
    if 'Venkat' not in i:
        print(i.split(',')[0])


#39. Write a program to display company name where Narayana is working?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()    #NTH
for i in x:
    if 'Narayana' in i:
        print(i.split(',')[0])

#40. Write a program to display the first word and last word from each line in dict format?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()
lst=[]
for i in range(len(x)):
    for j in x[i].replace('\n',',').split(','):
        lst.extend([(x[i].split(',')[0],x[i].replace('\n','').split(',')[-1])])
d={}.fromkeys(lst)
print(d)

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()
d={}
for j in x:
    i=j.split(',')
    d[i[0]]=i[-1].replace('\n','')
print(d)
       
#41. Write a program to fetch all names whose name starts with 'a' in NTH company?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()
for i in x:
    if i.split(',')[0]=='NTH':
        for j in i.split(','):
            if j[0]=='A':
                print(j)

#42. Write a program to count total number of employees in CTS company?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()   #8
lst=[]
for i in x:
    if i.split(',')[0]=='CTS':
        for j in i.replace('\n','').split(','):
            if j!='CTS':
                lst.append(j)
print(len(lst))

#43. Write a program to fetch all companies where Venkat employee is working?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines() #['TCS', 'INFOSYS', 'CTS', 'NTH', 'ABC']
lst=[]
for i in x:
    if 'Venkat' in i:
        lst.append(i.split(',')[0])
print(lst)
#44. Write a program to fetch all companies names which name starts with Vowel?

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()  #INFOSYS,ABC
y=x.replace('\n',',').split(',')
for i in y:
    if i.isupper() and i[0] in 'AEIOU':
        print(i)

#45. Write a program to fetch all palindrome names from the file? ['sas', 'pop', 'aha']
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()    #[]
y=x.replace('\n',',').split(',')
lst=[]
for i in y:
    if i==i[-1::-1]:
        lst.append(i)
print(lst)

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read().lower()
y=x.replace('\n',',').split(',')
lst=[]
for i in y:
    if i==i[-1::-1]:
        lst.append(i)
print(lst)

#46. Write a program to fetch all companies names where palindrome named employees working?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').lower().readlines()
for i in range(len(x)):
    for j in x[i].replace('\n','').split(','):
        if j==j[-1::-1] in x[i]:
            print(x[i].replace('\n','').split(',')[0])
        
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').lower().readlines()
for i in x:
    for j in i.replace('\n','').split(','):
        if j==j[-1::-1] in i:
            print(i.replace('\n','').split(',')[0])

#47. Write a program to fetch the lengthiest company name?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').read()    #INFOSYS
y=x.replace('\n',',').split(',')
lst=[]
for i in y:
    if i ==i.upper():
        lst.append(len(i))
m=max(lst)
for i in y:
    if i ==i.upper() and len(i)==m:
        print(i)


#48. Write a program to fetch the lengthiest employee name in ABC company?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()   #Nikhilesh
lst=[]
for i in x:
    if i.replace('\n','').split(',')[0]=='ABC':
        for j in i.replace('\n','').split(','):
            if j!='ABC':
                lst.append(len(j))
m=max(lst)
for i in x:
    if 'ABC' in i.replace('\n','').split(','):
        for j in i.replace('\n','').split(','):
            if j!='ABC' and len(j)==m:
                print(j)

#49. Write a program to fetch shortest employee name in the WIPRO company?
x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()   #Ram,Pop
lst=[]
for i in x:
    if i.replace('\n','').split(',')[0]=='WIPRO':
        for j in i.replace('\n','').split(','):
            if j!='WIPRO':
                lst.append(len(j))
m=min(lst)
for i in x:
    if 'WIPRO' in i.replace('\n','').split(','):
        for j in i.replace('\n','').split(','):
            if j!='WIPRO' and len(j)==m:
                print(j)

#50. Write a program count total number of employees in each company(in dict format)?
#{'TCS': 8, 'INFOSYS': 7, 'WIPRO': 8, 'CTS': 8, 'NTH': 8, 'ABC': 8}

x=open('C:\\Users\\Aadesh\\Desktop\\my folder\\nthdata.txt').readlines()
lst=[]
for i in range(len(x)):
    for j in x[i].split(','):
        if j.isupper():
            lst.append(j)
d={}.fromkeys(lst,0)
for i in range(len(x)):
    for j in x[i].split(','):
            for a in d:
                if a in x[i]:
                    if j!= a:
                        d[a]=d[a]+1
print(d)
'''