#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data = {"players" :["vk","roh","sehwag","msd","vk","roh","seh","msd"],
    "matches" :[100,200,300,400,100,200,300,400],
    "total_runs" :[5000,8000,9000,7500,5200,8500,9200,7800],
    "highest_score":[183,264,219,183,160,209,201,150],
    "balls_faced" :[6000,9000,8500,8200,6100,9200,8600,8300]}
df = pd.DataFrame(data)
df["strikerate"] = (df["total_runs"]*df["balls_faced"])/100
print(df["strikerate"])


# In[ ]:


import pandas as pd
data = {"players" :["vk","roh","sehwag","msd","vk","roh","seh","msd"],
    "matches" :[100,200,300,400,100,200,300,400],
    "total_runs" :[5000,8000,9000,7500,5200,8500,9200,7800],
    "highest_score":[183,264,219,183,160,209,201,150],
    "balls_faced" :[6000,9000,8500,8200,6100,9200,8600,8300]}
df = pd.DataFrame(data)
total =df.groupby("players")["total_runs"].sum().reset_index()
print(total)


# In[ ]:


import pandas as pd
data = {"players" :["vk","roh","sehwag","msd","vk","roh","seh","msd"],
    "matches" :[100,200,300,400,100,200,300,400],
    "total_runs" :[5000,8000,9000,7500,5200,8500,9200,7800],
    "highest_score":[183,264,219,183,160,209,201,150],
    "balls_faced" :[6000,9000,8500,8200,6100,9200,8600,8300]}
df = pd.DataFrame(data)
virat_kholi = df[(df["players"]=="vk") & (df["highest_score"]> 150)]
print(virat_kholi)


# In[ ]:


import pandas as pd
data = {
    "players" :["vk","roh","sehwag","msd","vk","roh","seh","msd"],
    "matches" :[100,200,300,400,100,200,300,400],
    "total_runs" :[5000,8000,9000,7500,5200,8500,9200,7800],
    "highest_score":[183,264,219,183,160,209,201,150],
    "balls_faced" :[6000,9000,8500,8200,6100,9200,8600,8300]

}
df = pd.DataFrame(data)
print(df)


# In[ ]:


print(df["players"])

