import streamlit as st
import numpy as np
import pandas as pd
import joblib
import matplotlib

def main():
    st.title("Salary Predictor")
    activity=['eda','Prediction','metrics']
    choice=st.sidebar.selectbox("Function", activity)
    
    # EDA
    if choice=='eda':
        st.subheader("EDA section")
        st.text("Exploratory Data Analysis")
        # Load File
        df=pd.read_csv("data/adult_salary.csv")
        
        #Show rows
        num=st.number_input("How many rows to show",min_value=0)
        
        if num:
            st.dataframe(df.head(num))
        # Show columns
        if st.sidebar.checkbox("Columns Show"):
            columns=st.sidebar.multiselect("Select Columns",df.columns.to_list())
            st.dataframe(df[columns])
        # Describe our data
        if st.sidebar.checkbox("Describe Data"):
            st.dataframe(df.describe())
        
        if st.sidebar.checkbox("Give me the shape of the dataset"):
            st.write(df.shape)
        
        # Selections
        # Plot
        
        
    
    
    
    #Predictions
    elif choice=='Prediction':
        st.subheader("Prediction Section")
    
    
    
    
    
    #Metrics
    else:
        st.subheader("Metric Section")
    
    
    
    
    pass














if __name__=="__main__":
    main()
    