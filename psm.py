import re
import streamlit as st


# page styling
st.set_page_config(page_title= "Password Strength Meter by Sidra Masood", page_icon= "🔒", layout= "centered")

#custom css
st.markdown(""" 
<style>
    .main {text-align: center;}
    .stTextInput {width: 100% !important; margin:auto;}
    .stButton button {width: 100%; background-color: #ff33c4; color: black; font-size: 18px;  }
    .stButton button:hover { background-color: #3380ff; color: white;}
</style>              
""", unsafe_allow_html=True)

#page title and description
st.title("🔒 Password Strength Meter")
st.text("Enter your password below to check its security level. 🔍")

#Function to password strength

def check_password_strength(password):
    score= 0
    feedback=[]

    if len(password) >=8:
        score += 1 #score increased by 1
    else:
        feedback.append("❌ Password should be **atleast 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both upper case (A-Z) and lower case (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number(0-9)**.")

    # special characters:
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*)**.")

    # display password strength result:

    if score == 4:
        st.success("🛡️ **Strong Password - Your password is secure.**")
    elif score == 3:
        st.info(" ⚠️ **Moderate Password ** - Consider improving security by adding more features. ")
    else:
        st.error(" ❌ ** Weak Password ** - Follow the suggestion below to strength your password.")

    # feedback:
    if feedback:
        with st.expander("🛠️**Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong.🔒")

    # button working:
if st.button("Check Strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("⚠️ Please enter a password first!") # show warning if password is empty
