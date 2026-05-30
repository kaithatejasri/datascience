#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
data = {
    "StudentId": ["S001","S002","S003","S004","S005","S006","S007","S008","S009","S010","S011","S012","S013","S014","S015"],
    "Name": ["Alice","Bob","Charlie","David","rohit","agastya","amar","joy","Rohit","Mahi","Jhanvi","Shubham","Priya","Anit","Rahul"],
    "Maths": [85.0,90.0,np.nan,92.0,88.0,95.0,80.0,91.0,89.0,94.0,87.0,90.0,85.0,88.0,92.0],
    "Science": [80.0,85.0,90.0,np.nan,88.0,92.0,np.nan,89.0,90.0,40.0,56.0,78.0,85.0,90.0,30.0],
    "English": [75,80,85,90,88,92,84,89,90,40,56,78,85,90,30],
    "Attendance": [90.0,85.0,95.0,80.0,88.0,np.nan,84.0,89.0,90.0,40.0,56.0,78.0,85.0,90.0,30.0],
    "Grade": ["A","A","B","A","B","A","C","B","A","C","B","B","B","A","A"],
    "Phone": [8989657890,9876543210,7654321098,6543210987,5432109876,4321098765,3210987654,2109876543,1098765432,987654321,9876543210,8765432109,7654321098,6543210987,5432109876],
    "Email": ["alice@example.com","bob@example.com","charlie@example.com","david@example.com","rohit@example.com","agastya@example.com","amar@example.com","joy@example.com","rohit@example.com","mahi@example.com","jhanvi@example.com","shubham@example.com","priya@example.com","anit@example.com","rahul@example.com"],
    "Remarks": ["Excellent","Excellent","Good","Excellent","Good","Excellent","Average","Good","Excellent","Average","Good","Good","Good","Excellent","Excellent"]
}
df = pd.DataFrame(data)
df


# In[ ]:


df.notnull().sum()


# In[ ]:


df.describe()


# In[ ]:


df.describe(include="all")


# to print all the rows which are having atleast one missing value in any column

# In[ ]:


df[df.isnull().any(axis=1)]


# In[ ]:


df.isnull().any(axis=1)


# In[ ]:


df.notnull().sum()


# In[ ]:


df.describe(include="all")


# In[ ]:


df["Maths"].isnull()


# In[ ]:


df[df["Maths"].isnull()]


# In[ ]:


df["Maths"].isnull().sum()


# delete a column

# In[ ]:


df.drop("Maths",axis=1)


# In[ ]:


df["Total"]=df["Maths"]+df["Science"]+df["English"]
df.fillna({"Attendance":df["Attendance"].mean(),"Total":df["Total"].mean()})


# In[ ]:


df.drop("Total",axis=1)


# In[ ]:


df["Grade"].fillna(df["Grade"].mode()[0])


# In[ ]:


df["Grade"].fillna(df["Grade"].mode()[0],inplace=True)


# In[ ]:


df


# In[ ]:


df.drop("Total",axis=1)


# In[ ]:


df["Science"].fillna(df["Science"].mean())


# In[ ]:


df["Maths"]=df["Maths"].fillna(df["Maths"].mean())
df


# In[ ]:


df["Maths"].dtype


# In[ ]:


df["Maths"]=df["Maths"].astype("int64")
df


# In[ ]:


df["Maths"].dtype


# In[ ]:


df["Attendance"]=df["Attendance"].fillna(df["Attendance"].mean())
df


# In[ ]:


df["Attendance"].dtype


# In[ ]:


df["Attendance"]=df["Attendance"].astype("int64")
df


# In[ ]:


df["Attendance"].dtype

