#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
df=pd.DataFrame({
    "Name":["Rahul","Joy","Kumar","Mahi","Jhanvi","Shubham","Priya","Anit"],
    "Age":[25,np.nan,35,40,50,np.nan,43,45],
    "City":["mumbai","delhi","chicago","kolkata",np.nan,"hongkong","delhi","kolkata"],
    "Sal":[50000,60000,70000,80000,30000,32000,45000,87000],
    "Experience":[2,5,7,np.nan,15,1,8,np.nan],
    "Department":["IT","HR","Finance",np.nan,"HR","Finance","IT","HR"]
})
df


# TO FETCH FIRST 5 ROWS FROM DATA USE HEAD()

# In[ ]:


df.head()


# TO KNOW THE COUNT OF NON-NULL VALUES IN EACH COLUMN ALONG WITH THEIR DATATYPE USE INFO()

# In[ ]:


df.info()#specifies count of not-null values in each col,&  datatypes of col


# TO GET COUNT,MIN,MAX,STD FOR NUMERICAL VALUES(NUMERICAL SUMMARY) USE DESCRIBE()

# In[ ]:


df.describe()


# TO GET COUNT OF NON-NUMERICAL COLUMNS(CATEGORICAL SUMMARY) USE (INCLUDE="OBJECT") ALONG WITH DESCRIBE()

# In[ ]:


df.describe(include="object")#here 1.count gives count of non-null values
                                    #2.unique gives count of unique values
                                    #3.top gives the value which is more repeated in the column(incase their are no repeated values it considers the first value from the column)
                                    #4.freq gives count of how many types the top value repeated


# TO GET SUMMARY OF BOTH NUMERICAL AND CATEGORICAL USE STATISTICAL SUMMARY ,HERE WE USE (INCLUDE="ALL") ALONG WITH DESCRIBE()

# In[ ]:


df.describe(include="all")


# TO CHECK MISSING VALUES USE ISNULL()
# IF THEIR IS NAN VALUE IT RETURNS TRUE ELSE RETURNS FALSE

# In[ ]:


df.isnull()


# TO GET COUNT OF MISSING VALUES

# In[ ]:


df.isnull().sum()#in isnull() we get true/false where true=1,false=0 then sum() adds these 0's & 1's and returns count of missing values (as result is int type pandas display dtype as int64)


# TO REPLACE/CONVERT NAN VALUES IN ANY COLUMN USE FILLNA()

# In[ ]:


df.fillna(0)


# In[ ]:


df.fillna(3)

