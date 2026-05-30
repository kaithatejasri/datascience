#!/usr/bin/env python
# coding: utf-8

# DATA TYPES
# 

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
df#age & experience col shows values in float type because it's containing NaN values,so pandas does this
  #for non-numerical cols no changes


# CHECK DATA TYPES

# In[ ]:


df.dtypes


# step 1: TO convert age col into int type we must ensure col doesn't contain NaN values

# In[ ]:


df["Age"].fillna(0).astype(int)


# step2: When we display age col we get float values cause we didn't change original data and now our type is still float

# In[ ]:


df["Age"]


# step3: TO permanently convert into int

# In[ ]:


df["Age"]=df["Age"].fillna(0).astype(int)
df["Age"]#without this we won't get outpur


# In[ ]:


df["Age"].dtype


# step4: here u can say it changed our original dataset

# In[ ]:


df


# Example-2

# In[ ]:


df["Experience"]


# In[ ]:


df["Experience"].dtype


# In[ ]:


df["Experience"].fillna(0).astype(int)


# In[ ]:


df["Experience"]


# In[ ]:


df["Experience"].dtype


# In[ ]:


df["Experience"]=df["Experience"].fillna(0).astype(int)
df["Experience"]


# In[ ]:


df["Experience"]


# In[ ]:


df


# Converting int -----> float

# In[ ]:


df["Experience"]=df["Experience"].astype(float)
df["Experience"]


# Converting int/float -------> string

# In[ ]:


df["Age"]=df["Age"].astype(str)
df["Age"]


# In[ ]:


df["Age"]=df["Age"].astype(int)#converting back to int so original data does'nt effect
df["Age"]


# Number -------> boolean

# EX-1 : checking the condition and storing boolean result by creating new column (changes original data)

# In[ ]:


df["flag"]=df["Age"]>30
df


# In[ ]:


df


# EX-2 : Number ----> boolean (By Adding NEW COL..)
# 1. Add new column 
# 2. convert to  boolean using condition on new col

# In[ ]:


#df["Bonus"]=500 --> I'm not using this because all values will be 500 and this concept is called "BROADCASTING"
df["Bonus"]=df["Sal"]*500
df


# In[ ]:


df["High-paid"]=df["Bonus"]>30000000
df


# In[ ]:


df["High-paid"].dtype


# In[ ]:


df


# EX-3: Number ----> boolean (Temporary change)

# In[ ]:


df["Sal"]<50000


# In[ ]:


df


# Converting datatypes Of Categorical Cols 

# In[ ]:


df[["City","Department","Name"]]#Ensure to use double square brackets in case of multiple cols


# Temporary conversion

# In[ ]:


df["City"].astype("category").cat.codes #1.  df["City"] is selecting city col
                                        #2.  .astype("category") here pandas is treating text data as categories not as plain text
                                        #3.  .cat.codes here pandas convert data into numbers alphabetical wise ex-c,d,h,k,m is order so numbers 0,1,2,3,4
                                        #4.  NaN becomes -1 cuz pandas consider missing values as -1


# In[ ]:


df["City"]


# Permanent Change

# In[ ]:


df["City"]=df["City"].astype("category").cat.codes
df["City"]


# In[ ]:


df


# NAME COL - SEE CAREFULLY

# 1. Temporary

# In[ ]:


df["Name"]


# In[ ]:


df["Name"].astype("category").cat.codes #order a,j,k,m,p,r,s = 0,1,2,3,4,5,6,7 (first jh then jo , o comes after h)


# In[ ]:


df["Name"]


# Permanent

# In[ ]:


df["Name"]=df["Name"].astype("category").cat.codes
df["Name"]


# In[ ]:


df["Name"]


# In[ ]:


df

