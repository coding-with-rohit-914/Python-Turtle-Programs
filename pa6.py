#Assignment:6
emp={
 'emp1':{'name':'sai','salary':20000,'age':30,'company':'TCS','exp':3},
 'emp2':{'name':'Nani','salary':30000,'age':25,'company':'wipro','exp':2},
 'emp3':{'name':'satya','salary':40000,'age':23,'company':'TCS','exp':4},
 'emp4':{'name':'Rjesh','salary':33000,'age':26,'company':'Infosys','exp':4},
 'emp5':{'name':'Aakash','salary':50000,'age':35,'company':'HCL','exp':7},
 'emp6':{'name':'Renu','salary':10000,'age':20,'company':'wipro','exp':1},
    }
    

#Q.1]write a comprehension to fetch all employes names?
print([emp[i]['name'] for i in emp ])

#Q.2]write a comprehension to fetch all unique company names?
print(list({emp[i]['company'] for i in emp}))

#Q.3]write a comprehension to fetch all salaries which are above 25000?
print([emp[i]['salary'] for i in emp if emp[i]['salary']>25000])

#Q.4]write a comprehension to fetch all ages which are in 30?
print([emp[i]['age'] for i in emp if emp[i] ['age']>=30 and emp[i]['age']<40])

#Q.5]write a comprehension to fetch all exps which are above 2 years?
print([emp[i]['exp'] for i in emp if emp[i]['exp']>2])

#Q.6]write a comprehension to fetch employe name who is getting less  salary?
x=min(emp[i]['salary'] for i in emp)
print([emp[i]['name']for i in emp if emp[i] ['salary']==x])

#Q.7]write a comprehension to fetch emp name who is getting more salary?
print([emp[i]['name'] for i in emp if emp[i] ['salary']==max(emp[i]['salary'] for i in emp)])

#Q.8]write a comprehension to fetch emp name who is getting more or less salary?
x=min(emp[i]['salary'] for i in emp)
y=max(emp[i]['salary'] for i in emp)
print([emp[i]['name'] for i in emp if emp[i]['salary']!=x and emp[i]['salary']!=y])

#Q.9]write a comprehension to display oldest emp name who is getting more salary?
print([emp[i]['name'] for i in emp if emp[i]['age']==max(emp[i]['age'] for i in emp )])

#Q.10]write a comprehension to display youngest emp name?
print([emp[i]['name'] for i in emp if emp[i]['age']==min(emp[i]['age'] for i in emp )])

#Q.11]write a comprehension to display emp name who is not oldest and youngest?
x=min(emp[i]['age'] for i in emp)
y=max(emp[i]['age'] for i in emp)
print([emp[i]['name'] for i in emp if emp[i]['age']!=x and emp[i]['age']!=y])

#Q.12]write a comprehension to display emp name who age is even number?
print([emp[i]['name'] for i in emp if emp[i]['age']%2==0])

#Q.13]write a comprehension to display emp name who age is divisible by 3 but not 5?
print([emp[i]['name'] for i in emp if emp[i]['age']%3==0 and emp[i] ['age']%5!=0])

#Q.14]write a comprehension to display emp name who is working in TCS?
print([emp[i]['name']for i in emp if emp[i]['company']=='TCS'])

#Q.15]write a comprehension to display emp name who is not working in HCL?
print([emp[i]['name']for i in emp if emp[i]['company']=='HCL'])

#Q.16]write a comprehension to display emp name who has more exp?
print([emp[i]['name']for i in emp if emp[i]['exp']==max(emp[i]['exp'] for i in emp)])

#Q.17]write a comprehension to display emp name who has less exp?
print([emp[i]['name']for i in emp if emp[i]['exp']==min(emp[i]['exp'] for i in emp)])

#Q.18]write a comprehension to display emp name who is does not have more or less exp?
x=min(emp[i]['exp'] for i in emp)
y=max(emp[i]['exp'] for i in emp)
print([emp[i]['name'] for i in emp if emp[i]['exp']!=x and emp[i]['exp']!=y])

#Q.19]write a comprehension to display emp name whose exp is odd number?
print([emp[i]['name'] for i in emp if emp[i]['exp']%2==1])

#Q.20]write a comprehension to display emp name whose exp is above 3 years?
print([emp[i]['name'] for i in emp if emp[i]['exp']>3])

#Q.21]write a comprehension to display emp name whose salary is above 30000 and working in TCS?
print([emp[i]['name'] for i in emp if emp[i]['salary']==30000 and emp[i]['company']=='TCS'])
                                             
#Q.22]write a comprehension to display emp name whose age is above 25 and getting less than 30000?
print([emp[i]['name'] for i in emp if emp[i]['age']>25 and emp[i] ['salary']>30000])
                                            
#Q.23]write a comprehension to display emp name who is working in TCS and has more exp?
x=max(emp[i]['exp'] for i in emp if emp[i]['company']=='TCS')
print([emp[i]['name'] for i in emp if emp[i]['exp']==x and emp[i]['company']=='TCS'])

