# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 21:24:12 2022

@author: Hoa Tran
Project 4: Market Penetration
"""
import matplotlib.pyplot as mpl
import matplotlib.pyplot as pyplot

#Part 1: 

def productDiffusion(chanceAdoption, socialContagion, weeks, dt): 

    '''
Parameters: 
    chanceAdoption: Rate of adoptions by chance alone 
    socialContagion: Rate of adoptions caused by interactions between 
                     adopters and non-adopters
    weeks: Number of weeks 
    dt: time step (fraction of a week)
Functions used to calculate the fraction of new adopters over 15 weeks 
and the total rate of exchange. After that, it plots these value into a plot.

Return value: None
    
    '''    
    Adopters_list=[] # List of proportion of new adopters
    
    proportionadopters=0 # Set the fraction of adopters to 0 
    rate_exchangelist=[] # List of the total rate of exchange
    Timelist=[] # List of time
    time=0 # Set time to 0 
    while time < weeks: # while loop used when the value of time is smaller than weeks
        newadopters_social= socialContagion*proportionadopters*(1-proportionadopters)*dt # new adopters by social contagion 
        newadopters_constant= chanceAdoption*(1-proportionadopters)*dt # new adopters with constant rate
        proportionadopters=proportionadopters+newadopters_social+ newadopters_constant # calculate the proportion of new adopters 
        rate=(newadopters_social+ newadopters_constant)/dt # calculate rate of exchange
        Adopters_list.append(proportionadopters) # Assign value to list of adopters
        rate_exchangelist.append(rate) # Assign value to list of rate of exchange
        time=time+dt 
        Timelist.append(time) 
    mpl.plot(Timelist,Adopters_list , label = "New adopters") # plot the fraction of new adopters
    mpl.plot(Timelist,rate_exchangelist , label = "Rate of exchange") # plot the rate of exchange
    mpl.legend(loc = 'center right')
    mpl.xlabel('Weeks')
    mpl.ylabel('Proportion of Adopters')
    mpl.show()

#Part 2:
def productDiffusion2(inSize, imSize, rIn, sIn, rIm, sIm, weight, weeks, dt):
    '''
    Parameters: 
        inSize: the population of influentials 
        imSize: the population of immitators 
        rIn: rate of adoption for influentials 
        sIn: social contagion for influentials 
        rIm: rate of adoption for immitators 
        sIm: social contagion for immitators
        weight:The extent to which imitators are more likely to
               be influenced by influentials than other imitators
        weeks: number of weeks
        dt: time step(fraction of a week)
    
    This function is used to caculate the fraction of immitators and influentials 
    and the total rate of both groups. Morover, it is also used to calculate
    the number of influentials and imitators as well as the total for both groups. 
    After that, it will plot these calculations into two seperate plots. 
    
    Return value: None 
        
    '''
    proportionIn=0  #Set the fraction of influentials to 0
    proportionIm=0  # Set the fraction of imitators to 0 
    time=0 
    timeList=[] # List of time 
    proportion_In_list=[] # List of the fraction of influentials
    proportion_Im_list=[]
    total_rate_list=[] # List of the total rate of influentials and immitators
    numIn_list=[] # List of number of influentials
    numIm_list=[] # List of  number of imitators
    rateAdopt=[] # List of rate of adoption
    numTotallist=[] # List of total number of influentials and imitators
    while time < weeks: 
        proportionAdopt_In= rIn*(1-proportionIn)*dt # influentials with constant rate
        proportionSocial_In=sIn*(1-proportionIn)*dt*proportionIn # # influentials with social contagion
        proportionIn= proportionIn+ proportionAdopt_In+ proportionSocial_In 
        numIn= inSize*proportionIn #number of influentials
        rate_In=(proportionAdopt_In+ proportionSocial_In)/dt # rate of adoption for influentials
        proportionAdopt_Im=rIm*(1-proportionIm)*dt # immitators with constant rate
        proportionSocial_Im1=sIm*(1-proportionIm)*weight*dt*proportionIn # immitators with social contagions (by influentials)
        proportionSocial_Im2= (1-weight)*sIm*(1-proportionIm)*dt*proportionIm # immitators with social contagions (by immitators who already adopted)
        proportionIm= proportionIm+proportionAdopt_Im+ proportionSocial_Im1+proportionSocial_Im2
        numIm=imSize*proportionIm #number of immitators
        rate_Im=(proportionAdopt_Im+ proportionSocial_Im1+proportionSocial_Im2)/dt# rate of adoption for imitators
        total_num=numIn+numIm # total number of influentials and imitators
        total_rate=rate_In+rate_Im# total rate of adoption 
        proportion_In_list.append(proportionIn)
        proportion_Im_list.append(proportionIm)
        rateAdopt.append(total_rate)
        total_rate_list.append(total_rate)
        numTotallist.append(total_num)
        time=time+dt # time increase by dt
        timeList.append(time)
        numIn_list.append(numIn)
        numIm_list.append(numIm)
    mpl.plot(timeList,proportion_In_list, label = "Proportion of Influentials") # Plot the fraction of influentials
    mpl.plot(timeList,proportion_Im_list, label = "Proportion of Imitators")  # # Plot the fraction of imitators
    mpl.plot(timeList, total_rate_list , label = "Total rate of exchange") # Plot the total rate of exchange
    mpl.legend(loc = 'center left')
    mpl.xlabel('Weeks')
    mpl.ylabel('Proportion of Adopters')
    mpl.show()
    pyplot.plot(timeList, numIn_list, label="Number of Influentials") # Plot the number of influentials
    pyplot.plot(timeList, numIm_list, label="Number of Imitators") # Plot the number of imitators
    pyplot.plot(timeList, numTotallist, label="Total number") # Plot the total number of influentials and imitators
    pyplot.legend(loc = 'center left')
    pyplot.xlabel('Weeks')
    pyplot.ylabel('Number of people')
    pyplot.show()


def main():
    '''
    Used to call the productDiffusion(chanceAdoption, socialContagion, weeks, dt)
    function with each value in accordance with the listed parameters.
    Used to call the function productDiffusion2(inSize, imSize, rIn, sIn, rIm, sIm, weight, weeks, dt)
    with the value in accordance with the parameters. 

    Return value: None

    '''
    productDiffusion(0.002,1.03,15,0.01 ) 
    productDiffusion2(600, 400, 0.002, 1.03, 0, 0.8, 0.01, 15, 0.01)
main()

    