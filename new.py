import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="new",
    layout="centered"
)

# ---------------------------------------------------
# CUSTOM STYLE
# ---------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom, #fff5f7, #ffeef2);
}

h1 {
    color: #ff4f8b;
    text-align: center;
    font-size: 48px;
    margin-bottom: 10px;
}

h3 {
    text-align: center;
    color: #777777;
    font-weight: normal;
    margin-bottom: 40px;
}

p {
    font-size: 18px;
}

div.stButton > button {
    background-color: #ffb6c1;
    color: white;
    border-radius: 18px;
    border: none;
    padding: 14px 20px;
    font-size: 16px;
    width: 100%;
    margin-top: 12px;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #ff8fab;
    color: white;
    transform: scale(1.02);
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}

.message-box {
    background-color: white;
    padding: 22px;
    border-radius: 22px;
    color: #ff4f8b;
    font-size: 20px;
    text-align: center;
    margin-top: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
    line-height: 1.7;
}

.footer {
    text-align: center;
    color: #999999;
    margin-top: 50px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("✨ Things i hope you know ✨")

st.markdown(
    "<h3>A tiny corner of the internet that belongs to you.</h3>",
    unsafe_allow_html=True
)

st.write("")

# ---------------------------------------------------
# BUTTONS
# ---------------------------------------------------

if st.button("💭 Something I should tell you"):

    st.markdown(
        """
        <div class="message-box">
        When you smile back at me, something in me lights up.
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("👀 A small observation"):

    st.markdown(
        """
        <div class="message-box">
        You have very beautiful eyes.
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("🌱 Thank you"):

    st.markdown(
        """
        <div class="message-box">
        Thank you for pushing me to learn and grow without making me feel small.
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("🫶 Something I admire"):

    st.markdown(
        """
        <div class="message-box">
        I love how we continue choosing each other no matter what.
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("✨ You should know"):

    st.markdown(
        """
        <div class="message-box">
        I genuinely believe you can build the life you dream about, and I hope you never stop believing that either.
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("🌸 Little things"):

    st.markdown(
        """
        <div class="message-box">
        I appreciate all the little things you do for me more than you probably realize.
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("☁️ And also"):

    st.markdown(
        """
        <div class="message-box">
        I think about you every day more naturally than i even realize.
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("🌸 One last thing"):

    st.markdown(
        """
        <div class="message-box">
        ♡ ♡ ♡
        <br><br>
        I just really love you ^^
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
    <div class="footer">
    made with a lot of love ♡
    </div>
    """,
    unsafe_allow_html=True
)