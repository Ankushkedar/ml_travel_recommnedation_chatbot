import streamlit as st

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
    {"Place Name": "European Tombs", "Address": "Photozinco press road, Pune"},
    {"Place Name": "Modern High School", "Address": "Jangali Maharaj Road, Shivajinagar, Pune"},
    {"Place Name": "Ramji Gosavi Mandir", "Address": "15 Aug chowk, Somwarpeth, Pune"},
    {"Place Name": "Jhashi Rani Kanyashala", "Address": "Sadashiv Peth, Shanipar, Pune"},
    {"Place Name": "South Court", "Address": "Pune"},
    {"Place Name": "Hotel National", "Address": "14, Wilson Road, Pune"},
    {"Place Name": "Johari Mahadeo Mandir", "Address": "Sadashiv Peth, Pune"},
    {"Place Name": "Bhave School", "Address": "1214 - 1215, Limayewadi, Sadashiv Peth, Pune"},
    {"Place Name": "Sardar Mudliar House", "Address": "334 Rasta Peth, Pune"},
    {"Place Name": "Panchaleshwar Mandir", "Address": "Opp Hotel Pallavi, Lakdi Pul, Pune"},
    {"Place Name": "Narsimha Bhavan Temple", "Address": "Narsimha Vachanalaya, 73 Kasba Peth Pune"},
    {"Place Name": "Ruia Bungalow", "Address": "Mangaldas Road, Pune"},
    {"Place Name": "Pushtimarg Mandir", "Address": "Near Daruwala pool, 61, Raviwar Peth, Pune"},
    {"Place Name": "Samadhis and Temple near Omkareshwar", "Address": "Shaniwar Peth, on banks of river mutha, Pune"},
    {"Place Name": "Rameshwar Temple", "Address": "10, 11 Shukrawar Peth, near Mahatma Phule Mandai, Pune"},
    {"Place Name": "Raste Wada", "Address": "501 - A3, Rasta Peth, Near Apollo Theatre opp. Rupee co - op.Bank, Pune"},
    {"Place Name": "Shinde Chatri", "Address": "Jagtap Nagar, Wanowarie close to Fatima Nagar on tha way to Hadapsar off.Solapur road. Pune"},
    {"Place Name": "Simla Office", "Address": "Shivajinagar, in front of Akashwani, Pune"},
    {"Place Name": "Tulshibaug Mandir Complex", "Address": "177/178, Budhwar Peth, Pune"},
    {"Place Name": "Thorla Sheikh Salla Dargah", "Address": "Shaniwar Peth, pune"},
    {"Place Name": "Aryabhushan Bhavan", "Address": "Fergusson college road, Pune"},
    {"Place Name": "Gupchup Ganpati Mandir", "Address": "106, Shaniwar Peth, Pune"},
    {"Place Name": "Ashley House", "Address": "42, Sasoon Road, Opp. Wadia College, Pune"},
    {"Place Name": "Ashtabhuja Mandir", "Address": "624, Shaniwar Peth, ( Juna 42, Narayan Peth), Pune"},
    {"Place Name": "Fritzgerald Bridge", "Address": "Bund Garden Road, Pune"},
    {"Place Name": "Aundh Vitthal Mandir", "Address": "Near Aundh Rajiv Gandhi Bridge, Aundh, Pune"},
    {"Place Name": "Huzoorpaga School Complex", "Address": "Near Cosmos Bank, Sadashiv Peth,  Pune"},
    {"Place Name": "NMV Highschool New", "Address": "21, Budhwar Peth, Bajirao Road, Pune"},
    {"Place Name": "Holkar Chatri", "Address": "Khadki, Pune"},
    {"Place Name": "Sangam Bungalow", "Address": "Near Sangam Bridge, Pune"},
    {"Place Name": "Lakdi Pul Vitthal Mandir", "Address": "Baburao Phule Path, Lokmanya Nagar, Sadashiv Peth, Pune"},
    {"Place Name": "Shivaji Bridge", "Address": "Near Shaniwar Wada, Pune"},
    {"Place Name": "Lakshmeshwar Mandir", "Address": "Inside lane Opp. Apollo theater, Rasta Peth, Pune"},
    {"Place Name": "Succath Sheloma Synagogue", "Address": "93, Rasta Peth, Pune"},
    {"Place Name": "Tata Bungalow", "Address": "Opp Residency club, Pune"},
    {"Place Name": "Holkar Bridge", "Address": "Khadki, Pune"},
    {"Place Name": "Shri Kedareshwar Mandir", "Address": "Kasba Peth, Near Kasba Ganpati, Pune"},
    {"Place Name": "SNDT Kanyashala", "Address": "591, Narayan Peth, Pune"},
    {"Place Name": "Someshwar Temple", "Address": "Someshwarwadi, Baner - Pashan Link Road, Pune"},
    {"Place Name": "Spicer Adventist University", "Address": "Aundh Road, GaneshKhind, Pune"},
    {"Place Name": "St Helena's School", "Address": "8, Susie Sorabji Road, Pune"},
    {"Place Name": "St. Mira's Secondary School", "Address": "10, Sadhu vasvani Marg, Pune"},
    {"Place Name": "Ornellas High School", "Address": "Quarter Gate, 443, Nana Peth, Pune"},
    {"Place Name": "Tata Management Training Centre", "Address": "42, Mangaldas Road, Opp. Wadia College, Pune"},
    {"Place Name": "Theosophical Society Poona Lodge", "Address": "918, Ganeshwadi, Deccan Gymkhana, Pune"},
    {"Place Name": "Mamledar Kacheri Haveli No 1", "Address": "Khadakmal Ali, Shahu Chowk, Shukrawar Peth, Pune"},
    {"Place Name": "Wadia College Campus Pune", "Address": "Girl's Hostel,19, V.K. Jog Path, Pune"},
    {"Place Name": "Yerwada Prison", "Address": "Samrat Ashok Path, Phule Nagar, Yerawada, Pune"},
    {"Place Name": "Savarkar Smarak", "Address": "Karve Road, near S M Joshi Bridge, Pune"},
    {"Place Name": "Panchmukhi Maruti Mandir", "Address": "Shukrawar Peth, Pune"},
    {"Place Name": "Shree Siddhivinayak Mandir", "Address": "398, Ganesh Peth, Dulya Maruti Chowk, Pune"},
    {"Place Name": "Emmanuel Church Assembly Of God", "Address": "12, Napier Road, Nr M G Bus Stand, Nana Peth, Pune"},
    {"Place Name": "St. Felix High School", "Address": "4, Boat club Road, Pune"},
    {"Place Name": "CID Office", "Address": "Shivajinagar, Pune"},
    {"Place Name": "Patrya-Maruti Sarvjanik Ganeshotsav Mitra Mandal", "Address": "Narayan Peth, Pune"},
    {"Place Name": "Perugate Police Chowky", "Address": "1227 Sadashiv Peth, Pune"},
    {"Place Name": "Aga Khan Palace", "Address": "Nagar Road, Yerawada, Pune"},
    {"Place Name": "Shivkalin Peshvekalin Amruteshwar Mandir Samuh", "Address": "Plot R.No.A/804, Opp. Tilak Bridge, Shaniwar Peth, Pune"},
    {"Place Name": "Belbaug Chowk", "Address": "177/178 Budhwar Peth, Belbaug Chowk Near City Post, Laxmi Road"},
    {"Place Name": "The Bhandarkar Oriental Research Institute", "Address": "812, Shivaji Nagar, Law College Road, Pune"},
    {"Place Name": "Bharat Itihaas Sanshodhak Mandal", "Address": "1321, Sadashiv Peth, next to the Bharatnatya Mandir, Pune"},
    {"Place Name": "Sassoon General Hospitals", "Address": "Sassoon Road, Pune"},
    {"Place Name": "Botanical Survey of India", "Address": "7, Koregaon Park, Pune"},
    {"Place Name": "Central Building", "Address": "Finance Road (B J Road), Near Sassoon Hospital, Pune"},
    {"Place Name": "General Post Office Shivajinagar", "Address": "3, Connaught Road, Pune"},
    {"Place Name": "Chattushringi Mandir", "Address": "Senapati Bapat Road, Near Pune University, Pune"},
    {"Place Name": "Pune City Post Office", "Address": "852 Budhwar Peth, Laxmi Road, Pune"},
    {"Place Name": "College of Agriculture", "Address": "Pune-05, Ganesh Khind Road, Shivajinagar, Pune"},
    {"Place Name": "College of Engineering Pune", "Address": "RB Motilal Kennedy Road, Shivajinagar, Pune"},
    {"Place Name": "District Court Pune", "Address": "Shivajinagar, Pune"},
    {"Place Name": "Dewan Housing Finance Corporation Ltd", "Address": "Pune"},
    {"Place Name": "Don Bosco Youth Centre", "Address": "4, Koregaon Park Road, Pune"},
    {"Place Name": "Fergusson College", "Address": "Fergusson College, F C Road, Pune"},
    {"Place Name": "Gokhale Hall", "Address": "570, Sadashiv Peth, Laxmi Road, Pune"},
    {"Place Name": "Gokhale Institute Of Politics And Economics Staff Quarters", "Address": "Hostel And Guest House, BMCC Road, Deccan Gymkhana, Pune"},
    {"Place Name": "Pataleshwar Cave Temple", "Address": "Near Budhwar Peth, Pune"},
    {"Place Name": "Raja Kelkar Museum", "Address": "52, Ganeshkhind, Pune"},
    {"Place Name": "Ramnivas Ruia College", "Address": "213, Laxmi Road, Pune"},
    {"Place Name": "Shaniwar Wada", "Address": "Narayan Peth, Pune"},
    {"Place Name": "Sir Parshurambhau College", "Address": "436, Tilak Road, Pune"},
    {"Place Name": "State Bank of India, Deccan Gymkhana Branch", "Address": "Near Lakshmi Road, Pune"},
    {"Place Name": "Sinhagad College", "Address": "Balajinagar, Pune"},
    {"Place Name": "Tilak Maharashtra Vidyapeeth", "Address": "Tilak Road, Pune"},
    {"Place Name": "University of Pune", "Address": "Ganeshkhind, Pune"},
    {"Place Name": "Vasantdada Sugar Institute", "Address": "Manjari, Pune"},
    {"Place Name": "Vishrambaug Wada", "Address": "Shaniwar Peth, Pune"}
    {"Place Name": "Mobos Hotel", "Address": "21, Bund Garden Road, Pune"},
    {"Place Name": "Laxmi Narsinha Temple", "Address": "1429, Sadashiv Peth, Pune"},
    {"Place Name": "Natu Wada", "Address": "418, Shaniwar Peth, Pune"},
    {"Place Name": "Navin Marathi School", "Address": "342, Shaniwar Peth, Near Rajaram Bridge, Pune"},
    {"Place Name": "Pasodya Vitthal Mandir", "Address": "440, Budhwar Peth, Pune"},
    {"Place Name": "The Poona Club Ltd.", "Address": "6, Bund Garden Road, Pune"},
    {"Place Name": "Pune Nagar Vachan Mandir", "Address": "181, Budhwar Peth, Pune"},
    {"Place Name": "Rokdoba Temple", "Address": "558, Shivajinagar Gaonthan, Pune"},
    {"Place Name": "Ramabai Hall", "Address": "Lokmanya Nagar, Sadashiv Peth, Pune"},
    {"Place Name": "Sambhaji Bridge", "Address": "Tilak Road, Pune"},
    {"Place Name": "Sangam Bridge", "Address": "Wellesley Road or Bombay Poona Road, near R.T.O, Pune"},
    {"Place Name": "All India Radio", "Address": "Pune University, Shivajinagar, Pune"},
    {"Place Name": "Anandashram Sanstha", "Address": "Ganpatrao Nalavade Chowk, Budhwar Peth, Pune"},
    {"Place Name": "Bank Of Maharashtra", "Address": "Bajirao Road, Pune"},
    {"Place Name": "Bhangya Maruti Mandir", "Address": "Bhausaheb Pandurang Chavan Chouk, Ganesh Peth, Pune"},
    {"Place Name": "Bhikardas Maruti Mandir", "Address": "Madiwale Colony, 1911 Sadashiv Peth, Pune"},
    {"Place Name": "Biniwale Wada", "Address": "595, Budhwar peth, Pune"},
    {"Place Name": "Dagdi Nagoba Mandir", "Address": "Bhausaheb Pandurang Chavan chowk, Ganesh peth, Pune"},
    {"Place Name": "Shri Datta Mandir", "Address": "Shree Dagadusheth Halawai Trust, Ganapati Bhavan, 1098, Budhwar Peth, Pune"},
    {"Place Name": "Deccan Police Station", "Address": "Prabhat road, Deccan Gymkhana, Pune"},
    {"Place Name": "Post Office", "Address": "Deccan Gymkhana Road, Pune"},
    {"Place Name": "Blue Nile Restaurant", "Address": "P Jog Marg, Pune"},
    {"Place Name": "Hotel Homeland", "Address": "18, Wilson Garden, Near Railway Station, Pune"},
    {"Place Name": "Hotel Milan agarwal", "Address": "19, Wilson Garden, Near Railway Station, Pune"},
    {"Place Name": "Hotel Ritz", "Address": "Sadhu Vaswani Marg, Pune"},
    {"Place Name": "Joshi Shree Ram Mandir", "Address": "750, Kasba Peth, Pune"},
    {"Place Name": "Shree Kadbe Ali Talim Mandal", "Address": "483, Shaniwar Peth, Pune"},
    {"Place Name": "Kakakuwa Mansion", "Address": "Budhwar Peth, Laxmi Road, Pune"},
    {"Place Name": "Kali Jogeshwari Mandir", "Address": "275, Budhwar Peth, Pune"},
    {"Place Name": "laxminarayan mandir", "Address": "Raviwar Peth, Pune"},
    {"Place Name": "L I C", "Address": "Branch no. 988, Laxmi Road, Sadashiv peth, Pune"},
    {"Place Name": "Limbraj Maharaj Vittahl Mandir (Zanjale Vittahl Mandir)", "Address": "Budhwar Peth, Pune"},
    {"Place Name": "Khunya Murlidhar Mandir", "Address": "1236, Sadashiv Peth, Pune"},
    {"Place Name": "N. M. Wadia Hospital", "Address": "283, Subhashnagar, behind BSNL office, Pune"},
    {"Place Name": "Nana Haud Rasvanthi Ghru", "Address": "592, Budhwar Peth, Shivaji Rasta, Pune"},
    {"Place Name": "Nana Saheb Peshwa Samadhi", "Address": "Below S.M. Joshi Bridge, Pune"},
    {"Place Name": "Nivdunga Vithoba Mandir", "Address": "Raghunathas Gulabdas Kirad Road (aruna chowk) 571/572, Nana Peth, Pune"},
    {"Place Name": "Tilak Maharashtra Vidyapeeth", "Address": "Tilak Maharashtra Vidyapeeth, Vidyapeeth Bhavan, Gultekadi, Pune"},
    {"Place Name": "Shivajinagar Railway Station", "Address": "Shivajinagar, Pune"},
    {"Place Name": "Brihan Maharashtra Collage", "Address": "845, Shivajinagar, Pune"},
    {"Place Name": "Deccan Collage Compplex", "Address": "Yerwada, Pune"},
    {"Place Name": "Jangli Maharaj Samadhi Temple", "Address": "Jangli Maharaj Road, Shivajinagar, Pune"}

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

 
