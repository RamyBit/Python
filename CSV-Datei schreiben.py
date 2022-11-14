#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import ipywidgets as widgets
from IPython.display import display


# In[19]:


liste=[]

name = widgets.Text(description="Name")
surname = widgets.Text(description="Nachname")
subject = widgets.Dropdown(
            options=["---","Mathe","Informatik","Philosophie","Kulturwissenschaften","Psychologie"],
            value = "---",
            description="Fach"
)
button = widgets.Button(description="Speischern!")
display(name)
display(surname)
display(subject)
display(button)

 
def is_valid():
    if name.value !="" and surname.value!="" and subject.value!="---":
        return True
def create_list():
    liste.append( name.value)
    liste.append (surname.value)
    liste.append(subject.value)
    
def save_file():
    with open("fachsutdents.csv","a", newline='',encoding="utf-8") as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = ';', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(liste)
    
def button_click(p):
    if is_valid() == True:
        create_list()
        print(liste)
        save_file()
    else:
        print("Error not valid")
        
button.on_click(button_click)


# In[ ]:





# In[ ]:




