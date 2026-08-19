# Python Basic 2026 @ IT Genius

เอกสารประกอบหลักสูตรอบรม **Python Basic 2026 — ปูพื้นฐานการเขียนโปรแกรมภาษา Python ตั้งแต่เริ่มต้นจนถึงการประยุกต์ใช้งานจริง** ของ **สถาบันไอทีจีเนียส เอ็นจิเนียริ่ง (IT Genius Engineering)**

เป็นหลักสูตรอบรมเชิงปฏิบัติการ (Hands-on Workshop) แบบ Onsite ระยะเวลา **2 วัน (12 ชั่วโมง)** ระดับ **Beginner** ไม่จำเป็นต้องมีพื้นฐานการเขียนโปรแกรมมาก่อน
Repository นี้เก็บ **Course Outline**, **เอกสารประกอบการสอน (Instructor Notes)** และ **สไลด์นำเสนอ** ของหลักสูตร

> ผู้สอน: อ.สามิตร โกยม และทีมงาน | เวลาอบรม 09:00-16:00 น.

---

## 📂 โครงสร้างของ Repository

```
Python Basic 2026 at itgenius/
├── outlines/                          # Course Outline ของหลักสูตร
│   ├── Python Basic 2026.md           # ต้นฉบับ Outline (Markdown)
│   └── Python Basic 2026 - Course Outline.pdf
├── notes/                             # เอกสารประกอบการสอนแบบละเอียด
│   ├── Day1_note.md                   # วันที่ 1 (~2,500 บรรทัด)
│   └── Day2_note.md                   # วันที่ 2 (~3,200 บรรทัด)
├── presentation/                      # สไลด์ประกอบการบรรยาย
│   ├── Python-Basic-2026-Day1.pdf
│   └── Python-Basic-2026-Day2.pdf
├── .gitignore
└── README.md
```

> **หมายเหตุ:** โฟลเดอร์ `cover/`, `example/` และ `prepostest/` ถูกกำหนดไว้ใน `.gitignore` จึงไม่ได้รวมอยู่ในเอกสารฉบับนี้

---

## 📄 รายละเอียดของแต่ละส่วน

### `outlines/` — Course Outline

Outline ฉบับสมบูรณ์ของหลักสูตร ประกอบด้วยข้อมูลหลักสูตร วัตถุประสงค์ กลุ่มเป้าหมาย ความรู้พื้นฐานที่ควรมี เครื่องมือที่ใช้ หัวข้อการอบรมทั้ง 13 Modules เงื่อนไขการอบรม และช่องทางติดต่อสำหรับการจัด In-house Training
มีทั้งไฟล์ต้นฉบับ Markdown สำหรับแก้ไข และไฟล์ PDF สำหรับส่งให้ลูกค้า/ผู้เข้าอบรม

### `notes/` — เอกสารประกอบการสอน

เอกสารเชิงลึกสำหรับผู้สอนและผู้เรียน แยกตามวัน แต่ละไฟล์ประกอบด้วยวัตถุประสงค์การเรียนรู้ประจำวัน กำหนดการรายชั่วโมง เนื้อหาแต่ละ Module พร้อมโค้ดตัวอย่างอธิบายเป็นภาษาไทย Workshop ท้ายแต่ละ Module และบทสรุปประจำวัน

### `presentation/` — สไลด์นำเสนอ

ไฟล์ PDF สไลด์ที่ใช้บรรยายจริงในห้องอบรม แยกเป็นวันที่ 1 และวันที่ 2

---

## 🗓️ ภาพรวมเนื้อหา 2 วัน

### วันที่ 1 — ปูพื้นฐานภาษา Python และเครื่องมือการพัฒนา

| Module | หัวข้อ |
| --- | --- |
| 1 | แนะนำภาษา Python (Overview) — จุดเด่น ข้อจำกัด การใช้งานจริง และเส้นทางอาชีพปี 2026 |
| 2 | การเตรียมเครื่องมือและสภาพแวดล้อมด้วย **uv** — `uv python install`, `uv init`, `uv venv`, `uv run`, ตั้งค่า VS Code / PyCharm |
| 3 | พื้นฐานภาษา Python — Indentation, ตัวแปร, ชนิดข้อมูล, f-string, ตัวดำเนินการ, `if`/`elif`/`else`, `match-case`, `for`/`while`, PEP 8 |
| 4 | ชนิดข้อมูลแบบกลุ่ม (Collections) — List, Tuple, Set, Dictionary และ List Comprehension |
| 5 | ฟังก์ชัน (Function) — Positional / Keyword / Default / `*args` / `**kwargs`, Scope, Docstring, Type Hints, Lambda |
| 6 | โมดูลและแพ็กเกจ — `import`, โมดูลมาตรฐาน, `uv add` / `remove` / `sync` / `lock` / `tree`, `pyproject.toml` และ `uv.lock` |
| Workshop | **PyShop Mini v1** — โปรแกรมจัดการสินค้าคงคลังแบบ Console |

### วันที่ 2 — การประยุกต์ใช้งานจริง ฐานข้อมูล และการทำงานเป็นทีม

