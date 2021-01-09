#!/usr/bin/env python
# coding: utf-8

# In[15]:


def quarantine_message():
    
    name = input ("Γράψε το ονοματεπώνυμό σου\n")
    
    print (" ")
    
    residence = input ("Γράψε τον δρόμο και τον αριθμό στον οποίο μένεις: ")
    
    print (" ")
    
    menu()
    
    choice = input ("Διάλεξε τον αριθμό που χρειάζεσαι από το παραπάνω μενού: ")
    
    choice_int = int(choice)
    
    while (choice_int!=1 and choice_int!=2 and choice_int!=3 and choice_int!=4 and choice_int!=5 and choice_int!=6):
             
            choice = input ("Διάλεξε τον αριθμό που χρειάζεσαι από το παραπάνω μενού (1-6): ")
    
            choice_int = int(choice)
        
    else:
        
        result = (f"{choice_int} {name} {residence}")
        
        return (result)


# In[13]:


def menu():
    print ("ΕΠΙΛΟΓΕΣ\n")
    print ("1- Μετάβαση σε φαρμακείο ή επίσκεψη στον γιατρό εφόσον αυτό συνιστάται μετά από σχετική επικοινωνία\n")
    print ("2- Μετάβαση σε εν λειτουργία κατάστημα προμηθειών αγαθών αναγκών πρώτης ανάγκης, σούπερ μάρκετ, μίνι μάρκετ όπου δεν είναι δυνατή η αποστολή τους\n")
    print ("3- Μετάβαση στην τράπεζα στο μέτρο που δεν είναι δυνατή η ηλεκτρονική συναλλαγή\n")
    print ("4- Κίνηση για παροχή βοήθειας σε ανθρώπους που βρίσκονται σε ανάγκη\n")
    print ("5- Μετάβαση σε τελετή υπό τους όρους που προβλέπει ο νόμος ή μετάβαση διαζευγμένων γονέων ή γονέων που τελούν σε διάσταση που είναι αναγκαία για την διασφάλιση της επικοινωνίας γονέων και τέκνων σύμφωνα με τις κείμενες διατάξεις\n")
    print ("6- Σωματική άσκηση σε εξωτερικό χώρο ή κίνηση με κατοικίδιο ατομικά ή ανά δυο άτομα\n")
    


# In[16]:


quarantine_message()


# In[ ]:




