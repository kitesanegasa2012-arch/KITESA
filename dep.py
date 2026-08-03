import streamlit as st
import base64
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os

# Page Configurationimport streamlit as st
import base64
import random
import io
from gtts import gTTS  # Google Text-to-Speech
from io import BytesIO
import tempfile
import os

# Page Configuration
st.set_page_config(
    page_title="Hiika Way (HW)", 
    page_icon="📚", 
    layout="centered"
)

# Custom CSS for beautiful UI
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Card styling */
    .stButton > button {
        background: linear-gradient(to right, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 12px 24px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
        margin: 5px 0;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(0px);
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
    
    /* Input fields */
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #667eea;
        padding: 10px 15px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 0 3px rgba(118, 75, 162, 0.3);
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Cards for modules */
    .module-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 15px 0;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .module-card:hover {
        border-color: #667eea;
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
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
    
    /* Balloon container for celebration */
    .balloon-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
        overflow: hidden;
    }
    
    /* Audio player styling */
    .stAudio {
        border-radius: 20px;
        background: #f0f0f0;
        padding: 5px;
    }
    
    /* Border and shadow for containers */
    .border-container {
        border: 3px solid #667eea;
        border-radius: 25px;
        padding: 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        background: white;
        margin: 15px 0;
    }
    
    /* Icon styling */
    .icon-large {
        font-size: 48px;
        text-align: center;
        margin: 10px 0;
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
    
    /* Cover page styling */
    .cover-page {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 50px 30px;
        border-radius: 30px;
        text-align: center;
        color: white;
        margin: 20px 0;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
    }
    
    .cover-page h1 {
        color: white !important;
        -webkit-text-fill-color: white !important;
        font-size: 48px;
        margin-bottom: 10px;
    }
    
    .cover-page h3 {
        color: rgba(255,255,255,0.9) !important;
        -webkit-text-fill-color: rgba(255,255,255,0.9) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "students" not in st.session_state:
    st.session_state.students = []
if "current_student" not in st.session_state:
    st.session_state.current_student = None
if "page" not in st.session_state:
    st.session_state.page = "register"
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

# Text-to-Speech function
def text_to_speech(text, lang='om'):
    """Convert text to speech and return audio data"""
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    except Exception as e:
        # Fallback: generate a simple beep or return None
        st.warning(f"⚠️ Sagaleen hin dhaga'amu: {str(e)}")
        return None

# Audio player function
def play_audio(text, lang='om'):
    """Play audio for given text"""
    if text and len(text) > 0:
        try:
            audio_data = text_to_speech(text, lang)
            if audio_data:
                st.audio(audio_data, format='audio/mp3')
                return True
        except Exception as e:
            st.error(f"⚠️ Sagaleen hin dhaga'amu: {str(e)}")
            return False
    return False

# Cover Page
def cover_page():
    st.markdown("""
    <div class="cover-page">
        <div style="font-size: 80px; margin-bottom: 20px;">📚</div>
        <h1>Hiika Way (HW)</h1>
        <h3>Galmee & Qormaata Barsiisaa</h3>
        <p style="font-size: 18px; margin-top: 20px; opacity: 0.9;">
            Barattoota afaan Oromoo, dubbisuu, barreessuu fi herregaa barachuu dandeessu!
        </p>
        <div style="margin-top: 30px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <span style="background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 20px;">📖 Dubbisuu</span>
            <span style="background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 20px;">✍️ Barreessuu</span>
            <span style="background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 20px;">🔢 Herregaa</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Galmee Barattootaatti Galchu", use_container_width=True):
        st.session_state.page = "register"
        st.rerun()

# Page 1: Student Registration (Hanga 80)
def registration_page():
    cover_page()
    
    st.subheader("📝 Galmee Barattoota Daree (Max 80)")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        name = st.text_input("Maqaa Barataa", placeholder="Maqaa guutuu barreessi...")
    with col2:
        student_id = st.text_input("ID (Lakk)", placeholder="Lakkoofsa ID")
    with col3:
        st.write("")
        st.write("")
        if st.button("➕ Galchi", use_container_width=True):
            if not name.strip():
                st.warning("⚠️ Mee maqaa barataa barreessi!")
            elif len(st.session_state.students) >= 80:
                st.warning("⚠️ Daree tokko keessatti barataan 80 guutameera!")
            else:
                sid = student_id.strip() if student_id.strip() else str(len(st.session_state.students) + 1)
                st.session_state.students.append({"id": sid, "name": name.strip()})
                st.success(f"✅ Barataan {name} milkaa'inaan galmaa'e!")
                st.rerun()
    
    st.markdown(f"""
    <div class="score-display">
        📊 Barattoota Galmaa'an: {len(st.session_state.students)} / 80
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    if not st.session_state.students:
        st.info("ℹ️ Ammaaf barataan galmaa'e hin jiru. Maqaa barataa galchaa!")
    else:
        for idx, st_data in enumerate(st.session_state.students):
            with st.container():
                col1, col2, col3, col4 = st.columns([1, 3, 1.5, 1])
                col1.markdown(f"**🆔 {st_data['id']}**")
                col2.markdown(f"**{st_data['name']}**")
                
                if col3.button("🚀 Jalqabi", key=f"start_{idx}", use_container_width=True):
                    st.session_state.current_student = st_data["name"]
                    st.session_state.page = "home"
                    st.rerun()
                
                if col4.button("🗑️ Haqi", key=f"del_{idx}", use_container_width=True):
                    st.session_state.students.pop(idx)
                    st.rerun()

# Page 2: Home Screen (Module Selection)
def home_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 20px;">
        <h2>👋 Baga nagaan dhufte, {st.session_state.current_student}!</h2>
        <p style="color: white; opacity: 0.9;">Damee barachuu barbaaddu filadhu:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Module Cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card" style="text-align: center;">
            <div class="icon-large">📖</div>
            <h3>Dubbisuu & Dhaggeeffachuu</h3>
            <p>Qubeewwan, jechoota, fi sagalee</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📖 Dubbisuu", use_container_width=True, key="read_btn"):
            st.session_state.page = "reading"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="module-card" style="text-align: center;">
            <div class="icon-large">✍️</div>
            <h3>Barreessuu & Qormaata</h3>
            <p>Barreessuu, hiikuu, fi qormaata</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("✍️ Barreessuu", use_container_width=True, key="write_btn"):
            st.session_state.page = "writing"
            st.rerun()
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="module-card" style="text-align: center;">
            <div class="icon-large">🔢</div>
            <h3>Herregaa</h3>
            <p>Shallaggaa, lakkoofsa, fi walitti bu'ii</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔢 Herregaa", use_container_width=True, key="math_btn"):
            st.session_state.page = "math"
            st.rerun()
    
    with col4:
        st.markdown("""
        <div class="module-card" style="text-align: center;">
            <div class="icon-large">📊</div>
            <h3>Qormaata Waliigalaa</h3>
            <p>Dandeettiwwan cimsuu</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 Qormaata", use_container_width=True, key="quiz_btn"):
            st.session_state.page = "quiz"
            st.rerun()
    
    st.divider()
    if st.button("⬅️ Gara Galmee Barattootaatti Deebi'i", use_container_width=True):
        st.session_state.current_student = None
        st.session_state.page = "register"
        st.rerun()

# Page 3: Reading Module
def reading_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 15px;">
        <h3>📖 Dubbisuu - {st.session_state.current_student}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    lessons = [
        {
            "title": "Qubee A",
            "text": "A - Afaan (Red Apple)",
            "text_audio": "Qubee A sirriitti dubbifameera.",
            "letter": "A",
            "words": ["Afaan", "Adeemsa", "Arba"],
            "image": "🍎",
            "example": "Afaan Oromoo"
        },
        {
            "title": "Qubee B",
            "text": "B - Bishaan (Water)",
            "text_audio": "Qubee B sirriitti dubbifameera.",
            "letter": "B",
            "words": ["Bishaan", "Biyya", "Bosona"],
            "image": "💧",
            "example": "Bishaan dhuguu"
        },
        {
            "title": "Jecha Bishaan",
            "text": "Bishaan - Water 💧",
            "text_audio": "Jechi Bishaan jedhu dhaga'amaa jira.",
            "letter": "B",
            "words": ["Bishaan", "Galaana", "Haroo"],
            "image": "🌊",
            "example": "Bishaan qulqulluu"
        },
        {
            "title": "Qubee C",
            "text": "C - Cabbana",
            "text_audio": "Qubee C sirriitti dubbifameera.",
            "letter": "C",
            "words": ["Cabbana", "Cimaa", "Cabsee"],
            "image": "❄️",
            "example": "Cabbana dhuguu"
        }
    ]
    
    if "r_index" not in st.session_state:
        st.session_state.r_index = 0
    
    item = lessons[st.session_state.r_index]
    progress = (st.session_state.r_index + 1) / len(lessons)
    st.progress(progress)
    
    # Display content with styling
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        <div class="border-container">
            <h3>{item['image']} {item['title']}</h3>
            <p style="font-size: 24px; font-weight: bold;">{item['text']}</p>
            <p style="font-size: 18px; color: #667eea;">Qubee: {item['letter']}</p>
            <p style="font-size: 16px; color: #666;">Fakkeenya: {item['example']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show related words
        st.markdown("### 📝 Jechoota Waliin:")
        for word in item['words']:
            st.markdown(f"- {word}")
    
    with col2:
        st.markdown(f"""
        <div class="border-container" style="text-align: center;">
            <div style="font-size: 80px;">{item['image']}</div>
            <div style="font-size: 48px; font-weight: bold; margin: 10px 0; color: #667eea;">{item['letter']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Audio playback with text-to-speech
        if st.button("🔊 Sagalee Dhaggeeffadhu", use_container_width=True):
            with st.spinner("🎵 Sagalee qophaa'aa jira..."):
                audio_text = f"{item['text']}. {item['text_audio']}"
                if play_audio(audio_text):
                    st.success(f"🎧 {st.session_state.current_student}, sagaleen dhaga'ameera!")
                else:
                    st.warning("⚠️ Sagaleen hin dhaga'amu, garuu barreeffama dubbisuu dandeessa!")
    
    # Image-based questions
    st.markdown("### 🖼️ Gaaffii Suuraa")
    if st.button(f"Suura {item['image']} ilaali fi maqaa isaa barreessi:", use_container_width=True):
        answer = st.text_input("Deebii kee", key="img_answer")
        if st.button("Mirkaneessi", key="img_check", use_container_width=True):
            if answer.strip().lower() in [item['title'].lower(), item['letter'].lower()]:
                st.success("🎉 Sirriidha! Qabxii argatte!")
                st.session_state.quiz_score += 5
                st.balloons()
            else:
                st.error("❌ Mee irra deebi'iitii yaali!")
    
    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.r_index > 0:
            if st.button("⬅️ Duubatti", use_container_width=True):
                st.session_state.r_index -= 1
                st.rerun()
    with col2:
        if st.session_state.r_index < len(lessons) - 1:
            if st.button("➡️ Fuuldharatti", use_container_width=True):
                st.session_state.r_index += 1
                st.rerun()
    
    st.divider()
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Page 4: Writing Module
def writing_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 15px;">
        <h3>✍️ Barreessuu - {st.session_state.current_student}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if "w_index" not in st.session_state:
        st.session_state.w_index = 0
        st.session_state.w_score = 0
    
    questions = [
        {
            "prompt": "Jecha 'Bishaan' jedhu qubee sirriidhaan asitti barreessi:",
            "answer": "bishaan",
            "hint": "B + i + sh + aa + n",
            "image": "💧",
            "audio": "Bishaan jechuun bishaan dhuguu"
        },
        {
            "prompt": "Jecha 'Afaan' jedhu qubee meeqaani (kamii) eegala? (Fkn: a)",
            "answer": "a",
            "hint": "Afaan jechuun A eegala",
            "image": "🔤",
            "audio": "Afaan jechuun afaan Oromoo"
        },
        {
            "prompt": "Jecha 'Arba' jedhu qubee meeqaani eegala?",
            "answer": "a",
            "hint": "Arba jechuun A eegala",
            "image": "🐘",
            "audio": "Arba jechuun bineensa"
        },
        {
            "prompt": "'Biyya' jedhu qubee kamii eegala?",
            "answer": "b",
            "hint": "Biyya jechuun B eegala",
            "image": "🌍",
            "audio": "Biyya jechuun biyya keenya"
        }
    ]
    
    q = questions[st.session_state.w_index]
    
    # Display score and progress
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            📝 Gaaffii: {st.session_state.w_index + 1} / {len(questions)}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            ⭐ Qabxii: {st.session_state.w_score}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="border-container">
        <div style="font-size: 40px; text-align: center;">{q['image']}</div>
        <h4>Gaaffii {st.session_state.w_index + 1}:</h4>
        <p style="font-size: 18px;">{q['prompt']}</p>
        <details>
            <summary>💡 Qorqaallii (Hint)</summary>
            <p>{q['hint']}</p>
        </details>
    </div>
    """, unsafe_allow_html=True)
    
    # Audio hint button
    if st.button("🔊 Sagalee Dhaggeeffachuuf", use_container_width=True):
        if play_audio(q['audio']):
            st.success("🎧 Sagaleen dhaga'ameera!")
        else:
            st.info("💡 Qorqaallii: " + q['hint'])
    
    ans = st.text_input("Deebii kee asitti barreessi", key="w_ans_input", placeholder="Deebii kee barreessi...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mirkaneessi", use_container_width=True):
            if ans.strip().lower() == q["answer"]:
                st.success(f"🎉 Jabaadhu {st.session_state.current_student}! Sirriidha!")
                st.session_state.w_score += 10
                st.balloons()
            else:
                st.error(f"❌ {st.session_state.current_student}, dogoggora qaba! Mee irra deebi'iitii yaali.")
    
    with col2:
        if st.button("⏭️ Gaaffii Aanu / Xumuruu", use_container_width=True):
            if st.session_state.w_index < len(questions) - 1:
                st.session_state.w_index += 1
                st.rerun()
            else:
                st.balloons()
                st.success(f"🏆 Galatoomi {st.session_state.current_student}! Qabxii waliigalaa: {st.session_state.w_score}")
    
    st.divider()
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Page 5: Math Module
def math_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 15px;">
        <h3>🔢 Shallaggaa Herregaa - {st.session_state.current_student}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if "m_index" not in st.session_state:
        st.session_state.m_index = 0
        st.session_state.m_score = 0
    
    m_questions = [
        {
            "question": "15 + 12 = ?",
            "options": ["A) 25", "B) 27", "C) 30", "D) 22"],
            "answer": "27",
            "image": "➕",
            "difficulty": "Salphoo",
            "audio": "Shanii kudhan lama walitti dabala"
        },
        {
            "question": "45 - 20 = ?",
            "options": ["A) 15", "B) 25", "C) 20", "D) 35"],
            "answer": "25",
            "image": "➖",
            "difficulty": "Salphoo",
            "audio": "Afurtamii shan keessaa digdama hir'isaa"
        },
        {
            "question": "6 × 7 = ?",
            "options": ["A) 36", "B) 42", "C) 48", "D) 54"],
            "answer": "42",
            "image": "✖️",
            "difficulty": "Giddugaleessa",
            "audio": "Jahaa torbaan baay'isaa"
        },
        {
            "question": "72 ÷ 8 = ?",
            "options": ["A) 8", "B) 9", "C) 7", "D) 10"],
            "answer": "9",
            "image": "➗",
            "difficulty": "Giddugaleessa",
            "audio": "Torbaatamii lama saddeet qoodaa"
        }
    ]
    
    mq = m_questions[st.session_state.m_index]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            🔢 Gaaffii: {st.session_state.m_index + 1} / {len(m_questions)}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            ⭐ Qabxii: {st.session_state.m_score}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="border-container">
        <div style="font-size: 60px; text-align: center;">{mq['image']}</div>
        <h4>Gaaffii {st.session_state.m_index + 1}:</h4>
        <p style="font-size: 24px; font-weight: bold;">{mq['question']}</p>
        <p style="color: #666; font-size: 14px;">⚠️ {mq['difficulty']}</p>
        <div style="background: #f0f0f0; padding: 15px; border-radius: 10px; margin: 10px 0;">
            {'  '.join(mq['options'])}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Audio hint
    if st.button("🔊 Sagalee Dhaggeeffachuuf", use_container_width=True):
        if play_audio(mq['audio']):
            st.success("🎧 Sagaleen dhaga'ameera!")
    
    m_ans = st.text_input("Deebii kee asitti barreessi (Fkn: 27 ykn B)", key="m_ans_input", placeholder="Deebii kee barreessi...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mirkaneessi Herregaa", use_container_width=True):
            if (m_ans.strip() == mq["answer"] or 
                (m_ans.strip().upper() == "B" and mq["answer"] in ["27", "42", "9"])):
                st.success(f"🎉 Jabaadhu {st.session_state.current_student}! Herregni sirriidha!")
                st.session_state.m_score += 10
                st.balloons()
            else:
                st.error(f"❌ {st.session_state.current_student}, dogoggora qaba! Mee irra deebi'iitii yaali.")
    
    with col2:
        if st.button("⏭️ Gaaffii Aanu / Xumuruu Herregaa", use_container_width=True):
            if st.session_state.m_index < len(m_questions) - 1:
                st.session_state.m_index += 1
                st.rerun()
            else:
                st.balloons()
                st.success(f"🏆 Galatoomi {st.session_state.current_student}! Qabxii herregaa waliigalaa: {st.session_state.m_score}")
    
    # Visual math helper
    st.markdown("### 🧮 Yoo barbaadde karoora (calculator) fayyadami:")
    if st.button("🧮 Karoora", use_container_width=True):
        st.info("Karoora herregaa fayyadamiitii shallaggi:")
        num1 = st.number_input("Lakkoofsa 1", value=0)
        num2 = st.number_input("Lakkoofsa 2", value=0)
        operation = st.selectbox("Filannoo", ["➕ Walitti dabala", "➖ Hanga", "✖️ Baay'isuu", "➗ Qooduu"])
        
        if operation == "➕ Walitti dabala":
            result = num1 + num2
            st.success(f"{num1} + {num2} = {result}")
        elif operation == "➖ Hanga":
            result = num1 - num2
            st.success(f"{num1} - {num2} = {result}")
        elif operation == "✖️ Baay'isuu":
            result = num1 * num2
            st.success(f"{num1} × {num2} = {result}")
        else:
            if num2 != 0:
                result = num1 / num2
                st.success(f"{num1} ÷ {num2} = {result}")
            else:
                st.error("❌ Qooduuf lakkoofsi 0 ta'uu hin danda'u!")
    
    st.divider()
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Page 6: Comprehensive Quiz
def quiz_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 15px;">
        <h3>📊 Qormaata Waliigalaa - {st.session_state.current_student}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0
    
    quiz_questions = [
        {
            "question": "Afaan Oromoon 'Water' maal jedhu?",
            "options": ["A) Bishaan", "B) Biyya", "C) Bosona", "D) Arba"],
            "answer": "A",
            "category": "Afaan",
            "audio": "Bishaan"
        },
        {
            "question": "7 + 8 = ?",
            "options": ["A) 12", "B) 15", "C) 18", "D) 21"],
            "answer": "B",
            "category": "Herregaa",
            "audio": "Torbayyii saddeet walitti dabala"
        },
        {
            "question": "Qubee 'A' jedhu jecha kamii eegala?",
            "options": ["A) Afaan", "B) Bishaan", "C) Cabbana", "D) Daraan"],
            "answer": "A",
            "category": "Afaan",
            "audio": "Afaan"
        },
        {
            "question": "30 - 15 = ?",
            "options": ["A) 10", "B) 12", "C) 15", "D) 20"],
            "answer": "C",
            "category": "Herregaa",
            "audio": "Soddoma keessaa kudhan shan hir'isaa"
        }
    ]
    
    q = quiz_questions[st.session_state.quiz_index]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            📊 Gaaffii: {st.session_state.quiz_index + 1} / {len(quiz_questions)}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            ⭐ Qabxii: {st.session_state.quiz_score}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="border-container">
        <p style="color: #666; font-size: 14px;">🏷️ {q['category']}</p>
        <h4>Gaaffii {st.session_state.quiz_index + 1}:</h4>
        <p style="font-size: 20px;">{q['question']}</p>
        <div style="background: #f0f0f0; padding: 15px; border-radius: 10px; margin: 10px 0;">
            {'  '.join(q['options'])}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔊 Sagalee Dhaggeeffachuuf", use_container_width=True):
        if play_audio(q['audio']):
            st.success("🎧 Sagaleen dhaga'ameera!")
    
    quiz_ans = st.text_input("Deebii kee asitti barreessi (Fkn: A)", key="quiz_ans_input", placeholder="Filannoo kee barreessi...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mirkaneessi Qormaata", use_container_width=True):
            if quiz_ans.strip().upper() == q["answer"]:
                st.success(f"🎉 Sirriidha {st.session_state.current_student}!")
                st.session_state.quiz_score += 10
                st.balloons()
            else:
                st.error(f"❌ {st.session_state.current_student}, deebiin sirrii miti!")
    
    with col2:
        if st.button("⏭️ Gaaffii Aanu", use_container_width=True):
            if st.session_state.quiz_index < len(quiz_questions) - 1:
                st.session_state.quiz_index += 1
                st.rerun()
            else:
                st.balloons()
                st.success(f"🏆 Galatoomi {st.session_state.current_student}! Qabxii waliigalaa: {st.session_state.quiz_score}")
                
                # Performance analysis
                total_possible = len(quiz_questions) * 10
                percentage = (st.session_state.quiz_score / total_possible) * 100
                
                if percentage >= 80:
                    st.balloons()
                    st.success("🌟 Akkaan gaarii! Barachuu kee cimaa! Galatoomi!")
                elif percentage >= 60:
                    st.info("📚 Fooca cimsuu barbaaduu dandeessa! Mee itti fufi!")
                else:
                    st.warning("⚡ Mee barachuu kee itti fufi! Siif hin rakkatu!")
    
    st.divider()
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Route Navigation
if st.session_state.page == "register":
    registration_page()
elif st.session_state.page == "home":
    home_page()
elif st.session_state.page == "reading":
    reading_page()
elif st.session_state.page == "writing":
    writing_page()
elif st.session_state.page == "math":
    math_page()
elif st.session_state.page == "quiz":
    quiz_page()
else:
    cover_page()
st.set_page_config(
    page_title="Hiika Way (HW)", 
    page_icon="📚", 
    layout="centered"
)

# Custom CSS for beautiful UI
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Card styling */
    .stButton > button {
        background: linear-gradient(to right, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 12px 24px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
        margin: 5px 0;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(0px);
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
    
    /* Input fields */
    .stTextInput > div > div > input {
        border-radius: 15px;
        border: 2px solid #667eea;
        padding: 10px 15px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #764ba2;
        box-shadow: 0 0 0 3px rgba(118, 75, 162, 0.3);
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    /* Cards for modules */
    .module-card {
        background: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 15px 0;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .module-card:hover {
        border-color: #667eea;
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.2);
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
    
    /* Balloon animation for celebration */
    .balloon-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 9999;
        overflow: hidden;
    }
    
    /* Audio player styling */
    .stAudio {
        border-radius: 20px;
        background: #f0f0f0;
        padding: 5px;
    }
    
    /* Border and shadow for containers */
    .border-container {
        border: 3px solid #667eea;
        border-radius: 25px;
        padding: 20px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
        background: white;
        margin: 15px 0;
    }
    
    /* Icon styling */
    .icon-large {
        font-size: 48px;
        text-align: center;
        margin: 10px 0;
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
    
    /* Cover page styling */
    .cover-page {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 50px 30px;
        border-radius: 30px;
        text-align: center;
        color: white;
        margin: 20px 0;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
    }
    
    .cover-page h1 {
        color: white !important;
        -webkit-text-fill-color: white !important;
        font-size: 48px;
        margin-bottom: 10px;
    }
    
    .cover-page h3 {
        color: rgba(255,255,255,0.9) !important;
        -webkit-text-fill-color: rgba(255,255,255,0.9) !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "students" not in st.session_state:
    st.session_state.students = []
if "current_student" not in st.session_state:
    st.session_state.current_student = None
if "page" not in st.session_state:
    st.session_state.page = "register"
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}
if "reading_audio" not in st.session_state:
    st.session_state.reading_audio = None

# Cover Page
def cover_page():
    st.markdown("""
    <div class="cover-page">
        <div style="font-size: 80px; margin-bottom: 20px;">📚</div>
        <h1>Hiika Way (HW)</h1>
        <h3>Galmee & Qormaata Barsiisaa</h3>
        <p style="font-size: 18px; margin-top: 20px; opacity: 0.9;">
            Barattoota afaan Oromoo, dubbisuu, barreessuu fi herregaa barachuu dandeessu!
        </p>
        <div style="margin-top: 30px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <span style="background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 20px;">📖 Dubbisuu</span>
            <span style="background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 20px;">✍️ Barreessuu</span>
            <span style="background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 20px;">🔢 Herregaa</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Galmee Barattootaatti Galchu", use_container_width=True):
        st.session_state.page = "register"
        st.rerun()

# Page 1: Student Registration (Hanga 80)
def registration_page():
    cover_page()
    
    st.subheader("📝 Galmee Barattoota Daree (Max 80)")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        name = st.text_input("Maqaa Barataa", placeholder="Maqaa guutuu barreessi...")
    with col2:
        student_id = st.text_input("ID (Lakk)", placeholder="Lakkoofsa ID")
    with col3:
        st.write("")
        st.write("")
        if st.button("➕ Galchi", use_container_width=True):
            if not name.strip():
                st.warning("⚠️ Mee maqaa barataa barreessi!")
            elif len(st.session_state.students) >= 80:
                st.warning("⚠️ Daree tokko keessatti barataan 80 guutameera!")
            else:
                sid = student_id.strip() if student_id.strip() else str(len(st.session_state.students) + 1)
                st.session_state.students.append({"id": sid, "name": name.strip()})
                st.success(f"✅ Barataan {name} milkaa'inaan galmaa'e!")
                st.rerun()
    
    st.markdown(f"""
    <div class="score-display">
        📊 Barattoota Galmaa'an: {len(st.session_state.students)} / 80
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    if not st.session_state.students:
        st.info("ℹ️ Ammaaf barataan galmaa'e hin jiru. Maqaa barataa galchaa!")
    else:
        for idx, st_data in enumerate(st.session_state.students):
            with st.container():
                col1, col2, col3, col4 = st.columns([1, 3, 1.5, 1])
                col1.markdown(f"**🆔 {st_data['id']}**")
                col2.markdown(f"**{st_data['name']}**")
                
                if col3.button("🚀 Jalqabi", key=f"start_{idx}", use_container_width=True):
                    st.session_state.current_student = st_data["name"]
                    st.session_state.page = "home"
                    st.rerun()
                
                if col4.button("🗑️ Haqi", key=f"del_{idx}", use_container_width=True):
                    st.session_state.students.pop(idx)
                    st.rerun()

# Page 2: Home Screen (Module Selection)
def home_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 20px;">
        <h2>👋 Baga nagaan dhufte, {st.session_state.current_student}!</h2>
        <p style="color: white; opacity: 0.9;">Damee barachuu barbaaddu filadhu:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Module Cards
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card" style="text-align: center;">
            <div class="icon-large">📖</div>
            <h3>Dubbisuu & Dhaggeeffachuu</h3>
            <p>Qubeewwan, jechoota, fi sagalee</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📖 Dubbisuu", use_container_width=True, key="read_btn"):
            st.session_state.page = "reading"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div class="module-card" style="text-align: center;">
            <div class="icon-large">✍️</div>
            <h3>Barreessuu & Qormaata</h3>
            <p>Barreessuu, hiikuu, fi qormaata</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("✍️ Barreessuu", use_container_width=True, key="write_btn"):
            st.session_state.page = "writing"
            st.rerun()
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="module-card" style="text-align: center;">
            <div class="icon-large">🔢</div>
            <h3>Herregaa</h3>
            <p>Shallaggaa, lakkoofsa, fi walitti bu'ii</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🔢 Herregaa", use_container_width=True, key="math_btn"):
            st.session_state.page = "math"
            st.rerun()
    
    with col4:
        st.markdown("""
        <div class="module-card" style="text-align: center;">
            <div class="icon-large">📊</div>
            <h3>Qormaata Waliigalaa</h3>
            <p>Dandeettiwwan cimsuu</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📊 Qormaata", use_container_width=True, key="quiz_btn"):
            st.session_state.page = "quiz"
            st.rerun()
    
    st.divider()
    if st.button("⬅️ Gara Galmee Barattootaatti Deebi'i", use_container_width=True):
        st.session_state.current_student = None
        st.session_state.page = "register"
        st.rerun()

# Page 3: Reading Module
def reading_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 15px;">
        <h3>📖 Dubbisuu - {st.session_state.current_student}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    lessons = [
        {
            "title": "Qubee A",
            "text": "A - Afaan (Red Apple)",
            "sound": "Qubee A sirriitti dubbifameera.",
            "image": "🍎",
            "letter": "A",
            "words": ["Afaan", "Adeemsa", "Arba"]
        },
        {
            "title": "Qubee B",
            "text": "B - Bishaan (Water)",
            "sound": "Qubee B sirriitti dubbifameera.",
            "image": "💧",
            "letter": "B",
            "words": ["Bishaan", "Biyya", "Bosona"]
        },
        {
            "title": "Jecha Bishaan",
            "text": "Bishaan - Water 💧",
            "sound": "Jechi Bishaan jedhu dhaga'amaa jira.",
            "image": "🌊",
            "letter": "B",
            "words": ["Bishaan", "Galaana", "Haroo"]
        }
    ]
    
    if "r_index" not in st.session_state:
        st.session_state.r_index = 0
    
    item = lessons[st.session_state.r_index]
    progress = (st.session_state.r_index + 1) / len(lessons)
    st.progress(progress)
    
    # Display content with styling
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        <div class="border-container">
            <h3>{item['image']} {item['title']}</h3>
            <p style="font-size: 24px; font-weight: bold;">{item['text']}</p>
            <p style="font-size: 18px; color: #667eea;">Qubee: {item['letter']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Show related words
        st.markdown("### 📝 Jechoota Waliin:")
        for word in item['words']:
            st.markdown(f"- {word}")
    
    with col2:
        st.markdown(f"""
        <div class="border-container" style="text-align: center;">
            <div style="font-size: 80px;">{item['image']}</div>
            <div style="font-size: 48px; font-weight: bold; margin: 10px 0;">{item['letter']}</div>
            <button style="background: #667eea; color: white; border: none; border-radius: 20px; padding: 10px 20px; margin-top: 10px;">
                🔊 Sagalee Dhaggeeffadhu
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    # Audio playback
    if st.button("🔊 Sagalee Dhaggeeffadhu", use_container_width=True):
        st.toast(f"🎧 {st.session_state.current_student}, {item['sound']}")
        # Play audio with natural voice simulation
        st.audio(item['sound'], format="audio/ogg")
    
    # Image-based questions
    st.markdown("### 🖼️ Gaaffii Suuraa")
    if st.button(f"Suura {item['image']} ilaali fi maqaa isaa barreessi:"):
        st.info("Maqaa suuraa barreessi:")
        answer = st.text_input("Deebii kee", key="img_answer")
        if st.button("Mirkaneessi", key="img_check"):
            if answer.strip().lower() == item['title'].lower():
                st.success("🎉 Sirriidha! Qabxii argatte!")
                st.session_state.quiz_score += 5
            else:
                st.error("❌ Mee irra deebi'iitii yaali!")
    
    # Navigation
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.r_index > 0:
            if st.button("⬅️ Duubatti", use_container_width=True):
                st.session_state.r_index -= 1
                st.rerun()
    with col2:
        if st.session_state.r_index < len(lessons) - 1:
            if st.button("➡️ Fuuldharatti", use_container_width=True):
                st.session_state.r_index += 1
                st.rerun()
    
    st.divider()
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Page 4: Writing Module
def writing_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 15px;">
        <h3>✍️ Barreessuu - {st.session_state.current_student}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if "w_index" not in st.session_state:
        st.session_state.w_index = 0
        st.session_state.w_score = 0
    
    questions = [
        {
            "prompt": "Jecha 'Bishaan' jedhu qubee sirriidhaan asitti barreessi:",
            "answer": "bishaan",
            "hint": "B + i + sh + aa + n",
            "image": "💧"
        },
        {
            "prompt": "Jecha 'Afaan' jedhu qubee meeqaani (kamii) eegala? (Fkn: a)",
            "answer": "a",
            "hint": "Afaan jechuun A eegala",
            "image": "🔤"
        },
        {
            "prompt": "Jecha 'Arba' jedhu qubee meeqaani eegala?",
            "answer": "a",
            "hint": "Arba jechuun A eegala",
            "image": "🐘"
        }
    ]
    
    q = questions[st.session_state.w_index]
    
    # Display score and progress
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            📝 Gaaffii: {st.session_state.w_index + 1} / {len(questions)}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            ⭐ Qabxii: {st.session_state.w_score}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="border-container">
        <div style="font-size: 40px; text-align: center;">{q['image']}</div>
        <h4>Gaaffii {st.session_state.w_index + 1}:</h4>
        <p style="font-size: 18px;">{q['prompt']}</p>
        <details>
            <summary>💡 Qorqaallii (Hint)</summary>
            <p>{q['hint']}</p>
        </details>
    </div>
    """, unsafe_allow_html=True)
    
    ans = st.text_input("Deebii kee asitti barreessi", key="w_ans_input", placeholder="Deebii kee barreessi...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mirkaneessi", use_container_width=True):
            if ans.strip().lower() == q["answer"]:
                st.success(f"🎉 Jabaadhu {st.session_state.current_student}! Sirriidha!")
                st.session_state.w_score += 10
                # Balloons for correct answer
                st.balloons()
            else:
                st.error(f"❌ {st.session_state.current_student}, dogoggora qaba! Mee irra deebi'iitii yaali.")
    
    with col2:
        if st.button("⏭️ Gaaffii Aanu / Xumuruu", use_container_width=True):
            if st.session_state.w_index < len(questions) - 1:
                st.session_state.w_index += 1
                st.rerun()
            else:
                st.balloons()
                st.success(f"🏆 Galatoomi {st.session_state.current_student}! Qabxii waliigalaa: {st.session_state.w_score}")
    
    # Writing practice with audio
    st.markdown("### 🎙️ Sagalee Ofii Dubbisuu")
    audio_value = st.audio_recorder("🔴 Sagalee kee galchi", key="audio_recorder")
    if audio_value:
        st.success("🎵 Sagaleen kee galmaa'eera!")
        st.audio(audio_value, format="audio/wav")
    
    st.divider()
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Page 5: Math Module
def math_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 15px;">
        <h3>🔢 Shallaggaa Herregaa - {st.session_state.current_student}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if "m_index" not in st.session_state:
        st.session_state.m_index = 0
        st.session_state.m_score = 0
    
    m_questions = [
        {
            "question": "15 + 12 = ?",
            "options": ["A) 25", "B) 27", "C) 30", "D) 22"],
            "answer": "27",
            "image": "➕",
            "difficulty": "Easy"
        },
        {
            "question": "45 - 20 = ?",
            "options": ["A) 15", "B) 25", "C) 20", "D) 35"],
            "answer": "25",
            "image": "➖",
            "difficulty": "Easy"
        },
        {
            "question": "6 × 7 = ?",
            "options": ["A) 36", "B) 42", "C) 48", "D) 54"],
            "answer": "42",
            "image": "✖️",
            "difficulty": "Medium"
        }
    ]
    
    mq = m_questions[st.session_state.m_index]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            🔢 Gaaffii: {st.session_state.m_index + 1} / {len(m_questions)}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            ⭐ Qabxii: {st.session_state.m_score}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="border-container">
        <div style="font-size: 60px; text-align: center;">{mq['image']}</div>
        <h4>Gaaffii {st.session_state.m_index + 1}:</h4>
        <p style="font-size: 24px; font-weight: bold;">{mq['question']}</p>
        <p style="color: #666; font-size: 14px;">⚠️ {mq['difficulty']}</p>
        <div style="background: #f0f0f0; padding: 15px; border-radius: 10px; margin: 10px 0;">
            {'  '.join(mq['options'])}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    m_ans = st.text_input("Deebii kee asitti barreessi (Fkn: 27 ykn B)", key="m_ans_input", placeholder="Deebii kee barreessi...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mirkaneessi Herregaa", use_container_width=True):
            if (m_ans.strip() == mq["answer"] or 
                (m_ans.strip().upper() == "B" and mq["answer"] == "27") or
                (m_ans.strip().upper() == "B" and mq["answer"] == "42")):
                st.success(f"🎉 Jabaadhu {st.session_state.current_student}! Herregni sirriidha!")
                st.session_state.m_score += 10
                st.balloons()
            else:
                st.error(f"❌ {st.session_state.current_student}, dogoggora qaba! Mee irra deebi'iitii yaali.")
    
    with col2:
        if st.button("⏭️ Gaaffii Aanu / Xumuruu Herregaa", use_container_width=True):
            if st.session_state.m_index < len(m_questions) - 1:
                st.session_state.m_index += 1
                st.rerun()
            else:
                st.balloons()
                st.success(f"🏆 Galatoomi {st.session_state.current_student}! Qabxii herregaa waliigalaa: {st.session_state.m_score}")
    
    # Visual math helper
    st.markdown("### 🧮 Yoo barbaadde karoora (calculator) fayyadami:")
    if st.button("🧮 Karoora", key="calc_btn"):
        st.info("Karoora herregaa fayyadamiitii shallaggi:")
        num1 = st.number_input("Lakkoofsa 1", value=0)
        num2 = st.number_input("Lakkoofsa 2", value=0)
        operation = st.selectbox("Filannoo", ["➕ Walitti dabala", "➖ Hanga", "✖️ Baay'isuu", "➗ Qooduu"])
        
        if operation == "➕ Walitti dabala":
            result = num1 + num2
            st.success(f"{num1} + {num2} = {result}")
        elif operation == "➖ Hanga":
            result = num1 - num2
            st.success(f"{num1} - {num2} = {result}")
        elif operation == "✖️ Baay'isuu":
            result = num1 * num2
            st.success(f"{num1} × {num2} = {result}")
        else:
            if num2 != 0:
                result = num1 / num2
                st.success(f"{num1} ÷ {num2} = {result}")
            else:
                st.error("❌ Qooduuf lakkoofsi 0 ta'uu hin danda'u!")
    
    st.divider()
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Page 6: Comprehensive Quiz
def quiz_page():
    st.markdown(f"""
    <div class="cover-page" style="padding: 15px;">
        <h3>📊 Qormaata Waliigalaa - {st.session_state.current_student}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0
    
    quiz_questions = [
        {
            "question": "Afaan Oromoon 'Water' maal jedhu?",
            "options": ["A) Bishaan", "B) Biyya", "C) Bosona", "D) Arba"],
            "answer": "A",
            "category": "Afaan"
        },
        {
            "question": "7 + 8 = ?",
            "options": ["A) 12", "B) 15", "C) 18", "D) 21"],
            "answer": "B",
            "category": "Herregaa"
        },
        {
            "question": "Qubee 'A' jedhu jecha kamii eegala?",
            "options": ["A) Afaan", "B) Bishaan", "C) Cabbana", "D) Daraan"],
            "answer": "A",
            "category": "Afaan"
        }
    ]
    
    q = quiz_questions[st.session_state.quiz_index]
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            📊 Gaaffii: {st.session_state.quiz_index + 1} / {len(quiz_questions)}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="score-display" style="font-size: 16px; padding: 10px;">
            ⭐ Qabxii: {st.session_state.quiz_score}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="border-container">
        <p style="color: #666; font-size: 14px;">🏷️ {q['category']}</p>
        <h4>Gaaffii {st.session_state.quiz_index + 1}:</h4>
        <p style="font-size: 20px;">{q['question']}</p>
        <div style="background: #f0f0f0; padding: 15px; border-radius: 10px; margin: 10px 0;">
            {'  '.join(q['options'])}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    quiz_ans = st.text_input("Deebii kee asitti barreessi (Fkn: A)", key="quiz_ans_input", placeholder="Filannoo kee barreessi...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Mirkaneessi Qormaata", use_container_width=True):
            if quiz_ans.strip().upper() == q["answer"]:
                st.success(f"🎉 Sirriidha {st.session_state.current_student}!")
                st.session_state.quiz_score += 10
                st.balloons()
            else:
                st.error(f"❌ {st.session_state.current_student}, deebiin sirrii miti!")
    
    with col2:
        if st.button("⏭️ Gaaffii Aanu", use_container_width=True):
            if st.session_state.quiz_index < len(quiz_questions) - 1:
                st.session_state.quiz_index += 1
                st.rerun()
            else:
                st.balloons()
                st.success(f"🏆 Galatoomi {st.session_state.current_student}! Qabxii waliigalaa: {st.session_state.quiz_score}")
                
                # Performance analysis
                if st.session_state.quiz_score >= 30:
                    st.balloons()
                    st.success("🌟 Akkaan gaarii! Barachuu kee cimaa! Galatoomi!")
                elif st.session_state.quiz_score >= 20:
                    st.info("📚 Fooca cimsuu barbaaduu dandeessa! Mee itti fufi!")
                else:
                    st.warning("⚡ Mee barachuu kee itti fufi! Siif hin rakkatu!")
    
    st.divider()
    if st.button("🏠 Gara Manayeessaa (Home)", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

# Route Navigation
if st.session_state.page == "register":
    registration_page()
elif st.session_state.page == "home":
    home_page()
elif st.session_state.page == "reading":
    reading_page()
elif st.session_state.page == "writing":
    writing_page()
elif st.session_state.page == "math":
    math_page()
elif st.session_state.page == "quiz":
    quiz_page()
else:
    cover_page()
