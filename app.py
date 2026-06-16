import streamlit as st
import pandas as pd
import base64

# Page configuration
st.set_page_config(page_title="Digital Comm Career Hub", page_icon="🚀", layout="wide")

st.markdown ("""
             
<style>

/* =======================================================
    BACKGROUND AND LAYOUT
   ======================================================= */
             
 /* Applies a 125-degree linear gradient transitioning from deep midnight blue to dark indigo */            
.stApp {
    background: linear-gradient(125deg, #0b0f19 0%, #1e1b4b 50%, #020617 100%) !important;
             
/* Fixes the background in place to prevent it from scrolling with the page content */
    background-attachment: fixed !important;
}

/* Removes default Streamlit padding and force the layout to span across 100% of the viewport width */
[data-testid="stAppViewBlockContainer"] {
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}

/* =======================================================
   READABILITY ENHANCEMENT: TEXT COLORS AND PLACEHOLDERS
   ======================================================= */
/* Targets all headers, paragraphs, labels, markdown blocks, and expander titles */
             
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, 
.stApp p, .stApp label, .stApp .stMarkdown, .stApp [data-testid="stExpander"] span,
[data-testid="stWidgetLabel"] p, [data-testid="stWidgetLabel"] span {
    color: #ffffff !important;
             
/* Makes white text sharper and easier to read on dark backgrounds, especially on Safari/iPhone */
    -webkit-font-smoothing: antialiased;
}

/* Adjust the placeholder text ("Choosen options" e "All") */
.stApp div[data-placeholder="true"], .stApp span[data-readonly="true"] {
    color: rgba(255, 255, 255, 0.7) !important;
}

/* =======================================================
   CUSTOMIZATION OF INTERACTIVE ELEMENTS (BUTTONS, LINK_BUTTON)
   ======================================================= */
/* Main button styles */
div.stButton > button, div[data-testid="stFormSubmitButton"] > button,
[data-testid="stLinkButton"] a, [data-testid="stLinkButton"] span, div.stButton a {
    background-color: #1e1b4b !important; 
    color: #ffffff !important;             
    border: 1px solid #312e81 !important;  
    text-decoration: none !important;      
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background-color 0.2s ease, border-color 0.2s ease;
}

div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover,
[data-testid="stLinkButton"] a:hover, div.stButton > button:active {
    background-color: #0b0f19 !important; 
    border-color: #312e81 !important;  
}

/* =======================================================
   (SELECTBOX, MULTISELECT, TEXTINPUT)
   ======================================================= */
             
/* Dark backgound */
.stSelectbox div[data-baseweb="select"], .stMultiSelect div[data-baseweb="select"],
div[data-testid="stTextInput"] [data-baseweb="base-input"], div[data-testid="stTextInput"] > div > div,
.stSelectbox [role="button"], .stMultiSelect [role="button"], div[data-testid="stSelectbox"] > div {
    background-color: #262730 !important;
    background: #262730 !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
}

/* Avoid that Streamlit generates white layers */
.stSelectbox div, .stMultiSelect div {
    background-color: transparent !important;
}

/* Force text color */
.stSelectbox div[data-baseweb="select"] *, .stMultiSelect div[data-baseweb="select"] *,
div[data-testid="stTextInput"] input, div[data-testid="stSelectbox"] span {
    color: #ffffff !important;
}

/* =======================================================
   DROPDOWN OPTIONS AND POPOVERS
   ======================================================= */
/* Management of dropdown options */
div[data-baseweb="popover"] ul, div[data-baseweb="popover"] li, 
div[data-baseweb="menu"] div, [data-testid="stSelectbox"] ul li {
    background-color: #262730 !important;
    color: #ffffff !important;
}

div[data-baseweb="popover"] li:hover, [data-testid="stSelectbox"] ul li:hover {
    background-color: #1e1b4b !important;
}

/* Force text color to white for all child elements within expanded popover menu items */
div[data-baseweb="popover"] li * {
    color: #ffffff !important;
}

/* Style the selected option tags/badges inside the skills and interests multiselect widget */
div[data-testid="stMultiSelect"] [data-baseweb="tag"] {
    background-color: #1e1b4b !important;
    color: #ffffff !important;
    border: 1px solid #312e81 !important;
}

/* =======================================================
   STRUCTURE OF THE NEWSLETTER FORM CONTAINER
   ======================================================= */
div[data-testid="stForm"] {
    background-color: rgba(30, 41, 59, 0.2) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    padding: 20px !important;
    border-radius: 12px !important;
}

</style>
             
""", unsafe_allow_html=True)

# --- DATA LOADING (FROM MANUAL CSV ONLY) ---
@st.cache_data
def load_opportunities():
    try:
        df = pd.read_csv("jobs.csv")
        df = df.dropna(how="all")
    except Exception:
        df = pd.DataFrame(columns=["Title", "Company", "Location", "Role", "Type", "Link", "Skills"])
    df = df.fillna("N/A")
    return df

df_postings = load_opportunities()


# --- MANAGEMENT OF NAVIGATION IN THE TOP (SESSION STATE) ---
# If the user enters for the first time, we set the default page to "Home"
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Function to change the page on button click
def change_page(page_name):
    st.session_state["current_page"] = page_name

# --- HORIZONTAL NAVBAR AT THE TOP ---
# Create 3 columns to place the navigation buttons
nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 1])


with nav_col1:
    if st.button("Home", use_container_width=True, type="primary" if st.session_state["current_page"] == "Home" else "secondary"):
        change_page("Home")
        st.rerun()

with nav_col2:
    if st.button("💼 Jobs", use_container_width=True, type="primary" if st.session_state["current_page"] == "Jobs" else "secondary"):
        change_page("Jobs")
        st.rerun()

with nav_col3:
    if st.button("📚 More Information", use_container_width=True, type="primary" if st.session_state["current_page"] == "More Information" else "secondary"):
        change_page("More Information")
        st.rerun()

# ==========================================
# PAGE 1: HOME
# ==========================================
if st.session_state["current_page"] == "Home":
    with open("plane.png", "rb") as f:
        img_data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
<style>

/* Center and clean the layout borders */
[data-testid="stAppViewBlockContainer"] {{
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}}
                
.hero-section {{
    position: relative;
    display: block;           
    width: 100%;
    min-width: 100%;
    height: 300px;
    overflow: hidden;
    border-radius: 0px;
    background: linear-gradient(to bottom, #87CEEB 0%, #b0e0ff 60%, #e0f4ff 100%);
    margin-bottom: 2rem;
    padding-left: 120px;
    box-sizing: border-box;
}}

.plane {{
    position: absolute;
    top: 30%;
    width: 660px;
    height: auto;
    z-index: 1;
    animation: fly-across 2s ease-out forwards;
}}

@keyframes fly-across {{
    0%   {{ left: -660px; }}
    100% {{ left: 40%; }}
}}

.hero-title {{
    position: absolute;
    top: 30%;
    transform: translateY(-50%); /* Center vertically */
    left: 60px; /* Fixed distance from the left edge of the banner */
    z-index: 2;
    margin: 0;
    /* Align the text at the beginning of the content below using percentages of the window */
    margin-left: 10vw;
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
    text-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25);
    max-width: 50%;
    text-transform: uppercase;
    opacity: 0;
    animation: fade-in-text 1.5s ease-out forwards;
    animation-delay: 2s;
}}

@keyframes fade-in-text {{
    0%   {{ opacity: 0; transform: translateY(10px); }}
    100% {{ opacity: 1; transform: translateY(0); }}
}}

/* =======================================================
   STYLE ADJUSTMENTS FOR MOBILE DEVICES (RESPONSIVE DESIGN)
   ======================================================= */
@media (max-width: 768px) {{
    .hero-section {{
        height: 220px !important;
        padding-left: 0 !important;
    }}
    .plane {{
        width: 250px !important;
        top: 45% !important;
        animation: fly-across-mobile 2s ease-out forwards !important;
    }}
    .hero-title {{
        font-size: 22px !important;
        top: 10% !important;
        left: 40% !important;
        transform: translateX(-50%) !important;
        margin-left: 0 !important;
        max-width: 90% !important;
        text-align: center !important;
        opacity: 1 !important;
        animation: fade-in-text 1.5s ease-out 2s forwards !important;
    }}
}}
@keyframes fly-across-mobile {{
    0%   {{ left: -250px; }}
    100% {{ left: 15%; }}
}}
                
                
</style>

