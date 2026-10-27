import streamlit as st


# ---------- Cipher functions (same as caesar.py) ----------

def shift_letter(letter, key):
    if letter.isupper():
        start = ord("A")
    elif letter.islower():
        start = ord("a")
    else:
        return letter
    position = ord(letter) - start
    new_position = (position + key) % 26
    return chr(start + new_position)


def encrypt(message, key):
    result = ""
    for letter in message:
        result += shift_letter(letter, key)
    return result


def decrypt(message, key):
    return encrypt(message, -key)


# ---------- Web page ----------

st.title("🔐 Caesar Cipher")
st.write("Shift every letter along the alphabet by a key. Type a message and watch it change.")

# Encrypt / decrypt
mode = st.radio("What do you want to do?", ["Encrypt", "Decrypt"], horizontal=True)
message = st.text_input("Message", placeholder="e.g. Hello")
key = st.slider("Key", min_value=1, max_value=25, value=3)

if message:
    if mode == "Encrypt":
        st.success(encrypt(message, key))
    else:
        st.success(decrypt(message, key))

st.divider()

# Brute-force crack
st.subheader("🔓 Crack a message")
st.write("Don't know the key? Try all 25 and look for the one that makes sense.")
secret = st.text_input("Scrambled message", placeholder="e.g. Khoor")

if secret:
    results = []
    for k in range(1, 26):
        results.append({"Key": k, "Result": decrypt(secret, k)})
    st.table(results)

st.caption("Why it's insecure: only 25 possible keys, so a computer can try them all instantly.")
