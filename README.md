# Project_4_Market_Pen

Project 4: Market penetration 
Hoa Tran 
20/2/2022 

I. Introduction:

The main goal of this project is to simulate how a product is adopted over time by using the difference equation called the Bass fusion model. It presents a rationale of how current adopters and potential adopters of a new product interact as seen through the calculations required of the model. This is basically how new customers accustomed to new product and technologies. The reason this is intriguing is that by successfully understanding and analyzing the results, we will be able to utilize it in a broader context such as forecasting product’s sales as well as technology. 

II. Methods: 

a/ Explaining the algorithm: 

Part 1:

In the first part of this project, the goal is to plot the fraction of new adopters and total rate of exchange on the same graph. To do this, we first must calculate the fraction of new adopters from a constant rate and from social contagion so that we will get the fraction of new adopters in total. This calculation is then placed in the while loop with the appropriate conditions so that the calculations are updated until the condition is false. After that,  it plots the calculations on the a graph with two curves: fraction of new adopters and rate of exchange over time. 

Part 2: 
 
 For the second part, the goal is to create two graphs, one for the number of influentials and imitators and their total number and another one for the fraction of the two groups and their rate of adoption. To do this, we calculate each of the required calculations by their respective methods. That is to say that for instance, we calculate the number of influential in accordance with the instructions in the project and do the same thing with the others. We update these calculations in a while loop. At the end of the loop, we plot these calculations into two different graphs. 

b/ Algorithm implementation: 

Part 1:

Our program has two functions productDiffusion and main: 
The productDiffusion takes float values, chanceAdoption, socialContagion and dt, and integer value, weeks, as parameter. Then it creates a list for the fraction of new adopters, total rate of exchange and time (weeks) so that it could assign value in the while loop to plot the calculations required. It also set the value of the initial fraction of new adopters and time as 0. Afterwards, it uses a while loop to calculate the fraction of new adopters and total rate of exchange. After calculating them, it assigns those values into the lists created above it could plot these values into the same graph. This will go on while the condition of the loop is true (being time step (dt) smaller than weeks). When we arrive at the end of the loop, the fraction of new adopters and total rate of exchange has already been updated from the beginning to the final week with each update in accordance with the assigned time step. 
The main function is where the program begins.  It simply calls the productDiffusion function with values for the parameter in the following order chanceAdoption, socialContagion, weeks, and dt. 

Part 2: 

For part two, we have two functions productDiffusion2 and main. 

The productDiffusion2 takes inSize, imSize, rIn, sIn, rIm, sIm, weight, weeks, and dt as its parameter (with weeks being an integer value and the rest is float). It also set the value of the proportion of imitators and influential as well as time as 0. Moreover, the function creates the necessary lists so that the values can be assigned to them for the required visualizations. Then, it uses a while loop to calculate the proportion of influentials, the number of influentials and their rate of adoption. These calculations are updated as long as the condition for the loop holds true. After they are calculated, each calculation is assigned to its according list for the purpose of visualizing them in a graph. The loop does these same things for the imitators and the resulting calculations are plotted after having been assigned to the correct lists. The function also calculate the total number of imitators and influentials as well as their total rate of adoption and visualize them. If we arrive at the end of the loop, the result of this function is two graphs with weeks on the x-axis and the proportion of adopters (for the first graph) and total number of people (for the second graph).  

The main function is where the program begins as it simply calls the productDiffusions2 function and assign the values to its parameter. 

III. Results and conclusion 

