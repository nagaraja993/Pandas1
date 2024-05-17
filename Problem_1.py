import pandas as pd  
    
lst = [['hello', 1], ['world', 2]] 

# creating pandas dataframe from 2D lists
df = pd.DataFrame(lst, columns = ['col1', 'col2']) 
