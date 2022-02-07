#!/usr/bin/env python
# coding: utf-8

# In[1]:


import camelot
import ghostscript
from camelot import read_pdf


# In[67]:


#!pip install selenium


# In[7]:


# Import required module
import time
from selenium import webdriver


# In[14]:


from tkinter import * 
from PIL import ImageTk,Image


# In[68]:


# root = Tk() 
# root.title('Table Extraction');
# # root.iconbitmap('c:/path')
# root.geometry("400x400")

# #Dropdown Boxes

# def show():
#     label = Label(root, text=clicked.get()).pack()
    
    
# options = [".csv",".json",".xslx"]

# clicked = StringVar()
# clicked.set(options[0])

# drop = OptionMenu(root, clicked , *options)
# drop.pack()

# myButton = Button(root, text="Show Selection" , command=show).pack()

# root.mainloop()


# In[66]:


def csv():
    for i in range(all_tables.n):
        all_tables[i].to_csv(f'PowerGeneration_{i+1}.csv', index=True)

def xlsx():
    # export individually as Excel (.xlsx extension)
    for i in range(all_tables.n):
        all_tables[i].to_excel(f'PowerGeneration_{i+1}.xlsx')

def html():
    # export to HTML
    all_tables.export(f'PowerGeneration_{t+1}.html', f="html")
    
def method():
    
    option = int(input("Enter your option from 1-3  : "))

    if option == 1:
        csv()
 
    elif option == 2:
        xlsx()
 
    elif option == 3:
        html()
 
    else:
        print("Incorrect option")
       
if __name__ == "__main__":
    a= input('Enter the Page Number for Detect the tables in the Page ')
    print("\n")
    user_list = a.split()
    
    # Get all the tables within the file
    all_tables = read_pdf('/Users/Asus/Documents/Atmel Studio/OCR/Report_1.pdf', pages=a)

    # Show the total number of tables in the file
    print("Total number of table: {}".format(all_tables.n))
    
    # Show the total number of tables in the file
    print("Total number of table: {}".format(all_tables.n))

    # print all the tables in the file
    for t in range(all_tables.n):
        print("Table n°{}".format(t))
        print((all_tables[t].df).head())
        
    for t in range(all_tables.n):
        print (all_tables[t].parsing_report)
        print ('\n')
        
    print("Table Extarction Options:")
    print("Csv Export = 1")
    print("Excel Export = 2")
    print("Html Export = 3")
    print("\n")
    
    #xlsx()
    method()
    print("\n")
    
    print("Table Extraction Completed")


# In[ ]:




