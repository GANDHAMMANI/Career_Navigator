import numpy as np
import pickle as pkl 
import streamlit as st

st.set_page_config(
   page_title="Checking Placement opportunity ",
   page_icon="🚀",
   layout="wide",
   initial_sidebar_state="expanded",
)

Gender_mapping = {
    'Female': 0,
    'Male': 1
}
Stream_mapping = {
    'Civil': 0,
    'Computer Science': 1,
    'Electrical': 2,
    'Electronics And Communication': 3,
    'Information Technology': 4,
    'Mechanical': 5
}

placements = {
    'Congratulations! You are shortlisted for the Placement opportunity': 1,
    'Unfortunately, your application for the placement opportunity was not successful': 0
}

import joblib

# Reading Pickle File
with open("placements_model.joblib", "rb") as f:
    model = joblib.load(f)


def predict(Age, Gender, Stream, Internships, CGPA, HistoryOfBacklogs):
    selected_Gender = Gender_mapping[Gender]
    selected_stream = Stream_mapping[Stream]
    # Standardize user input features
    input_data = np.array([[Age, selected_Gender, selected_stream, Internships, CGPA, HistoryOfBacklogs]])
    return model.predict(input_data)[0]

def display_emotion(result):
    video_width = 50
    video_height = 50

    if result == 1:
        st.write("<p style='font-size: 40px;'>🎉 Congratulations! You are shortlisted for the Placement opportunity!</p>", unsafe_allow_html=True)
        st.video("selected.mp4", format='video/mp4', start_time=0)
        st.balloons()
    else:
        st.write("<p style='font-size:40px;'>😞 Unfortunately, your application for the placement opportunity was not successful👎.</p>", unsafe_allow_html=True)

    

    # Apply CSS to adjust the size of the video container
    st.markdown(
        f"""
        <style>
            .stVideo > div > video {{
                width: {video_width}px !important;
                height: {video_height}px !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

def footer():
    # Footer Section
    st.markdown('<style>div.block-container{padding-bottom: 100px;,text-align: center;}</style>', unsafe_allow_html=True)
    st.markdown("""---""")
    st.markdown("""
       <p  🚀 Let's Connect!
        align="center">Developed by Mani Saketh. If you want any assistances or have any  queries. just, feel free to reach out!
        </p>
        <p align="center">
          <a href="www.linkedin.com/in/gandhammanisaketh2421" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/linkedin.png" alt="LinkedIn" style="width:40px;"/>
          </a>
          <a href="https://github.com/GANDHAMMANI" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/github.png" alt="GitHub" style="width:40px;"/>
          </a>
          <a href="mailto:gandhammani2421@yahoo.com">
            <img src="https://img.icons8.com/fluent/48/000000/mail.png" alt="Email" style="width:40px;"/>
          </a>
          <a href="https://www.instagram.com/mr.pandapal/">
            <img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" alt="Instagram" style="width: 40px;">
          </a>
          

        </p>

       <p align="center"> 
        G.Mani Saketh
        </p>
    """, unsafe_allow_html=True)

def main():
    
    st.markdown("<h1 style='text-align: center; font-size: 100px;'>CareerNavigator 🧭</h1>", unsafe_allow_html=True)
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("Welcome to CareerCatalyst: Guiding Your Career Path", expanded=True):
            st.image("placement_drive.png", caption="Placement opportunities ", width=200, use_column_width=True)
            st.markdown("""
            <div style="text-align: justify;">
                At CareerCatalyst, we're committed to helping individuals navigate their career
                journey with confidence and clarity. Leveraging cutting-edge machine learning algorithms,
                particularly the powerful AdaBoost algorithm, our platform provides personalized insights 
                and recommendations to empower you in making informed career decisions.
                Whether you're a recent graduate exploring job opportunities, a mid-career professional 
                seeking advancement, or someone considering a career change, CareerCatalyst equips you
                with the tools and resources needed to thrive in today's dynamic job market.
            </div>
            """, unsafe_allow_html=True)
        st.warning("Note: This A.I application is for educational purposes only.")   

    with col2:
        st.subheader(''' Hey Engineer check your status of placement opportunity ✅''')

        Age = st.number_input("Enter your age", max_value=100, min_value=19)
        Gender = st.selectbox("Select gender", list(Gender_mapping.keys()))
        Stream = st.selectbox("Select the Stream of your study", list(Stream_mapping.keys()))
        Internships = st.slider("No. of Internships Completed", max_value=5, min_value=0)
        CGPA = st.number_input("Enter your CGPA marks", max_value=10, min_value=0)
        HistoryOfBacklogs = st.number_input("Enter your no. of backlogs during your education. If completed also", max_value=40, min_value=0)

        result = predict(Age, Gender, Stream, Internships, CGPA, HistoryOfBacklogs)
        placement_result = list(placements.keys())[list(placements.values()).index(result)]
        submit_button = st.button("Check for Placements")


        if submit_button:
            display_emotion(result)



    footer()

if __name__ == '__main__':
    main()
