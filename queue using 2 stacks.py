#!/usr/bin/env python
# coding: utf-8

# In[36]:


class queue2stacks (object):
    def __init__(self):
        self.instack=[]
        self.outstack=[]
    def enqueue (self,item):
        self.instack.append(item)
    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()
        
        


# In[37]:


c1=queue2stacks()


# In[38]:


c1.enqueue(2)
c1.enqueue(3)
c1.enqueue(4)


# In[ ]:




