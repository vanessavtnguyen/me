TODO: Reflect on what you learned this week and what is still unclear.
# Plotting Data

# Lollipop Chart 
- In the lollipop chart the column 'Numbers of Death' were not in numeric form, to change this the code is: 
    causes['Number of Deaths'] = causes['Number of Deaths'].astype(str).astype(int)
    - the 'int' part can be changes to 'float' as well
- I thought the lollipop chart was going to be a struggle but it was not so bad

# Heat Map Chart 
- The heat map was much easier than I expected it to be, and successfully showed the distribution of the top 20 causes of death across each age group.
- However, when I generated the Heat Map the Age group 1-14 and 15-24 were swapped around and I still yet to find a solution

## Donut Graph 
- I enjoyed creating the donut graph and was similar to creating a pie chart but with more aesthetics. I paired it with a histogram to show a better numeric value of each cause
- I still need to figure out how to add the value to each bar to make the graph more digestable.
