from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
default_profile_pic_path = current_dir / "assets" / "profile-pic.png"
current_profile_pic_path = current_dir / "assets" / "current_profile.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Diana Rose C. Mesa // Biography"
PAGE_ICON = ":wave:"
NAME = "Mesa, Diana Rose C."
DESCRIPTION = """
Bachelor of Science in Computer Engineering - BSCpE 1A
"""
EMAIL = "dmesa1@ssct.edu.ph"
SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/diannarose.mesa",
    "Instagram": "https://www.instagram.com/myxnza/",
}
BIRTHDAY = "April 29,2006"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- SESSION STATE FOR PROFILE PICTURE ---
if "profile_pic_path" not in st.session_state:
    # Initialize session state with the current profile picture
    if current_profile_pic_path.exists():
        st.session_state.profile_pic_path = current_profile_pic_path
    else:
        st.session_state.profile_pic_path = default_profile_pic_path

# --- PROFILE ---
col1, col2 = st.columns(2, gap="small")
with col1:
    # Load and display the current profile picture
    profile_pic = Image.open(st.session_state.profile_pic_path)
    st.image(profile_pic, width=250, caption="Profile Picture")
    
# Upload a new profile picture
uploaded_file = st.file_uploader("Change Profile Pic", type=["png", "jpg", "jpeg"])
    
if uploaded_file is not None:
    # Save the uploaded file as the new profile picture
    with open(current_profile_pic_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
    # Update session state to point to the new profile picture
    st.session_state.profile_pic_path = current_profile_pic_path
        

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("Birthday: ", BIRTHDAY)
    st.write("📫", EMAIL)
    

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
st.write ("---")


# --- BACKGROUND ---
st.markdown ("""I'm Diana Rose C. Mesa, a computer engineering student from Surigao del Norte State University. For me, engineering is more than just a degree; it's a gateway to realizing technology's promise and developing meaningful solutions that can change the future. With each step forward on my path, I am motivated by curiosity and a desire to understand more about how systems work and how I can improve them. 

Beyond my education, I like the basic yet meaningful parts of life. Watching movies helps me to explore a variety of stories and ideas, whereas keeping my room clean provides me with a sense of quiet and order—a balance that I value greatly as I negotiate the pressures of college life. Moments of reflection fuel my motivator and a reminder of the value of discipline and attention.

I regard myself as a motivated and passionate learner who wants to progress not only technically but also personally. My goals extend beyond academic accomplishment; I want to make a lasting influence in my area and welcome the challenges that come with it. With each new experience, I am laying the groundwork for a future full of invention, resilience, and purpose.""",
unsafe_allow_html=True,
)

# --- EDUCATIONAL ATTAINMENT ---
st.write('\n')
st.write ("---")
tab1, tab2 = st.tabs(["📚 Educational Attainments", "🎯 Accomplishments"])
tab1.markdown(
    """
    ELEMENTARY:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Mat-i Central Elementary School</li>
            <li>BRGY. MAT- I SURIGAO CITY</li>
            <li>2017-2018</li>
        </ul>
    </ul>
    
    SECONDARY:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Kapayapaan Integrated School  ,  Assemblywoman Felicita G. Bernardino Memorial Trade School</li>
            <li>Kapayapaan Ville, Canlubang, Calamba City, Calamba, LIAS MARILAO BULACAN</li>
            <li>2023-2024</li>
        </ul>
    </ul>
    
    TERTIARY:
    <ul style="margin-left: 20px; font-size: 16px;">
        <ul style="margin-left: 20px;">
            <li>Surigao Del Norte State University</li>
            <li>Narciso Street, Surigao City, 8400 Surigao del Norte</li>
        </ul>
    </ul>
    
    """,
    unsafe_allow_html=True,
)

# Initialize session state for accomplishments if not present
if 'accomplishments' not in st.session_state:
    st.session_state.accomplishments = {
        'elementary': [
            "With honor ,    Academic Achiever award"
            
        ],
        'secondary': [
            "🏅Grade 11: With Honors",
            "🏅Grade 12: With High Honors (Salutatorian)"
        ],
        'extracurricular activities': [
            "Certificate of Recognition (Math game, Agricultural training institute, Immersion, Ms. Intramurals, Research Congress, Poster Presenter) , Leadership award ,  Academic Excellence award, Outstanding performance in TVL(Agri-crop production) award , Research Award(Agri-Crop Production)"
            
        ]
    }

# Function to display accomplishments
def display_accomplishments(data):
    for key, values in data.items():
        st.markdown(f"**{key.upper()}**:")
        st.markdown("<ul style='margin-left: 20px;'>", unsafe_allow_html=True)
        for value in values:
            st.markdown(f"<li>{value}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)

# --- Tab 2: Accomplishments ---
with tab2:
    st.write("### Current Accomplishments:")
    display_accomplishments(st.session_state.accomplishments)

    # --- Add/Update Accomplishment ---
    st.write("### Add/Update Accomplishment")
    level = st.selectbox("Choose accomplishment level:", ["Elementary", "Secondary", "Extracurricular Activities"])
    accomplishment = st.text_input(f"Enter accomplishment for {level}:")

    # Button to add or update
    if st.button(f"Add/Update {level}"):
        level_key = level.lower()
        if accomplishment:
            st.session_state.accomplishments[level_key].append(accomplishment)
            st.success(f"Accomplishment added/updated for {level}!")
        else:
            st.warning("Please enter an accomplishment.")

    # --- Remove Accomplishment ---
    st.write("### Remove Accomplishment")
    remove_level = st.selectbox("Select level to remove an accomplishment from:", ["Elementary", "Secondary", "Extracurricular Activities"])
    accomplishments_to_remove = st.session_state.accomplishments[remove_level.lower()]
    accomplishment_to_remove = st.selectbox("Select accomplishment to remove:", accomplishments_to_remove)

    # Button to remove an accomplishment
    if st.button(f"Remove Accomplishment from {remove_level}"):
        if accomplishment_to_remove in accomplishments_to_remove:
            st.session_state.accomplishments[remove_level.lower()].remove(accomplishment_to_remove)
            st.success(f"Accomplishment removed from {remove_level}!")
        else:
            st.warning("Accomplishment not found.")