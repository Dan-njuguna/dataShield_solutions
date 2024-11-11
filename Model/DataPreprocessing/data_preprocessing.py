import pandas as pd
import numpy as np
#import my asyncio main function from pipeline_kfk
from pipeline_kfk import main
#from pipeline_kfk import main()
#from sklearn.pipeline import Pipeline
import asyncpg
import asyncio

#run the main coroutine
if __name__ == "__main__":
  data= asyncio.run(main())


async def access_data_from_script(data):
    """
    This function is used to fetch the asyncio main function from pipeline_kfk python script 
    It should then use the fetched data to create a pandas dataframe which should be used in model training
    :return: None
    """
   
    dataf= await pd.DataFrame(data)
    return dataf
data = run(access_data_from_script())
print(data)
#Data preprocessing steps 
# async def preprocess_data(df:pd.DataFrame)->pd.DataFrame:
#     """
#     This function is used to preprocess the data fetched from the database
#     :param df: The data fetched from the database
#     :return: The preprocessed data
#     """
#     #select columns whose data type is object
#     categorical_columns=df.select_dtypes(include=['object']).columns

#     #select columns whose data type is float or int
#     numerical_columns=df.select_dtypes(include=['float','int']).columns

#     #handle missing values
#     df[categorical_columns]=df[categorical_columns].fillna("unknown")
#     df[numerical_columns]=df[numerical_columns].fillna(df[numerical_columns],method='ffill')

#     #creation of an array from the dataframe
#     preprocessed_data=np.array(df)
#     return preprocessed_data 

# #return preprocessed_data
# preprocessed_data=asyncio.run(preprocess_data(data))  
# print(preprocessed_data.head(5))







