#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to list datatype :


# In[ ]:


defination : A list is a collection of items declared in a Particular order.
classification : it is classified as an mutable data type
how to define the list.....? []


# In[ ]:





# In[ ]:





# In[2]:


students = ['anil' , 'kumar' , 'sreeja' , 'keerthi' , 'rafi' , 'simran'] # 0,1,2,3,4,5


# In[3]:


print(students)


# In[ ]:


# req : i want to access kumar name from the above list.......?


# In[ ]:


introduction to indexing : 0,1,2,3......n


# In[4]:


print(students[1])


# In[ ]:


# req : i want to access keerthi name from the above list.......?


# In[5]:


print(students[3])


# In[ ]:





# In[ ]:


1. how to add new elements to the list.......?
2. how to modify the elements in the list......?
3. how to delete the elements in the list......?


# In[ ]:





# In[ ]:


1. how to add new elements to the list.......?


# In[ ]:





# In[ ]:


# req : i want to add naveen name to the above list.......?


# In[ ]:


note :- always use "student.append('')"  in order to add a new element


# In[7]:


students.append('naveen')


# In[8]:


print(students)


# In[ ]:


# req : i want to add adil name to the above list.......?


# In[ ]:





# In[9]:


students.append('adil')


# In[10]:


print(students)


# In[ ]:





# In[ ]:





# In[ ]:


#req : i want to add pallavi to the second index.......?


# In[ ]:


note :- use "[students.insert(no.,'name')] to add and insert the element between index


# In[ ]:





# In[12]:


students.insert(2,'pallavi')


# In[13]:


print(students)


# In[ ]:





# In[14]:


print(students[2])


# In[ ]:





# In[ ]:


what is the diffrence between append and insert method in a list.....?
ans ---- append method is used to add new elements in the list while insert method is used to 
add and insert new elements between the indexes


# In[ ]:





# In[ ]:


2. how to modify the elements in the list......?


# In[15]:


print(students)


# In[ ]:


# i want to change sreeja name to meghana....?


# In[16]:


print(students[3])


# In[19]:


students[3] = 'meghana'


# In[20]:


print(students[3])


# In[21]:


print(students)


# In[ ]:





# In[ ]:


3. how to delete the elements in the list......?


# In[ ]:


#req : i want to delete anil name from the list......?


# In[ ]:





# In[ ]:


use (del students[index]) to delete the element from the list


# In[ ]:





# In[22]:


del students[0]


# In[23]:


print(students)


# In[ ]:





# In[ ]:




