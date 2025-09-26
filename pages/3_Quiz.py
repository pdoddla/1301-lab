import streamlit as st

st.title("Basketball Quiz!") #NEW
st.caption("Are you a true ball-knower? Take this quiz and find out!") #NEW


st.image("Images/chalktoss.jpg")

st.write("")
st.write("")
st.write("")
st.write("")


q1 = st.radio( #NEW
    "Who is the only player in the modern NBA to lead the league in both total points and total assists in a single season?",
    ["Trae Young", "Russell Westbrook", "James Harden", "Nikola Jokic"]
)


if st.button ("Check your answer for Q1"): #NEW
    if q1 == "Trae Young":
        st.success("Correct! Trae Young did it in the 2021-2022 season.") #NEW
        st.image("Images/trae_ny.jpg")
                   
    else:
        st.error("Wrong. The correct answer is Trae Young.") #NEW
        st.image("Images/trae_ny.jpg")

st.write("")
st.write("")
st.write("")
st.write("")

q2 = st.number_input( #NEW
    "How many seasons did Russell Westbrook average a triple double?",
    min_value = 0,
    max_value = None,
    step = 1,
)

if st.button("Check your answer for Q2"):
    if q2 == 4:
        st.success("Correct! Westbrook averaged a triple-double for 4 seasons.")
        st.image("Images/russ.jpg")
    else:
        st.error("Wrong. The correct answer is 4")
        st.image("Images/russ.jpg")


st.write("")
st.write("")
st.write("")
st.write("")


q3 = st.multiselect(  #NEW
    "Which of the following players have won all of these: NBA Scoring Title, Olympic Gold Medal, NBA Finals MVP, NBA Regular Season MVP.",
    [
        "Kevin Durant", "Stephen Curry", "Isiah Thomas", "Kareem Abdul-Jabbar", "LeBron James", "Steve Nash", "Michael Jordan", "Dwyane Wade", "Tim Duncan"
    ]
)

if st.button("Check your answer for Q3"):
    correct = {"LeBron James", "Michael Jordan", "Kevin Durant", "Stephen Curry"}
    your_answer = set(q3)

    if correct == your_answer:
        st.success("Correct! The players to win all four are LeBron James, Michael Jordan, Stephen Curry, and Kevin Durant.")
        st.image("Images/bron_dunk.jpg")
    else:
        st.error("Wrong. The players to win all four are LeBron James, Michael Jordan, Stephen Curry, and Kevin Durant.")



st.write("")
st.write("")
st.write("")
st.write("")



st.write("Q4: True or False - Get all 3 right to get the point!")

tf1 = st.radio("1. LeBron James played in 8 NBA Finals in the 2010's.", ["True", "False"])
tf2 = st.radio("2. Derrick Rose is the youngest MVP.", ["True", "False"])
tf3 = st.radio("3. Kevin Garnett went to North Carolina for college.", ["True", "False"])


if st.button("Check your answers for Q4"):
    correct = ("True", "True", "False")
    your_answer = (tf1, tf2, tf3)
    if correct == your_answer:
        st.success("Correct! You got all 3.")
        st.image("Images/drose.jpg")
    else:
        st.error("Wrong. You missed atleast 1.")



st.write("")
st.write("")
st.write("")
st.write("")

    

q5 = st.text_input( #NEW
    "Who is the first player to record 30 points, 20 assists, and 20 rebounds in a game?"
)

if st.button("Check your answer for Q5"):
    answer = q5.lower()
    if answer == "nikola jokic":
        st.success("Correct! Jokić is the first and only player to do it.")
        st.image("Images/jokic.jpg")
    elif answer == "nikola jokić":
        st.success("Correct! Jokić is the first and only player to do it.")
        st.image("Images/jokic.jpg")
    else:
        st.error("Wrong, the right answer is Nikola Jokić")
        st.image("Images/jokic.jpg")


st.write("")
st.write("")
st.write("")
st.write("")



q6 = st.radio( 
    "Final Question: Who is the greatest player of all time?",
    ["LeBron James", "Michael Jordan", "Kobe Bryant", "Stephen Curry"]
)


if st.button ("Check your answer for Q6"): 
    if q6 == "LeBron James":
        st.success("Correct! LeGOAT is the greatest to ever do it!") 
        st.image("Images/bron_flex.jpg")
                   
    else:
        st.error("Wrong. It's LeBron.") 
        st.image("Images/bron_flex.jpg")
