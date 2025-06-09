#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ask_user_for_insight():
    print("\n🎯 What insight would you like to explore?")
    print("a) Top 10 cancer sites by count")
    print("b) Patient distribution by age")
    print("c) Tumour type frequency")
    print("d) Stage distribution")
    
    choice = input("Enter your choice (a/b/c/d): ").strip().lower()
    return choice


# In[ ]:




