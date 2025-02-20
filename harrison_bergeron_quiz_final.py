
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
    
    if "responses" not in st.session_state:
        st.session_state.responses = {}
    
    for i, question in enumerate(questions):
        st.session_state.responses[f'Q{i+1}'] = st.text_area(question, st.session_state.responses.get(f'Q{i+1}', ""))
    
    # Submission button
    if st.button("Submit Answers"):
        feedback = provide_feedback(st.session_state.responses)
        st.subheader("Personalized Feedback on Your Answers")
        for q, comment in feedback.items():
            st.write(f"**{q}:** {comment}")
            
            # Step-by-step concept checking
            if comment.startswith("Please re-read"):
                if f"{q}_step1" not in st.session_state:
                    st.session_state[f"{q}_step1"] = ""
                st.session_state[f"{q}_step1"] = st.text_input("Was everyone the same?", st.session_state[f"{q}_step1"])
                
                if st.session_state[f"{q}_step1"].strip().lower() in ["no", "not really", "they were forced to be"]:
                    if f"{q}_step2" not in st.session_state:
                        st.session_state[f"{q}_step2"] = ""
                    st.session_state[f"{q}_step2"] = st.text_input("What examples in this section are given?", st.session_state[f"{q}_step2"])
                    
                    if st.session_state[f"{q}_step2"]:
                        if f"{q}_step3" not in st.session_state:
                            st.session_state[f"{q}_step3"] = ""
                        st.session_state[f"{q}_step3"] = st.text_input("How might you rewrite 'Nobody was better looking than anybody else'?", st.session_state[f"{q}_step3"])
                        
                        if st.session_state[f"{q}_step3"]:
                            st.write("Great! Now, try rewriting it using this sentence starter: 'In the story, the government ensures that...'")

def provide_feedback(answers):
    feedback = {}
    
    reference_texts = {
        "Q1": "Nobody was smarter than anybody else. Nobody was better looking than anybody else. Nobody was stronger or quicker than anybody else.",
        "Q2": "Every twenty seconds or so, the transmitter would send out some sharp noise to keep people like George from taking unfair advantage of their brains.",
        "Q3": "If I was Diana Moon Glampers, said Hazel, I’d have chimes on Sunday—just chimes. Kind of in honor of religion.",
        "Q4": "He was exactly seven feet tall... Instead of a little ear radio for a mental handicap, he wore a tremendous pair of earphones, and spectacles with thick wavy lenses.",
        "Q5": "They leaped like deer on the moon. The studio ceiling was thirty feet high, but each leap brought the dancers nearer to it. It became their obvious intention to kiss the ceiling. They kissed it.",
    }
    
    for question, answer in answers.items():
        ref_text = reference_texts.get(question, "Reference not found.")
        if not answer.strip() or answer.lower().strip() in ["i don't know", "idk"]:
            feedback[question] = (f"Please re-read this section of the text: {ref_text}\n"
                                "Let's go step by step: \n"
                                "1. Was everyone the same? (Your answer)")
        else:
            feedback[question] = (f"Good response! Now, refine it further by considering the deeper implications of this passage: {ref_text}\n"
                                "How does this passage connect to the theme of equality? (Your answer)\n"
                                "What is the character experiencing? (Your answer)\n"
                                "How does this reinforce Vonnegut’s message? (Your answer)\n"
                                "Now, try rewriting it using this sentence starter: 'Vonnegut uses this passage to show that...'")
    
    return feedback

if __name__ == "__main__":
    main()
