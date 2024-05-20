import streamlit as st
import pandas as pd

# Function to calculate average salary based on user preferences
def calculate_average_salary(df, location, employment_status, job_role):
    # Convert employment status to lowercase and remove spaces
    employment_status = employment_status.lower().replace(" ", "")

    # Filter the dataframe based on user preferences
    filtered_df = df[(df['Location'] == location) &
                     (df['Employment Status'].str.lower().str.replace(" ", "") == employment_status) &
                     (df['Job Title'].str.lower() == job_role.lower())]

    # Check if there is any data matching the provided preferences
    if filtered_df.empty:
        return None

    # Calculate the average salary for the filtered data
    average_salary = filtered_df['Salary'].mean()

    return average_salary

# Load your dataframe here, assuming it's named df
df = pd.read_csv('cleaned_salary_dataset.csv')

# Define Streamlit app function
def main():
    st.title("Average Salary Calculator")
    
    # Input preferences from the user
    location = st.text_input("Enter your preferred location: ")
    employment_status = st.text_input("Enter your preferred employment status (e.g., Full-time, Part-time, etc.): ")
    job_role = st.text_input("Enter your preferred job role (e.g., Software Engineer, Data Analyst, etc.): ")

    if st.button("Calculate Average Salary"):
        # Calculate average salary based on user preferences
        average_salary = calculate_average_salary(df, location, employment_status, job_role)

        if average_salary is not None:
            st.success(f"Average Salary based on preferences per annum: ${average_salary:.2f}")
        else:
            st.error("No data found matching the provided preferences.")

if __name__ == "__main__":
    main()
