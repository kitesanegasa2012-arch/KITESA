import streamlit as st
import time
from datetime import datetime
import re

# Page Configuration
st.set_page_config(
    page_title="Hiika Way (HW) - Learning Platform", 
    page_icon="📚", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 2rem;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Card styling with shadow and color */
    .custom-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15), 0 6px 10px rgba(0,0,0,0.1);
        margin: 1rem 0;
        transition: transform 0.3s ease;
        border-left: 5px solid #4CAF50;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.2);
    }
    
    .card-blue {
        border-left-color: #2196F3;
        background: linear-gradient(135deg, #ffffff 0%, #e3f2fd 100%);
    }
    
    .card-purple {
        border-left-color: #9C27B0;
        background: linear-gradient(135deg, #ffffff 0%, #f3e5f5 100%);
    }
    
    .card-orange {
        border-left-color: #FF9800;
        background: linear-gradient(135deg, #ffffff 0%, #fff3e0 100%);
    }
    
    .card-green {
        border-left-color: #4CAF50;
        background: linear-gradient(135deg, #ffffff 0%, #e8f5e9 100%);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(0px) scale(0.98);
    }
    
    /* Different button colors */
    .btn-primary > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .btn-success > button {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);
        box-shadow: 0 4px 15px rgba(86, 171, 47, 0.4);
    }
    
    .btn-danger > button {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.4);
    }
    
    .btn-warning > button {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        box-shadow: 0 4px 15px rgba(253, 160, 133, 0.4);
        color: #333;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.6rem 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
    }
    
    /* Success/Error/Warning messages */
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    
    /* Progress bar styling */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        height: 8px;
    }
    
    /* Metric cards */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        text-align: center;
        border-top: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    }
    
    /* Title styling */
    h1, h2, h3 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }
    
    /* Divider styling */
    hr {
        border: none;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
        border-radius: 3px;
        margin: 2rem 0;
    }
    
    /* Info box */
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        margin: 1rem 0;
        text-align: center;
    }
    
    /* Login card */
    .login-card {
        background: white;
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        max-width: 400px;
        margin: 2rem auto;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    /* Cover page */
    .cover-page {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 25px;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .cover-page h1 {
        background: none;
        -webkit-text-fill-color: white;
        font-size: 3.5rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .cover-page p {
        font-size: 1.2rem;
        opacity: 0.95;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    
    /* Module cards */
    .module-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 1rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
        border: 2px solid transparent;
    }
    
    .module-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.15);
        border-color: #667eea;
    }
    
    /* Badge */
    .badge {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .cover-page h1 {
            font-size: 2.5rem;
        }
        .custom-card {
            padding: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "students" not in st.session_state:
    st.session_state.students = []
if "current_student" not in st.session_state:
    st.session_state.current_student = None
if "page" not in st.session_state:
    st.session_state.page = "cover"
if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
if "teacher_name" not in st.session_state:
    st.session_state.teacher_name = ""
if "last_login" not in st.session_state:
    st.session_state.last_login = None

# Cover Page
def cover_page():
    st.markdown("""
    <div class="cover-page">
        <h1>📚 Hiika Way (HW)</h1>
        <p>🤖 Learning Platform for Students</p>
        <p style="font-size: 0.9rem; opacity: 0.8;">Barumsaa Oromoo | Afaan Oromoo | Herrega</p>
        <div style="margin-top: 2rem;">
            <span class="badge">📖 Dubbisuu</span>
            <span class="badge" style="background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);">✍️ Barreessuu</span>
            <span class="badge" style="background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);">🔢 Herrega</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="login-card">
            <h3 style="text-align: center; margin-bottom: 1.5rem;">🔐 Login System</h3>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form("login_form"):
            username = st.text_input("👤 Username", placeholder="Enter your username")
            password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.form_submit_button("✅ Login", use_container_width=True):
                    if username == "admin" and password == "admin123":
                        st.session_state.is_logged_in = True
                        st.session_state.teacher_name = username
                        st.session_state.last_login = datetime.now().strftime("%Y-%m-%d %H:%M")
                        st.session_state.login_attempts = 0
                        st.session_state.page = "register"
                        st.success("✅ Login successful! Welcome back!")
                        time.sleep(0.5)
                        st.rerun()
                    else:
                        st.session_state.login_attempts += 1
                        remaining = 3 - st.session_state.login_attempts
                        if remaining > 0:
                            st.error(f"❌ Invalid credentials! {remaining} attempts remaining.")
                        else:
                            st.error("🚫 Too many failed attempts! Please try again later.")
                            
            with col2:
                if st.form_submit_button("ℹ️ Demo", use_container_width=True):
                    st.info("👤 Username: admin\n🔑 Password: admin123")
        
        st.markdown("""
        <div style="text-align: center; margin-top: 1rem; font-size: 0.9rem; color: #666;">
            <p>💡 Demo credentials: admin / admin123</p>
            <p style="font-size: 0.8rem;">© 2026 Hiika Way Learning Platform</p>
        </div>
        """, unsafe_allow_html=True)

# Student Registration Page
def registration_page():
    # Stats Card
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>📊 Total</h4>
            <h2>{}</h2>
            <p style="color: #666; font-size: 0.9rem;">Barattoota Galmaa'an</p>
        </div>
        """.format(len(st.session_state.students)), unsafe_allow_html=True)
    
    with col2:
        remaining = 80 - len(st.session_state.students)
        st.markdown("""
        <div class="metric-card" style="border-top-color: #FF9800;">
            <h4>📝 Remaining</h4>
            <h2>{}</h2>
            <p style="color: #666; font-size: 0.9rem;">Bakki Haafaa</p>
        </div>
        """.format(remaining), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card" style="border-top-color: #4CAF50;">
            <h4>🎯 Capacity</h4>
            <h2>80</h2>
            <p style="color: #666; font-size: 0.9rem;">Daree Guutuu</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="custom-card card-blue">
        <h3>📝 Galmee Barattoota Daree (Max 80)</h3>
        <p style="color: #666; margin-bottom: 1rem;">Barattoota haaraa galmeessuu fi barattoota jiran ilaaluu dandeessu.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        name = st.text_input("👤 Maqaa Barataa", placeholder="Maqaa guutuu barreessi...", key="student_name_input")
    with col2:
        student_id = st.text_input("🆔 ID (Lakk)", placeholder="ID dhaan galchi", key="student_id_input")
    with col3:
        st.write("")
        st.write("")
        if st.button("➕ Galchi Barataa", use_container_width=True, key="add_student_btn"):
            if not name.strip():
                st.warning("⚠️ Mee maqaa barataa barreessi!", icon="⚠️")
            elif len(st.session_state.students) >= 80:
                st.error("🚫 Daree tokko keessatti barataan 80 guutameera!", icon="🚫")
            else:
                sid = student_id.strip() if student_id.strip() else str(len(st.session_state.students) + 1)
                st.session_state.students.append({
                    "id": sid,
                    "name": name.strip(),
                    "registered_at": datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                st.success(f"✅ Barataan {name} milkaa'inaan galmaa'e!", icon="✅")
                time.sleep(0.3)
                st.rerun()
    
    st.markdown("---")
    
    if not st.session_state.students:
        st.info("📢 Ammaaf barataan galmaa'e hin jiru. Maqaa barataa galchaa!", icon="ℹ️")
    else:
        st.markdown(f"### 📋 Barattoota Galmaa'an ({len(st.session_state.students)} / 80)")
        
        # Search/filter
        search = st.text_input("🔍 Barataa barbaadi...", placeholder="Maqaan ykn ID'n barbaadi...")
        
        filtered_students = st.session_state.students
        if search:
            filtered_students = [s for s in st.session_state.students 
                               if search.lower() in s['name'].lower() or search in s['id']]
        
        for idx, st_data in enumerate(st.session_state.students):
            if st_data not in filtered_students:
                continue
                
            color_class = ["card-green", "card-blue", "card-purple", "card-orange"][idx % 4]
            st.markdown(f"""
            <div class="custom-card {color_class}" style="padding: 1rem;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong style="font-size: 1.1rem;">🆔 {st_data['id']}</strong>
                        <span style="margin-left: 1rem; font-size: 1.1rem;">{st_data['name']}</span>
                        <br>
                        <span style="font-size: 0.8rem; color: #666;">📅 {st_data.get('registered_at', 'N/A')}</span>
                    </div>
                    <div style="display: flex; gap: 0.5rem;">
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button("🚀 Jalqabi", key=f"start_{idx}", use_container_width=True):
                    st.session_state.current_student = st_data["name"]
                    st.session_state.page = "home"
                    st.rerun()
            with col2:
                if st.button("🗑️ Haqi", key=f"del_{idx}", use_container_width=True):
                    st.session_state.students.pop(idx)
                    st.rerun()
            
            st.markdown("</div></div></div>", unsafe_allow_html=True)
    
    # Teacher info
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.is_logged_in = False
            st.session_state.teacher_name = ""
            st.session_state.page = "cover"
            st.rerun()

# Home Page
def home_page():
    st.markdown(f"""
    <div class="info-box">
        <h2 style="color: white; -webkit-text-fill-color: white;">👋 Baga nagaan dhufte, {st.session_state.current_student}!</h2>
        <p style="color: white; opacity: 0.95;">Damee barachuu barbaaddu filadhu 👇</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Module selection with improved styling
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;">
            <div style="text-align: center; padding: 1rem;">
                <h3 style="color: white; -webkit-text-fill-color: white; font-size: 2.5rem;">📖</h3>
                <h4 style="color: white; -webkit-text-fill-color: white;">Dubbisuu &</h4>
                <h4 style="color: white; -webkit-text-fill-color: white;">Dhaggeeffachuu</h4>
                <p style="color: rgba(255,255,255,0.9);">Reading & Listening</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📖 Start Reading", use_container_width=True, key="btn_reading"):
            st.session_state.page = "reading"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="module-card" style="background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%); color: white;">
            <div style="text-align: center; padding: 1rem;">
                <h3 style="color: white; -webkit-text-fill-color: white; font-size: 2.5rem;">✍️</h3>
                <h4 style="color: white; -webkit-text-fill-color: white;">Barreessuu &</h4>
                <h4 style="color: white; -webkit-text-fill-color: white;">Qormaata</h4>
                <p style="color: rgba(255,255,255,0.9);">Writing & Assessment</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("✍️ Start Writing", use_container_width=True, key="btn_writing"):
            st.session_state.page = "writing"
            st.rerun()
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <div class="module-card" style="background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); color: #333;">
            <div style="text-align: center; padding: 1rem;">
                <h3 style="color: #333; -webkit-text-fill-color: #333; font-size: 2.5rem;">🔢</h3>
                <h4 style="color: #333; -webkit-text-fill-color: #333;">Shallaggaa</h4>
                <h4 style="color: #333; -webkit-text-fill-color: #333;">Herregaa</h4>
                <p style="color: rgba(0,0,0,0.8);">Mathematics</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔢 Start Maths", use_container_width=True, key="btn_math"):
            st.session_state.page = "math"
            st.rerun()
    
    with col4:
        st.markdown("""
        <div class="module-card" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white;">
            <div style="text-align: center; padding: 1rem;">
                <h3 style="color: white; -webkit-text-fill-color: white; font-size: 2.5rem;">🎨</h3>
                <h4 style="color: white; -webkit-text-fill-color: white;">Creative</h4>
                <h4 style="color: white; -webkit-text-fill-color: white;">Activities</h4>
                <p style="color: rgba(255,255,255,0.9);">Coming Soon</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("🎨 Coming Soon", use_container_width=True, disabled=True, key="btn_creative")
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 3])
    with col2:
        if st.button("⬅️ Gara Galmee Barattootaatti Deebi'i", use_container_width=True):
            st.session_state.current_student = None
            st.session_state.page = "register"
            st.rerun()

# Reading Page
def reading_page():
    st.markdown(f"""
    <div class="custom-card card-purple">
        <h3>📖 Dubbisuu - {st.session_state.current_student}</h3>
        <p style="color: #666;">Qubeefi jechoota Afaan Oromoo dubbisuu fi dhaggeeffachuu baradhu.</p>
    </div>
    """, unsafe_allow_html=True)
    
    lessons = [
        {"title": "Qubee A", "text": "A - Afaan (Red Apple)", "sound": "Qubee A sirriitti dubbifameera.", "emoji": "🍎"},
        {"title": "Qubee B", "text": "B - Bishaan (Water)", "sound": "Jechi Bishaan jedhu dhaga'amaa jira.", "emoji": "💧"},
        {"title": "Qubee C", "text": "C - Ciree (Knife)", "sound": "Jechi Ciree jedhu dhaga'amaa jira.", "emoji": "🔪"},
        {"title": "Qubee D", "text": "D - Daraaraa (Flower)", "sound": "Jechi Daraaraa jedhu dhaga'amaa jira.", "emoji": "🌺"},
        {"title": "Qubee E", "text": "E - Ejersa (Tree)", "sound": "Jechi Ejersa jedhu dhaga'amaa jira.", "emoji": "🌳"},
        {"title": "Qubee F", "text": "F - Foon (Meat)", "sound": "Jechi Foon jedhu dhaga'amaa jira.", "emoji": "🥩"},
        {"title": "Qubee G", "text": "G - Galaana (River)", "sound": "Jechi Galaana jedhu dhaga'amaa jira.", "emoji": "🌊"},
        {"title": "Qubee H", "text": "H - Hoolaa (Sheep)", "sound": "Jechi Hoolaa jedhu dhaga'amaa jira.", "emoji": "🐑"},
        {"title": "Qubee I", "text": "I - Illubbaa (Ball)", "sound": "Jechi Illubbaa jedhu dhaga'amaa jira.", "emoji": "⚽"},
        {"title": "Qubee J", "text": "J - Jaba (Strong)", "sound": "Jechi Jaba jedhu dhaga'amaa jira.", "emoji": "💪"},
    ]
    
    if "r_index" not in st.session_state:
        st.session_state.r_index = 0
    
    item = lessons[st.session_state.r_index]
    progress = (st.session_state.r_index + 1) / len(lessons)
    
    st.progress(progress, text=f"📊 Progress: {int(progress * 100)}%")
    
    # Main content card
    st.markdown(f"""
    <div class="custom-card" style="text-align: center; padding: 2rem;">
        <h2 style="font-size: 4rem; margin: 0;">{item['emoji']}</h2>
        <h3 style="margin: 1rem 0;">{item['title']}</h3>
        <div style="background: #f5f5f5; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;">
            <p style="font-size: 1.5rem; margin: 0;">{item['text']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔊 Sagalee Dhaggeeffadhu", use_container_width=True):
            st.success(f"🔊 {st.session_state.current_student}, {item['sound']}")
            st.balloons()
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.session_state.r_index > 0:
            if st.button("⬅️ Duubatti", use_container_width=True):
                st.session_state.r_index -= 1
                st.rerun()
    with col3:
        if st.session_state.r_index < len(lessons) - 1:
            if st.button("Fuuldharatti ➡️", use_container_width=True):
                st.session_state.r_index += 1
                st.rerun()
        else:
            if st.button("🏆 Xumuruu", use_container_width=True):
                st.balloons()
                st.success(f"🎉 Galatoomi {st.session_state.current_student}! Qubee hunda baratte! 🎉")
    
    st.markdown("---")
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Writing Page
def writing_page():
    st.markdown(f"""
    <div class="custom-card card-orange">
        <h3>✍️ Barreessuu - {st.session_state.current_student}</h3>
        <p style="color: #666;">Jechoota sirriidhaan barreessuu fi qormaata qabxii argachuuf.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if "w_index" not in st.session_state:
        st.session_state.w_index = 0
        st.session_state.w_score = 0
    
    questions = [
        {"prompt": "Jecha 'Bishaan' jedhu qubee sirriidhaan asitti barreessi:", "answer": "bishaan", "hint": "bi-sh-a-n"},
        {"prompt": "Jecha 'Afaan' jedhu qubee meeqaani (kamii) eegala? (Fkn: a)", "answer": "a", "hint": "qubee jalqabaa"},
        {"prompt": "Jecha 'Dubbisuu' jedhu qubee sirriidhaan barreessi:", "answer": "dubbisuu", "hint": "du-bbi-suu"},
        {"prompt": "Jecha 'Barreessuu' jedhu qubee sirriidhaan barreessi:", "answer": "barreessuu", "hint": "ba-rreess-uu"},
        {"prompt": "Jecha 'Herrega' jedhu qubee sirriidhaan barreessi:", "answer": "herrega", "hint": "he-rre-ga"},
    ]
    
    q = questions[st.session_state.w_index]
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📝 Gaaffii", f"{st.session_state.w_index + 1} / {len(questions)}")
    with col2:
        st.metric("⭐ Qabxii", f"{st.session_state.w_score}")
    
    st.markdown(f"""
    <div class="custom-card" style="padding: 1.5rem;">
        <p style="font-size: 1.1rem; font-weight: bold;">❓ {q['prompt']}</p>
        <p style="color: #666; font-size: 0.9rem;">💡 Qorsa: {q['hint']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    ans = st.text_input("✍️ Deebii kee asitti barreessi", key="w_ans_input", placeholder="Deebii kee barreessi...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mirkaneessi", use_container_width=True, key="check_writing"):
            if ans.strip().lower() == q["answer"]:
                st.success(f"🎉 Jabaadhu {st.session_state.current_student}! Sirriidha!")
                st.session_state.w_score += 10
                st.balloons()
            else:
                st.error(f"❌ {st.session_state.current_student}, dogoggora qaba! Mee irra deebi'iitii yaali.")
    
    with col2:
        if st.button("⏭️ Gaaffii Aanu", use_container_width=True, key="next_writing"):
            if st.session_state.w_index < len(questions) - 1:
                st.session_state.w_index += 1
                st.rerun()
            else:
                st.balloons()
                st.success(f"🏆 Galatoomi {st.session_state.current_student}! Qabxii waliigalaa: {st.session_state.w_score}")
                st.balloons()
    
    st.markdown("---")
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Math Page
def math_page():
    st.markdown(f"""
    <div class="custom-card card-green">
        <h3>🔢 Shallaggaa Herregaa - {st.session_state.current_student}</h3>
        <p style="color: #666;">Gaaffii herregaa furuun qabxii argadhu!</p>
    </div>
    """, unsafe_allow_html=True)
    
    if "m_index" not in st.session_state:
        st.session_state.m_index = 0
        st.session_state.m_score = 0
    
    m_questions = [
        {"question": "15 + 12 = ?", "options": ["A) 25", "B) 27", "C) 30", "D) 22"], "answer": "27", "hint": "15 + 10 = 25, 25 + 2 = ?"},
        {"question": "45 - 20 = ?", "options": ["A) 15", "B) 25", "C) 20", "D) 35"], "answer": "25", "hint": "45 - 20 = 25"},
        {"question": "8 × 7 = ?", "options": ["A) 48", "B) 56", "C) 64", "D) 54"], "answer": "56", "hint": "7 × 8 = 56"},
        {"question": "100 ÷ 4 = ?", "options": ["A) 15", "B) 25", "C) 30", "D) 20"], "answer": "25", "hint": "100 ÷ 4 = 25"},
        {"question": "12 × 12 = ?", "options": ["A) 124", "B) 144", "C) 134", "D) 154"], "answer": "144", "hint": "12 × 12 = 144"},
    ]
    
    mq = m_questions[st.session_state.m_index]
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("📝 Gaaffii", f"{st.session_state.m_index + 1} / {len(m_questions)}")
    with col2:
        st.metric("⭐ Qabxii", f"{st.session_state.m_score}")
    
    st.markdown(f"""
    <div class="custom-card" style="padding: 1.5rem;">
        <p style="font-size: 1.3rem; font-weight: bold; text-align: center;">{mq['question']}</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; margin: 1rem 0;">
            <div style="background: #
