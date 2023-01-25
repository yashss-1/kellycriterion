import numpy
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

#this is a simulation to compare the geometric mean and arithmetic mean of cells that stay alive after a certain while
#the kelly fraction is not highlighted on the graph specially but can be found below and can certainly be highlighted on the graph


# this is the function that decides whether the cell lives or dies (1 or 0)
def trial(p):
    if numpy.random.random() < p:
        return 1
    else:
        return 0
# based on the trial outcome, the cells are added or subtracted (here the total_money refers to the amount of cells left)
def bets( wager, p = 0.5, Total_money = 1000, loss_f = 1, profit_f = 1):
    if trial(p):
        change = wager * profit_f * Total_money * 0.01
    else:
        change = wager * -(loss_f) * Total_money * 0.01
    Total_money += change
    return Total_money
#defining the geometric mean function
def gmean(a):
    a = np.log(a)
    a = np.mean(a,axis = 0)
    a = np.exp(a)
    return a
#this is the function that plots the graph
def plot(p,a, b):
    iterations=200 #number of times the simulation is run for each percentage of cells to stay active
    rangevalue=100 #number of percentages of cells to stay active
    steps = 100 #number of times you have to divide or go through the fight with disease in each simulataion 
    # in each percentage of cells to keep active
    wagerlist=np.zeros(rangevalue)  
    wagerlist2=np.zeros(rangevalue)   
    np1 = np.zeros((iterations,rangevalue,steps)) #this is the array that stores the amount of cells after each bet (3d array)
    for k in range(iterations):
        for j in range(rangevalue):
            for i in range(1,steps): #rangevalue=percentage of cells to stay active
                np1[:,:,0]=total #initial money
                np1[k,j,i] = bets(j, p, np1[k,j,i-1], a, b) #getting total number of active cells after each fight and incorporating it into the array
        print(k)
    for k in range(rangevalue): #calculating the geometric mean and arithmetic mean of money after 100 fights
        wagerlist[k]=gmean(np1[:,k,-1]) # in the 100 simulations we have done
        wagerlist2[k]=np.mean(np1[:,k,-1])
    plt.bar(range(rangevalue),wagerlist)  #plotting the graph
    plt.xlabel("Percentage of cells to stay alive out of 100")
    plt.ylabel("Geometric Mean of life at the end of 100 divisions")
    plt.title("Considering geometric mean of values")
    plt.legend()
    plt.show()
    plt.bar(range(rangevalue),wagerlist2)
    plt.xlabel("Percentage of cells to stay alive out of 100")
    plt.ylabel("Arithmetic Mean of life at the end of 100 divisions")
    plt.title("Considering arithmetic mean of values")
    plt.legend()
    
    plt.show()




p=0.55 #probability of survival after each fight
q = 1-p #probability of death after each fight
total=100 #initial number of cells
q = round(q, 2) #rounding off the probabilities
a = 1 #loss factor
b = 1 #profit factor



#calculating kelly fraction which you can see on your screen
wager5 = (p*b - q*a) / (a*b)
if wager5<0:
    wager5=0
wager5=wager5*100

wager5=round(wager5, 3) #rounding off the kelly fraction
print(wager5)

#p = st.button('randomize profit', on_click=randp)
plot(p,a, b) 
#calling plot function
