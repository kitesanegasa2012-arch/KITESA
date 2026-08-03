import streamlit as st
import random
import json
import hashlib
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Hiika Way (HW)", 
    page_icon="📚", 
    layout="centered"
)

# Initialize Session State
if "students" not in st.session_state:
    st.session_state.students = []
if "current_student" not in st.session_state:
    st.session_state.current_student = None
if "page" not in st.session_state:
    st.session_state.page = "cover"
if "w_score" not in st.session_state:
    st.session_state.w_score = 0
if "m_score" not in st.session_state:
    st.session_state.m_score = 0
if "r_index" not in st.session_state:
    st.session_state.r_index = 0
if "w_index" not in st.session_state:
    st.session_state.w_index = 0
if "m_index" not in st.session_state:
    st.session_state.m_index = 0
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_role" not in st.session_state:
    st.session_state.user_role = None
if "student_data" not in st.session_state:
    st.session_state.student_data = {}
if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = []
if "current_quiz_index" not in st.session_state:
    st.session_state.current_quiz_index = 0
if "quiz_attempts" not in st.session_state:
    st.session_state.quiz_attempts = {}
if "student_scores" not in st.session_state:
    st.session_state.student_scores = {}
if "teacher_questions" not in st.session_state:
    st.session_state.teacher_questions = []

# Custom CSS for beautiful UI
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Cover Page Styling */
    .cover-page {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 40px 30px;
        border-radius: 30px;
        text-align: center;
        color: white;
        margin: 20px 0;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.5);
        border: 3px solid rgba(255,255,255,0.2);
        position: relative;
        overflow: hidden;
    }
    
    .cover-page::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .cover-page h1 {
        color: white !important;
        -webkit-text-fill-color: white !important;
        font-size: 52px;
        font-weight: 900;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        position: relative;
        z-index: 1;
    }
    
    .cover-page h3 {
        color: rgba(255,255,255,0.95) !important;
        -webkit-text-fill-color: rgba(255,255,255,0.95) !important;
        font-size: 22px;
        font-weight: 600;
        position: relative;
        z-index: 1;
    }
    
    .cover-page p {
        color: rgba(255,255,255,0.9);
        font-size: 18px;
        line-height: 1.8;
        position: relative;
        z-index: 1;
    }
    
    .cover-icon {
        font-size: 80px;
        margin: 10px 0;
        display: inline-block;
        animation: bounce 2s infinite;
        position: relative;
        z-index: 1;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }
    
    /* Subject Cards */
    .subject-card {
        background: white;
        padding: 25px 20px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 15px 0;
        border: 3px solid transparent;
        transition: all 0.4s ease;
        cursor: pointer;
        text-align: center;
    }
    
    .subject-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.3);
        border-color: #667eea;
    }
    
    .subject-card .icon {
        font-size: 48px;
        display: block;
        margin-bottom: 10px;
    }
    
    .subject-card .title {
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }
    
    .subject-card .subtitle {
        font-size: 14px;
        color: #666;
        margin-top: 5px;
    }
    
    /* Oromo Subject - Green Theme */
    .oromo-card {
        border-color: #28a745;
        background: linear-gradient(135deg, #f8fff9 0%, #e8f5e9 100%);
    }
    
    .oromo-card:hover {
        border-color: #28a745;
        box-shadow: 0 15px 40px rgba(40, 167, 69, 0.3);
    }
    
    /* English Subject - Blue Theme */
    .english-card {
        border-color: #007bff;
        background: linear-gradient(135deg, #f0f7ff 0%, #e3f2fd 100%);
    }
    
    .english-card:hover {
        border-color: #007bff;
        box-shadow: 0 15px 40px rgba(0, 123, 255, 0.3);
    }
    
    /* Math Subject - Red Theme */
    .math-card {
        border-color: #dc3545;
        background: linear-gradient(135deg, #fff5f5 0%, #fbe9e7 100%);
    }
    
    .math-card:hover {
        border-color: #dc3545;
        box-shadow: 0 15px 40px rgba(220, 53, 69, 0.3);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(to right, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 14px 28px;
        font-weight: bold;
        font-size: 18px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
        margin: 5px 0;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(0px);
    }
    
    /* Welcome button special style */
    .welcome-btn > button {
        background: linear-gradient(135deg, #f7971e 0%, #ffd200 100%);
        box-shadow: 0 4px 20px rgba(247, 151, 30, 0.5);
        color: #333;
        font-size: 22px;
        padding: 18px 30px;
    }
    
    .welcome-btn > button:hover {
        box-shadow: 0 8px 30px rgba(247, 151, 30, 0.7);
        transform: translateY(-3px) scale(1.02);
    }
    
    /* Key/Furtuu button */
    .key-btn > button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        box-shadow: 0 4px 20px rgba(245, 87, 108, 0.4);
    }
    
    .key-btn > button:hover {
        box-shadow: 0 8px 30px rgba(245, 87, 108, 0.6);
    }
    
    /* Login button */
    .login-btn > button {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        box-shadow: 0 4px 20px rgba(76, 175, 80, 0.4);
    }
    
    .login-btn > button:hover {
        box-shadow: 0 8px 30px rgba(76, 175, 80, 0.6);
    }
    
    /* Success/Error messages */
    .stAlert {
        border-radius: 15px;
        border-left: 5px solid;
    }
    
    .stSuccess {
        border-left-color: #28a745;
        background: #d4edda;
    }
    
    .stError {
        border-left-color: #dc3545;
        background: #f8d7da;
    }
    
    .stWarning {
        border-left-color: #ffc107;
        background: #fff3cd;
    }
    
    /* Header styling */
    h1, h2, h3 {
        background: linear-gradient(120deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    
    h1 {
        font-size: 42px !important;
    }
    h2 {
        font-size: 32px !important;
    }
    h3 {
        font-size: 24px !important;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #667eea;
        padding: 12px 18px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 0 3px rgba(118, 75, 162, 0.3);
    }
    
    /* Select box */
    .stSelectbox > div > div {
        border-radius: 15px;
        border: 2px solid #667eea;
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Score display */
    .score-display {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px 25px;
        border-radius: 15px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        margin: 10px 0;
    }
    
    /* Border container */
    .border-container {
        border: 3px solid #667eea;
        border-radius: 25px;
        padding: 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        background: white;
        margin: 15px 0;
    }
    
    /* Dashboard card */
    .dashboard-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 10px 0;
        border-left: 5px solid #667eea;
    }
    
    /* Sidebar */
    .sidebar-content {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 20px;
        color: white;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #666;
        padding: 20px 0;
        margin-top: 30px;
        border-top: 2px solid #eee;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# ============ COVER PAGE ============
def cover_page():
    st.markdown("""
    <div class="cover-page">
        <div class="cover-icon">📚</div>
        <h1>Hiika Way App</h1>
        <h3>🏫 Dandeettii Dubbisuu, Barreessuu fi Shallaguu</h3>
        <p>
            <strong>Baga Nagaan gara Hiika Way App Dandeettii dubbisuu, barreessuu fi shallaguu baratootaa kutaa 1-5 tiif Kitesa Negasa tiin kalaqameetti Dhuftan!</strong>
        </p>
        <div style="margin: 20px 0; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; position: relative; z-index: 1;">
            <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; font-size: 14px;">📖 Dubbisuu</span>
            <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; font-size: 14px;">✍️ Barreessuu</span>
            <span style="background: rgba(255,255,255,0.2); padding: 8px 16px; border-radius: 20px; font-size: 14px;">🔢 Shallaguu</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Subject Cards
    st.markdown("### 📚 Qabiyyee Gosa Barnootaa")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="subject-card oromo-card">
            <span class="icon">🌿</span>
            <div class="title">AFAAN OROMOO</div>
            <div class="subtitle">Kutaa 1-5</div>
            <div style="margin-top: 8px; font-size: 12px; color: #28a745;">📖 Dubbisuu & ✍️ Barreessuu</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="subject-card english-card">
            <span class="icon">🌍</span>
            <div class="title">AFAAN INGILIFFAA</div>
            <div class="subtitle">Kutaa 1-5</div>
            <div style="margin-top: 8px; font-size: 12px; color: #007bff;">📖 Reading & ✍️ Writing</div>
        </div>
        """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="subject-card math-card">
            <span class="icon">🔢</span>
            <div class="title">HERREGA</div>
            <div class="subtitle">Kutaa 1-5</div>
            <div style="margin-top: 8px; font-size: 12px; color: #dc3545;">➕ Subtraction & ✖️ Multiplication</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="subject-card" style="border-color: #ff6b6b; background: linear-gradient(135deg, #fff5f5 0%, #ffe0e0 100%);">
            <span class="icon">🏆</span>
            <div class="title">QORMAATA WALIIGALAA</div>
            <div class="subtitle">Kutaa 1-5</div>
            <div style="margin-top: 8px; font-size: 12px; color: #ff6b6b;">📊 Comprehensive Assessment</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Welcome button with hand icon
    st.markdown("""
    <div style="text-align: center; margin: 20px 0;">
        <p style="font-size: 20px; font-weight: bold; color: #667eea;">👋 WELCOME TO HIKA WAY APP</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🤝 Harka Fuudha Galchi", use_container_width=True, key="welcome_btn"):
            st.session_state.page = "login"
            st.rerun()
    
    st.divider()
    
    # Furtuu (Key) section
    st.markdown("""
    <div style="text-align: center; margin: 10px 0;">
        <p style="font-size: 16px; color: #666;">🔑 FURTUU (KEY)</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔐 Furtuu Galchi", use_container_width=True, key="key_btn"):
            st.info("🔑 Furtuun galmaa'eera! Amma app fayyadamuu dandeessa.")
            st.balloons()

# ============ LOGIN SYSTEM ============
def login_page():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); 
                padding: 20px; border-radius: 20px; text-align: center; margin: 10px 0;">
        <h2 style="color: white !important; -webkit-text-fill-color: white !important;">🔐 Login System</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.container():
            email = st.text_input("📧 Gmail", placeholder="name@gmail.com")
            password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("👨‍🎓 Barataa Login", use_container_width=True):
                    if email and password:
                        st.session_state.logged_in = True
                        st.session_state.user_role = "student"
                        st.session_state.page = "student_dashboard"
                        st.success("✅ Barataa milkaa'inaan galmaa'e!")
                        st.rerun()
                    else:
                        st.warning("⚠️ Mee Gmail fi Password barreessi!")
            
            with col2:
                if st.button("👨‍🏫 Barsiisaa Login", use_container_width=True):
                    if email and password:
                        if email == "teacher@hiika.com" and password == "teacher123":
                            st.session_state.logged_in = True
                            st.session_state.user_role = "teacher"
                            st.session_state.page = "teacher_dashboard"
                            st.success("✅ Barsiisaa milkaa'inaan galmaa'e!")
                            st.rerun()
                        else:
                            st.warning("⚠️ Gmail ykn Password dogoggora qaba!")
                    else:
                        st.warning("⚠️ Mee Gmail fi Password barreessi!")
            
            st.divider()
            if st.button("🏠 Gara Fuula Duraatti Deebi'i", use_container_width=True):
                st.session_state.page = "cover"
                st.rerun()

# ============ STUDENT DASHBOARD ============
def student_dashboard():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 20px; border-radius: 20px; text-align: center; margin: 10px 0;">
        <h2 style="color: white !important; -webkit-text-fill-color: white !important;">👨‍🎓 Dashboard Barataa</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Student registration form
    with st.container():
        st.markdown("### 📝 Galmee Barataa")
        
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Maqaa Guutuu Barataa", placeholder="Maqaa kee barreessi...")
            grade = st.selectbox("Kutaa", ["Kutaa 1", "Kutaa 2", "Kutaa 3", "Kutaa 4", "Kutaa 5"])
        
        with col2:
            class_number = st.selectbox("Lakkoofsa Daree", list(range(1, 101)))
            section = st.selectbox("Section (Daree)", ["A", "B", "C", "D", "E", "F", "G", "H"])
        
        if st.button("💾 Save", use_container_width=True):
            if full_name:
                st.session_state.student_data = {
                    "name": full_name,
                    "grade": grade,
                    "class": class_number,
                    "section": section,
                    "registered": True
                }
                st.success(f"✅ Barataa {full_name} galmoofteetta! Qormaataaf qophaa'i!")
                st.balloons()
            else:
                st.warning("⚠️ Mee maqaa kee barreessi!")
    
    st.divider()
    
    # Navigation buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("➡️ Gara Gaaffiitti Darbi", use_container_width=True):
            if st.session_state.student_data.get("registered"):
                st.session_state.page = "quiz_start"
                st.rerun()
            else:
                st.warning("⚠️ Mee dura galmaa'i!")
    
    with col2:
        if st.button("⬅️ Gara Duubatti Deebi'i", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

# ============ QUIZ START PAGE ============
def quiz_start_page():
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%); 
                padding: 20px; border-radius: 20px; text-align: center; margin: 10px 0;">
        <h2 style="color: white !important; -webkit-text-fill-color: white !important;">📝 Baga nagaan Gara Kutaa Gaaffiitti Dhuftan!</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate 60 questions (20 from each subject)
    if not st.session_state.quiz_questions:
        st.session_state.quiz_questions = generate_questions()
    
    if "current_quiz_index" not in st.session_state:
        st.session_state.current_quiz_index = 0
    if "quiz_attempts" not in st.session_state:
        st.session_state.quiz_attempts = {}
    
    q = st.session_state.quiz_questions[st.session_state.current_quiz_index]
    
    # Progress
    progress = (st.session_state.current_quiz_index + 1) / len(st.session_state.quiz_questions)
    st.progress(progress)
    st.write(f"Gaaffii: {st.session_state.current_quiz_index + 1} / {len(st.session_state.quiz_questions)}")
    
    # Display question
    st.markdown(f"""
    <div class="border-container">
        <div style="font-size: 40px; text-align: center;">{q.get('image', '❓')}</div>
        <h4>Gaaffii {st.session_state.current_quiz_index + 1}:</h4>
        <p style="font-size: 18px; font-weight: bold;">{q['question']}</p>
        <p style="color: #666; font-size: 14px;">🏷️ {q['category']} | ⭐ {q['difficulty']}</p>
        <div style="background: #f0f0f0; padding: 15px; border-radius: 10px; margin: 10px 0;">
            {'  '.join(q['options'])}
        </div>
        <p style="color: #666; font-size: 14px;">📝 Yeroo yaala: {3 - q.get('attempts', 0)} hafte</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Audio button if available
    if q.get('audio'):
        if st.button("🔊 Sagalee Dhaggeeffadhu", use_container_width=True):
            st.toast(f"🎧 {q['audio']}")
    
    # Answer input
    ans = st.text_input("Deebii kee asitti barreessi (Fkn: A)", key=f"quiz_ans_{st.session_state.current_quiz_index}", placeholder="Filannoo kee barreessi...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mirkaneessi", use_container_width=True):
            if ans.strip().upper() == q["answer"]:
                st.success(f"🎉 Sirriidha {st.session_state.student_data.get('name', 'Barataa')}!")
                q['correct'] = True
                q['attempts'] = q.get('attempts', 0)
                st.balloons()
            else:
                q['attempts'] = q.get('attempts', 0) + 1
                if q['attempts'] >= 3:
                    st.error(f"❌ {st.session_state.student_data.get('name', 'Barataa')}, hin deebisne!")
                    q['correct'] = False
                else:
                    st.error(f"❌ {st.session_state.student_data.get('name', 'Barataa')}, yeroo {q['attempts']} dogoggora qaba! Mee irra deebi'iitii yaali.")
    
    with col2:
        if st.button("⏭️ Gaaffii Aanu", use_container_width=True):
            if st.session_state.current_quiz_index < len(st.session_state.quiz_questions) - 1:
                st.session_state.current_quiz_index += 1
                st.rerun()
            else:
                st.session_state.page = "quiz_results"
                st.rerun()
    
    st.divider()
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "student_dashboard"
        st.rerun()

# ============ GENERATE QUESTIONS ============
def generate_questions():
    questions = []
    
    # Afaan Oromoo Questions (20)
    oromo_questions = [
        {
            "question": "Afaan Oromoon 'Water' maal jedhu?",
            "options": ["A) Bishaan", "B) Biyya", "C) Bosona", "D) Arba"],
            "answer": "A",
            "category": "Afaan Oromoo",
            "difficulty": "Salphoo",
            "image": "💧",
            "audio": "Bishaan"
        },
        {
            "question": "Qubee 'A' jedhu jecha kamii eegala?",
            "options": ["A) Afaan", "B) Bishaan", "C) Cabbana", "D) Daraan"],
            "answer": "A",
            "category": "Afaan Oromoo",
            "difficulty": "Salphoo",
            "image": "🔤",
            "audio": "Afaan"
        },
        {
            "question": "'Arba' jechuun maal?",
            "options": ["A) Elephant", "B) Lion", "C) Tiger", "D) Zebra"],
            "answer": "A",
            "category": "Afaan Oromoo",
            "difficulty": "Giddugaleessa",
            "image": "🐘",
            "audio": "Arba"
        },
        {
            "question": "Afaan Oromoon 'Good morning' maal jedhu?",
            "options": ["A) Akkam", "B) Baga nagaan", "C) Galatoomaa", "D) Nagaatti"],
            "answer": "B",
            "category": "Afaan Oromoo",
            "difficulty": "Giddugaleessa",
            "image": "🌅",
            "audio": "Baga nagaan"
        },
        {
            "question": "'Biyya' jechuun maal?",
            "options": ["A) Water", "B) Country", "C) Tree", "D) House"],
            "answer": "B",
            "category": "Afaan Oromoo",
            "difficulty": "Salphoo",
            "image": "🌍",
            "audio": "Biyya"
        },
        {
            "question": "Qubee 'C' jedhu jecha kamii eegala?",
            "options": ["A) Cabbana", "B) Bishaan", "C) Afaan", "D) Daraan"],
            "answer": "A",
            "category": "Afaan Oromoo",
            "difficulty": "Salphoo",
            "image": "❄️",
            "audio": "Cabbana"
        }
    ]
    
    # English Questions (20)
    english_questions = [
        {
            "question": "What is the English word for 'Bishaan'?",
            "options": ["A) Water", "B) Fire", "C) Air", "D) Earth"],
            "answer": "A",
            "category": "Afaan Ingiliffaa",
            "difficulty": "Salphoo",
            "image": "💧",
            "audio": "Water"
        },
        {
            "question": "What is the English word for 'Arba'?",
            "options": ["A) Elephant", "B) Lion", "C) Tiger", "D) Giraffe"],
            "answer": "A",
            "category": "Afaan Ingiliffaa",
            "difficulty": "Giddugaleessa",
            "image": "🐘",
            "audio": "Elephant"
        },
        {
            "question": "What is the English word for 'Biyya'?",
            "options": ["A) Water", "B) Country", "C) Tree", "D) House"],
            "answer": "B",
            "category": "Afaan Ingiliffaa",
            "difficulty": "Salphoo",
            "image": "🌍",
            "audio": "Country"
        },
        {
            "question": "How do you say 'Good morning' in English?",
            "options": ["A) Hello", "B) Good morning", "C) Good night", "D) Good evening"],
            "answer": "B",
            "category": "Afaan Ingiliffaa",
            "difficulty": "Salphoo",
            "image": "🌅",
            "audio": "Good morning"
        },
        {
            "question": "What is the English word for 'Cabbana'?",
            "options": ["A) Ice", "B) Water", "C) Fire", "D) Wind"],
            "answer": "A",
            "category": "Afaan Ingiliffaa",
            "difficulty": "Salphoo",
            "image": "❄️",
            "audio": "Ice"
        },
        {
            "question": "What is the English word for 'Bosona'?",
            "options": ["A) Forest", "B) Desert", "C) Ocean", "D) Mountain"],
            "answer": "A",
            "category": "Afaan Ingiliffaa",
            "difficulty": "Giddugaleessa",
            "image": "🌲",
            "audio": "Forest"
        }
    ]
    
    # Math Questions (20)
    math_questions = [
        {
            "question": "15 + 12 = ?",
            "options": ["A) 25", "B) 27", "C) 30", "D) 22"],
            "answer": "B",
            "category": "Herregaa",
            "difficulty": "Salphoo",
            "image": "➕",
            "audio": "15 plus 12 equals 27"
        },
        {
            "question": "45 - 20 = ?",
            "options": ["A) 15", "B) 25", "C) 20", "D) 35"],
            "answer": "B",
            "category": "Herregaa",
            "difficulty": "Salphoo",
            "image": "➖",
            "audio": "45 minus 20 equals 25"
        },
        {
            "question": "6 × 7 = ?",
            "options": ["A) 36", "B) 42", "C) 48", "D) 54"],
            "answer": "B",
            "category": "Herregaa",
            "difficulty": "Giddugaleessa",
            "image": "✖️",
            "audio": "6 times 7 equals 42"
        },
        {
            "question": "72 ÷ 8 = ?",
            "options": ["A) 8", "B) 9", "C) 7", "D) 10"],
            "answer": "B",
            "category": "Herregaa",
            "difficulty": "Giddugaleessa",
            "image": "➗",
            "audio": "72 divided by 8 equals 9"
        },
        {
            "question": "30 + 15 = ?",
            "options": ["A) 40", "B) 45", "C) 50", "D) 55"],
            "answer": "B",
            "category": "Herregaa",
            "difficulty": "Salphoo",
            "image": "➕",
            "audio": "30 plus 15 equals 45"
        },
        {
            "question": "100 - 35 = ?",
            "options": ["A) 55", "B) 65", "C) 75", "D) 85"],
            "answer": "B",
            "category": "Herregaa",
            "difficulty": "Giddugaleessa",
            "image": "➖",
            "audio": "100 minus 35 equals 65"
        }
    ]
    
    # Combine and shuffle all questions
    all_questions = oromo_questions + english_questions + math_questions
    random.shuffle(all_questions)
    
    # Add attempts tracking
    for q in all_
