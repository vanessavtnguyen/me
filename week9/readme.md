

# Plotting Data

## Number of Deaths across the Years and PYLL Data
- The columns are not in numerics but the to_numeric does not work with commas so first step was to remove the ','.
    - I did this using: astype(str).str.replace(',','').astype(int) which did not require me to use the to_numeric function 
- I created line graphs for each separate data and decided to merge it to show the relationship between Number of Deaths and PYLL across the millenium

## Population Pyramid
- The population pyramid was not too difficult as through researching how to plot it the code was easy to digest and understand