import streamlit as st

from recommend import load_data, get_filtered_data
 
# Load data once

df = load_data()
 
st.title("Pune Travel Recommendation Bot")
 
# Select category filter

category = st.selectbox(

    "Choose a category",

    [""] + sorted(df['category'].unique())

)
 
# Select subtype filter (filtered based on category)

if category:

    subtypes = sorted(df[df['category'] == category]['subtype'].unique())

else:

    subtypes = sorted(df['subtype'].unique())
 
subtype = st.selectbox(

    "Choose a subtype",

    [""] + subtypes

)
 
# Get filtered results

results = get_filtered_data(df, category=category if category else None, subtype=subtype if subtype else None)
 
# Display results

st.write(f"### Recommended Places ({len(results)})")
 
for idx, row in results.iterrows():

    st.markdown(f"**{row['destination']}**")

    st.markdown(f"- Category: {row['category']}")

    st.markdown(f"- Type: {row['subtype']}")

    st.markdown(f"- Notes: {row['notes']}")

    st.write("---")
