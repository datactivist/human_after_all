# Import libraries
import streamlit as st
import pandas as pd
from io import StringIO
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.switch_page_button import switch_page

# Function to calculate the CSV size
def calculate_csv_size(file):
    try:
        # Convert bytes data to a string-based file-like object
        string_data = file.decode("utf-8")
        stringio = StringIO(string_data)

        # Read the CSV file into a DataFrame
        dataframe = pd.read_csv(stringio)

        num_attributes = len(dataframe.columns)
        num_entities = len(dataframe)

        csv_size = num_attributes * num_entities
        return csv_size
    except Exception as e:
        st.error(f"Error: {e}")
        return 0

# Function to extract the number of relationships
def extract_relationships(file):
    try:
        # Convert bytes data to a string-based file-like object
        string_data = file.decode("utf-8")
        stringio = StringIO(string_data)

        # Read the CSV file into a DataFrame
        dataframe = pd.read_csv(stringio)

        # Calculate the number of relationships
        num_rows = len(dataframe)
        num_columns = len(dataframe.columns)

        # Check if the dataset has multi-index
        if isinstance(dataframe.index, pd.MultiIndex):
            # Calculate the number of index combinations
            num_index_combinations = 1

            # Iterate over the index levels to extract unique values
            for i in range(dataframe.index.nlevels):
                index_values = dataframe.index.get_level_values(i)
                num_index_combinations *= len(index_values.unique())

            # Calculate the total number of relationships
            num_relationships = num_rows * num_columns * num_columns * num_index_combinations
        else:
            # Calculate the total number of relationships
            num_relationships = num_rows * num_columns * num_columns

        return num_relationships
    except Exception as e:
        st.error(f"Error: {e}")
        return 0


# Streamlit app
def main():
    st.title("Complexity Detector")
    st.subheader('Find out how complex your dataset is !')

    st.markdown('You\'re probably here because you told yourself **:blue["I can do something with this data"]** :bulb: and you\'re right. But before, we need to know how complex your data is, so we now what we have to deal with :boxing_glove:')

    
    # File selection
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Read file as bytes
            file = uploaded_file.getvalue()

            # Calculate CSV size
            csv_size = calculate_csv_size(file)
            
            #Former display of info
            #st.subheader("CSV Size")
            #st.write(f"The size of the dataset is: {csv_size}")

            # Extract number of relationships
            num_relationships = extract_relationships(file)
            
            #Former display of infos
            #st.subheader("Number of Relationships")
            #st.write(f"The number of relationships in the dataset is: {num_relationships}")
        
        except Exception as e:
            st.error(f"Error: {e}")
           
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Dataset size", value=csv_size)
        col2.metric(label="Number of Realationships", value=num_relationships)
        col3.metric(label="Dataset complexity", value=num_relationships/csv_size)
        style_metric_cards()
    
    next_page = st.button("Next step ⏭️ !")
    if next_page:
        switch_page("Duck talk 🦆")

if __name__ == "__main__":
    main()
