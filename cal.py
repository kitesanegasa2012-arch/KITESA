import streamlit as st

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Hiika Way (HW) App", page_icon="📖", layout="centered"
)

# CUSTOM STYLING (Background, Border, and Cover Page UI Enhancements)
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
    }
    
    /* Student Button: Blue */
    .stButton:nth-of-type(1) > button, div.stButton > button[kind="secondary"] {
        background-color: #1976D2;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 14px 22px;
        border: 2px solid #0d47a1;
        width: 100%;
        box-shadow: 0 4px 10px rgba(25, 118, 210, 0.3);
        transition: 0.3s ease;
    }
    .stButton:nth-of-type(1) > button:hover {
        background-color: #0d47a1;
        color: white;
        border-color: #002171;
        box-shadow: 0 6px 15px rgba(13, 71, 161, 0.4);
    }

    /* Teacher Button: Purple */
    .teacher-btn button {
        background-color: #7B1FA2;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 14px 22px;
        border: 2px solid #4a148c;
        width: 100%;
        box-shadow: 0 4px 10px rgba(123, 31, 162, 0.3);
        transition: 0.3s ease;
    }
    .teacher-btn button:hover {
        background-color: #4a148c;
        color: white;
        border-color: #311b92;
        box-shadow: 0 6px 15px rgba(74, 20, 140, 0.4);
    }

    /* General Button Styling fallback */
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
        background: linear-gradient(135deg, #004d40 0%, #00695c 50%, #00897b 100%);
        padding: 45px 30px;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 25px rgba(0, 77, 64, 0.4);
        border: 3px solid #80cbc4;
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
        color: #e0f2f1;
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

# Global data store for students, grades (1-6), and scores in Session State
if "global_students" not in st.session_state:
  st.session_state.global_students = {}
if "current_page" not in st.session_state:
  st.session_state.current_page = "role_selection"
if "current_student" not in st.session_state:
  st.session_state.current_student = ""
if "current_grade" not in st.session_state:
  st.session_state.current_grade = "Kutaa 1"

# Track attempt counts per question (max 3 attempts, 3rd attempt saves/locks)
if "attempts" not in st.session_state:
  st.session_state.attempts = {}


# ==========================================
# 1. ROLE SELECTION SCREEN (COVER PAGE WITH BOOK ICON & IMAGE)
# ==========================================
def role_selection_screen():
  st.markdown(
      """
        <div class="hero-box">
            <h1>📖 Hiika Way (HW) APP</h1>
            <p>
                Baga Nagaan Gara App Dandeettii Dubbisuu, Barreessuu Fi Shallaguu Barattootaa Adda Baasu Hiika Way itti Nagaan Dhuftan!<br><br>
                <b>App kanaaf: Kutaa 1 - Kutaa 6 (Afaan Oromoo, Herrega, Ingliffaa)</b><br>
                <b>Created by Kitesa Negasa Feyisa</b>
            </p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  # Displaying a textbook image representing student learning materials
  st.image(
      "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=800&q=80",
      caption="Kitaabota Barattootaa Kutaa 1 - 6",
      use_container_width=True,
  )

  st.markdown(
      "<h3 style='text-align: center; color: #004d40; margin-top: 20px;"
      " margin-bottom: 20px;'>🔑 Furtuu Filadhu:</h3>",
      unsafe_allow_html=True,
  )

  col1, col2 = st.columns(2)
  with col1:
    st.markdown("👤 **Barataa (Student)**")
    if st.button("🔑 Seeni (Barataa)", key="student_btn"):
      st.session_state.current_page = "name_input"
      st.rerun()

  with col2:
    st.markdown("🎓 **Barsiisaa (Teacher)**")
    # Using an image of a person wearing a graduation gown/robe (academic gown) for the teacher icon
    st.image(
        "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=200&q=80",
        width=80,
    )
    st.markdown('<div class="teacher-btn">', unsafe_allow_html=True)
    if st.button("📊 Gabaasa Barsiisaa", key="teacher_btn"):
      st.session_state.current_page = "teacher_dashboard"
      st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# 2. NAME & GRADE INPUT SCREEN
# ==========================================
def name_input_screen():
  st.markdown(
      """
        <div class="hero-box">
            <h2>Galmee Maqaa & Kutaa Barataa</h2>
            <p>Maaloo maqaa kee guutuu fi kutaa kee filadhu</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  name = st.text_input("Maqaa Kee", placeholder="Maqaa kee guutuu barreessi...")
  grade = st.selectbox(
      "Kutaa Barumsaa (Grade 1 - 6)",
      ["Kutaa 1", "Kutaa 2", "Kutaa 3", "Kutaa 4", "Kutaa 5", "Kutaa 6"],
  )

  col1, col2 = st.columns(2)
  with col1:
    if st.button("Gara Appiitti Darbi"):
      if name.strip():
        st.session_state.current_student = name.strip()
        st.session_state.current_grade = grade
        if name.strip() not in st.session_state.global_students:
          st.session_state.global_students[name.strip()] = {
              "grade": grade,
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
            <h2>Baga nagaan dhuftte, {st.session_state.current_student} ({st.session_state.current_grade})!</h2>
            <p>Gosa barnootaa barachuu barbaaddu filadhu</p>
        </div>
    """,
      unsafe_allow_html=True,
  )

  if st.button(
      "📖 Afaan Oromoo (Dubbisuu, Qubee, Jechoota, Hiika & Caqasa)"
  ):
    st.session_state.current_page = "afaan_oromoo"
    st.rerun()

  st.write("")
  if st.button("🔢 Herrega - Mathematics (Shallaggaa fi Rakkoo Hiikuu)"):
    st.session_state.current_page = "math"
    st.rerun()

  st.write("")
  if st.button("🔤 Ingliffaa - English (Reading, Grammar & Vocabulary)"):
    st.session_state.current_page = "english"
    st.rerun()

  st.markdown("---")
  if st.button("⬅️ Ba'uu / Maqaa Jijjiiruu"):
    st.session_state.current_student = ""
    st.session_state.current_page = "role_selection"
    st.rerun()


# ==========================================
# 4. AFAAN OROMOO MODULE (Grades 1-6)
# ==========================================
def afaan_oromoo_screen():
  grade = st.session_state.current_grade
  st.subheader(f"Afaan Oromoo - {grade} ({st.session_state.current_student})")

  ao_db = {
      "Kutaa 1": [
          {
              "type": "reading",
              "title": "Dubbisa 1: Harmee Koo",
              "text": (
                  "Harmeen koo bultii keenyaaf cufa dabarsiti. Inni sun"
                  " jaalala guddaadha. Harmeen harka qabdee nu barsiifti."
              ),
              "question": (
                  "Gaaffii Dubbisaa: Harmeen maaliin nu barsiifti? (Deebii"
                  " gabaabaa barreessi)"
              ),
              "expected": ["harka", "harka qabdee", "jaalala"],
          },
          {
              "type": "mcq",
              "title": "Qubee fi Jechoota Laafaa",
              "text": "Qubee Afaan Oromoo keessaa qubeen laafaa isa kam?",
              "options": ["A) c", "B) b", "C) q", "D) x"],
              "answer": "B",
          },
      ],
      "Kutaa 2": [
          {
              "type": "reading",
              "title": "Dubbisa 2: Beeylada Manaa",
              "text": (
                  "Beeylada manaa keessaa loon, re'ee fi hoolaan ni argamu."
                  " Isaanis nyaata nuu kennu."
              ),
              "question": (
                  "Gaaffii Dubbisaa: Beeyladni manaa maal nuu kennu?"
              ),
              "expected": ["nyaata", "aanan", "foniin"],
          },
          {
              "type": "mcq",
              "title": "Jechoota Gabaabaa",
              "text": "Jechi 'bishaan' jedhu gosa maaliiti?",
              "options": [
                  "A) Jecha gabaabaa",
                  "B) Jecha dheeraa",
                  "C) Qubee",
                  "D) Lakkoofsa",
              ],
              "answer": "A",
          },
      ],
      "Kutaa 3": [
          {
              "type": "reading",
              "title": "Dubbisa 3: Qonna Biyya Keenyaa",
              "text": (
                  "Qonnaan bultootni keenya bonaaf ganna midhaan facaasuun"
                  " biyya nyaachisu. Qonnaan ooluun kabaja guddaadha."
              ),
              "question": (
                  "Gaaffii Dubbisaa: Qonnaan bultootni yoom midhaan facaasu?"
              ),
              "expected": ["bonaaf ganna", "bona fi ganna", "ganna"],
          },
          {
              "type": "mcq",
              "title": "Gaalee fi Himoota",
              "text": "Hima sirrii ta'e isa kam?",
              "options": [
                  "A) Mana deemna nuyi.",
                  "B) Nuyi gara manaatti deemna.",
                  "C) Deemna nuyi mana.",
                  "D) Mana nuyi deemna.",
              ],
              "answer": "B",
          },
      ],
      "Kutaa 4": [
          {
              "type": "reading",
              "title": "Dubbisa 4: Beekumsa Aadaa Oromoo",
              "text": (
                  "Gadaan sirna bulchiinsa dimokraasii durii ti. Inni"
                  " dhugaa, walqixxummaa fi nagaaf dhaabata."
              ),
              "question": "Gaaffii Dubbisaa: Gadaan sirna maalii ti?",
              "options": [
                  "A) Bulchiinsa dimokraasii",
                  "B) Waraanaa",
                  "C) Daldala qofa",
                  "D) Ispoortii",
              ],
              "answer": "A",
          },
          {
              "type": "mcq",
              "title": "Qama Hiika Jechootaa",
              "text": "Hiika jecha 'Goota' jedhuu isa kam?",
              "options": ["A) Sodaataa", "B) Jabduu/Cicha", "C) Damaqaa", "D) Lafa"],
              "answer": "B",
          },
      ],
      "Kutaa 5": [
          {
              "type": "reading",
              "title": "Dubbisa 5: Seenaa fi Ogbarruu",
              "text": (
                  "Oggbarruun Afaan Oromoo afoola keessaa mammaaksa, hibboo fi"
                  " weedduu qabateesoo dhalootaa dhalootatti darbe."
              ),
              "question": "Gaaffii Dubbisaa: Afoolli maal of keessaa qaba?",
              "options": [
                  "A) Mammaaksa, hibboo fi weedduu",
                  "B) Herrega qofa",
                  "C) Seera lakkoofsaa",
                  "D) Faayinaansii",
              ],
              "answer": "A",
          },
          {
              "type": "mcq",
              "title": "Ergaa Mammaaksaa",
              "text": "Mammaaksi 'Harka tokkoon qilleensi hin qabamne' maal ibsa?",
              "options": [
                  "A) Tokkummaan humna ta'uu",
                  "B) Qilleensa qabachuu",
                  "C) Kophaa deemuu",
                  "D) Humna dhabuu",
              ],
              "answer": "A",
          },
      ],
      "Kutaa 6": [
          {
              "type": "reading",
              "title": "Dubbisa 6: Xiinsammuu fi Hojii Gamtaa",
              "text": (
                  "Hojjiin gamtaa milkaa'ina fida. Namoonni waliin hojjetan"
                  " rakkoo salphaatti injifatu."
              ),
              "question": "Gaaffii Dubbisaa: Hojjiin gamtaa maal fida?",
              "expected": ["milkaa'ina", "milkaa ina", "injifannoo"],
          },
          {
              "type": "mcq",
              "title": "Qeeqqa Barruu",
              "text": "Barruu keessatti 'Milkaa'ina' jechuun hiika maal qaba?",
              "options": [
                  "A) Kufaatii",
                  "B) Galma ga'uu",
                  "C) Daddaffii",
                  "D) Boqonnaa",
              ],
              "answer": "B",
          },
      ],
  }

  questions = ao_db.get(grade, ao_db["Kutaa 1"])

  if "ao_index" not in st.session_state:
    st.session_state.ao_index = 0
    st.session_state.ao_score = 0

  idx = st.session_state.ao_index
  q = questions[idx]

  st.progress((idx + 1) / len(questions))
  c1, c2 = st.columns([3, 1])
  c1.markdown(f"**Gaaffii {idx + 1} / {len(questions)} : {q['title']}**")
  c2.markdown(f"**Qabxii: {st.session_state.ao_score}**")

  if q["type"] == "reading" and "text" in q:
    st.markdown(
        f"""
            <div style="background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 15px;">
                <b>📚 Qajeelfama Dubbisuu:</b><br>{q['text']}
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown(f"### {q.get('question', q.get('text'))}")

  if "options" in q:
    for opt in q["options"]:
      st.write(opt)

  attempt_key = ("afaan_oromoo", grade, idx)
  if attempt_key not in st.session_state.attempts:
    st.session_state.attempts[attempt_key] = 0

  current_attempts = st.session_state.attempts[attempt_key]
  st.write(
      f"⚠️ Carraa deebii yaaluu: **{current_attempts} / 3** (Carraan 3ffaan"
      " ni kuusama/save ta'a)"
  )

  ans = st.text_input("Deebii kee asitti barreessi:", key=f"ao_ans_{grade}_{idx}")

  if st.button("Mirkaneessi Afaan Oromoo"):
    if current_attempts < 3:
      st.session_state.attempts[attempt_key] += 1
      is_correct = False

      if "answer" in q:
        if (
            ans.strip().upper() == q["answer"]
            or ans.strip().lower() == q["answer"].lower()
        ):
          is_correct = True
      elif "expected" in q:
        if any(exp in ans.strip().lower() for exp in q["expected"]):
          is_correct = True

      if is_correct:
        st.session_state.ao_score += 10
        st.success("🎉 Sirriitti deebiste, Foyyee qabda, Si hafa!")
        st.session_state.attempts[attempt_key] = 3
      else:
        rem = 3 - st.session_state.attempts[attempt_key]
        if rem > 0:
          st.warning(
              f"❌ Dogoggora! Ammas yaali. Carraan hafe: {rem} (Carraan"
              " 3ffaan ni kuusama)"
          )
        else:
          st.error(
              "❌ Carraan 3ffaan xumurameera. Deebiin sirrii kuufameera (0"
              " qabxii carraa kanaaf)."
          )
    else:
      st.info("Barataan carraa 3 guutee xumureera.")

  st.markdown("---")
  b1, b2 = st.columns(2)
  with b1:
    if idx > 0 and st.button("⬅️ Duubatti (Previous)"):
      st.session_state.ao_index -= 1
      st.rerun()
  with b2:
    if idx < len(questions) - 1:
      if st.button("Fuuldharatti (Next) ➡️"):
        st.session_state.ao_index += 1
        st.rerun()
    else:
      if st.button("Xumuruu & Galchuu"):
        st.session_state.global_students[st.session_state.current_student][
            "afaanOromoo"
        ] = st.session_state.ao_score
        st.success("Qabxiin Afaan Oromoo guutuu galmeeffameera!")
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
# 5. MATH MODULE (Grades 1-6)
# ==========================================
def math_screen():
  grade = st.session_state.current_grade
  st.subheader(f"Herrega - {grade} ({st.session_state.current_student})")

  math_db = {
      "Kutaa 1": [
          {
              "question": "8 + 7 = ?",
              "options": ["A) 14", "B) 15", "C) 16", "D) 13"],
              "answer": "15",
          },
          {
              "question": "10 - 4 = ?",
              "options": ["A) 5", "B) 6", "C) 7", "D) 4"],
              "answer": "6",
          },
      ],
      "Kutaa 2": [
          {
              "question": "25 + 34 = ?",
              "options": ["A) 59", "B) 58", "C) 69", "D) 55"],
              "answer": "59",
          },
          {
              "question": "50 - 18 = ?",
              "options": ["A) 32", "B) 34", "C) 22", "D) 42"],
              "answer": "32",
          },
      ],
      "Kutaa 3": [
          {
              "question": "14 × 3 = ?",
              "options": ["A) 42", "B) 38", "C) 44", "D) 36"],
              "answer": "42",
          },
          {
              "question": "72 ÷ 8 = ?",
              "options": ["A) 8", "B) 9", "C) 7", "D) 6"],
              "answer": "9",
          },
      ],
      "Kutaa 4": [
          {
              "question": "1/2 + 1/4 = ?",
              "options": ["A) 3/4", "B) 2/6", "C) 1/6", "D) 2/4"],
              "answer": "3/4",
          },
          {
              "question": "150 + 275 - 125 = ?",
              "options": ["A) 300", "B) 250", "C) 275", "D) 320"],
              "answer": "300",
          },
      ],
      "Kutaa 5": [
          {
              "question": "0.5 + 3/4 = ? (Deebii lakkoofsa decimal/fraction)",
              "options": ["A) 1.25", "B) 1.5", "C) 0.75", "D) 1.1"],
              "answer": "1.25",
          },
          {
              "question": (
                  "Pariimerii hirdhicha (rectangle) dheerinni 10cm, bal'inni"
                  " 5cm hammami?"
              ),
              "options": ["A) 30cm", "B) 50cm", "C) 15cm", "D) 25cm"],
              "answer": "30cm",
          },
      ],
      "Kutaa 6": [
          {
              "question": "L.C.M of 6 and 8 = ?",
              "options": ["A) 24", "B) 48", "C) 12", "D) 18"],
              "answer": "24",
          },
          {
              "question": (
                  "Hangi oowwii 20% dabaluun 60 ta'e, jalqaba hammami ture?"
              ),
              "options": ["A) 50", "B) 48", "C) 55", "D) 45"],
              "answer": "50",
          },
      ],
  }

  questions = math_db.get(grade, math_db["Kutaa 1"])

  if "m_index" not in st.session_state:
    st.session_state.m_index = 0
    st.session_state.m_score = 0

  idx = st.session_state.m_index
  q = questions[idx]

  c1, c2 = st.columns([3, 1])
  c1.markdown(f"**Gaaffii Herregaa: {idx + 1} / {len(questions)}**")
  c2.markdown(f"**Qabxii: {st.session_state.m_score}**")

  st.markdown(f"### {q['question']}")
  for opt in q["options"]:
    st.write(opt)

  attempt_key = ("math", grade, idx)
  if attempt_key not in st.session_state.attempts:
    st.session_state.attempts[attempt_key] = 0

  current_attempts = st.session_state.attempts[attempt_key]
  st.write(
      f"⚠️ Carraa deebii yaaluu: **{current_attempts} / 3** (Carraan 3ffaan"
      " ni kuusama/save ta'a)"
  )

  m_ans = st.text_input(
      "Deebii kee asitti barreessi (Fkn: 15 ykn A):", key=f"m_ans_{grade}_{idx}"
  )

  if st.button("Mirkaneessi Herregaa"):
    if current_attempts < 3:
      st.session_state.attempts[attempt_key] += 1
      is_correct = False
      cleaned_ans = m_ans.strip().upper()

      if cleaned_ans == q["answer"].upper() or cleaned_ans == q["answer"][0]:
        is_correct = True

      if is_correct:
        st.session_state.m_score += 10
        st.success("🎉 Sirriitti deebiste, Foyyee qabda, Si hafa!")
        st.session_state.attempts[attempt_key] = 3
      else:
        rem = 3 - st.session_state.attempts[attempt_key]
        if rem > 0:
          st.warning(
              f"❌ Dogoggora qaba! Carraan hafe: {rem} (Carraan 3ffaan ni"
              " kuusama)"
          )
        else:
          st.error(
              f"❌ Carraan 3ffaan xumurameera. Deebiin sirrii: {q['answer']}"
          )
    else:
      st.info("Barataan carraa 3 guutee xumureera.")

  st.markdown("---")
  b1, b2 = st.columns(2)
  with b1:
    if idx > 0 and st.button("⬅️ Duubatti (Previous)"):
      st.session_state.m_index -= 1
      st.rerun()
  with b2:
    if idx < len(questions) - 1:
      if st.button("Fuuldharatti (Next) ➡️"):
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
# 6. ENGLISH MODULE (Grades 1-6)
# ==========================================
def english_screen():
  grade = st.session_state.current_grade
  st.subheader(f"English - {grade} ({st.session_state.current_student})")

  english_db = {
      "Kutaa 1": [
          {
              "type": "reading",
              "title": "Reading 1: My School",
              "text": (
                  "This is my school. My school name is Hiika Way. We learn"
                  " English and Afaan Oromoo here everyday."
              ),
              "question": "Question: What is the name of the school?",
              "expected": ["hiika way", "hiikaway"],
          },
          {
              "type": "mcq",
              "title": "Alphabet & Greetings",
              "text": "Complete: Good ______!",
              "options": ["A) Morning", "B) Table", "C) Book", "D) Pen"],
              "answer": "Morning",
          },
      ],
      "Kutaa 2": [
          {
              "type": "reading",
              "title": "Reading 2: Animals",
              "text": (
                  "Cats and dogs are domestic animals. Dogs guard our houses"
                  " and cats catch mice."
              ),
              "question": "Question: What do dogs do?",
              "expected": ["guard", "guard our houses", "house"],
          },
          {
              "type": "mcq",
              "title": "Vocabulary",
              "text": "Which word means a place where we buy things?",
              "options": ["A) Market", "B) River", "C) Mountain", "D) Cloud"],
              "answer": "Market",
          },
      ],
      "Kutaa 3": [
          {
              "type": "reading",
              "title": "Reading 3: The Family",
              "text": (
                  "A family consists of a father, mother, brothers and sisters."
                  " They live together and help each other."
              ),
              "question": "Question: Who are members of a family?",
              "expected": [
                  "father",
                  "mother",
                  "brothers and sisters",
                  "parents",
              ],
          },
          {
              "type": "mcq",
              "title": "Grammar Tense",
              "text": "Choose the correct past tense of 'go':",
              "options": ["A) Goes", "B) Went", "C) Gone", "D) Going"],
              "answer": "Went",
          },
      ],
      "Kutaa 4": [
          {
              "type": "reading",
              "title": "Reading 4: Water Cycle",
              "text": (
                  "Water evaporates from oceans, forms clouds, and falls back as"
                  " rain on the earth."
              ),
              "question": "Question: What falls back on the earth?",
              "expected": ["rain", "water"],
          },
          {
              "type": "mcq",
              "title": "Parts of Speech",
              "text": "Identify the noun in: 'The boy runs fast.'",
              "options": ["A) Boy", "B) Runs", "C) Fast", "D) The"],
              "answer": "Boy",
          },
      ],
      "Kutaa 5": [
          {
              "type": "reading",
              "title": "Reading 5: Solar System",
              "text": (
                  "The Earth revolves around the Sun. It takes 365 days to"
                  " complete one full orbit."
              ),
              "question": (
                  "Question: How many days does Earth take to orbit the Sun?"
              ),
              "expected": ["365", "365 days"],
          },
          {
              "type": "mcq",
              "title": "Synonyms",
              "text": "Choose the synonym of 'Big':",
              "options": ["A) Small", "B) Large", "C) Cold", "D) Short"],
              "answer": "Large",
          },
      ],
      "Kutaa 6": [
          {
              "type": "reading",
              "title": "Reading 6: Scientific Research",
              "text": (
                  "Researchers analyze data, study patterns, and draw valid"
                  " conclusions based on empirical evidence."
              ),
              "question": "Question: What do researchers analyze?",
              "expected": ["data", "empirical evidence"],
          },
          {
              "type": "mcq",
              "title": "Advanced Grammar",
              "text": "Choose the correct passive voice: 'She writes a letter.'",
              "options": [
                  "A) A letter is written by her.",
                  "B) A letter was written.",
                  "C) She wrote a letter.",
                  "D) Letter is write.",
              ],
              "answer": "A",
          },
      ],
  }

  questions = english_db.get(grade, english_db["Kutaa 1"])

  if "e_index" not in st.session_state:
    st.session_state.e_index = 0
    st.session_state.e_score = 0

  idx = st.session_state.e_index
  q = questions[idx]

  st.progress((idx + 1) / len(questions))
  c1, c2 = st.columns([3, 1])
  c1.markdown(f"**Question {idx + 1} / {len(questions)} : {q['title']}**")
  c2.markdown(f"**Score: {st.session_state.e_score}**")

  if q["type"] == "reading" and "text" in q:
    st.markdown(
        f"""
            <div style="background-color: #f1f8e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 15px;">
                <b>📚 Reading Passage:</b><br>{q['text']}
            </div>
        """,
        unsafe_allow_html=True,
    )

  st.markdown(f"### {q.get('question', q.get('text'))}")
  if "options" in q:
    for opt in q["options"]:
      st.write(opt)

  attempt_key = ("english", grade, idx)
  if attempt_key not in st.session_state.attempts:
    st.session_state.attempts[attempt_key] = 0

  current_attempts = st.session_state.attempts[attempt_key]
  st.write(
      f"⚠️ Attempt count: **{current_attempts} / 3** (3rd attempt saves/locks"
      " final record)"
  )

  e_ans = st.text_input("Type your answer here:", key=f"e_ans_{grade}_{idx}")

  if st.button("Check Answer"):
    if current_attempts < 3:
      st.session_state.attempts[attempt_key] += 1
      is_correct = False
      cleaned_ans = e_ans.strip().lower()

      if "answer" in q:
        if (
            cleaned_ans == q["answer"].lower()
            or cleaned_ans == q["answer"][0].lower()
        ):
          is_correct = True
      elif "expected" in q:
        if any(exp in cleaned_ans for exp in q["expected"]):
          is_correct = True

      if is_correct:
        st.session_state.e_score += 10
        st.success("🎉 Sirriitti deebiste, Foyyee qabda, Si hafa!")
        st.session_state.attempts[attempt_key] = 3
      else:
        rem = 3 - st.session_state.attempts[attempt_key]
        if rem > 0:
          st.warning(
              f"❌ Incorrect! Remaining attempts: {rem} (3rd attempt will be"
              " saved)"
          )
        else:
          ans_text = q.get("answer", q.get("expected", [""])[0])
          st.error(
              f"❌ 3rd attempt reached. Saved as incorrect. Correct answer:"
              f" {ans_text}"
          )
    else:
      st.info("Maximum attempts completed for this question.")

  st.markdown("---")
  b1, b2 = st.columns(2)
  with b1:
    if idx > 0 and st.button("⬅️ Duubatti (Previous)"):
      st.session_state.e_index -= 1
      st.rerun()
  with b2:
    if idx < len(questions) - 1:
      if st.button("Fuuldharatti (Next) ➡️"):
        st.session_state.e_index += 1
        st.rerun()
    else:
      if st.button("Finish & Return"):
        st.session_state.global_students[st.session_state.current_student][
            "english"
        ] = st.session_state.e_score
        st.success(
            f"Well done! Total English Score: {st.session_state.e_score}"
        )
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
# 7. TEACHER DASHBOARD (INTERACTIVE TABLE & EXCEL REPORT DOWNLOAD)
# ==========================================
def teacher_dashboard_screen():
  st.subheader("🎓 Gabaasa Barsiisaa - Kutaa Barsiisaa (Teacher Report & Table)")
  st.markdown(
      "**Gosa Barnoota Sadii (Afaan Oromoo, Herrega, Ingliffaa) Qabxii"
      " Barattootaa, Parsantii (%) fi Cuunfaa Gamaaggamaa**"
  )

  students = st.session_state.global_students
  st.write(f"**Baay'inni barattoota galmaa'an:** {len(students)}")

  if not students:
    st.info(
        "Ammaaf barataan galmaa'e hin jiru. Barataan yeroo appii fayyadamu asitti"
        " dhiyaata."
    )
  else:
    max_subject_score = 20
    max_total_score = 60

    table_data = []
    csv_data = (
        "Maqaa Barataa,Kutaa,Afaan"
        " Oromoo,Herrega,Ingliffaa,Waliigala,Parsantii (%),Cuunfaa"
        " Gabaasa\n"
    )

    for name, data in students.items():
      ao = data["afaanOromoo"]
      math = data["math"]
      eng = data["english"]
      total = ao + math + eng
      percentage = (total / max_total_score) * 100

      def get_subject_summary(score):
        pct = (score / max_subject_score) * 100
        if pct == 100:
          return "Sirriitti deebise"
        elif pct >= 75:
          return "Foyyee qaba"
        else:
          return "Irra haa deebi'u"

      ao_summary = get_subject_summary(ao)
      math_summary = get_subject_summary(math)
      eng_summary = get_subject_summary(eng)

      summary_text = (
          f"Afaan Oromoo: {ao_summary} | Herrega: {math_summary} | Ingliffaa:"
          f" {eng_summary}"
      )

      table_data.append({
          "Maqaa Barataa": name,
          "Kutaa": data["grade"],
          "Afaan Oromoo": f"{ao}/20",
          "Herrega": f"{math}/20",
          "Ingliffaa": f"{eng}/20",
          "Waliigala": f"{total}/60",
          "Parsantii (%)": f"{percentage:.1f}%",
          "Cuunfaa Gabaasa": summary_text,
      })

      csv_data += (
          f"{name},{data['grade']},{ao},{math},{eng},{total},{percentage:.1f}%,\\\"{summary_text}\\\"\n"
      )

    # Display using Streamlit's clean, built-in interactive table component (`st.dataframe` or `st.table`)
    st.dataframe(table_data, use_container_width=True)

    # Download button for CSV report
    st.download_button(
        label="📥 Download Excel-Compatible Report (CSV)",
        data=csv_data,
        file_name="HiikaWay_Student_Report.csv",
        mime="text/csv",
        help="Gabaasa kana Excel irratti banuun print gochuun ni danda'ama",
    )

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