<div class="hero-section">
<h1 class="hero-title">Welcome to the Digital Comm Career Hub</h1>
<img class="plane" src="data:image/png;base64,{img_data}" />
</div>
""", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="about-content">
        <h2>About This Platform</h2>
        <p>Welcome to your first step for an international career in Digital Communication. 
        This platform was built to bridge the gap between academic studies and global professional growth. We know that sometimes navigating the job market,
                building the right cv and finding useful information can be overwhelming. 
                For this reason, this website tries to make it easier for you by providing jobs and most important information all in one place.</p>
        <ul>
            <li><strong>Skill-Based Job Matching:</strong> Input your core competencies to instantly uncover the roles most aligned with your profile.</li>
            <li><strong>Curated Global Opportunities:</strong> Discover verified job listings and international internships tailored to the modern communication market.</li>
            <li><strong>Mobility & Career Guides:</strong> Access straightforward resources on EU grants, Erasmus+ Traineeship, and digital-first resume optimization.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # A little space before the interactive section
    st.markdown("<br>", unsafe_allow_html=True)
    
    # === SIMULATION SECTION ===
    with st.container():
        st.markdown("### Where can your skills take you?")
        st.write("Select one or more of your core skills below to see how our matching system works in real-time:")
        
        # Streanlit multi-select component with a custom label and options relevant to the digital communication field
        test_skills = st.multiselect(
            label="Choose your skills:",
            options=["Python", "SQL", "Social Media Management", "Content Creation", "SEO & Copywriting", "Data Visualization"],
            key="about_skills_simulator",
            label_visibility="collapsed" # Hide the standard Streamlit label to use our custom st.write above
        )
        
        # When the user selects skills, we show a custom-styled feedback message that simulates the matching process and encourages them to explore the Jobs page
        if test_skills:
            # Create the string with the skills in bold
            skills_str = ", ".join([f"**{skill}**" for skill in test_skills])
            
            st.markdown(f"""
            <div style="
                background: rgba(255, 255, 255, 0.07);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                border: 1px solid rgba(255, 255, 255, 0.15);
                padding: 1.5rem;
                border-radius: 12px;
                margin-top: 1rem;
                margin-bottom: 1.5rem;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
            ">
                <p style="color: #ffffff; font-size: 16px; margin-bottom: 0.8rem; line-height: 1.5;">
                    <strong>Boom! Excellent combination!</strong> We detected that roles requiring {skills_str} are highly requested right now in international hubs like Madrid, London, and Milan.
                </p>
                <p style="color: #cbd5e1; font-size: 15px; margin-bottom: 0; line-height: 1.5;">
                    Ready to see the real open positions? Head over to the <strong>Jobs</strong> tab at the top of the page, insert your skills in the main filter, and start applying!
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            # Button to take the user to the Jobs page
            if st.button("Take me to the Jobs Page!", use_container_width=True):
                st.session_state["current_page"] = "Jobs"
                st.rerun()

# ==========================================
# PAGE 2: JOBS
# ==========================================

elif st.session_state["current_page"] == "Jobs":
    # Convert the local image abroad.png in Base64 text
    try:
        with open("abroad.png", "rb") as image_file:
            bin_str = base64.b64encode(image_file.read()).decode()
        background_html = f"url('data:image/png;base64,{bin_str}')"
    except Exception:
        background_html = "#003399"

# CSS: Management of the main container

    st.markdown(
        f"""
        <div style="
            background-image: linear-gradient(rgba(2, 6, 23, 0.55), rgba(2, 6, 23, 0.85)), {background_html};
            background-size: cover;
            background-position: center;
            padding: 100px 40px;
            margin-top: 30px;
            margin-bottom: 40px;
            width: 100%;
            box-sizing: border-box;
            border-bottom: 2px solid rgba(255, 255, 255, 0.1);
        ">
            <h1 style='margin: 0; color: #ffffff; font-size: 48px; font-weight: 700; font-family: "Helvetica Neue", sans-serif;'>🇪🇺 International Job Board</h1>
        </div>
        """,    
        unsafe_allow_html=True
    )

