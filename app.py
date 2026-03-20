import streamlit as st

# Title of the app
st.title('Financial Coach App')

# Sidebar for user inputs
st.sidebar.header('User Input')

# Define user inputs
income = st.sidebar.number_input('Enter your monthly income:', min_value=0)
expenses = st.sidebar.number_input('Enter your monthly expenses:', min_value=0)

# Calculate savings
savings = income - expenses

# Display results
st.write(f'Your monthly savings: ${savings}')

if savings < 0:
    st.error('You are spending more than you earn!')
else:
    st.success('Great job! You are saving money!')
