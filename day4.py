#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
data={"Name":["Rahul","Joy","Kumar","Mahi","Jhanvi","Shubham","Priya","Anit"],
      "Sal":[50000,60000,70000,80000,30000,32000,45000,87000],
      "Department":["IT","HR","Finance","IT","HR","Finance","IT","HR"],
      "City":["Mumbai","Delhi","Chicago","Kolkata","Hongkong","Delhi","Mumbai","Kolkata"],
      "Age":[25,30,35,40,50,21,43,45],
      "Experience":[4,7,0,0,2,8,3,5]}
df=pd.DataFrame(data)
print(df.loc[:,["Name","Sal"]])


# In[ ]:


df.iloc[:,5]


# In[ ]:


print(df.iloc[:,5])


# In[ ]:


print(df.loc[:,["Name","Sal","Department","City","Age"]])


# In[ ]:


df.iloc[:,5]


# In[ ]:


df.iloc[:,5]


# In[ ]:


df.iloc[:,2]


# In[ ]:


df.iloc[:0:3]


# In[ ]:


df.iloc[:,[0,5]]
df.iloc[:,0:3]


# In[ ]:


## here we are using .loc function to get rows+columns together


# In[ ]:


#syntax:df/loc[rows_selection,col_selection]
df.loc[0,"Name"]


# In[ ]:


df.loc[1,"Sal"]#here we are accessing specific row and specific col
#now multi rows and single col
df.loc[0:3,"Name"]
#multi col and multi row
df.loc[0:3,["Name","Age","Department"]]


# In[ ]:


df.loc[df["Age"]>25,["Name","Sal","Age","Department"]]#simple way


# In[ ]:


df.loc[0:3,["Name"]]#multi rows and single col


# In[ ]:


mask=df["Age"]>25
df.loc[mask,["Name","Sal","Age","Department"]]#using mask


# In[ ]:


df.loc[(df["Age"]>25) & (df["Sal"]>50000)],["Name","Sal","Age","Department"]#here we are using multi conditions
# this is doubtful


# In[ ]:


#quer method  like sql


# In[ ]:


df.query("Age>25 and Sal>50000 and Department=='IT'")#this is query method to filter the data based on conditions


# In[ ]:


df.query("Age>25 and Sal>30000 and City in ['Chicago','Mumbai']")


# In[ ]:


con=30#here we have taken a var and we will use this in query method by using @symbol to refer the var
df.query("Age>@con and Sal>30000 and City in ['Chicago','Mumbai']")


# #### isin() method this is like memebership method

# In[ ]:


df[df["City"].isin(["Delhi","Mumbai"])]


# #between() - range checking
# 

# In[ ]:


# age should be greater than 30 and less than 40
df[df["Age"].between(30,40)]#both ranges are inclusive


# In[ ]:


df[df["Age"].between(30,40)][["Name","Department"]]


# #1.only to print sal and name cols
# #2.show the data whose age>40
# #3.display the row no 2 3 4 using .iloc()
# #4.show only first 4 rows of name and department columns
# #5.show all the names where department is it
# #6.show the first 3 cols of last 3 rows
# #7.show the data where sal is between 60k to 80k along with name and city col

# In[ ]:


df[["Name","Sal"]]


# In[ ]:


df[df["Age"]>40]


# In[ ]:


df.iloc[2:5]


# In[ ]:


df.iloc[2:5, :]


# In[ ]:


df.loc[0:3,["Name","Department"]]


# In[ ]:


df[df["Department"]=="IT"]["Name"]


# In[ ]:


df[df["Department"].isin(["IT"])]["Name"]


# In[ ]:


df.iloc[-3:,0:3]


# In[ ]:


df.loc[(df["Sal"]>=60000)&(df["Sal"]<=80000,["Name","City"])]


# In[ ]:


df.loc[df["Sal"].between(60000, 80000), ["Name","City"]]


# In[ ]:


df.iloc[2:5]


# #groupby()

# In[ ]:


df.groupby("City")['Sal'].mean()


# In[ ]:


df.groupby("Department")["Sal"].agg(['min','max','sum','count','mean'])


# In[ ]:


df.agg({'Age' : ['min','max','mean']})


# In[ ]:


df.agg({'Age' : ['min','max','mean'],
        'Sal' : ['min','max','std'],
        'Experience': ['min','max','median']})


# ####sorting + EDA (Exploratory Data Analysis)

# In[ ]:


#sort_values() this is the functions to sort the things
#it has multiple params like by,ascending,inplace
df.sort_values("Experience")


# In[ ]:


df.sort_values("Experience",ascending=False)


# In[ ]:


df.sort_values("Name",ascending=False)


# In[ ]:


df.sort_values(["Department","Sal"])


# In[ ]:


df.sort_values(["Department","Sal"],ascending=[True,False])


# In[ ]:


df['Sal_rank']=df['Sal'].rank()
df


# In[ ]:


df['Sal_rank']=df['Sal'].rank(ascending=False)
df


# ####EDA-its the process to understand the data without assumptions

# #### responsibility of analyst is to :
# 1.understand the data
# 2.find the pattern
# 3.find the problem in the data

# In[ ]:


df.head()#it will show first 5 rows of data by default


# In[ ]:


df.tail()#it will  show last 5 rows of data by default


# In[ ]:


df.sample(3)#it will return random 
df.sample(frac=0.5)


# In[ ]:


df.shape#  gives no of rows and cols in tuple format


# In[ ]:


df.info()# it will return


# In[ ]:


df.dtypes


# In[ ]:


type(df.dtypes)


# In[ ]:


num_cols=df.select_dtypes(include=['int64','float64']).columns
print(num_cols)


# In[ ]:


cat_col=df.select_dtypes(include=['object','string']).columns
print(cat_col)


# In[ ]:


print("Numerical columns:",len(list(num_cols)),"Categorical columns:",len(list(cat_col)))
type(num_cols)


# In[ ]:


df['Age']=df['Age']*1.0
df


# In[ ]:


num_cols=df.select_dtypes(include=['int64','float64']).columns
print(num_cols)
cat_col=df.select_dtypes(include=['object','string']).columns
print(cat_col)
print("Numerical columns:",len(list(num_cols)),"Categorical columns:",len(list(cat_col)))
type(num_cols)


# In[ ]:


df['Age']=df['Age']*1.0
df['Age']=df['Age']## inka edho cheparuuu...


# In[ ]:


df.describe()


# In[ ]:


df['Sal'].mean()


# In[ ]:


df['Sal'].agg(['min','max','mean','std'])


# In[ ]:


df['Experience'].agg(['min','max','mean','std'])


# In[ ]:


df.describe(include=("object","string"))


# In[ ]:


df.describe(include="all")


# In[ ]:


City_count=df['City'].value_counts()
City_count


# In[ ]:


City_count=df['City'].value_counts(normalize=True)*100
City_count

