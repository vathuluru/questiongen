import streamlit as st
from llmcall import get_answer
#from llmapi  import llmcall

# Add an image to the top of the page
st.image("ui/setting_35.png")

# Streamlit app
st.title("Question Generator")

# Dropdown for Grade
grade = st.selectbox("Select Grade", [ "Grade 8", "Grade 9", "Grade 10","Grade 11","Grade 12"])

# Dropdown for Topic
topic = st.selectbox("Select Topic", ["Math", "Physics", "Chemistry"])

# Text box for Focus Area Question
focus_area = st.text_input("Enter Focus Area Question")

# Radio button for Multiple Choice or Not
question_type = st.radio("Select Question Type", ["Multiple Choice", "Open Ended"])

# Radio button for Complexity
complexity = st.radio("Select Complexity", ["Easy", "Medium", "Hard"])

# Generate Question Button


generate_button = st.button("Generate Question")
prompt = "Grade =" + grade + "Topic = " + topic +   \
   "Focus Area =" + focus_area + "Question Format =" + question_type + \
   "Complexity = " + complexity + "Generate a question with the options given"

if generate_button:
    # Call the LLM function to get the answer
    answer = get_answer(prompt)
    st.write("Generated Question: ", answer)

st.write ("AI is experimental and may not always be accurate. Please verify the generated questions and answers*.")