#Q.24]write a comprehension to display emp name who is not working in TCS and getting more then 25000?
print([emp[i]['name'] for i in emp if emp[i]['salary']>25000 and emp[i]['company']!='TCS'])

#Q.25]write a comprehension to display emp name who has 4 years exp and working in Infosys and getting less then 35000?
print([emp[i]['name'] for i in emp if emp[i]['exp']==4 and emp[i]['company']=='Infosys' and emp[i] ['salary']>30000])

#26. Write a comprehension to display number of employees in TCS?
print(len([emp for i in emp if emp[i]['company'] in 'TCS']))

#27. Write a comprehension to display number of employees whose salary less then 30000?
print(len([emp[i]['name'] for i in emp if emp[i]['salary']<30000]))

#28. Write a comprehension to display emp names whose name starts with 'S' Character? 
print([emp[i]['name'] for i in emp if emp[i]['name'][0] == 's'])

#29. Write a comprehension to display salaries of emps whose name ends with vowel? 
print([emp[i]['salary']for i in emp if emp[i]['name'][-1] in 'aeiou'])

#30. Write a comprehension to display age of emp who has 4 years exp?
print([emp[i]['age'] for i in emp if emp[i]['exp']==4])

#31. Write a comprehension to display age of emp whose has highest salary?
print([emp[i]['age']for i in emp if emp[i]['salary']==max(emp[i]['salary'] for i in emp)])

#32. Write a comprehension to display age and exp of emp who is not from Infosys? 
print([emp[i]['age'] and emp[i]['exp'] for i in emp if emp[i]['company'] != 'Infosys'])

#33. Write a comprehension to display age of emp whose name has 6 characters?
print([emp[i]['age'] for i in emp if len(emp[i]['name']) == 6])

#34. Write a comprehension to display age of emp whose company name has more then 4 characters?
print([emp[i]['age'] for i in emp if len(emp[i]['company']) >= 4])

#35. Write a comprehension to display salary of oldest employee?
print([emp[i]['salary'] for i in emp if emp[i]['age']==max(emp[i]['age'] for i in emp )])

#36. Write a comprehension to display salary of youngest employee?
print([emp[i]['salary'] for i in emp if emp[i]['age']==min(emp[i]['age'] for i in emp )])

#37. Write a comprehension to display salary of emp who is not oldest and not youngest?
x=max(emp[i]['age'] for i in emp)
y=min(emp[i]['age'] for i in emp)
print([emp[i]['salary'] for i in emp if emp[i]['age']!=max(emp[i]['age'] for i in emp) and emp[i]['age']!=min(emp[i]['age'] for i in emp)])

#38. Write a comprehension to display salary of most exp emp?
print([emp[i]['salary'] for i in emp if emp[i]['exp']==max(emp[i]['exp'] for i in emp )])

#39. Write a comprehension to display salary of least exp emp?
print([emp[i]['salary'] for i in emp if emp[i]['exp']==min(emp[i]['exp'] for i in emp )])

#40. Write a comprehension to display salary and age of emp whose has 4 years exp? !
print([(emp[i]['salary'],emp[i]['age']) for i in emp if emp[i]['exp']==4])

#41. Write a comprehension to display company name of all emps whose salary more then 30000?
print([emp[i]['company'] for i in emp if emp[i]['salary'] > 30000])

#42. Write a comprehension to display company name of all emps who has more then 3years exp?
print([emp[i]['company'] for i in emp if emp[i]['exp'] > 3])

#43. Write a comprehension to display company name of all emps whose age between 25 and 30?
print([emp[i]['company'] for i in emp if emp[i]['age']>=25 and emp[i]['age']<=30])

#44. Write a comprehension to display company name of all emps whose name contains 4 characters?
print([emp[i]['company'] for i in emp if len(emp[i]['name'])==4])

#45. Write a comprehension to display emp name who has highest salary and more exp?
print([emp[i]['name'] for i in emp if emp[i]['salary'] == max(emp[i]['salary'] for i in emp) and(emp[i]['exp'] for i in emp)])

#46. Write a comprehension to display salary and age of Satya?
print([(emp[i]['salary'],emp[i]['age']) for i in emp if emp[i]['name']=='satya'])

#47. Write a comprehension to display company name and exp of emp whose has highest salary?
print([(emp[i]['company'],emp[i]['exp']) for i in emp if emp[i]['salary']==max(emp[i]['salary']for i in emp)])

#48. Write a comprehension to display salary and company name of youngest emp?
print([(emp[i]['salary'],emp[i]['company']) for i in emp if emp[i]['age']==min(emp[i]['age']for i in emp)])

#49. Write a comprehension to display emp name and exp of emp who is getting less then 30000?
print([(emp[i]['name'],emp[i]['exp']) for i in emp if emp[i]['salary'] < 30000])

#50. Write a comprehension to display emp name and salary of emp who is not working in TCS and HCL?
print([(emp[i]['name'],emp[i]['salary']) for i in emp if emp[i]['company'] != 'TCS' and emp[i]['company'] != 'HCL'])
