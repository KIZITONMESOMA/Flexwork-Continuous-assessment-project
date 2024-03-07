#!/usr/bin/env python
# coding: utf-8

# ## Name: KIZITO NMESOMA ODIZILIKE
# ## Email: odizilike@gmail.com
# ## Contact: 08165573234
# ## FE/23/7670924
# 
# 

# + INSTRUCTIONS:
# # Create a table using the Basic Python Dictionaries and plot the charts.(minimum of 2 charts of your choice)
# 

# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


## This is a data set comprising of students rating (at a scale of /100) of their choice of Pure Mathematics, 
## Applied Mathematics and Rudiments of Advanced Calculus. This sample was taken by picking ten(10) students at random from Part III
## At the Department of Mathematics, Faculty of Sciences, Obafemi Awolow University, Ile Ife Osun State Nigeria.
## It should be noted that the courses below represents Pure Mathematics, Advanced calculus and Applied mathematics in the other.


# In[24]:


plotdata = pd.DataFrame({
    "MTH310(ABSTRACT ALGEBRA I)" :[57,67,77,83,87,90,95,97,100,110],
    "MTH318(MATHEMATICAL METHODS III)" :[18,28,38,48,58,68,78,88,98,108],
    "MTH315(SOLID MECHANICS)" :[10,20,30,40,50,60,70,80,90,100]}, 
    index=["Adburaman", "Emma Balogun", "Olalekan", "Oluwatosin", "Hadassah", "Yusuf(Course Rep)","Faith", "Deborah","Christianah","Henry"]
)


# In[25]:


df = pd.DataFrame(plotdata)


# In[26]:


df


# In[27]:


mathsdataset = pd.DataFrame({
    "MTH310(ABSTRACT ALGEBRA I)" :[57,67,77,83,87,90,95,97,100,110],
    "MTH318(MATHEMATICAL METHODS III)" :[18,28,38,48,58,68,78,88,98,108],
    "MTH315(SOLID MECHANICS)" :[10,20,30,40,50,60,70,80,90,100]},
    index=["Adburaman", "Emma Balogun", "Olalekan", "Oluwatosin", "Hadassah", "Yusuf(Course Rep)","Faith", "Deborah","Christianah","Henry"])
mathsdataset.plot(kind='bar', stacked=True,figsize=(15, 8))


# + The above chat was drawn to a scale 50 units to 1cm and the data was first arranged in descending other of arrangement prior to tabulation.

# + The names of students interviewed and their responses are as shown above

# + It can be deduced from the above chart that the students are generally cool with MTH310 which signifies a great interest in Pure mathematics. It also follows that MTH318 an avarage interest rate. By implications, a slight improvement can help the students advance into this area of mathematics,while the interest for Advanced calculus is sparsely distributed.

# In[ ]:


##  Let us now represent the above in a linear graph. This is shown below with a scale of 20 units to 1cm.


# In[28]:


plotdata.plot()


# ## 1. Define and state the difference between Data analysis and Data science.

# Ans: Data Analysis is a simply the sequential process of obtaining data, manipulating and analysisng the data for further results. It cmprises an order of steps,mostly using some statistical tools in presenting information with respect to the task given.
#  It can be seen as the process of inspecting, cleansing, transforming and modelling data with the goal of discovering useful information, informing conclusion and supporting decision making.
#  Data Analysis is different from Data science in the sense that a data scientist does not stop at the result so obtained (information) but goes further to employ more sophisticated programming skilss, mathematical tools and algebraic manipultions to  build a lasting  solution to a given problem. 
#  Data Scientists builds most tools used by Data analysts in their data manipulations. Hence they usually have more programming and mathematical skills and then apply this skills in machine learning process. While Data analysis have a better communication skills, creating a better report with stronger story telling skills.
# 

# ## 2. State the Basic Libraries used in Python Data Analysis

# The Basic Libraries in Python Used by Data Analysts inludes (but not limited to);
# + Numpy
# + Matplot Library
# + Seaborn
# + Pandas
# + Statsmodel
# + Scipy
# + Scikit-Learn
# and others

# ## 3. State the Process of Data Analysis.

# The Basic steps involved in Data Analysis Includes;
# + Obtaining Data(Data Extraction)
# + Data Cleaning
# + Data Wangling
# + Analysis
# + Action(s)

# In[ ]:


## Let us Attempt a representation of the information using pie chart.


# In[45]:


# Creating dataset
Students = ["Adburaman", "Emma Balogun", "Olalekan", "Oluwatosin", "Hadassah", "Yusuf(Course Rep)","Faith", "Deborah","Christianah","Henry"]
 
MTH310 = [57,67,77,83,87,90,95,97,100,110]
 
# Creating plot
fig = plt.figure(figsize=(9, 6))
plt.pie(MTH310, labels=Students)
plt.title("MTH310(ABSTRACT ALGEBRA I")

plt.xlabel("PART III Students")


# show plot
plt.show()


# In[46]:


Students = ["Adburaman", "Emma Balogun", "Olalekan", "Oluwatosin", "Hadassah", "Yusuf(Course Rep)","Faith", "Deborah","Christianah","Henry"]
 
MTH318 = [18,28,38,48,58,68,78,88,98,108]
 
# Creating plot
fig = plt.figure(figsize=(9, 6))
plt.pie(MTH318, labels=Students)
plt.title("MTH318(MATHEMATICAL METHODS III")

plt.xlabel("PART III Students")


# show plot
plt.show()


# In[49]:


Students = ["Adburaman", "Emma Balogun", "Olalekan", "Oluwatosin", "Hadassah", "Yusuf(Course Rep)","Faith", "Deborah","Christianah","Henry"]
 
MTH315 = [10,20,30,40,50,60,70,80,90,100]
 
# Creating plot
fig = plt.figure(figsize=(9, 6))
plt.pie(MTH315, labels=Students)
plt.title("MTH315(SOLID MECHANICS)")

plt.xlabel("PART III Students")


# show plot
plt.show()


# In[50]:


X=(mathsdataset)


# In[54]:


plt.plot(X, X**2)
plt.title('FLEXWORK PRACTICAL CONTINUOUS')
plt.figure()


# ## This is where we shall draw the curtain for now.
