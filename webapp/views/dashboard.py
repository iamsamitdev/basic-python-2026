import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import pandas as pd
from connectpg import get_connection

# ดักความปลอดภัย (Route Protection)
if not st.session_state.get("authenticated", False):
    st.warning("กรุณาเข้าสู่ระบบก่อนเข้าใช้งาน")
    st.stop()

st.title("📦 Product Dashboard")

def get_products():
    conn = get_connection()
    try:
        query = "SELECT id, name, price, stock, created_at FROM product ORDER BY id ASC;"
        return pd.read_sql_query(query, conn)
    finally:
        conn.close()

df = get_products()

if not df.empty:
    m1, m2, m3 = st.columns(3)
    m1.metric("จำนวนสินค้าทั้งหมด", f"{len(df)} รายการ")
    m2.metric("มูลค่าสินค้ารวม", f"฿{(df['price'] * df['stock']).sum():,.2f}")
    m3.metric("สต็อกสินค้ารวม", f"{df['stock'].sum():,} ชิ้น")

    st.markdown("---")
    search = st.text_input("🔍 ค้นหาชื่อสินค้า", "")
    if search:
        df = df[df["name"].str.contains(search, case=False, na=False)]

    st.dataframe(
        df,
        use_container_width=True,
        column_config={
            "id": "รหัส",
            "name": "ชื่อสินค้า",
            "price": st.column_config.NumberColumn("ราคา (บาท)", format="฿%.2f"),
            "stock": st.column_config.NumberColumn("คงเหลือ", format="%d ชิ้น"),
            "created_at": "วันที่เพิ่ม"
        }
    )
else:
    st.info("ยังไม่มีข้อมูลสินค้าในระบบ")