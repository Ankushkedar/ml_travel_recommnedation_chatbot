import streamlit as st
from recommend import load_data, recommend_destinations

st.title("🏙️ Pune Spot Recommendation Bot")

df = load_data()

category = st.selectbox("Choose a type", ["", *sorted(df['category'].unique())])
subtype = st.selectbox("Choose a subtype (optional)", ["", *sorted(df[df['category']==category]['subtype'].unique())] if category else [""])

if st.button("Get Recommendations"):
    res = recommend_destinations(df, category, subtype)
    if not res.empty:
        st.success(f"Found {len(res)} spot(s):")
        for i,row in res.iterrows():
            st.markdown(f"**{row.destination}** • *{row.category}* — {row.notes}")
    else:
        st.warning("No places match your filters.")
 
