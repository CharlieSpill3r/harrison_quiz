import streamlit as st

def main():
    st.title("Harrison Bergeron - Reading & Analysis")
    
    # Provide text access
    with st.expander("Read the Full Text of *Harrison Bergeron* by Kurt Vonnegut"):
        st.markdown("""
        **Harrison Bergeron** is a dystopian short story that explores themes of equality, government control, and individuality.
        
        *(Insert full text here, or provide a link to an authorized source.)*
        """)
    
    st.header("Comprehension & Analysis Questions")
    
    # Define questions
    questions = [
        "1. What is the purpose of the handicaps used in the society of *Harrison Bergeron*? Give examples of different types of handicaps used.",
        "2. How does George Bergeron experience the effects of the government’s policies while watching television?",
        "3. What does Hazel suggest about how she would change the Handicapper General’s rules, and what does this reveal about her understanding of the system?",
        "4. How is Harrison Bergeron physically described when he appears on television? What do his handicaps tell us about him?",
        "5. What happens after Harrison declares himself Emperor and selects an Empress? How does the story end for him?",
        "6. How does Vonnegut use irony in *Harrison Bergeron*? Give at least one example.",
        "7. How does the story explore the theme of individuality versus conformity?",
        "8. What is the significance of Harrison and the ballerina’s dance? How does this scene contrast with the rest of the story?",
        "9. What message might Vonnegut be conveying about government control and the pursuit of equality? Do you think it is a warning or a satire?",
        "10. How do George and Hazel’s final conversation and forgetfulness contribute to the story’s impact? What does their reaction suggest about the success of the government’s control?"
    ]
    
    responses = {}
    
    for i, question in enumerate(questions):
        responses[f'Q{i+1}'] = st.text_area(question, "")

    # Submission button
    if st.button("Submit Answers"):
        feedback = provide_feedback(responses)
        st.subheader("Personalized Feedback on Your Answers")
        for q, comment in feedback.items():
            st.write(f"**{q}:** {comment}")

def provide_feedback(answers):
    feedback = {}
    
    for question, answer in answers.items():
        if question == "Q1":
            feedback[question] = ("Re-read the section where the text describes how handicaps enforce equality: \"Nobody was smarter than anybody else... \"\n"
                                "Think about how the handicaps function. For example, George had to wear a mental radio that disrupted his thoughts.\n"
                                "Concept-checking questions: \n"
                                "- What did George have to wear?\n"
                                "- Did Hazel have a handicap? Why or why not?\n"
                                "- What does this tell us about how equality is enforced?")
        elif question == "Q2":
            feedback[question] = ("Re-read the section where George experiences mental disruptions: \"Every twenty seconds or so, the transmitter would send out some sharp noise...\"\n"
                                "Think about how this prevents deep thinking.\n"
                                "Concept-checking questions:\n"
                                "- What type of noises does George hear?\n"
                                "- How does he react to them?\n"
                                "- Why does this make it hard for him to resist the system?")
        elif question == "Q5":
            feedback[question] = ("Re-read the scene where Harrison and the ballerina perform their dance: \"They leaped like deer on the moon...\"\n"
                                "Think about how their rebellion is expressed through dance.\n"
                                "Concept-checking questions:\n"
                                "- What does their dance symbolize?\n"
                                "- What happens immediately after their moment of freedom?\n"
                                "- How does this reinforce the government's control?")
        else:
            feedback[question] = "Good response! Now, refine it further by considering the deeper implications of the text. Ask yourself: What message is Vonnegut trying to convey about society and human nature?"
    
    return feedback

if __name__ == "__main__":
    main()
