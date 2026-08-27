import streamlit as st
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
st.set_page_config(page_title="Shop Management System", page_icon="🛍️", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.user_name = ""

# กำหนดหน้าต่างๆ
login_page = st.Page("views/login.py", title="Login", icon="🔐")
register_page = st.Page("views/register.py", title="Register", icon="📝")
dashboard_page = st.Page("views/dashboard.py", title="Dashboard", icon="📦")

# สลับเมนูตามสถานะการล็อกอิน
if not st.session_state.authenticated:
    pg = st.navigation([login_page, register_page])
else:
    pg = st.navigation([dashboard_page])
    with st.sidebar:
        st.write(f"👤 ผู้ใช้งาน: **{st.session_state.user_name}**")
        if st.button("ออกจากระบบ", type="primary", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.user_name = ""
            st.rerun()

pg.run()