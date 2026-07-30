import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Hiika Way (HW) App", page_icon="📚", layout="centered"
)

# CUSTOM STYLING (Magariisa nama hawwatu, border fi background miidhagina UI)
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    }
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 14px 22px;
        border: 2px solid #1B5E20;
        width: 100%;
        box-shadow: 0 4px 10px rgba(46, 125, 50, 0.3);
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1B5E20;
        color: white;
        border-color: #0d3b12;
        box-shadow: 0 6px 15px rgba(27, 94, 32, 0.4);
    }
    .hero-box {
        background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 50%, #4caf50 100%);
        padding: 45px 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(46, 125, 50, 0.4);
        border: 3px solid #a5d6a7;
    }
    .hero-box h1 {
        font-size: 2.2rem;
        margin-bottom: 15px;
        font-weight: 800;
        letter-spacing: 1px;
    }
    .hero-box p {
        font-size: 1.15rem;
        line-height: 1.6;
        color: #f1f8e9;
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
# 1. ROLE SELECTION SCREEN (FUULA JALQABAA)
# ==========================================
def role_selection_screen():
  st.markdown(
      """
        <div class="hero-box">
            <h1>📚 Hiika Way (HW) APP</h1>
            <p>
                Baga Nagaan Gara app Dandeettii Dubbisuu, barreessuu Fi shallaguu Barattootaa Adda baasu Hiika Way itti Nagaan Dhuftan!<br><br>
                <b>Created by Kitesa Negasa Feyisa</b>
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  st.markdown(
      "<h3 style='text-align: center; color: #1b5e20; margin-bottom:"
      " 20px;'>Gatii Furtuu Filadhu:</h3>",
      unsafe_allow_html=True,
  )

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
