import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import bcrypt
from connectpg import get_connection

st.title("🔐 เข้าสู่ระบบ")

# ฟังก์ชันสำหรับตรวจสอบผู้ใช้
def verify_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT password_hash, full_name FROM users WHERE username = %s;", (username,))
        row = cursor.fetchone()
        if row and bcrypt.checkpw(password.encode("utf-8"), row[0].encode("utf-8")):
            return row[1]
        return None
    finally:
        cursor.close()
        conn.close()

# สร้างฟอร์มสำหรับการเข้าสู่ระบบ
with st.form("login_form"):
    username = st.text_input("ชื่อผู้ใช้")
    password = st.text_input("รหัสผ่าน", type="password")
    submit = st.form_submit_button("Login", use_container_width=True)

    if submit:
        if not username or not password:
            st.warning("กรุณากรอกข้อมูลให้ครบถ้วน")
        else:
            full_name = verify_user(username, password)
            if full_name:
                st.session_state.authenticated = True
                st.session_state.user_name = full_name
                st.success("เข้าสู่ระบบสำเร็จ!")
                st.rerun()
            else:
                st.error("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")