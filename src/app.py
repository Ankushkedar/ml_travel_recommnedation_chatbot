import streamlit as st
 
# Pune heritage places data you gave

pune_heritage_places = [

    {"Place Name": "Sapindya Mahadeo Mandir", "Address": "Kasba Peth, Pune"},

    {"Place Name": "Sadashiv Haud and Nagoba", "Address": "Sadashiv peth, Pune"},

    {"Place Name": "Shri Vrudheshwar Pachi Pandav Mandir", "Address": "Wadarwadi, Pune"},

    {"Place Name": "S V Union Shiv Mandir", "Address": "322 Somwar Peth, Pune"},

    {"Place Name": "Daulat House", "Address": "Pune"},

    {"Place Name": "Mujumdar Wada", "Address": "Kasba Peth, Pune"},

    {"Place Name": "Steps of old Kokan Darvaza", "Address": "Kasba Peth, Pune"},

    {"Place Name": "St Ornella's Church", "Address": "Quarter Gate, 443, Nana Peth, Pune"},

    {"Place Name": "Vriddheshwar Siddheshwar Temple and Ghats", "Address": "563, Shivajinagar, Bhamburda, Pune"},

    {"Place Name": "Naik Wada", "Address": "878/879, Shukrawar Peth, Near Naik Hospital, Pune"},

    {"Place Name": "Phani Ali Talim", "Address": "61, Kasba Peth, Pune"},

    {"Place Name": "Trimbakeshwar Mahadev Mandir", "Address": "Wyavahar Ali, Kasba Peth, Pune"},

    {"Place Name": "Chinchechi Talim and Maruti Temple", "Address": "237, Shukrawar Peth, Pune"},

    {"Place Name": "Government Polytechnique College", "Address": "Ganeshkhind, University Road, Shivajinagar, Pune"},

    {"Place Name": "Vimlabai Garware High School", "Address": "Prabhat Road, Deccan Gymkhana, Pune"},

    {"Place Name": "Twashta Kasar Kali Mandir", "Address": "1385, Kasba Peth, Pune"},

    {"Place Name": "War Memorial", "Address": "Jayprakash Narayan Path, Zilla Parishad Chowk, Pune"},

    {"Place Name": "Mrityunjayeshwar Mandir", "Address": "Karve Nagar, 4B/29, Kothrud, Pune"},

    {"Place Name": "Laxmibai Raste Mandir", "Address": "Raste Wada, Rasta Peth, Pune"},

    {"Place Name": "Narpatgir Vishnu Mandir", "Address": "320, Somwar peth, Opp. Shahu Udyan, Pune"},

    {"Place Name": "Parnakuti Bungalow and Hill", "Address": "Yerawada Hill, Pune"},

    {"Place Name": "Controller of Defence Accounts", "Address": "Gultekdi Path, Near Golibar Maidan, Camp, Pune"},

    {"Place Name": "Phadake Ganpati Mandir", "Address": "Sinhgad Road, front of Sharada Math, Pune"},

    {"Place Name": "Chaphekar Smarak", "Address": "Ganeshkhind Road, Pune"},

    {"Place Name": "Govt Photo Zinco Press", "Address": "5, Photo zinco Press Road, Pune"},

    {"Place Name": "Prabhat Film Studio", "Address": "Law College Road, Pune"},

    {"Place Name": "Police Chowkey Complex Aundh", "Address": "Bremen Chowk, Aundh, Pune"},

    {"Place Name": "Poona District Co-Operative Bank", "Address": "Near old City Post"},

    {"Place Name": "Church of Holy Angles", "Address": "Mother Teresa Road, 84, Rasta peth, Pune"},

    {"Place Name": "Dashnam Gosavi Samstha", "Address": "432, Somwar peth, Narpatgiri Chowk, Station Road, Pune"},

    {"Place Name": "Ganpati Mandir Phadake Wada", "Address": "245, Shukrawar Peth, Pune"},

]
 
def get_pune_heritage_places():

    output = ""

    for place in pune_heritage_places:

        output += f"**{place['Place Name']}**\nAddress: {place['Address']}\n\n"

    return output
 
def main():

    st.title("Pune Heritage Places Chatbot")
 
    city = st.selectbox("Choose City", ["Pune", "Mumbai"])

    place_type = st.selectbox("Choose Type of Place", ["Heritage", "Modern", "Parks", "Others"])
 
    if st.button("Show Places"):

        if city == "Pune":

            if place_type == "Heritage":

                st.markdown("### Heritage Places in Pune:")

                st.markdown(get_pune_heritage_places())

            else:

                st.warning("Sorry, data is available only for Heritage places in Pune at the moment.")

        elif city == "Mumbai":

            st.info("Data for Mumbai is coming soon!")

        else:

            st.error("Sorry, currently only Pune and Mumbai are supported.")
 
if __name__ == "__main__":

    main()

 
