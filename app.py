import streamlit as st 
st.title("My First Streamlit App")
st.write("Hello! This is my first streamlit application.")

import streamlit as st
st.title("Edunet Foundation")
st.write("Welcome Streamlit")
st.header("Student Information")
st.markdown("# Streamlit")
st.markdown("**Interactive Python Application**")

# Page configuration
import streamlit as st
st.set_page_config(
    page_title="Student Dashboard",
    page_icon=":mortar_board:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page content 
st.title("Student Performance Dashboard")
st.write("This dashboard shows sample data about student marks.")

# Create sample data 
# Suppose there are marks of 5 students over 3 tests
data = {
    "Test 1": [65,78,88,75,90],
    "Test 2": [68,72,78,80,92],
    "Test 3": [70,75,82,85,95]
}

# Convert data into a DataFrame 
import pandas as pd
df =pd.DataFrame(data, index=["Student A","Student B",
                       "Student C","Student D","Student E"])

# print(df)

# Display the DataFrame 
st.subheader("Marks Data")
st.dataframe(df)

# Display a line chart
st.subheader("Performance Tend (Line Chart)")
st.line_chart(df)


# Display elements
import streamlit as st
 
# Title
st.title("Siddhi Gamer")
 
# Header
st.header("Main Section")
 
# Subheader
st.subheader("Sub Section")
 
# Write
st.write("This is an example of st.write() displaying text, data, or charts.")
 
# Text
st.text("This is plain text shown using st.text(). No formatting is applied.")
 
# Markdown
st.markdown("""
# Markdown Section
- You can use **bold text**
- You can use *italic text*
- You can create lists  """)

# Text and Formatting
import streamlit as st
st.title("Student Performance Dashborad")
st.success("Data Loaded Successfully")
st.warning("Some records contain missing values")
st.error("Failed to connect to the database")
st.info("Analysis is in progress")