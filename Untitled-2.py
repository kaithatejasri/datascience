#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
df=pd.DataFrame({
    "Name":["Rahul","Joy","Kumar","Mahi","Jhanvi","Shubham","Priya","Anit"],
    "Age":[25,np.nan,35,40,50,np.nan,43,45],
    "City":["mumbai","delhi","chicago","kolkata","np.nan","hongkong","delhi","kolkata"],
    "Sal":[50000,60000,70000,80000,30000,32000,45000,87000],
    "Experience":[2,5,7,np.nan,15,1,8,np.nan],
    "Department":["IT","HR","Finance",np.nan,"HR","Finance","IT","HR"]
})
df


# In[ ]:


df.isna()


# In[ ]:


df.isna().sum()


# In[ ]:


df.isnull()


# In[ ]:


df.notna()


# In[ ]:


df.notnull().sum()


# In[ ]:


len(df)


# In[ ]:


df.isna()


# In[ ]:


df.isna().sum()#it will  return count of missing values in each col of data frame


# In[ ]:


df.isna().sum()/len(df)*100


# In[ ]:


df[df.isna().any(axis=1)]#it will return the rows which have at least one missing value in any column


# In[ ]:


df[df["Name"].isna()]


# In[ ]:


df[df.isna().all(axis=1)]#it will return the rows which have at least one missing value in any column


# In[ ]:


df[df.isna().all(axis=1)]
df[df.isna().any(axis=1)]


# In[ ]:


df[df["Age"].isna()]


# In[ ]:


df.dropna(subset=["Age"])#this will drop the rows which have missing values in the age col only


# In[ ]:


#df.dropna(subset=["Experience"])#it will drop the rows which have missing values in experience col


# In[ ]:


#df.dropna(subset=["Experience","Age","City"])


# In[ ]:


#df2=df.dropna(axis=1)
#df2


# In[ ]:


#df["Experience"].fillna(0)


# In[ ]:


df


# In[ ]:


df=pd.DataFrame({
    "Name":["Rahul","Joy","Kumar","Mahi","Jhanvi","Shubham","Priya","Anit"],
    "Age":[25,np.nan,35,40,50,np.nan,43,45],
    "City":["mumbai","delhi","chicago","kolkata",np.nan,"hongkong","delhi","kolkata"],
    "Sal":[50000,60000,70000,80000,30000,32000,45000,87000],
    "Experience":[2,5,7,np.nan,15,1,8,np.nan],
    "Department":["IT","HR","Finance",np.nan,"HR","Finance","IT","HR"]
})
df


# In[ ]:


df["Experience"].fillna(0)


# In[ ]:


df["City"].fillna("unknown")


# In[ ]:


df["City"].fillna("NA")#unknown and NA are same


# In[ ]:


df.fillna({"Experience":0,"City":"unknown"})


# Filling empty values Statistically
# 

# In[ ]:


df["Age"].fillna(df["Age"].mean())


# In[ ]:


df["Age"].fillna(df["Age"].median())


# In[ ]:


df["Experience"].fillna(df["Experience"].mean())


# In[ ]:


df["City"].fillna(df["City"].mode()[1])


# In[ ]:


df


# In[ ]:


df["City"].fillna(df["City"].mode()[0])


# In[ ]:


df["Department"].fillna(df["Department"].mode()[0])


# Replace

# In[ ]:


df.replace("Finance","Fina",inplace=True)
df


# In[ ]:


df=pd.DataFrame({
    "Name":["Rahul","Joy","Kumar","Mahi","Jhanvi","Shubham","Priya","Anit"],
    "Age":[25,np.nan,35,40,50,np.nan,43,45],
    "City":["mumbai","delhi","chicago","kolkata",np.nan,"hongkong","delhi","kolkata"],
    "Sal":[50000,60000,70000,80000,30000,32000,45000,87000],
    "Experience":[2,5,7,np.nan,15,1,8,np.nan],
    "Department":["IT","HR","Finance",np.nan,"HR","Finance","IT","HR"]
})
df


# In[ ]:


data=pd.DataFrame({
    "Student":["Alice","Bob","Charlie","David","rohit","agastya","amar","joy"],
    "maths":[85,90,np.nan,92,88,95,80,91],
    "science":[80,85,90,np.nan,88,92,np.nan,89],
    "English":[75,80,85,90,88,92,84,89],
    "Sanskrit":[70,75,np.nan,85,88,90,82,87],
    "Attendance":[90,85,95,80,88,np.nan,84,89]
})
data


# Task
# 1. count the missing values
# 2. Fill all missing values in maths with mean value without using mean function
# 3. in english fill missing values with 0
# 4. verify whether your data is having any missing values or not
# 5. fill nan values in attendance column using mean value
# 6. remove that row which have more than 2 nan values 

# In[ ]:


data.isnull().sum()


# In[ ]:


mean = data['maths'].sum() / data['maths'].count()
data['maths'] = data['maths'].fillna(mean)
data


# In[ ]:


data['English'] = data['English'].fillna(0)
data


# In[ ]:


data.isnull().sum()


# In[ ]:


mean = data['Attendance'].sum() / data['Attendance'].count()
data['Attendance'] = data['Attendance'].fillna(mean)
data

