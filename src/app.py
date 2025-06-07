import streamlit as st
from recommend import load_data, recommend_destinations

st.set_page_config(page_title="Travel Recommendation Bot")

st.title("🧳 Travel Recommendation Bot")

continent = st.selectbox("Continent", ["", "Asia", "Europe", "Africa", "North America"])
weather = st.selectbox("Weather", ["", "warm", "cool"])
budget = st.selectbox("Budget", ["", "low", "medium", "high"])
interest = st.text_input("What activity do you enjoy? (e.g., beach, hiking, shopping)")

if st.button("Get Recommendations"):
    df = load_data()
    results = recommend_destinations(df, continent, weather, budget, interest)

    if not results.empty:
        st.subheader("🌍 Recommended Destinations:")
        for _, row in results.iterrows():
            st.markdown(f"**{row['destination']}** — {row['activities']}")
    else:
        st.warning("😕 No matches found. Try changing your preferences.")
 
