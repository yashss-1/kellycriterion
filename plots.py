import numpy
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np



def trial(p):
    if numpy.random.random() < p:
        return 1
    else:
        return 0
    
def bets( wager, p = 0.5, Total_money = 1000, loss_f = 1, profit_f = 1):
    if trial(p):
        change = wager * profit_f * Total_money * 0.01
    else:
        change = wager * -(loss_f) * Total_money * 0.01
    Total_money += change
    return Total_money
def gmean(a):
    a = np.log(a)
    a = np.mean(a,axis = 0)
    a = np.exp(a)
    return a
def plot(p,a, b):
    iterations=200
    rangevalue=100
    steps = 100
    wagerlist=np.zeros(rangevalue)  
    wagerlist2=np.zeros(rangevalue)   
    np1 = np.zeros((iterations,rangevalue,steps))
    for k in range(iterations):
        for j in range(rangevalue):
            for i in range(1,steps): #rangevalue=percentage of money to bet
                np1[:,:,0]=total
                np1[k,j,i] = bets(j, p, np1[k,j,i-1], a, b)
        print(k)
    for k in range(rangevalue):
        wagerlist[k]=gmean(np1[:,k,-1])
        wagerlist2[k]=np.mean(np1[:,k,-1])
    plt.bar(range(rangevalue),wagerlist)
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


# p = st.slider('Probability of winning:', 0.0, 1.0, 0.5)
# num_player = st.number_input('Number of players:', 1, 5, 1)
# total = st.number_input('Total amount of money:', 1, 100, 100)
# a = st.number_input('Number of players:', 1, 10, 1)
# wager1 = st.number_input('First Fraction of money to bet:', 0, 100, 1)
# wager2 = st.number_input('Section Fraction of money to bet:', 0, 100, 1)
# wager3 = st.number_input('Third Fraction of money to bet:', 0, 100, 1)
# wager4 = st.number_input('fourth Fraction of money to bet:', 0, 100, 1)

p=0.55
q = 1-p
total=100
q = round(q, 2)
a = 1
b = 1




wager5 = (p*b - q*a) / (a*b)
if wager5<0:
    wager5=0
wager5=wager5*100

wager5=round(wager5, 3)
print(wager5)

#p = st.button('randomize profit', on_click=randp)
plot(p,a, b)
