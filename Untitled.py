#!/usr/bin/env python
# coding: utf-8

# In[1]:


class stack (object):
    def __init__(self):
        self.items=[]
    def isEmpty (self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop (self):
        self.items.pop()


# In[ ]:


def matching (array):
    ends=list("]})")
    starts=list("{[(")
    match=list([["{","}"],["[","]"],["(",")"]])
    arr=list(array)
    c1=stack()
    if len(arr)%2!=0:
        return False
    else:
        for i in range(len(arr)):
            if arr[i] in starts:
                c1.push(arr[i])
            else:
                if [c1.items[-1],arr[i]] not in match:
                    return False
                else:
                    c1.pop()
                
                
                
                    
    return c1.isEmpty()

