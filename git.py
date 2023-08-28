#!/usr/bin/env python
# coding: utf-8

# In[1]:


#get_ipython().system('pip install streamlit')


# In[2]:


import streamlit as st
def find_largest(num1, num2, num3):
  return max(num1, num2, num3)

def main():
  st.title('Find the largest number')
  num1=st.number_input('Enter the first number:')
  num2=st.number_input('Enter the second number:')
  num3=st.number_input('Enter the third number:')
  if st.button('Find largest'):
    largest=find_larges(num1, num2, num3)
    st.write("The largest number is {largest}")
if __name__=='__main__':
  main()


# In[ ]:





# In[ ]:





# In[ ]:




