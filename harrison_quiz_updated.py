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
        if len(answer.strip()) == 0:
            feedback[question] = "Your answer is empty. Try rereading the text and focusing on the key details. Consider why the government enforces handicaps and how they affect individuals."
        elif len(answer.split()) < 20:
            feedback[question] = "Your response is too brief. Try elaborating with specific textual references. For example, how does George react to his handicaps? What effect do they have on his thinking?"
        elif "Harrison" not in answer and question in ["Q4", "Q5", "Q8"]:
            feedback[question] = "You need to discuss Harrison’s role in this scene. Revisit the section where he declares himself Emperor and reflect on how his appearance contrasts with others. What does his rebellion symbolize?"
        elif "government" not in answer and question in ["Q6", "Q7", "Q9"]:
            feedback[question] = "Consider discussing the government’s role in enforcing equality. Look at the way Diana Moon Glampers reacts to Harrison’s rebellion. What does her immediate action suggest about the government’s priorities?"
        else:
            feedback[question] = "Good response! Now, refine it further by considering the deeper implications of the text. Ask yourself: What message is Vonnegut trying to convey about society and human nature?"
    
    return feedback

if __name__ == "__main__":
    main()
