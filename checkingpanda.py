# Pandas is a high level data manipulation tool, used by data scientists all over the world.
#In pandas, we store data in a so-called dataframe. Have a look at this data frame, called `brics`.
# we use pandas inplace of numpy when we have to work on multi types of data.
import pandas as pd
data_frame=pd.read_csv("webservice.csv")#in index column we tell that the column 0 actually are indexces otherwise it will consider
print(data_frame)
#different ways to print a single column
print(data_frame["Country"])
print(data_frame.Country)
#Way to add a column
#data_frame["Mine1"]=["A","B","C"]
#By merging to existing columns
#or we can find mean or multiply or add columns and generate new one
data_frame["Mine"]=data_frame["IP_Address"]+data_frame["Country"]
print(data_frame["Mine"])
#to print row we use loc
print(data_frame.loc[1])
#Different ways to access the single element
print(data_frame.loc[1,"AS"])
print(data_frame["AS"].loc[1])#loc value represent the row while other represents the column
print(data_frame.loc[1]["AS"])
pd.dropna()#method for missing values
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("webservice.csv") 
  
# making new data frame with dropped NA values 
new_data = data.dropna(axis = 0, how ='any') 
  
# comparing sizes of data frames 
print("Old data frame length:", len(data), "\nNew data frame length:",  
       len(new_data), "\nNumber of rows with at least 1 NA value: ", 
       (len(data)-len(new_data)))
# dropping column with all null values 
data.dropna(axis = 1, how ='all', inplace = True) 