![](https://github.com/HoaTran2003/Project_4_Market_Pen/blob/main/1.jpg)
The graph shows the changes in the proportion of new adopters as well as rate of exchange over the course of 15 weeks. For the first 4 weeks, the two curves overlap with each other with little to no differences. But as week 4 and onwards, the fraction of new adopters experiences a significant spike, especially from week 6 to week 8, and this increment slows down during the last few weeks. As for the rate of exchange, its curve peaks during the 6th week and then gradually curves down for the rest of the period. The reason behind this pattern is that the rate of exchange can be understood as the fractions of new adopters added divided by the time step. Therefore, as more people are becoming adopters, which is an increase in the fraction of adopters, the rate of exchange will decline. This explains the peak at the 6th week for the rate of exchange, indicating that the fraction of new adopters rises significantly at the same time. As the rate of exchange approaches 0, the proportion will approach 1 since as time goes on, less people are likely to become new adopters, leading to a decrease in interactions among adopters and non-adopters. 

![](https://github.com/HoaTran2003/Project_4_Market_Pen/blob/main/2.jpg)
This graph is the result of setting the adoption rate significantly lower compared to the first graph. The two curves overlap with each other until around the 9th week mark and then we start to see a sharp increase in the proportion of new adopters afterwards, approaching the value of 1. As for the rate of exchange, its curve decreases and approaches zero with an increase around the 12th week. The reason for this is that as the rate of social contagion stays the same, a decrease in adoption rate means that it will take longer for the proportion of new adopters to increase. This also means that the rate of exchange will increase at a lower rate or in other words, peak at 0.2 longer compared to the first graph (in the previous question). The reason for this is that lower adoption rate means that it is going to take people longer to adopt the product, meaning that there will less interactions between adopters and non-adopters at the earlier weeks (until the fraction of new adopters start to increase).

 ![](https://github.com/HoaTran2003/Project_4_Market_Pen/blob/main/3.jpg)
The trend for the proportion of new adopters and rate of exchange are different in this graph as the social contagion rate is set to 0. As for the fraction of new adopters, it increases throughout the 15 weeks while the curve for the rate of exchange declines to nearly 0 at the 15th week. Compared to other graphs, the rate of exchange peaks at 0.2 and then starts to decline. The reason for this is that the fraction of new adopters is not affected by social contagion, meaning that the current number of new adopters cannot convince any non-adopters to adopt the product. This leads to the rate of exchange peaks at the start and then decline throughout the period due to the constant rate of adoption (based on the calculation for it as s is set to 0 so rate of exchange is reliant on the value of r).

![](https://github.com/HoaTran2003/Project_4_Market_Pen/blob/main/4.jpg)
The proportion of influentials and imitators seem to have a similar trend and that is increasing over time until they both overlap after the 12th week, both of which are approaching 1. As for the total rate of adoption, it peaks at around week 6 and then falls of at the later weeks and it seems that it is approaching 0. An interesting trend is that all three curves start at 0 and have quite a similar trend from week 2 to week 6 (all three increasing). The reason for all of this is that imitators are influenced by influentials so as the fraction of influentials rises, so do the fraction of imitators. However, it is clear that the rate of increase must be different since one group is influenced by the other group (influentials influence imitators and other imitators can persuade one another). For the adoption rate, as the fraction of adopters approach 1, it will approach 0 since less people are becoming more adopters as time go on. 

![](https://github.com/HoaTran2003/Project_4_Market_Pen/blob/main/5.jpg)
All three curves both increase throughout the 15 weeks but at varying degree. Moreover, it is clear that the rate of increase for the number of influentials compared to that of imitators. The reason is the same as above since the population of imitators are dictated by the number of influentials and even among other imitators (influentials can persuade imitators to use the product). Moreover, there are more influential adopters compared to adopters, contributing to the different rate of increase.

![](https://github.com/HoaTran2003/Project_4_Market_Pen/blob/main/6.jpg)
 
When weight variable is set to 0.01 instead of 0.6, there is a greater difference in the proportion of influentials and imitators regarding their rate of increase. Although both curve increase throughout the period, the fraction of influentials increase at a much faster rate compared to those of imitators. As for the rate of exchange, even though it peaks at week 6th , there is a clear fluctuation in its curve for the later weeks. To be more specific, there is a slight increase around week 10 and then the curve starts to go downward later on. All of this is because imitators are mostly influenced by imitators who already adopted the product compared to influential adopters since weight is lower by a large amount (based on the calculation for social contagion). Such a change also leads to the difference in the curve for total rate of exchange. 
 
 ![](https://github.com/HoaTran2003/Project_4_Market_Pen/blob/main/7.jpg)
All three curves experience a rise throughout the 15-week period. However, the rate of increase for influentials are much more drastic compared to that of imitators. This is because as the weight variable gets lower, imitators are more likely to be influenced by other imitators compared to influential. That is to say that imitators are less likely to be influenced by influential adopters and are more affected by imitators who already adopted the product. This leads to the difference in the rise in the number of imitators compared to the previous graph. The total number still has the same trend compared to the previous graphs as a change in weight does not affect it. 

IV. Conclusion: 

Overall, this project has helped me understand more about difference equation but there are certain challenges. First of all, this is the first time I’ve ever worked on a project related to computer science and the process of creating algorithms, explaining it and implementing it in Python are quite challenging to me. Moreover, making codes for a longer problem is also a challenge to me as I have run into errors where I forgot to multiply the correct variables leading to wrong calculations and other similar problems. Finally, I find it quite difficult to understand the project as there are long explanations and lots of variables in the calculations to fully comprehend. Therefore, it took me and Huy quite a while to create a program for the project. 

