import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np 
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

st.title("Food Recommendation System")
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.write(' ')

# with col2:
    
st.text("Let us help you with food")
st.image("food.jpg")
# with col3:
#     st.write(' ')



st.subheader("How many recommendation you want?")  
val = st.slider("from 1 to the 10!",1,10)


rs = pd.read_csv("rs.csv")



names = rs['antecedents'].tolist()
x = np.array(names)
ans1 = np.unique(x)

finallist = ""
bruh = st.checkbox("Choose your Dish")
if bruh == True:
    finallist = st.selectbox("Our Choices",ans1)


##### IMPLEMENTING RECOMMENDER ######

def food_recommendation(Food_Name):
     recommend=[]  

     for i in range(len(rs)):
      if Food_Name==(rs["antecedents"][i]) :
        recommend.append(rs.iloc[i]["consequents"])
     
     
     if recommend:
            try:
               return recommend[:val]
            except: return recommend
     else:recommend="No similar items found"
 


display = food_recommendation(finallist)

if bruh == True:
    bruh1 = st.checkbox("We also Recommend : ")
    if bruh1 == True:
        for i in display:
            st.write(i)
