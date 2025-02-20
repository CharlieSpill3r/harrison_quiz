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
    ]
    
    if "responses" not in st.session_state:
        st.session_state.responses = {}
    
    for i, question in enumerate(questions):
        key = f'Q{i+1}'
        st.session_state.responses[key] = st.text_area(question, st.session_state.responses.get(key, ""))
    
    # Submission button
    if st.button("Submit Answers"):
        feedback = provide_feedback(st.session_state.responses)
        st.subheader("Personalized Feedback on Your Answers")
        for q, comment in feedback.items():
            st.write(f"**{q}:** {comment}")
            
            # Step-by-step concept checking
            step1_key = f"{q}_step1"
            if step1_key not in st.session_state:
                st.session_state[step1_key] = ""
            response1 = st.text_input(f"{q}: Does this mean everyone had the same intelligence or different intelligence?", key=step1_key)
            
            if response1.lower().strip() == "same intelligence":
                step2_key = f"{q}_step2"
                if step2_key not in st.session_state:
                    st.session_state[step2_key] = ""
                response2 = st.text_input(f"{q}: What does the next sentence say?", key=step2_key)
                
                if response2:
                    step3_key = f"{q}_step3"
                    if step3_key not in st.session_state:
                        st.session_state[step3_key] = ""
                    response3 = st.text_input(f"{q}: How does this support the theme of enforced equality?", key=step3_key)
                    
                    if response3:
                        st.write("Great! Now, try rewriting it using this sentence starter: 'Vonnegut uses this passage to show that...'")

def provide_feedback(answers):
    feedback = {}
    
    reference_texts = {
        "Q1": "*Nobody was smarter than anybody else. Nobody was better looking than anybody else. Nobody was stronger or quicker than anybody else.*",
        "Q2": "*Every twenty seconds or so, the transmitter would send out some sharp noise to keep people like George from taking unfair advantage of their brains.*",
        "Q3": "*If I was Diana Moon Glampers, said Hazel, I’d have chimes on Sunday—just chimes. Kind of in honor of religion.*",
        "Q4": "*He was exactly seven feet tall... Instead of a little ear radio for a mental handicap, he wore a tremendous pair of earphones, and spectacles with thick wavy lenses.*",
        "Q5": "*They leaped like deer on the moon. The studio ceiling was thirty feet high, but each leap brought the dancers nearer to it. It became their obvious intention to kiss the ceiling. They kissed it.*",
    }
    
    for question, answer in answers.items():
        ref_text = reference_texts.get(question, "*Reference not found.*")
        if not answer.strip() or answer.lower().strip() in ["i don't know", "idk"]:
            feedback[question] = (f"Please re-read this section of the text: {ref_text}\n"
                                "Does this mean everyone had the same intelligence or different intelligence?")
        else:
            feedback[question] = (f"Good response! Now, refine it further by considering the deeper implications of this passage: {ref_text}\n"
                                "What does the next sentence say?\n"
                                "How does this support the theme of enforced equality?\n"
                                "Now, try rewriting it using this sentence starter: 'Vonnegut uses this passage to show that...'")
    
    return feedback

if __name__ == "__main__":
    main()
