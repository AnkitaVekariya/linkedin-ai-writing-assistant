import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post


st.set_page_config(
    page_title="LinkedIn AI Writer",
    layout="wide"
)

Length_opt = ["Short", "Medium", "Long"]

Language_opt = ["English", "Hinglish"]

Tone_opt = ["Professional", "Casual", "Motivational", "Storytelling","Technical"]


# CLEAN CSS
st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    max-width: 1000px;
}

h1 {
    text-align: center;
    margin-bottom: 0.3rem;
}

.subtext {
    text-align: center;
    color: gray;
    margin-bottom: 2rem;
}

.stButton button {
    width: 100%;
    height: 3em;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 600;
}

.post-box {
    padding: 30px;
    border-radius: 12px;
    border: 1px solid #333;
    margin-top: 30px;
    line-height: 1.9;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)


def main():

    fs = FewShotPosts()

    # HERO
    st.markdown(
        "<h1>LinkedIn AI Writing Assistant</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p class='subtext'>Write better LinkedIn posts with AI-powered assistance.</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        selected_tag = st.selectbox(
            "Topic",
            sorted(list(fs.get_tags()))
        )

    with col2:

        selected_length = st.selectbox(
            "Length",
            Length_opt
        )

    with col3:

        selected_language = st.selectbox(
            "Language",
            Language_opt
        )

    with col4:

        selected_tone = st.selectbox(
            "Tone",
            Tone_opt
        )

    # BUTTON
    if st.button("Generate Post"):

        with st.spinner("Generating post..."):

            examples = fs.get_filtered_post(
                selected_length,
                selected_language,
                selected_tag
            )

            post = generate_post(
                selected_length,
                selected_language,
                selected_tag,
                selected_tone,
                examples
            )

        # OUTPUT
        st.markdown(
            f"""
            <div class="post-box">
            {post}
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()