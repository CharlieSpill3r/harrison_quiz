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
    
    reference_texts = {
        "Q1": "'Nobody was smarter than anybody else. Nobody was better looking than anybody else. Nobody was stronger or quicker than anybody else.'",
        "Q2": "'Every twenty seconds or so, the transmitter would send out some sharp noise to keep people like George from taking unfair advantage of their brains.'",
        "Q3": "'If I was Diana Moon Glampers,' said Hazel, 'I’d have chimes on Sunday—just chimes. Kind of in honor of religion.'",
        "Q4": "'He was exactly seven feet tall... Instead of a little ear radio for a mental handicap, he wore a tremendous pair of earphones, and spectacles with thick wavy lenses.'",
        "Q5": "'They leaped like deer on the moon. The studio ceiling was thirty feet high, but each leap brought the dancers nearer to it. It became their obvious intention to kiss the ceiling. They kissed it.'",
        "Q6": "'That was a real pretty dance, that dance they just did,' said Hazel. 'Huh?' said George. 'That dance—it was nice,' said Hazel.'",
        "Q7": "'The minute people start cheating on laws, what do you think happens to society?' 'Reckon it’d fall all apart,' said Hazel.'",
        "Q8": "'Not only were the laws of the land abandoned, but the law of gravity and the laws of motion as well.'",
        "Q9": "'It was then that Diana Moon Glampers, the Handicapper General, came into the studio with a double-barreled ten-gauge shotgun.'",
        "Q10": "'What was it?' he said. 'It’s all kind of mixed up in my mind,' said Hazel. 'Forget sad things,' said George. 'I always do,' said Hazel.'"
    }
    
    for question, answer in answers.items():
        if not answer.strip() or answer.lower().strip() in ["i don't know", "idk"]:
            feedback[question] = (f"Please re-read this section of the text: {reference_texts[question]}\n"
                                "Key concepts: [highlight important terms]\n"
                                "Concept-checking questions:\n"
                                "- What does this tell us about the government’s control?\n"
                                "- How does this affect the characters?\n"
                                "- Why is this important to the theme of the story?")
        else:
            feedback[question] = (f"Good response! Now, refine it further by considering the deeper implications of this passage: {reference_texts[question]}\n"
                                "Think about these questions:\n"
                                "- How does this passage connect to the theme of equality?\n"
                                "- What is the character experiencing?\n"
                                "- How does this reinforce Vonnegut’s message?")
    
    return feedback

if __name__ == "__main__":
    main()
