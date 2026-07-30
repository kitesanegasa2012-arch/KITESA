import streamlit as st

st.set_page_config(
    page_title="Hiika Way (HW)", page_icon="📚", layout="centered"
)

# Initialize Session State
if "students" not in st.session_state:
  st.session_state.students = []
if "current_student" not in st.session_state:
  st.session_state.current_student = None
if "page" not in st.session_state:import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Hiikaa Way (HW)", page_icon="📚", layout="centered"
)

# CUSTOM STYLING (Magariisa nama hawwatu, border fi background miidhagina UI)
st.markdown(
    """
    <style>
    .main {
        background-color: #F7F9FC;
    }
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px 20px;
        border: 2px solid #1B5E20;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #1B5E20;
        color: white;
        border-color: #0d3b12;
    }
    .hero-box {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #4caf50 100%);
        padding: 35px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 6px 20px rgba(46, 125, 50, 0.4);
        border: 2px solid #a5d6a7;
    }
    .card-box {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #c8e6c9;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Global data store for students and scores in Streamlit Session State
if "global_students" not in st.session_state:
  st.session_state.global_students = {}  # {name: {afaanOromoo, math, english}}
if "current_page" not in st.session_state:
  st.session_state.current_page = "role_selection"
if "current_student" not in st.session_state:
  st.session_state.current_student = ""


# ==========================================
# 1. ROLE SELECTION SCREEN
# ==========================================
def role_selection_screen():
  st.markdown(
      """
        <div class="hero-box">
            <h1>📚 Hiikaa Way (HW)</h1>
            <p style="font-size: 16px; margin-top: 10px;">
                Baga Nagaan Gara App dandeetti Dubbisuu, barreessuu fi shallaguu Hiika Way(HW) tti nagaan Dhuftan!<br>
                <b>Kalaqaan App kana: Kitesa Negasa</b>
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown("### Gatii Furtuu Filadhu:")

  col1, col2 = st.columns(2)
  with col1:
    if st.button("👤 Barataa (Student)"):
      st.session_state.current_page = "name_input"
      st.rerun()

  with col2:
    if st.button(
        "👨‍🏫 Barsiisaa (Teacher Report)",
        help="Gabaasa Excel ilaaluuf",
    ):
      st.session_state.current_page = "teacher_dashboard"
      st.rerun()


# ==========================================
# 2. NAME INPUT SCREEN
# ==========================================
def name_input_screen():
  st.markdown(
      """
        <div class="hero-box">
            <h2>Galmee Maqaa Barataa</h2>
            <p>Barataa, maaloo maqaa kee guutuu galchi</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  name = st.text_input("Maqaa Kee", placeholder="Maqaa kee guutuu barreessi...")

  col1, col2 = st.columns(2)
  with col1:
    if st.button("Gara Appiitti Darbi"):
      if name.strip():
        st.session_state.current_student = name.strip()
        if name.strip() not in st.session_state.global_students:
          st.session_state.global_students[name.strip()] = {
              "afaanOromoo": 0,
              "math": 0,
              "english": 0,
          }
        st.session_state.current_page = "home"
        st.rerun()
      else:
        st.warning("Mee dura maqaa kee barreessi!")
  with col2:
    if st.button("⬅️ Duubatti"):
      st.session_state.current_page = "role_selection"
      st.rerun()


# ==========================================
# 3. HOME SCREEN (3 GOSA BARNOOTAA)
# ==========================================
def home_screen():
  st.markdown(
      f"""
        <div class="hero-box">
            <h2>Baga nagaan dhuftte, {st.session_state.current_student}!</h2>
            <p>Gosa barnootaa barachuu barbaaddu filadhu</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  if st.button("📖 Afaan Oromoo (Qubee, Jechoota, Hima Jaala Abba)"):
    st.session_state.current_page = "afaan_oromoo"
    st.rerun()

  st.write("")
  if st.button("🔢 Herrega - Mathematics (Shallaggaa)"):
    st.session_state.current_page = "math"
    st.rerun()

  st.write("")
  if st.button("🔤 Ingliffaa - English (Grammar & Words)"):
    st.session_state.current_page = "english"
    st.rerun()

  st.markdown("---")
  if st.button("⬅️ Ba'uu / Maqaa Jijjiiruu"):
    st.session_state.current_student = ""
    st.session_state.current_page = "role_selection"
    st.rerun()


# ==========================================
# 4. AFAAN OROMOO MODULE
# ==========================================
def afaan_oromoo_screen():
  st.subheader(f"Afaan Oromoo - {st.session_state.current_student}")

  lessons = [
      {
          "title": "Qubee Afaan Oromoo Hunda (A - Z)",
          "text": (
              "Qubeewwan Afaan Oromoo 33:\nA B C CH D DH E F G H I J K L M N O P"
              " Q R S SH T U W X Y Z Z\nQubeewwan sagalee fi qubeessuuf baay'ee"
              " murteessoodha."
          ),
          "type": "info",
      },
      {
          "title": "Jechoota Laafaa (6)",
          "text": (
              "Jechoota laafaa 6: bofa, sadii, farda, qoraan, mana, harka.\nMaaloo"
              " jechoota kana irraa tokko barreessi ykn qabxii fudhu:"
          ),
          "type": "practice",
          "expected": ["bofa", "sadii", "farda", "qoraan", "mana", "harka"],
      },
      {
          "title": "Jechoota Gabaabaa (6)",
          "text": (
              "Jechoota gabaabaa 6: bishaan, buna, lafa, foon, irbuu, daadhii.\nMaaloo"
              " keessaa tokko barreessi:"
          ),
          "type": "practice",
          "expected": ["bishaan", "buna", "lafa", "foon", "irbuu", "daadhii"],
      },
      {
          "title": "Jechoota Dheeraa (6)",
          "text": (
              "Jechoota dheeraa 6: barumsaa, qorannoo, qopheessaa, abbootii,"
              " dandeettii, miidiyaa.\nMaaloo jecha tokko barreessi:"
          ),
          "type": "practice",
          "expected": [
              "barumsaa",
              "qorannoo",
              "qopheessaa",
              "abbootii",
              "dandeettii",
              "miidiyaa",
          ],
      },
      {
          "title": "Jechoota Jabaata (6)",
          "text": (
              "Jechoota jabaata 6: gabbataa, cufa, dhagaa, jajjabaa, qaxqaxaa,"
              " huffaa.\nMaaloo jecha tokko barreessi:"
          ),
          "type": "practice",
          "expected": [
              "gabbataa",
              "cufa",
              "dhagaa",
              "jajjabaa",
              "qaxqaxaa",
              "huffaa",
          ],
      },
      {
          "title": "Hima Wa'ee Jaala Abbaa (Father's Love)",
          "text": (
              "Hima waa'ee jaala abbaa:\n'Abbaan koo gaaddisa mana kooti;"
              " jaalalli abbaa humna fiabdii jireenyaati.'\nMaaloo caqasa kana"
              " irratti hundaa'uudhaan yaada kee barreessi:"
          ),
          "type": "practice",
          "expected": ["abbaan", "gaaddisa", "jaalalli", "humna", "jireenyaati"],
      },
  ]

  if "ao_index" not in st.session_state:
    st.session_state.ao_index = 0
    st.session_state.ao_score = 0
    st.session_state.ao_feedback = ""

  idx = st.session_state.ao_index
  item = lessons[idx]

  st.progress((idx + 1) / len(lessons))
  col1, col2 = st.columns([3, 1])
  col1.markdown(f"**{item['title']}**")
  col2.markdown(f"**Qabxii: {st.session_state.ao_score}**")

  st.info(item["text"])

  if item["type"] == "practice":
    ans = st.text_input("Deebii kee asitti barreessi", key=f"ao_input_{idx}")
    if st.button("Mirkaneessi"):
      if ans.strip().lower() in [e.lower() for e in item["expected"]] or len(
          ans.strip()
      ) > 2:
        st.session_state.ao_score += 10
        st.success("🎉 Galatoomi! Deebiin kee sirriidha.")
      else:
        st.error("❌ Mee yaada kee sirreessii deebisi.")

  st.markdown("---")
  b1, b2 = st.columns(2)
  with b1:
    if idx > 0 and st.button("Duubatti"):
      st.session_state.ao_index -= 1
      st.rerun()
  with b2:
    if idx < len(lessons) - 1:
      if st.button("Fuuldharatti"):
        st.session_state.ao_index += 1
        st.rerun()
    else:
      if st.button("Xumuruu & Galchuu"):
        st.session_state.global_students[st.session_state.current_student][
            "afaanOromoo"
        ] = st.session_state.ao_score
        st.success("Qabxiin Afaan Oromoo galmeeffameera!")
        st.session_state.ao_index = 0
        st.session_state.ao_score = 0
        st.session_state.current_page = "home"
        st.rerun()

  if st.button("🏠 Gara Manayeessaa (Home)"):
    st.session_state.ao_index = 0
    st.session_state.ao_score = 0
    st.session_state.current_page = "home"
    st.rerun()


# ==========================================
# 5. MATH MODULE
# ==========================================
def math_screen():
  st.subheader(f"Herrega - {st.session_state.current_student}")

  math_questions = [
      {
          "question": "15 + 12 = ?",
          "options": ["A) 25", "B) 27", "C) 30", "D) 22"],
          "answer": "27",
      },
      {
          "question": "45 - 20 = ?",
          "options": ["A) 15", "B) 25", "C) 20", "D) 35"],
          "answer": "25",
      },
      {
          "question": "6 × 4 = ?",
          "options": ["A) 24", "B) 18", "C) 28", "D) 20"],
          "answer": "24",
      },
      {
          "question": "50 ÷ 5 = ?",
          "options": ["A) 5", "B) 10", "C) 15", "D) 20"],
          "answer": "10",
      },
      {
          "question": "12 + 18 = ?",
          "options": ["A) 30", "B) 28", "C) 32", "D) 25"],
          "answer": "30",
      },
  ]

  if "m_index" not in st.session_state:
    st.session_state.m_index = 0
    st.session_state.m_score = 0

  idx = st.session_state.m_index
  q = math_questions[idx]

  c1, c2 = st.columns([3, 1])
  c1.markdown(f"**Gaaffii: {idx + 1} / {len(math_questions)}**")
  c2.markdown(f"**Qabxii: {st.session_state.m_score}**")

  st.markdown(
      f"### {q['question']}\n" + "  |  ".join([opt for opt in q["options"]])
  )
  m_ans = st.text_input("Deebii kee asitti barreessi (Fkn: 27)", key=f"m_in_{idx}")

  if st.button("Mirkaneessi Herregaa"):
    if (
        m_ans.strip() == q["answer"]
        or m_ans.strip().upper() == q["answer"][0]
        or m_ans.strip().upper() == "B"
        and q["answer"] == "27"
    ):
      st.session_state.m_score += 10
      st.success("🎉 Jabaadhu! Deebbiin sirriidha!")
    else:
      st.error(f"❌ Dogoggora qaba! Deebiin sirrii: {q['answer']}")

  st.markdown("---")
  if idx < len(math_questions) - 1:
    if st.button("Fuuldharatti"):
      st.session_state.m_index += 1
      st.rerun()
  else:
    if st.button("Xumuruu & Deebi'i"):
      st.session_state.global_students[st.session_state.current_student][
          "math"
      ] = st.session_state.m_score
      st.success(
          f"Galatoomi! Qabxii Herregaa waliigalaa: {st.session_state.m_score}"
      )
      st.session_state.m_index = 0
      st.session_state.m_score = 0
      st.session_state.current_page = "home"
      st.rerun()

  if st.button("🏠 Gara Manayeessaa (Home)"):
    st.session_state.m_index = 0
    st.session_state.m_score = 0
    st.session_state.current_page = "home"
    st.rerun()


# ==========================================
# 6. ENGLISH MODULE
# ==========================================
def english_screen():
  st.subheader(f"English - {st.session_state.current_student}")

  english_questions = [
      {
          "question": "What is the capital city of Ethiopia?",
          "options": ["A) Nairobi", "B) Addis Ababa", "C) Cairo", "D) Washington"],
          "answer": "Addis Ababa",
      },
      {
          "question": "Complete: Good ______!",
          "options": ["A) Morning", "B) Table", "C) Book", "D) Pen"],
          "answer": "Morning",
      },
      {
          "question": "Which one is a fruit?",
          "options": ["A) Potato", "B) Banana", "C) Carrot", "D) Onion"],
          "answer": "Banana",
      },
  ]

  if "e_index" not in st.session_state:
    st.session_state.e_index = 0
    st.session_state.e_score = 0

  idx = st.session_state.e_index
  q = english_questions[idx]

  c1, c2 = st.columns([3, 1])
  c1.markdown(f"**Question: {idx + 1} / {len(english_questions)}**")
  c2.markdown(f"**Score: {st.session_state.e_score}**")

  st.markdown(
      f"### {q['question']}\n" + "  |  ".join([opt for opt in q["options"]])
  )
  e_ans = st.text_input("Type your answer here", key=f"e_in_{idx}")

  if st.button("Check Answer"):
    if e_ans.strip().lower() in q["answer"].lower():
      st.session_state.e_score += 10
      st.success("🎉 Correct! Excellent job!")
    else:
      st.error(f"❌ Incorrect! Correct answer: {q['answer']}")

  st.markdown("---")
  if idx < len(english_questions) - 1:
    if st.button("Next"):
      st.session_state.e_index += 1
      st.rerun()
  else:
    if st.button("Finish & Return"):
      st.session_state.global_students[st.session_state.current_student][
          "english"
      ] = st.session_state.e_score
      st.success(f"Well done! Total English Score: {st.session_state.e_score}")
      st.session_state.e_index = 0
      st.session_state.e_score = 0
      st.session_state.current_page = "home"
      st.rerun()

  if st.button("🏠 Home"):
    st.session_state.e_index = 0
    st.session_state.e_score = 0
    st.session_state.current_page = "home"
    st.rerun()


# ==========================================
# 7. TEACHER DASHBOARD (EXCEL REPORT)
# ==========================================
def teacher_dashboard_screen():
  st.subheader("Gabaasa Barsiisaa (Excel Report - 100 Students)")
  st.markdown(
      "**Gosa Barnoota Sadii (Afaan Oromoo, Herrega, Ingliffaa) Qabxii"
      " Barattoota Daree**"
  )

  students = st.session_state.global_students
  st.write(f"**Baay'inni barattoota galmaa'an:** {len(students)}")

  if not students:
    st.info(
        "Ammaaf barataan galmaa'e hin jiru. Barataan yeroo appii fayyadamu asitti"
        " dhiyaata."
    )
  else:
    csv_data = "Maqaa Barataa,Afaan Oromoo,Herrega,Ingliffaa,Waliigala\n"
    for name, scores in students.items():
      total = scores["afaanOromoo"] + scores["math"] + scores["english"]
      csv_data += (
          f"{name},{scores['afaanOromoo']},{scores['math']},{scores['english']},"
          f"{total}\n"
      )
      st.markdown(
          f"""
            <div class="card-box">
                <b>👤 {name}</b><br>
                Afaan Oromoo: {scores['afaanOromoo']} | Herrega: {scores['math']} | Ingliffaa: {scores['english']}<br>
                <b>Waliigala: {total}</b>
            </div>
        """,
          unsafe_allow_html=True,
      )

    st.text_area("Gabaasa Excel (CSV Format)", csv_data, height=150)

  st.write("")
  if st.button("⬅️ Gara Furtuu Hojii (Role Selection) Deebi'i"):
    st.session_state.current_page = "role_selection"
    st.rerun()


# ROUTE CONTROLLER
if st.session_state.current_page == "role_selection":
  role_selection_screen()
elif st.session_state.current_page == "name_input":
  name_input_screen()
elif st.session_state.current_page == "home":
  home_screen()
elif st.session_state.current_page == "afaan_oromoo":
  afaan_oromoo_screen()
elif st.session_state.current_page == "math":
  math_screen()
elif st.session_state.current_page == "english":
  english_screen()
elif st.session_state.current_page == "teacher_dashboard":
  teacher_dashboard_screen()
    page_title="Hiika way (HW)", page_icon="📚", layout="centered"
)

# CUSTOM STYLING (Magariisa nama hawwatu fi miidhagina UI)
st.markdown(
    """
    <style>
    .main {
        background-color: #F7F9FC;
    }
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1B5E20;
        color: white;
    }
    .hero-box {
        background: linear-gradient(135deg, #2E7D32 0%, #66BB6A 100%);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(46, 125, 50, 0.3);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize Session States
if "students" not in st.session_state:
  st.session_state.students = []
if "current_student" not in st.session_state:
  st.session_state.current_student = None
if "page" not in st.session_state:
  st.session_state.page = "register"


# ==========================================
# 0. MAQAA BARATAA GALCHUU (NAME INPUT SCREEN)
# ==========================================
def registration_page():
  st.markdown(
      """
        <div class="hero-box">
            <h1>📚 Hiika way (HW)</h1>
            <p>Galmee Barattoota Daree fi Barnoota Interaktii (Max 80)</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.subheader("Galmee Barattoota Haaraa")

  col1, col2, col3 = st.columns([2, 1, 1])
  with col1:
    name = st.text_input("Maqaa Barataa", placeholder="Fkn: Abarraa")
  with col2:
    student_id = st.text_input("ID (Lakk)", placeholder="Fkn: 01")
  with col3:
    st.write("")
    st.write("")
    if st.button("Galchi", use_container_width=True):
      if not name.strip():
        st.warning("Mee maqaa barataa barreessi!")
      elif len(st.session_state.students) >= 80:
        st.warning("Daree tokko keessatti barataan 80 guutameera!")
      else:
        sid = (
            student_id.strip()
            if student_id.strip()
            else str(len(st.session_state.students) + 1)
        )
        st.session_state.students.append({"id": sid, "name": name.strip()})
        st.success(f"Barataan {name} milkaa'inaan galmaa'e!")
        st.rerun()

  st.markdown("---")
  st.markdown(
      f"**Barattoota Galmaa'an Hanga Ammaa:** {len(st.session_state.students)} /"
      " 80"
  )

  if not st.session_state.students:
    st.info("Ammaaf barataan galmaa'e hin jiru. Maqaa barataa olitti galchaa!")
  else:
    for idx, st_data in enumerate(st.session_state.students):
      cols = st.columns([1, 3, 2, 1])
      cols[0].markdown(f"**ID:** {st_data['id']}")
      cols[1].markdown(f"**{st_data['name']}**")
      if cols[2].button("Barachuu Jalqabi", key=f"start_{idx}"):
        st.session_state.current_student = st_data["name"]
        st.session_state.page = "home"
        st.rerun()
      if cols[3].button("Haqi", key=f"del_{idx}"):
        st.session_state.students.pop(idx)
        st.rerun()


# ==========================================
# 1. HOME SCREEN (MENU SELECTION)
# ==========================================
def home_page():
  st.markdown(
      f"""
        <div class="hero-box">
            <h2>Baga nagaan dhufte, {st.session_state.current_student}! 👋</h2>
            <p>Damee barachuu barbaaddu armaan gadii keessaa filadhu</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  if st.button(
      "📖 Dubbisuu & Dhaggeeffachuu (Reading Module)", use_container_width=True
  ):
    st.session_state.page = "reading"
    st.rerun()

  st.write("")
  if st.button(
      "✍️ Barreessuu & Qormaata (Writing Module)", use_container_width=True
  ):
    st.session_state.page = "writing"
    st.rerun()

  st.write("")
  if st.button("🔢 Shallaggaa Herregaa (Maths Module)", use_container_width=True):
    st.session_state.page = "math"
    st.rerun()

  st.markdown("---")
  if st.button("⬅️ Gara Galmee Barattootaatti Deebi'i"):
    st.session_state.current_student = None
    st.session_state.page = "register"
    st.rerun()


# ==========================================
# 2. DUBBISUU FI DHAGGEEFFACHUU (READING)
# ==========================================
def reading_page():
  st.subheader(f"📖 Dubbisuu - {st.session_state.current_student}")

  lessons = [
      {
          "title": "Qubee A",
          "text": "A - Afaan",
          "image": (
              "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.svg/1200px-Red_Apple.svg.png"
          ),
          "sound": "Qubee A sirriitti dubbifameera.",
      },
      {
          "title": "Jecha Bishaan",
          "text": "Bishaan - Water",
          "image": (
              "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Blue_Water_Drop.svg/1024px-Blue_Water_Drop.svg.png"
          ),
          "sound": "Jechi Bishaan jedhu dhaga'amaa jira.",
      },
  ]

  if "r_index" not in st.session_state:
    st.session_state.r_index = 0

  item = lessons[st.session_state.r_index]
  st.progress((st.session_state.r_index + 1) / len(lessons))

  st.markdown(f"### {item['title']}")
  st.image(item["image"], width=150)
  st.markdown(f"## {item['text']}")

  if st.button("🔊 Sagalee Dhaggeeffadhu"):
    st.toast(
        f"📢 {st.session_state.current_student}, {item['sound']}", icon="🔊"
    )

  st.markdown("---")
  col1, col2 = st.columns(2)
  with col1:
    if st.session_state.r_index > 0:
      if st.button("⬅️ Duubatti"):
        st.session_state.r_index -= 1
        st.rerun()
  with col2:
    if st.session_state.r_index < len(lessons) - 1:
      if st.button("Fuuldharatti ➡️"):
        st.session_state.r_index += 1
        st.rerun()

  st.write("")
  if st.button("🏠 Gara Manayeessaa (Home)"):
    st.session_state.page = "home"
    st.rerun()


# ==========================================
# 3. BARREESSUU FI QORMAATA (WRITING)
# ==========================================
def writing_page():
  st.subheader(f"✍️ Barreessuu - {st.session_state.current_student}")

  if "w_index" not in st.session_state:
    st.session_state.w_index = 0
    st.session_state.w_score = 0
    st.session_state.w_answered = False

  questions = [
      {
          "prompt": "Jecha 'Bishaan' jedhu qubee sirriidhaan asitti barreessi:",
          "answer": "bishaan",
      },
      {
          "prompt": (
              "Jecha 'Afaan' jedhu qubee meeqaani (kamii) eegala? (Fkn: a)"
          ),
          "answer": "a",
      },
  ]

  q = questions[st.session_state.w_index]

  col1, col2 = st.columns(2)
  col1.markdown(
      f"**Gaaffii:** {st.session_state.w_index + 1} / {len(questions)}"
  )
  col2.markdown(f"**Qabxii:** {st.session_state.w_score}")

  st.info(q["prompt"])

  ans = st.text_input("Deebii kee asitti barreessi", key="w_input")

  if st.button("Mirkaneessi (Check)") and not st.session_state.w_answered:
    if ans.strip().lower() == q["answer"]:
      st.session_state.w_score += 10
      st.success(
          f"🎉 Jabaadhu {st.session_state.current_student}! Galchiifteetta,"
          " sirriidha!"
      )
    else:
      st.error(
          f"❌ {st.session_state.current_student}, dogoggora qaba! Deebiin"
          f" sirrii: {q['answer']}"
      )
    st.session_state.w_answered = True

  st.markdown("---")
  if st.button("Gaaffii Aanu / Xumuruu"):
    if st.session_state.w_index < len(questions) - 1:
      st.session_state.w_index += 1
      st.session_state.w_answered = False
      st.rerun()
    else:
      st.balloons()
      st.success(
          f"🏆 Galatoomi {st.session_state.current_student}! Qabxii waliigalaa"
          f" kee: {st.session_state.w_score}"
      )

  st.write("")
  if st.button("🏠 Gara Manayeessaa (Home)"):
    st.session_state.page = "home"
    st.rerun()


# ==========================================
# 4. SHALLAGGAA HERREGAAN (MATH MODULE)
# ==========================================
def math_page():
  st.subheader(f"🔢 Shallaggaa Herregaa - {st.session_state.current_student}")

  if "m_index" not in st.session_state:
    st.session_state.m_index = 0
    st.session_state.m_score = 0
    st.session_state.m_answered = False

  math_questions = [
      {
          "question": "15 + 12 = ?",
          "options": ["A) 25", "B) 27", "C) 30", "D) 22"],
          "answer": "27",
      },
      {
          "question": "45 - 20 = ?",
          "options": ["A) 15", "B) 25", "C) 20", "D) 35"],
          "answer": "25",
      },
  ]

  mq = math_questions[st.session_state.m_index]

  col1, col2 = st.columns(2)
  col1.markdown(
      f"**Gaaffii:** {st.session_state.m_index + 1} / {len(math_questions)}"
  )
  col2.markdown(f"**Qabxii:** {st.session_state.m_score}")

  st.markdown(
      f"### {mq['question']}\n" + "  |  ".join([opt for opt in mq["options"]])
  )

  m_ans = st.text_input(
      "Deebii kee asitti barreessi (Fkn: 27 ykn B)", key="m_input"
  )

  if st.button("Mirkaneessi Herregaa") and not st.session_state.m_answered:
    if (
        m_ans.strip() == mq["answer"]
        or m_ans.strip().upper() == "B"
        and mq["answer"] == "27"
    ):
      st.session_state.m_score += 10
      st.success(
          f"🎉 Jabaadhu {st.session_state.current_student}! Herregni sirriidha!"
      )
    else:
      st.error(
          f"❌ {st.session_state.current_student}, dogoggora qaba! Deebiin"
          f" sirrii: {mq['answer']}"
      )
    st.session_state.m_answered = True

  st.markdown("---")
  if st.button("Gaaffii Aanu / Xumuruu Herregaa"):
    if st.session_state.m_index < len(math_questions) - 1:
      st.session_state.m_index += 1
      st.session_state.m_answered = False
      st.rerun()
    else:
      st.balloons()
      st.success(
          f"🏆 Galatoomi {st.session_state.current_student}! Qabxii herregaa"
          f" waliigalaa: {st.session_state.m_score}"
      )

  st.write("")
  if st.button("🏠 Gara Manayeessaa (Home)"):
    st.session_state.page = "home"
    st.rerun()


# ==========================================
# ROUTE NAVIGATION CONTROLLER
# ==========================================
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
  st.session_state.page = "register"

st.title("Hiika way (HW) - Galmee & Qormaata Barsiisaa")


# Page 1: Student Registration (Hanga 80)
def registration_page():
  st.subheader("Galmee Barattoota Daree (Max 80)")

  col1, col2, col3 = st.columns([2, 1, 1])
  with col1:
    name = st.text_input("Maqaa Barataa")
  with col2:
    student_id = st.text_input("ID (Lakk)")
  with col3:
    st.write("")
    st.write("")
    if st.button("Galchi"):
      if not name.strip():
        st.warning("Mee maqaa barataa barreessi!")
      elif len(st.session_state.students) >= 80:
        st.warning("Daree tokko keessatti barataan 80 guutameera!")
      else:
        sid = (
            student_id.strip()
            if student_id.strip()
            else str(len(st.session_state.students) + 1)
        )
        st.session_state.students.append({"id": sid, "name": name.strip()})
        st.success(f"Barataan {name} milkaa'inaan galmaa'e!")
        st.rerun()

  st.write(f"**Barattoota Galmaa'an:** {len(st.session_state.students)} / 80")
  st.divider()

  if not st.session_state.students:
    st.info("Ammaaf barataan galmaa'e hin jiru. Maqaa barataa galchaa!")
  else:
    for idx, st_data in enumerate(st.session_state.students):
      cols = st.columns([1, 3, 2, 1])
      cols[0].write(f"ID: {st_data['id']}")
      cols[1].write(f"**{st_data['name']}**")
      if cols[2].button("Jalqabi", key=f"start_{idx}"):
        st.session_state.current_student = st_data["name"]
        st.session_state.page = "home"
        st.rerun()
      if cols[3].button("Haqi", key=f"del_{idx}"):
        st.session_state.students.pop(idx)
        st.rerun()


# Page 2: Home Screen (Module Selection)
def home_page():
  st.subheader(f"Baga nagaan dhufte, {st.session_state.current_student}!")
  st.write("Damee barachuu barbaaddu filadhu:")

  if st.button("📖 Dubbisuu & Dhaggeeffachuu (Reading)", use_container_width=True):
    st.session_state.page = "reading"
    st.rerun()
  if st.button("✍️ Barreessuu & Qormaata (Writing)", use_container_width=True):
    st.session_state.page = "writing"
    st.rerun()
  if st.button(
      "🔢 Shallaggaa Herregaa (Maths Module)", use_container_width=True
  ):
    st.session_state.page = "math"
    st.rerun()

  st.divider()
  if st.button("⬅️ Gara Galmee Barattootaatti Deebi'i"):
    st.session_state.current_student = None
    st.session_state.page = "register"
    st.rerun()


# Page 3: Reading Module
def reading_page():
  st.subheader(f"Dubbisuu - {st.session_state.current_student}")
  lessons = [
      {
          "title": "Qubee A",
          "text": "A - Afaan (Red Apple)",
          "sound": "Qubee A sirriitti dubbifameera.",
      },
      {
          "title": "Jecha Bishaan",
          "text": "Bishaan - Water",
          "sound": "Jechi Bishaan jedhu dhaga'amaa jira.",
      },
  ]

  if "r_index" not in st.session_state:
    st.session_state.r_index = 0

  item = lessons[st.session_state.r_index]
  st.progress((st.session_state.r_index + 1) / len(lessons))
  st.markdown(f"### {item['title']}")
  st.info(item["text"])

  if st.button("🔊 Sagalee Dhaggeeffadhu"):
    st.toast(f"{st.session_state.current_student}, {item['sound']}")

  col1, col2 = st.columns(2)
  with col1:
    if st.session_state.r_index > 0:
      if st.button("Duubatti"):
        st.session_state.r_index -= 1
        st.rerun()
  with col2:
    if st.session_state.r_index < len(lessons) - 1:
      if st.button("Fuuldharatti"):
        st.session_state.r_index += 1
        st.rerun()

  st.write("")
  if st.button("🏠 Gara Manayeessaa (Home)"):
    st.session_state.page = "home"
    st.rerun()


# Page 4: Writing Module
def writing_page():
  st.subheader(f"Barreessuu - {st.session_state.current_student}")
  if "w_index" not in st.session_state:
    st.session_state.w_index = 0
    st.session_state.w_score = 0

  questions = [
      {
          "prompt": "Jecha 'Bishaan' jedhu qubee sirriidhaan asitti barreessi:",
          "answer": "bishaan",
      },
      {
          "prompt": (
              "Jecha 'Afaan' jedhu qubee meeqaani (kamii) eegala? (Fkn: a)"
          ),
          "answer": "a",
      },
  ]

  q = questions[st.session_state.w_index]
  st.write(
      f"Gaaffii: {st.session_state.w_index + 1} / {len(questions)}  |  Qabxii:"
      f" {st.session_state.w_score}"
  )
  st.info(q["prompt"])

  ans = st.text_input("Deebii kee asitti barreessi", key="w_ans_input")
  if st.button("Mirkaneessi"):
    if ans.strip().lower() == q["answer"]:
      st.success(f"🎉 Jabaadhu {st.session_state.current_student}! Sirriidha!")
      st.session_state.w_score += 10
    else:
      st.error(
          f"❌ {st.session_state.current_student}, dogoggora qaba! Mee irra"
          " deebi'iitii yaali."
      )

  if st.button("Gaaffii Aanu / Xumuruu"):
    if st.session_state.w_index < len(questions) - 1:
      st.session_state.w_index += 1
      st.rerun()
    else:
      st.balloons()
      st.success(
          f"🏆 Galatoomi {st.session_state.current_student}! Qabxii waliigalaa:"
          f" {st.session_state.w_score}"
      )

  st.write("")
  if st.button("🏠 Gara Manayeessaa (Home)"):
    st.session_state.page = "home"
    st.rerun()


# Page 5: Math Module
def math_page():
  st.subheader(f"Shallaggaa Herregaa - {st.session_state.current_student}")
  if "m_index" not in st.session_state:
    st.session_state.m_index = 0
    st.session_state.m_score = 0

  m_questions = [
      {
          "question": "15 + 12 = ?",
          "options": ["A) 25", "B) 27", "C) 30", "D) 22"],
          "answer": "27",
      },
      {
          "question": "45 - 20 = ?",
          "options": ["A) 15", "B) 25", "C) 20", "D) 35"],
          "answer": "25",
      },
  ]

  mq = m_questions[st.session_state.m_index]
  st.write(
      f"Gaaffii: {st.session_state.m_index + 1} / {len(m_questions)}  |  Qabxii:"
      f" {st.session_state.m_score}"
  )
  st.info(f"**{mq['question']}**\n\n" + "  ".join(mq["options"]))

  m_ans = st.text_input(
      "Deebii kee asitti barreessi (Fkn: 27 ykn B)", key="m_ans_input"
  )
  if st.button("Mirkaneessi Herregaa"):
    if (
        m_ans.strip() == mq["answer"]
        or m_ans.strip().upper() == "B"
        and mq["answer"] == "27"
    ):
      st.success(
          f"🎉 Jabaadhu {st.session_state.current_student}! Herregni sirriidha!"
      )
      st.session_state.m_score += 10
    else:
      st.error(
          f"❌ {st.session_state.current_student}, dogoggora qaba! Mee irra"
          " deebi'iitii yaali."
      )

  if st.button("Gaaffii Aanu / Xumuruu Herregaa"):
    if st.session_state.m_index < len(m_questions) - 1:
      st.session_state.m_index += 1
      st.rerun()
    else:
      st.balloons()
      st.success(
          f"🏆 Galatoomi {st.session_state.current_student}! Qabxii herregaa"
          f" waliigalaa: {st.session_state.m_score}"
      )

  st.write("")
  if st.button("🏠 Gara Manayeessaa (Home)"):
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