| Module | หัวข้อ |
| --- | --- |
| 7 | การจัดการแฟ้มข้อมูล — `with`, Text / CSV / JSON, `pathlib` |
| 8 | การเขียนโปรแกรมเชิงวัตถุ (OOP) — Class, Constructor, Method, Inheritance, Encapsulation, `@dataclass` |
| 9 | การจัดการข้อผิดพลาดและการ Debug — `try/except/else/finally`, Custom Exception, `logging`, Debugger ใน VS Code |
| 10 | การเชื่อมต่อฐานข้อมูล **PostgreSQL** — `psycopg`, CRUD, Parameterized Query, Transaction |
| 11 | Git Version Control — `init`/`add`/`commit`/`log`, Branch, Merge, `.gitignore`, GitHub |
| 12 | Python GUI — Tkinter และ CustomTkinter, Layout, Form, Event Binding |
| 13 | **Workshop ปิดท้าย: PyShop Mini v2** — GUI + PostgreSQL พร้อมแนวทางต่อยอด |

> ทั้งสองวันพัฒนาโปรเจกต์เดียวต่อเนื่องคือ **PyShop Mini** ระบบจัดการสินค้าคงคลังร้านค้าขนาดเล็ก (ข้อมูลจำลองทั้งหมด) เริ่มจาก Console → ไฟล์ CSV/JSON → OOP → ฐานข้อมูล → GUI

---

## 🧰 เครื่องมือและเทคโนโลยีที่ใช้ในหลักสูตร

- **uv** — เครื่องมือหลักของหลักสูตร ใช้จัดการเวอร์ชัน Python, Virtual Environment, แพ็กเกจ และการรันโปรเจกต์
- **Python 3.13 / 3.14** — ติดตั้งและสลับเวอร์ชันผ่าน uv
- **Visual Studio Code + Python Extension** (หลัก) และ **PyCharm Community Edition** (ทางเลือก)
- **pyproject.toml / uv.lock** — มาตรฐานการกำหนดและตรึงเวอร์ชันไลบรารี
- **pip และ venv** — เรียนรู้ในฐานะเครื่องมือดั้งเดิมเพื่ออ่านโค้ดและเอกสารเก่าได้
- **PostgreSQL** (หรือ MySQL) — ฐานข้อมูลสำหรับ Workshop
- **Git และ GitHub** — ระบบบริหารจัดการเวอร์ชันซอร์สโค้ด
- **Tkinter / CustomTkinter** — สร้าง GUI เบื้องต้น
- **AI Coding Assistant** — แนวทางใช้ AI เป็นผู้ช่วยเรียนรู้อย่างเหมาะสม

---

## 🚀 การใช้งาน Repository นี้

**สำหรับผู้สอน**

1. อ่าน `outlines/Python Basic 2026.md` เพื่อดูภาพรวมและขอบเขตของหลักสูตร
2. ใช้ `notes/Day1_note.md` และ `notes/Day2_note.md` เป็นสคริปต์การสอน — มีกำหนดการรายชั่วโมง โค้ดตัวอย่าง และ Workshop ครบทุก Module
3. เปิด `presentation/Python-Basic-2026-Day*.pdf` ประกอบการบรรยายในห้องอบรม

**สำหรับผู้เข้าอบรม**

1. ทบทวนเนื้อหาย้อนหลังจากไฟล์ใน `notes/` ซึ่งอธิบายละเอียดกว่าสไลด์
2. คัดลอกโค้ดตัวอย่างจาก Code Block ในเอกสารไปทดลองรันด้วย `uv run`

**การแก้ไขเอกสาร** — แก้ที่ไฟล์ Markdown ต้นฉบับเสมอ แล้วจึง Export เป็น PDF ใหม่

---

## 📌 สิ่งที่ผู้เข้าอบรมต้องเตรียม

- Notebook ระบบ Windows หรือ macOS ที่มีสิทธิ์ติดตั้งโปรแกรมได้ พื้นที่ว่างอย่างน้อย 10 GB
- แนะนำให้ติดตั้ง Python, Visual Studio Code และ Git มาล่วงหน้า (หากติดปัญหาติดตั้งร่วมกับวิทยากรได้ใน Module 2)
- ไม่จำเป็นต้องมีพื้นฐานการเขียนโปรแกรมมาก่อน

---

## 📞 ติดต่อสอบถาม / จัดอบรม In-house

**บริษัท ไอทีจีเนียส เอ็นจิเนียริ่ง จำกัด**

- โทร. 02-570-8449 | มือถือ 088-807-9770, 092-841-7931
- Line ID: `@itgenius`
- เว็บไซต์: [www.itgenius.co.th](https://www.itgenius.co.th)
- อีเมล: contact@itgenius.co.th

---

## 📝 ลิขสิทธิ์

เอกสารทั้งหมดใน Repository นี้เป็นลิขสิทธิ์ของ **บริษัท ไอทีจีเนียส เอ็นจิเนียริ่ง จำกัด** จัดทำขึ้นเพื่อใช้ประกอบการอบรมภายในหลักสูตรเท่านั้น ห้ามทำซ้ำหรือเผยแพร่เพื่อการค้าโดยไม่ได้รับอนุญาต
