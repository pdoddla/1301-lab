import streamlit as st

if "total_score" not in st.session_state:
    st.session_state.total_score = 0

st.title("Basketball Archetype Quiz!") #New
st.caption("Want to find out your playstyle on the court? Take this quiz and find out!") #NEW


st.image("Images/chalktoss.jpg")
st.header("Note: Do not click an answer more than once for accurate results")


st.write("")
st.write("")
st.write("")
st.write("")


q1 = st.radio("Q1: Which kind of highlight gets you most excited?", #NEW
              
        ["Behind-the-back assist", "Monster block at the rim",
        "3 from the logo", "Crossover to a step-back jumper",]
)

if st.button("Lock in Q1"): #NEW
    if q1 == "Behind-the-back assist":
        st.session_state.total_score += 20
        st.success("Good choice!")
    elif q1 == "Monster block at the rim":
        st.session_state.total_score += 10
        st.success("Good choice!")
    elif q1 == "3 from the logo":
        st.session_state.total_score += 30
        st.success("Good choice!")
    elif q1 == "Crossover to step-back jumper":
        st.session_state.total_score += 40
        st.success("Good choice!")


st.write("")
st.write("")
st.write("")
st.write("")


st.image("Images/Q2.jpg")
q2 = st.number_input(             #NEW
    "Q2: Which player is your favorite to watch?",
    min_value=1,
    max_value=4,
    step=1,
)

if st.button("Lock in Q2"):
    if q2 == 1:   
        st.session_state.total_score += 30
        st.success("Good choice!")
    elif q2 == 2:
        st.session_state.total_score += 40
        st.success("Good choice!")
    elif q2 == 3: 
        st.session_state.total_score += 10
        st.success("Good choice!")
    elif q2 == 4: 
        st.session_state.total_score += 20
        st.success("Good choice!")


st.write("")
st.write("")
st.write("")
st.write("")


q3 = st.multiselect("Q3: Pick any of these all time scorers you love watching (choose as many as you like)", #NEW

    ["Stephen Curry", "Klay Thompson", "Kevin Durant", "James Harden", "Damian Lillard", "Dirk Nowitzki",
        "Ray Allen", "Reggie Miller", "Larry Bird", "Trae Young"]
)

if st.button("Lock in Q3"):
    n = len(q3)

    
    if n == 0:
         st.session_state.total_score += 0
         st.success("Nice!")
    elif 1 <= n <= 2:
         st.session_state.total_score += 10
         st.success("Nice!")
    elif 3 <= n <= 4:
         st.session_state.total_score += 20
         st.success("Nice!")
    elif 5 <= n <= 6:
         st.session_state.total_score += 30
         st.success("Nice!")
    else:
         st.session_state.total_score += 40
         st.success("Nice!")


st.write("")
st.write("")
st.write("")
st.write("")


q4 = st.radio("Q4: Game is on the line and your team need a basket to win. The ball is in your hands. What do you do?",
              
        ["Pass it to the point guard and get in the post", "Run the offense and try to find the open man",
        "Run around and get open for a 3", "Take the ball and go get a bucket",]
)

if st.button("Lock in Q4"):
    if q4 == "Pass it to the point guard and get in the post":
        st.session_state.total_score += 10
        st.success("Good choice!")
    elif q4 == "Run the offense and try to find the open man":
        st.session_state.total_score += 20
        st.success("Good choice!")
    elif q4 == "Run around and get open for a 3":
        st.session_state.total_score += 30
        st.success("Good choice!")
    elif q4 == "Take the ball and go get a bucket":
        st.session_state.total_score += 40
        st.success("Good choice!")

st.image("Images/bron_clutch.jpg")


st.write("")
st.write("")
st.write("")
st.write("")


q5 = st.radio("Q5: You walk into the gym and you realize you have the whole court to yourself. What do you do?",
              
        ["Work on conditioning and lateral quickness", "Work on ball handling",
        "Work on extending your 3 point range", "Do a 3-level scoring workout",]
)

if st.button("Lock in Q5"):
    if q5 == "Work on conditioning and lateral quickness":
        st.session_state.total_score += 10
        st.success("Good choice!")
    elif q5 == "Work on ball handling":
        st.session_state.total_score += 20
        st.success("Good choice!")
    elif q5 == "Work on extending your 3 point range":
        st.session_state.total_score += 30
        st.success("Good choice!")
    elif q5 == "Do a 3-level scoring workout":
        st.session_state.total_score += 40
        st.success("Good choice!")

st.write("")
st.write("")

if st.button("Show my archetype"):
    score = st.session_state.total_score

    if score <= 80:
        archetype = "Defensive anchor"
        comp = "Giannis Antetokounmpo, Victor Wembenyama, Evan Mobley"
        st.image("Images/final1.jpg")
    elif score <= 120:
        archetype = "Pass first guard"
        comp = "Trae Young, Tyrese Haliburton, Chris Paul"
        st.image("Images/final2.jpg")
    elif score <= 160:
        archetype = "Sharpshooter"
        comp = "Steph Curry, Reggie Miller, Ray Allen"
        st.image("Images/final3.jpg")
    else:
        archetype = "3-level scorer"
        comp = "Kevin Durant, Shai Gilgeous-Alexander, Devin Booker"
        st.image("Images/final4.jpg")
        
        

    st.subheader(f"Your archetype: {archetype}")
    st.subheader(f"Your player comparisons: {comp}")