# --- VIRTUAL ASSISTANT INTERFACE (QUIZ) ---
# ==========================================
# LAYOUT STRUCTURE: MAIN CONTENT vs RIGHT WIDGET
# ==========================================

    # Splitting the page layout: 70% for main content/filters, 30% for the top-right assistant widget
    col_main_content, col_right_widget = st.columns([7, 3])

    # --- RIGHT SIDE: VIRTUAL ASSISTANT WIDGET ---
    with col_right_widget:
        # Initialize the session state variable for widget toggle visibility if not present
        if "show_quiz" not in st.session_state:
            st.session_state["show_quiz"] = False

        # HTML injection for the widget card header styling 
        st.markdown(
            """
            <div style="background-color: rgba(0, 229, 255, 0.05); padding: 15px; border-radius: 10px; border: 1px solid rgba(0, 229, 255, 0.1); margin-bottom: 10px;">
                <p style='margin:0; font-size:14px; color:#cbd5e1; font-weight:600;'>Not sure yet about the best role for you? </p>
                <p style='margin:5px 0 0 0; font-size:12px; color:#94a3b8;'>Let the assistant find jobs that match your skills.</p>
            </div>
            """, unsafe_allow_html=True
        )
        
        # Action button positioned inside the right column
        if st.button("🤖 Your AI Assistant", use_container_width=True):
            st.session_state["show_quiz"] = not st.session_state["show_quiz"]

        # Render quiz fields if the user toggled the assistant section open
        if st.session_state["show_quiz"]:
            with st.container():
                st.markdown("<p style='color:#00e5ff; font-weight:600; margin-top:10px; margin-bottom:5px;'> Select your Skills, please :</p>", unsafe_allow_html=True)
                
                # --- SKILLS EXTRACTION FROM CSV ---
                # 1. Drop any empty rows in the Skills column and convert to string
                raw_skills = df_postings["Skills"].dropna().astype(str)
                
                # 2. Split each row by comma, explode into individual rows, and strip spaces
                all_skills_series = raw_skills.str.split(",").explode().str.strip()
                
                # 3. Get unique values, sort them alphabetically, and convert to a clean list
                available_skills = sorted(list(all_skills_series.unique()))
                
                # Multi-select UI component optimized for the narrow column layout
                user_skills = st.multiselect(
                    "Which tools do you have experience with?",
                    options=available_skills,
                    key="widget_skills_selection"
                )
                
                if st.button("Discover your matches", use_container_width=True):
                    if not user_skills:
                        st.warning("Please select at least one skill.")
                    else:
                        # Store user choices globally in session state and trigger page refresh to apply filter
                        st.session_state["quiz_skills_applied"] = user_skills
                        st.session_state["show_quiz"] = False
                        st.rerun()

    with col_main_content:
        st.markdown("## 💼 Available Opportunities")
        # Place your existing classic dropdown filters (col1, col2, col3) right here
        # so they render on the wider left section of the screen.
    # Initialize the filtered dataframe copy
    df_filtered = df_postings.copy()

    # Standard dropdown filtering logic for Roles and Locations

                
    # --- FILTERS AND JOB POSTS ---
    if df_postings.empty or len(df_postings) == 0:
        st.info("The job board is currently empty. Add listings to 'jobs.csv'.")
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            available_categories = ["All"] + list(df_postings["Title"].unique())
            selected_category = st.selectbox("Filter by Field:", available_categories, key="selectbox_field_filter")
        with col2:
            available_locations = ["All"] + list(df_postings["Location"].unique())
            selected_location = st.selectbox("Filter by Location:", available_locations, key="selectbox_location_filter")
        with col3:
            available_types = ["All"] + list(df_postings["Type"].unique())
            selected_type = st.selectbox("Filter by Contract Type:", available_types, key="selectbox_type_filter")
            
        df_filtered = df_postings.copy()
        if selected_category != "All":
            df_filtered = df_filtered[df_filtered["Title"] == selected_category]
        if selected_location != "All":
            df_filtered = df_filtered[df_filtered["Location"] == selected_location]
        if selected_type != "All":
            df_filtered = df_filtered[df_filtered["Type"] == selected_type]

    # 🌟 SKILLS QUIZ FILTER APPLICATION
    # Check if the user has applied any skills filter via the top-right widget
    if "quiz_skills_applied" in st.session_state and st.session_state["quiz_skills_applied"]:
        chosen_skills = st.session_state["quiz_skills_applied"]
        
        # Use regex join '|' (OR logic) to check if the Skills column text contains any of the selected keywords
        # case=False guarantees case-insensitivity, na=False skips missing or empty rows safely
        skill_mask = df_filtered["Skills"].str.contains("|".join(chosen_skills), case=False, na=False)
        df_filtered = df_filtered[skill_mask]
        
        # Visual feedback token for active skills filtering
        st.info(f"🎯 Opportunities found for your skills: {', '.join(chosen_skills)}")
        
        # Reset button to clear the session state variable and restore the full board view
        if st.button("Show all jobs 🔄", use_container_width=True):
            del st.session_state["quiz_skills_applied"]
            st.rerun()
            
    st.write(f"🔍 Found **{len(df_filtered)}** active opportunities:")
        
    for index, row in df_filtered.iterrows():
        with st.container():
            st.markdown(
                f"""
                <div style="background-color: #1e293b; padding:25px; border-radius:12px; border-left: 6px solid #00e5ff; margin-bottom:5px; border-top: 1px solid rgba(255, 255, 255, 0.08);">
                    <h4 style='margin-top:0; color:#ffffff; font-size:20px; margin-bottom:8px;'>{row['Role']}</h4>
                    <p style='margin:0; font-size:15px; color:#cbd5e1;'><b>Company:</b> {row['Company']} | <b>Location:</b> {row['Location']}</p>
                    <p style='margin:12px 0 0 0;'>
                        <span style='background-color: rgba(255, 255, 255, 0.1); padding:5px 10px; border-radius:6px; font-size:12px; color:#ffffff; font-weight:600;'>{row['Title']}</span> 
                        <span style='background-color: rgba(0, 229, 255, 0.15); padding:5px 10px; border-radius:6px; font-size:12px; color:#00e5ff; font-weight:600;'>{row['Type']}</span>
                    </p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            st.link_button("View Opportunity ↗️", row['Link'], key=f"btn_{index}")
            st.markdown("<br><br>", unsafe_allow_html=True)

# ==========================================
# PAGE 3: MORE INFORMATION
# ==========================================

elif st.session_state["current_page"] == "More Information":
    st.title("📚 Useful Guides & Mobility Info")
    st.subheader("Essential steps before applying for international roles")
    st.markdown("---")
    
    with st.expander("📝 How to build a Digital Comm CV"):
        st.markdown("""
        1. **Showcase Your Tech Stack:**
                    
        Don't be vague. Group your technical skills clearly:
       * *Data Analysis:* Python (Pandas/NumPy), SQL, Google Analytics.
       * *Web & Design:* Markdown, Figma.
    
        2. **Treat Academic Projects as Work Experience:**
                    
       If you have done a project for a university exam, put it under a **"Key Projects"** section. Describe the tools you used and the goals you achieved.
       
        3. **Go International:**
                    
       Tailor your resume for European recruiters. Use the CEFR scale (A1-C2) for languages and emphasize any background in intercultural environments.
       
        4. **Keep it Single-Page & ATS-Friendly:**
                    
       Avoid heavy graphics that block automated resume scanners, but maintain a clean, modern, digital-first layout.
            
        """)

    with st.expander("🛠️ Recommended CV Editors & Platforms"):
        st.markdown("""
        To build a standout, modern application, avoid outdated templates (like the standard Europass) and choose your platform based on your expertise and target role:
        
        * **Standard CV Builders (Ready-to-Use):**
          * **Novoresume / Kickresume:** Excellent online platforms with structured, fill-in-the-blank templates. They offer clean, professional single-page layouts that look sharp and are fully optimized for corporate screening software.
          * **Reactive Resume:** A fantastic, 100% free open-source CV builder. It gives you full control over privacy and formatting without premium paywalls.
                    
                    
                    
        * **Design & Tech Tools (Advanced / From Scratch):**
          * **Canva:** The most popular online graphic tool. Great for quick, visually engaging layouts if you are applying for creative or Social Media positions.
          * **Figma:** The global standard for digital design. Many digital professionals build their CV here from scratch to showcase their layouts and design skills directly to marketing agencies.
          * **Overleaf (LaTeX):** A code-based document editor. It is highly recommended if you are leaning towards data-driven roles (e.g., Data Analyst), as it creates flawless, ultra-professional geometric grids highly respected in tech environments.
        """)
        
    with st.expander("🇪🇺 Guide to Erasmus+ Traineeship"):
        st.markdown("""
        ### 🌍 International Mobility with Financial Support
        The **Erasmus+ Traineeship** program is a powerful EU initiative that grants you monthly funding (usually ranging from €400 to €700+ depending on the destination country) to complete an internship anywhere in Europe.
        
        ---
        
        ### Why it is a game-changer for Digital Comm Students:
        * **Double the Opportunities:** Many international agencies and startups in tech hubs (like Madrid, Berlin, or Dublin) specifically look for "Erasmus Trainees" because the EU covers a part of your financial costs, making you a highly attractive candidate.
        * **Post-Graduation Flexibility:** You can complete the traineeship even *after* your Master's degree, provided you officially apply to your university's bando **before** graduating.
        * **Technical Growth:** It is the perfect setup to test technical skills (such as Data Analysis, Python/SQL applications, or global marketing strategies) in a multicultural, real-world corporate environment.

        ---

        ### Step-by-Step Action Plan:
        1. **Check Your University Bando:** Keep a close eye on your university's international mobility portal. Bandi usually open once or twice a year.
        2. **Find a Host Company:** Don't wait for university listings. Reach out directly to European companies, marketing agencies, or research hubs. When applying, explicitly mention in your cover letter that you are an *Erasmus+ Traineeship candidate*—it gives you an immediate competitive edge!
        3. **The Learning Agreement:** Once selected by an international company, your university and the host company will sign a *Learning Agreement* outlining your tasks, ECTS credits (if applicable), and duration (from 2 to 12 months).
        """)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("Receive Updates & Stay Tuned")
    st.write("Enter your details to stay updated via email about new curated international opportunities.")

    with st.form(key="newsletter_form_info", clear_on_submit=True):
        col_name, col_email = st.columns(2)
        with col_name:
            user_name = st.text_input("Your Name:")
        with col_email:
            user_email = st.text_input("Your Email *:")
            
        interest = st.multiselect(
            "Which fields are you most interested in?",
            ["Social Media", "Data Analysis", "Corporate Communication", "Content Creation"]
        )
        submit_button = st.form_submit_button(label="Subscribe to Newsletter", use_container_width=True)

    # === Newsletter Subscription Logic ===
    if submit_button:
        # .strip() rimuove spazi vuoti invisibili che ingannano il controllo
        if not user_email.strip() or "@" not in user_email:
            st.error("Please enter a valid email address!")
        else:
            try:
                with open("subscribers.csv", "a", encoding="utf-8") as f:
                    # Data cleaning: if the name is empty or just spaces, we save it as "Anonymous". We also strip spaces from the email and interests.
                    clean_name = user_name.strip() if user_name.strip() else "Anonymous"
                    clean_email = user_email.strip()
                    selected_interests = ";".join(interest) if interest else "None"
                    
                    f.write(f"{clean_name},{clean_email},{selected_interests}\n")
                
                # Save the subscription status in session state to show a personalized success message after form submission
                st.session_state["newsletter_subscribed"] = True
                st.session_state["subscriber_name"] = clean_name
            except Exception:
                st.error("Error saving data.")

    # It show a personalized success message if the user just subscribed
    if "newsletter_subscribed" in st.session_state and st.session_state["newsletter_subscribed"]:
        st.success(f"Thank you {st.session_state['subscriber_name']}! You have successfully subscribed.")
        
        # Reset the subscription status after showing the message to avoid showing it again on page refresh or navigation
        st.session_state["newsletter_subscribed"] = False