
# Getting to know Pandas 

## Selecting Rows and Columns
- Selecting Roes and columns were crucial in producing my graphs 

df.loc[df[''] == '']: selects rows which contains the ''
- Discovered that you can use different signs such as >= to get values above a specific number
| : this means or
& : this means and 

## Removing Rows and Columns
- I learnt many functions to remove the data I did not need with much more ease in order to produce my graphs

df.drop(['']) : drops rows 
df.drop('', axis=1): drops columns
df[df.name != '']:  does not include roes that contain ''
