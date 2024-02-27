
import streamlit as st
import supabase

# Initialize Supabase client
supabase_url = "https://vlrdgrjxuihqtqiurveq.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZscmRncmp4dWlocXRxaXVydmVxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg3OTE1NDgsImV4cCI6MjAyNDM2NzU0OH0.KpRCFAVUW65rYMBZNhGMDODIw4zUMp2QCyvBizgLVso"
supabase_client = supabase.create_client(supabase_url, supabase_key)


def fetch_weight_data():
    try:
        # Example query to retrieve specific columns (e.g., created_at and weight) from the 'Weight' table
        # query = "SELECT created_at, weight FROM Weight"
        #  query = "SELECT created_at, weight FROM Weight ORDER BY created_at DESC LIMIT 1"
        
        # Execute the query
        response = supabase_client.from_("Weight").select("created_at, weight").execute()
        print(response)
        
        # Check if the query s successful
            # Access data using the `content` attribute
        return response.data

        if 'data' in data:
                return data['data']
              
        else:
                print("No data returned from Supabase.")
  
    except Exception as e:
        print(f"Error fetching data from Supabase: {str(e)}")


# def fetch_weight_data():
#     try:
#         # Example query to retrieve specific columns (e.g., created_at and weight) from a table called 'weight'
#         # query = "SELECT created_at, weight FROM Weight"
#         # Execute the query
#         # response = supabase_client.sql(query)

#         response = supabase_client.from_("Weight").select("created_at, weight").execute()
        
#         # response = supabase.table("Weight").select("created_at, weight").execute()
#         # Check if the query was success
        
#         if 'error' not in response:
#             return response['data']
#         else:
#             st.error(f"Failed to fetch weight data from Supabase: {response['error']}")
#     except Exception as e:
#         st.error(f"Error fetching data from Supabase: {str(e)}")

def display_weight_data(weight_data):
    if weight_data:
        # st.write("Weight Data:")
        lastdata = weight_data[-1]
        # st.write(lastdata['weight'])
        return lastdata['weight']
    else:
        st.warning("No weight data available")

def main():
    st.title("Weight Data from Supabase")
    weight_data = fetch_weight_data()
    display_weight_data(weight_data)

if __name__ == "__main__":
    main()
