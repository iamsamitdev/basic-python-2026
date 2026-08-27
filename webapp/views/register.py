import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import bcrypt
from connectpg import get_connection

st.title("📝 สมัครสมาชิก")

# ฟังก์ชันสำหรับสร้างผู้ใช้ใหม่
def create_user(username, password, full_name):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # เช็คชื่อผู้ใช้ซ้ำ
        cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
        if cur.fetchone():
            return False, "ชื่อผู้ใช้นี้มีอยู่ในระบบแล้ว"

        # เข้ารหัสผ่านและบันทึก
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        cur.execute("""
            INSERT INTO users (username, password_hash, full_name)
            VALUES (%s, %s, %s);
        """, (username, hashed, full_name))
        conn.commit()
        return True, "สมัครสมาชิกสำเร็จ! กรุณาเข้าสู่ระบบ"
    except Exception as e:
        return False, f"เกิดข้อผิดพลาด: {e}"
    finally:
        cur.close()
        conn.close()

# สร้างฟอร์มสำหรับการสมัครสมาชิก
with st.form("register_form"):
    full_name = st.text_input("ชื่อ-นามสกุล")
    username = st.text_input("ตั้งชื่อผู้ใช้ (Username)")
    password = st.text_input("ตั้งรหัสผ่าน (Password)", type="password")
    confirm_password = st.text_input("ยืนยันรหัสผ่าน", type="password")
    submit = st.form_submit_button("ลงทะเบียน", use_container_width=True)

    if submit:
        if not full_name or not username or not password:
            st.warning("กรุณากรอกข้อมูลให้ครบทุกช่อง")
        elif password != confirm_password:
            st.error("รหัสผ่านทั้งสองช่องไม่ตรงกัน")
        else:
            success, message = create_user(username, password, full_name)
            if success:
                st.success(message)
            else:
                st.error(message)