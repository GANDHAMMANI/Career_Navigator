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
    'After careful consideration, we regret to inform you that we will not be proceeding with your application.We wish you the very best in your future endeavors and hope you continue to strive for improvement': 0
}

# Reading Pickle File
with open("placements_model.pkl", "rb") as f:
    model = pkl.load(f)

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
        st.write("<p style='font-size:25px; text-align: justify;'>After careful consideration, we regret to inform you that we will not be proceeding with your application. We wish you the very best in your future endeavors and hope you continue to strive for improvement🤞.</p>", unsafe_allow_html=True)

    

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
    st.markdown("""   """)
    st.markdown("""
        <p  🚀 Let's Connect!
        align='center'>Developed by Gandham Mani Saketh</p>
        """, unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <img src="https://lh3.googleusercontent.com/pw/AP1GczOw-dWGOGG3dHdoVAk-DWMJg6HcVITQTysy8sjdNyIjnsLx-IADsaRe-HIl7ZyjIrQ9ElEjwk4JAu1FjCJyhf96mlBB9hH-rHj2huXQPYWcGI3MZASCvX5zJLUnZDybL8fBKwgJXLSykjKqVM8Xz8UYAe_ujD8EtWisNyfWLA3PNa1U_lYxYgaKJGWBZq1Zoha09vqNjuVbOcptk-OJKLnlagDFITSzfpw6jLCTvIDEn_wXxvvOGzMulJMQjFHvapDYM0XmoegC43rVcCjN874QHoEpd54PIyKCD8DQ8E43nUcnKyl7Guq1OLybaLWX5ot5orBnQi64AdYkBMYGyp6zVblcbqpdOx1LR7TFB3X6FLrcmpCr-u9Q1KQkPS41yZbGGp3bb4_aFOFnTjNz7EXuLPUikH5fdWfSvu3hENM2AfTjkHoQ63qbhtrs0rjoeg6OlrfiEhewXNX9vhalagO6CkcuYaTnSHG6yGdlkqVZNHPrIWKkNuS3Ios28Nisx5RxZJnYoaPewIG9PKbifvsmw05oFmS2HcFYykvDhFgMvnSxD7clsTbPHq7PAGWwTPDwXu_Q5y0slZWh97TUEU15pmUzF4-Z3lFKSlUg2cdafEFBCzYp-44o1bMR_DszodCNSBS4TR6_iXVTsjUtAeKOCWSKxVYoNwZ0RVS7lkYi6kZ9MKZI1IfD7UFkbQWYQc5z3ChrNgSoRtDxDcP1jp7R_V3OS-kXo9Alxw-6kwyus7GiIi45tHMEUMe8J656TKwMaJUv-SEXyGpibu0Nn2OL2-O-_st5Z1CHc9ylJ2DiNo-DwVtQLC9_H7JqzrLk0XMCEUGYIgfrJt49uTBpF2tT1ouwwk66pA6y65wTXkVQlwaH8Atv_vkKJM6jr0z6StdFFO9VwauiKUWJw1aOeT2e=w489-h869-s-no-gm?authuser=0.jpg" style="border-radius: 50%; width: 150px; height: 150px; object-fit: cover;">
        <p style="text-align: center; margin-top: 10px;">Saketh07</p>
    </div>"""
    , unsafe_allow_html=True)

    st.markdown(""" <p align="center">If you want any assistances or have any  queries. just, feel free to reach out!</p>
        <p align="center">
          <a href="https://www.linkedin.com/in/gandhammanisaketh2421/" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/linkedin.png" alt="LinkedIn" style="width:40px;"/>
          </a>
          <a href="https://github.com/GANDHAMMANI" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/github.png" alt="GitHub" style="width:40px;"/>
          </a>
          <a href="mailto:gandhammani2421@gmail.com" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/gmail.png" alt="GitHub" style="width:40px;"/>
          </a>
          <a href="https://www.instagram.com/mr.pandapal/">
            <img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" alt="Instagram" style="width: 40px;">
          </a>
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
        submit_button = st.button("CareerQuest")


        if submit_button:
            display_emotion(result)

    # Media screen CSS for responsiveness
    st.markdown(
        """
        <style>
            @media screen and (max-width: 600px) {
                .block-container {
                    padding-bottom: 50px;
                }
                h1 {
                    font-size: 50px !important;
                }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    footer()

if __name__ == '__main__':
    main()
