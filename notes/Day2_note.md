# Python Basic 2026 - วันที่ 2: การประยุกต์ใช้งานจริง ฐานข้อมูล และการทำงานเป็นทีม

**หลักสูตรอบรมเชิงปฏิบัติการ: Python Basic 2026 (พื้นฐานการเขียนโปรแกรมภาษา Python)**
**จัดอบรม: สถาบันไอทีจีเนียส เอ็นจิเนียริ่ง (Onsite Public Training)**
**วันที่ 2: จากโปรแกรมในหน่วยความจำ สู่ระบบที่เก็บข้อมูลจริงและมีหน้าจอใช้งาน**
วันที่: 21 สิงหาคม 2569 | เวลา 09:00-16:00 น. | Onsite Workshop
ผู้สอน: อ.สามิตร โกยม

---

## 🎯 วัตถุประสงค์การเรียนรู้ประจำวัน

เมื่อจบการอบรมวันที่ 2 ผู้เรียนจะสามารถ:

1. อ่านและเขียนไฟล์ Text, CSV และ JSON ด้วยคำสั่ง `with` และจัดการเส้นทางไฟล์ด้วย `pathlib` ได้
2. ออกแบบและสร้างคลาส (Class) พร้อม Constructor, Attribute, Method รวมถึงใช้ Inheritance, Encapsulation และ `@dataclass` ได้
3. จัดการข้อผิดพลาดด้วย `try / except / else / finally` สร้าง Exception ของตนเอง และใช้ `logging` แทน `print` ได้
4. ใช้ Debugger ของ Visual Studio Code (Breakpoint, Step, Watch) ไล่หาสาเหตุของบั๊กได้อย่างเป็นระบบ
5. ติดตั้ง PostgreSQL เชื่อมต่อด้วย `psycopg` และสั่งงาน SQL แบบ Parameterized Query พร้อมจัดการ Transaction ได้
6. ใช้ Git บันทึกประวัติโค้ด ทำงานกับ Branch และแชร์โปรเจกต์ขึ้น GitHub ได้
7. สร้างหน้าจอ GUI ด้วย Tkinter/CustomTkinter ที่รับค่าจากฟอร์มและเชื่อมกับฐานข้อมูลได้
8. ประกอบทุกอย่างเป็น **PyShop Mini v2** ระบบจัดการสินค้าที่มีหน้าจอ GUI และเก็บข้อมูลใน PostgreSQL จริง (Workshop ปิดท้าย)

> **ต่อเนื่องจากวันที่ 1:** เราจะพัฒนาโปรเจกต์ **PyShop Mini** ตัวเดิมต่อ โดยวันนี้จะเปลี่ยนข้อมูลจาก `sample_inventory()` ที่ฝังอยู่ในโค้ด ให้กลายเป็นข้อมูลที่อ่านจากไฟล์ CSV/JSON แล้วยกระดับเป็นฐานข้อมูล PostgreSQL พร้อมหน้าจอ GUI จริง

---

## 🧭 กำหนดการวันที่ 2 (โดยสังเขป)

| เวลา | หัวข้อ |
| ----------- | ------------------------------------------------------------- |
| 09:00-09:15 | ทบทวนวันที่ 1 + ตรวจความพร้อมโปรเจกต์ |
| 09:15-10:30 | **Module 7** การจัดการแฟ้มข้อมูล (Text / CSV / JSON / pathlib) + Workshop 7.1 |
| 10:30-12:00 | **Module 8** การเขียนโปรแกรมเชิงวัตถุ (OOP) + Workshop 8.1 |
| 12:00-13:00 | พักกลางวัน |
| 13:00-13:45 | **Module 9** การจัดการข้อผิดพลาดและการ Debug + Workshop 9.1 |
| 13:45-14:45 | **Module 10** การเชื่อมต่อฐานข้อมูล PostgreSQL + Workshop 10.1 |
| 14:45-15:15 | **Module 11** Git Version Control |
| 15:15-15:45 | **Module 12** Python GUI ด้วย Tkinter / CustomTkinter |
| 15:45-16:00 | **Module 13** Workshop ปิดท้าย + แนวทางต่อยอด + ทดสอบหลังเรียน |

---

## 🔁 ทบทวนวันที่ 1 และตรวจความพร้อม

### เวลา 09:00-09:15 น.

**เช็กลิสต์ก่อนเริ่ม** เปิด Terminal ในโฟลเดอร์ `pyshop` แล้วรัน:

```powershell
cd C:\PythonTraining\pyshop
uv run main.py
```

ถ้าเมนู PyShop Mini v1 ขึ้นมาได้ แปลว่าพร้อมเรียนต่อ ถ้าติดปัญหาให้ยกมือทันที

**สิ่งที่เราทำได้แล้วเมื่อวาน**

```
วันที่ 1 (เสร็จแล้ว):                    วันที่ 2 (วันนี้):
┌──────────────────────────┐           ┌──────────────────────────┐
│ ข้อมูลฝังในโค้ด            │           │ ข้อมูลอยู่ในไฟล์ CSV/JSON  │  ← Module 7
│ sample_inventory()       │           │ และฐานข้อมูล PostgreSQL   │  ← Module 10
│                          │    ⟶     │                          │
│ ข้อมูลเป็น dict           │           │ ข้อมูลเป็น class Product  │  ← Module 8
│ ปิดโปรแกรม = ข้อมูลหาย    │           │ ปิดแล้วข้อมูลยังอยู่        │
│ หน้าจอเป็นข้อความ         │           │ หน้าจอเป็น GUI จริง       │  ← Module 12
│ ผิดพลาดแล้วโปรแกรมพัง     │           │ จับ error ได้อย่างสง่างาม  │  ← Module 9
└──────────────────────────┘           └──────────────────────────┘
```

> 💡 **จุดที่ต้องเข้าใจให้ตรงกัน:** เมื่อวานเราออกแบบให้ `main.py` มีแต่ส่วนติดต่อผู้ใช้ ส่วนตรรกะอยู่ใน `src/pyshop/` ทั้งหมด **วันนี้จะพิสูจน์ว่าการออกแบบแบบนั้นคุ้มค่า** เพราะเราจะเปลี่ยนแหล่งข้อมูลและเปลี่ยนหน้าจอ โดยแทบไม่แตะโค้ดตรรกะเลย

---

## 📚 Module 7: การจัดการแฟ้ม (File) ข้อมูลใน Python

### เวลา 09:15-10:30 น.

> 💡 **หัวใจของ Module นี้:** ข้อมูลที่อยู่แค่ในหน่วยความจำจะหายไปทันทีที่ปิดโปรแกรม การเขียนลงไฟล์คือก้าวแรกสู่ระบบที่ใช้งานได้จริง และ **CSV กับ JSON คือสองรูปแบบที่คุณจะเจอมากที่สุดในชีวิตการทำงาน**

---

### 7.1 พื้นฐานการเปิดไฟล์และคำสั่ง with

**วิธีที่ถูกต้องคือใช้ `with`** เพราะจะปิดไฟล์ให้อัตโนมัติเสมอ แม้เกิดข้อผิดพลาดกลางทาง

```python
# ❌ วิธีเดิม: ถ้าเกิด error ระหว่างอ่าน ไฟล์จะไม่ถูกปิด
f = open("products.txt", "r", encoding="utf-8")
content = f.read()
f.close()

# ✅ วิธีที่ถูกต้อง: with จะปิดไฟล์ให้เองเสมอ
with open("products.txt", "r", encoding="utf-8") as f:
    content = f.read()
# ออกจากบล็อก with = ไฟล์ถูกปิดแล้วแน่นอน
```

> ⚠️ **`encoding="utf-8"` สำคัญมากสำหรับภาษาไทย:** บน Windows ค่าเริ่มต้นของการเข้ารหัสไม่ใช่ UTF-8 ถ้าไม่ระบุ ข้อความไทยจะกลายเป็นตัวประหลาดหรือเกิด `UnicodeDecodeError` **ให้ใส่ `encoding="utf-8"` ทุกครั้งที่เปิดไฟล์ที่มีภาษาไทย**

**โหมดการเปิดไฟล์**

| โหมด | ชื่อเต็ม | ความหมาย | ถ้าไฟล์ไม่มี | ถ้าไฟล์มีอยู่แล้ว |
| --- | --- | --- | --- | --- |
| `"r"` | read | อ่านอย่างเดียว (ค่าเริ่มต้น) | ❌ `FileNotFoundError` | อ่านได้ |
| `"w"` | write | เขียนทับทั้งไฟล์ | สร้างใหม่ | ⚠️ **ล้างข้อมูลเดิมทิ้งทั้งหมด** |
| `"a"` | append | เขียนต่อท้าย | สร้างใหม่ | เขียนต่อท้ายของเดิม |
| `"x"` | exclusive | สร้างใหม่เท่านั้น | สร้างใหม่ | ❌ `FileExistsError` |
| `"r+"` | read/write | อ่านและเขียน | ❌ error | เขียนทับตั้งแต่ต้น |
| `"rb"` / `"wb"` | binary | อ่าน/เขียนแบบไบนารี | | ใช้กับรูปภาพ, PDF |

> ⚠️ **โหมด `"w"` คือฆาตกรเงียบ:** เปิดไฟล์ด้วย `"w"` แม้ยังไม่ได้เขียนอะไรเลย ข้อมูลเดิมก็หายหมดแล้ว ถ้าตั้งใจจะเพิ่มข้อมูลให้ใช้ `"a"` เสมอ

### 7.2 การอ่านไฟล์ Text

```python
# 1) อ่านทั้งไฟล์เป็นข้อความก้อนเดียว (เหมาะกับไฟล์เล็ก)
with open("products.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# 2) อ่านเป็นรายการบรรทัด
with open("products.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()      # ['บรรทัด1\n', 'บรรทัด2\n', ...]
print(len(lines))

# 3) ★ อ่านทีละบรรทัด (แนะนำที่สุด ประหยัดหน่วยความจำ ใช้ได้แม้ไฟล์ใหญ่มาก)
with open("products.txt", "r", encoding="utf-8") as f:
    for line_no, line in enumerate(f, start=1):
        print(f"{line_no}: {line.rstrip()}")   # rstrip ตัด \n ท้ายบรรทัด

# 4) อ่านเฉพาะบรรทัดเดียว
with open("products.txt", "r", encoding="utf-8") as f:
    first_line = f.readline()
```

> 💡 **ทำไมวิธีที่ 3 ดีที่สุด:** ถ้าไฟล์มีขนาด 2 GB วิธีที่ 1 และ 2 จะโหลดทั้งหมดเข้าหน่วยความจำจนเครื่องค้าง แต่วิธีที่ 3 อ่านทีละบรรทัดจึงใช้หน่วยความจำเท่าเดิมเสมอไม่ว่าไฟล์จะใหญ่แค่ไหน

### 7.3 การเขียนและต่อท้ายข้อมูล

```python
products = ["เมาส์ไร้สาย", "คีย์บอร์ด", "จอภาพ 27 นิ้ว"]

# เขียนทับทั้งไฟล์
with open("products.txt", "w", encoding="utf-8") as f:
    f.write("รายการสินค้า\n")
    f.write("=" * 20 + "\n")
    for product in products:
        f.write(f"- {product}\n")

# เขียนหลายบรรทัดพร้อมกัน (ต้องใส่ \n เอง)
with open("products.txt", "w", encoding="utf-8") as f:
    f.writelines(f"- {p}\n" for p in products)

# ต่อท้ายไฟล์เดิม (Log)
from datetime import datetime

with open("activity.log", "a", encoding="utf-8") as f:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"[{timestamp}] เพิ่มสินค้า: ลำโพง\n")
```

### 7.4 การจัดการ Path ด้วย pathlib

`pathlib` คือวิธีสมัยใหม่ในการจัดการเส้นทางไฟล์ **ทำงานได้เหมือนกันทั้ง Windows และ macOS/Linux**

```python
from pathlib import Path

# ❌ วิธีเก่า: ต้องระวังเรื่อง \ กับ / ที่ต่างกันในแต่ละ OS
path = "data" + "\\" + "products.csv"      # พังบน macOS/Linux

# ✅ pathlib: ใช้ / เชื่อม path ได้เลย ทำงานถูกต้องทุก OS
data_dir = Path("data")
csv_path = data_dir / "products.csv"

# --- ข้อมูลของ path ---
print(csv_path)              # data\products.csv (บน Windows)
print(csv_path.name)         # products.csv
print(csv_path.stem)         # products
print(csv_path.suffix)       # .csv
print(csv_path.parent)       # data
print(csv_path.absolute())   # เส้นทางเต็ม

# --- ตรวจสอบและสร้าง ---
print(csv_path.exists())     # มีไฟล์นี้หรือไม่
print(csv_path.is_file())    # เป็นไฟล์หรือไม่
print(data_dir.is_dir())     # เป็นโฟลเดอร์หรือไม่

data_dir.mkdir(exist_ok=True)                 # สร้างโฟลเดอร์ (มีแล้วไม่ error)
Path("data/backup/2026").mkdir(parents=True, exist_ok=True)   # สร้างซ้อนหลายชั้น

# --- อ่าน/เขียนแบบสั้น (เหมาะกับไฟล์เล็ก) ---
csv_path.write_text("code,name,price\n", encoding="utf-8")
content = csv_path.read_text(encoding="utf-8")

# --- ค้นหาไฟล์ ---
for file in data_dir.glob("*.csv"):           # ไฟล์ .csv ในโฟลเดอร์นี้
    print(file.name)

for file in Path(".").rglob("*.py"):          # ไฟล์ .py ทุกโฟลเดอร์ย่อย
    print(file)

# --- ลบและเปลี่ยนชื่อ ---
# csv_path.rename("data/products_old.csv")
# csv_path.unlink(missing_ok=True)            # ลบไฟล์
```

> 💡 **เคล็ดลับสำคัญ - หาโฟลเดอร์ของสคริปต์เอง:** ถ้าโปรแกรมถูกรันจากโฟลเดอร์อื่น การใช้ path แบบสัมพัทธ์จะหาไฟล์ไม่เจอ วิธีแก้คือ
>
> ```python
> BASE_DIR = Path(__file__).resolve().parent     # โฟลเดอร์ที่ไฟล์นี้อยู่จริง
> DATA_FILE = BASE_DIR / "data" / "products.csv"
> ```

### 7.5 การอ่านและเขียนไฟล์ CSV

**CSV** (Comma-Separated Values) คือรูปแบบข้อมูลตารางที่ Excel เปิดได้ ใช้แลกเปลี่ยนข้อมูลมากที่สุดในงานสำนักงาน

ตัวอย่างไฟล์ `data/products.csv`:

```csv
code,name,price,stock,category
PRD-001,เมาส์ไร้สาย,890,25,อุปกรณ์เสริม
PRD-002,คีย์บอร์ด,1290,8,อุปกรณ์เสริม
PRD-003,จอภาพ 27 นิ้ว,6900,0,จอแสดงผล
PRD-004,หูฟัง,1590,42,เสียง
PRD-005,ลำโพง,2490,5,เสียง
```

**การอ่านด้วย `csv.DictReader` (แนะนำ เพราะได้ dict ที่อ่านง่าย)**

```python
import csv
from pathlib import Path

CSV_PATH = Path("data/products.csv")

products: list[dict] = []
with open(CSV_PATH, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        products.append({
            "code": row["code"],
            "name": row["name"],
            "price": float(row["price"]),    # ★ CSV อ่านมาเป็น str เสมอ ต้องแปลงเอง
            "stock": int(row["stock"]),
            "category": row["category"],
        })

print(f"อ่านข้อมูลได้ {len(products)} รายการ")
```

> ⚠️ **ทำไมต้อง `encoding="utf-8-sig"`:** ไฟล์ CSV ที่บันทึกจาก Excel บน Windows มักมีอักขระซ่อนชื่อ BOM อยู่ต้นไฟล์ ทำให้ชื่อคอลัมน์แรกกลายเป็น `\ufeffcode` แทนที่จะเป็น `code` การใช้ `utf-8-sig` จะตัด BOM ออกให้อัตโนมัติ
>
> ⚠️ **ทำไมต้อง `newline=""`:** ป้องกันบรรทัดว่างแทรกระหว่างแถวบน Windows ซึ่งเป็นข้อกำหนดของโมดูล `csv` โดยตรง

**การเขียนด้วย `csv.DictWriter`**

```python
import csv
from pathlib import Path

FIELDNAMES = ["code", "name", "price", "stock", "category"]
OUT_PATH = Path("data/products_export.csv")
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

with open(OUT_PATH, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
    writer.writeheader()                  # เขียนบรรทัดหัวตาราง
    writer.writerows(products)            # เขียนข้อมูลทั้งหมด
    # หรือทีละแถว: writer.writerow(product)

print(f"บันทึกไฟล์ {OUT_PATH} เรียบร้อย")
```

| คลาส | ใช้เมื่อ | ข้อมูลที่ได้/ต้องส่ง |
| --- | --- | --- |
| `csv.reader` | ไฟล์ไม่มีหัวตาราง | list ของ list |
| `csv.DictReader` | ★ ไฟล์มีหัวตาราง (ปกติ) | list ของ dict (อ้างชื่อคอลัมน์ได้) |
| `csv.writer` | เขียนแบบไม่มีหัวตาราง | ส่ง list |
| `csv.DictWriter` | ★ เขียนพร้อมหัวตาราง | ส่ง dict |

### 7.6 การอ่านและเขียนไฟล์ JSON

**JSON** คือรูปแบบข้อมูลมาตรฐานของการแลกเปลี่ยนข้อมูลผ่าน API และเก็บค่าตั้งค่าของโปรแกรม จุดเด่นคือเก็บโครงสร้างซ้อนกันได้ (ต่างจาก CSV ที่เป็นตารางแบน)

```python
import json
from pathlib import Path

JSON_PATH = Path("data/products.json")

# --- เขียน dict/list ลงไฟล์ JSON ---
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

# --- อ่านไฟล์ JSON กลับมาเป็น Python object ---
with open(JSON_PATH, "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(type(loaded))          # <class 'list'>
print(loaded[0]["name"])     # เมาส์ไร้สาย
```

> ⚠️ **`ensure_ascii=False` สำคัญมากสำหรับภาษาไทย:** ถ้าไม่ใส่ ข้อความไทยจะถูกเข้ารหัสเป็น `"\u0e40\u0e21\u0e32\u0e2a\u0e4c"` ซึ่งยังอ่านกลับได้ถูกต้องแต่มนุษย์อ่านไม่ออก การใส่ `ensure_ascii=False` ทำให้ไฟล์เก็บภาษาไทยเป็นตัวอักษรจริง

| ฟังก์ชัน | ทิศทาง | ทำงานกับ |
| --- | --- | --- |
| `json.dump(obj, f)` | Python → ไฟล์ | ไฟล์ |
| `json.dumps(obj)` | Python → ข้อความ | ข้อความ (มี s = string) |
| `json.load(f)` | ไฟล์ → Python | ไฟล์ |
| `json.loads(text)` | ข้อความ → Python | ข้อความ |

**การแปลงชนิดข้อมูลระหว่าง Python กับ JSON**

| Python | JSON |
| --- | --- |
| `dict` | object `{}` |
| `list`, `tuple` | array `[]` |
| `str` | string |
| `int`, `float` | number |
| `True` / `False` | `true` / `false` |
| `None` | `null` |
| `datetime` | ❌ **แปลงไม่ได้** ต้องแปลงเป็น str ก่อน |

```python
from datetime import datetime

# ❌ TypeError: Object of type datetime is not JSON serializable
# json.dumps({"time": datetime.now()})

# ✅ แปลงเป็นข้อความก่อน
json.dumps({"time": datetime.now().isoformat()})

# หรือใช้ default= สำหรับชนิดที่แปลงไม่ได้
json.dumps({"time": datetime.now()}, default=str)
```

### 7.7 CSV กับ JSON เลือกใช้อันไหน

| ประเด็น | CSV | JSON |
| --- | --- | --- |
| โครงสร้าง | ตารางแบน (แถว x คอลัมน์) | ซ้อนกันได้หลายชั้น |
| เปิดด้วย Excel | ✅ ได้ทันที | ❌ ไม่ได้ |
| ขนาดไฟล์ | เล็กกว่า | ใหญ่กว่า (มีชื่อฟิลด์ซ้ำทุกแถว) |
| ชนิดข้อมูล | เป็นข้อความหมด ต้องแปลงเอง | เก็บชนิดไว้ (number, bool, null) |
| ใช้กับ API | ไม่ค่อยใช้ | ✅ มาตรฐาน |
| เหมาะกับ | ข้อมูลตาราง ส่งให้ฝ่ายบัญชี/ผู้บริหาร | ค่าตั้งค่า, ข้อมูลซ้อนชั้น, API |

### 7.8 การสร้างและลบไฟล์อย่างปลอดภัย

```python
from pathlib import Path
import shutil

path = Path("data/products.csv")

# สร้างไฟล์เปล่า (ถ้ายังไม่มี)
path.touch(exist_ok=True)

# ★ สำรองก่อนเขียนทับเสมอ (แนวปฏิบัติที่ดี)
if path.exists():
    backup = path.with_name(f"{path.stem}_backup{path.suffix}")
    shutil.copy2(path, backup)

# ลบไฟล์
path.unlink(missing_ok=True)          # missing_ok ป้องกัน error เมื่อไม่มีไฟล์

# ลบโฟลเดอร์
Path("data/temp").rmdir()             # ต้องว่างเปล่าเท่านั้น
# shutil.rmtree("data/temp")          # ⚠️ ลบทั้งหมดรวมไฟล์ข้างใน ระวังมาก
```

> ⚠️ **ข้อควรระวังสูงสุด:** `shutil.rmtree()` ลบทุกอย่างในโฟลเดอร์โดยไม่ถามและไม่ไป Recycle Bin **ก่อนใช้งานจริงให้พิมพ์ path ออกมาดูก่อนเสมอ** และควรมีระบบสำรองข้อมูล การเขียนสคริปต์ลบไฟล์ควรทดสอบด้วยโหมด "แสดงว่าจะลบอะไรบ้าง" ก่อนลบจริง

---

### 🧪 Workshop 7.1 - เปลี่ยน PyShop Mini ให้อ่าน-เขียนไฟล์จริง

> **เป้าหมาย:** ย้ายข้อมูลสินค้าจาก `sample_inventory()` ที่ฝังในโค้ด ไปอยู่ในไฟล์ CSV แล้วเพิ่มความสามารถส่งออกรายงานเป็น CSV และ JSON

**ขั้นที่ 1 สร้างไฟล์ข้อมูล `data/products.csv`**

```csv
code,name,price,stock,category
PRD-001,เมาส์ไร้สาย,890,25,อุปกรณ์เสริม
PRD-002,คีย์บอร์ด,1290,8,อุปกรณ์เสริม
PRD-003,จอภาพ 27 นิ้ว,6900,0,จอแสดงผล
PRD-004,หูฟัง,1590,42,เสียง
PRD-005,ลำโพง,2490,5,เสียง
```

**ขั้นที่ 2 สร้างโมดูลใหม่ `src/pyshop/storage.py`**

```python
"""storage.py - อ่านและเขียนข้อมูลสินค้าลงไฟล์ (PyShop Mini)"""

import csv
import json
import shutil
from datetime import datetime
from pathlib import Path

from .models import Product, create_product

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data"
CSV_PATH = DATA_DIR / "products.csv"
JSON_PATH = DATA_DIR / "products.json"

FIELDNAMES = ["code", "name", "price", "stock", "category"]


def ensure_data_dir() -> None:
    """สร้างโฟลเดอร์ data หากยังไม่มี"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def load_products(path: Path = CSV_PATH) -> list[Product]:
    """อ่านรายการสินค้าจากไฟล์ CSV

    Returns:
        รายการสินค้า หรือ list ว่างถ้าไม่พบไฟล์
    """
    if not path.exists():
        print(f"  ⚠ ไม่พบไฟล์ {path.name} เริ่มต้นด้วยคลังว่าง")
        return []

    products: list[Product] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            products.append(
                create_product(
                    code=row["code"],
                    name=row["name"],
                    price=float(row["price"]),
                    stock=int(row["stock"]),
                    category=row.get("category", ""),
                )
            )
    return products


def save_products(products: list[Product], path: Path = CSV_PATH) -> None:
    """บันทึกรายการสินค้าลงไฟล์ CSV พร้อมสำรองไฟล์เดิมไว้ก่อน"""
    ensure_data_dir()

    if path.exists():
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = path.with_name(f"{path.stem}_{stamp}.bak.csv")
        shutil.copy2(path, backup)

    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(products)

    print(f"  ✅ บันทึก {len(products)} รายการลง {path.name} เรียบร้อย")


def export_json(products: list[Product], path: Path = JSON_PATH) -> None:
    """ส่งออกข้อมูลสินค้าเป็นไฟล์ JSON พร้อมข้อมูลสรุป"""
    ensure_data_dir()

    payload = {
        "exported_at": datetime.now().isoformat(timespec="seconds"),
        "total_items": len(products),
        "total_value": sum(p["price"] * p["stock"] for p in products),
        "products": products,
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"  ✅ ส่งออก JSON ไปยัง {path.name} เรียบร้อย")


def write_log(message: str) -> None:
    """บันทึกเหตุการณ์ต่อท้ายไฟล์ log"""
    ensure_data_dir()
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_DIR / "activity.log", "a", encoding="utf-8") as f:
        f.write(f"[{stamp}] {message}\n")
```

**ขั้นที่ 3 แก้ `main.py` ให้ใช้ไฟล์แทนข้อมูลฝังในโค้ด**

```python
# เปลี่ยนจาก
from src.pyshop.models import sample_inventory
inventory = sample_inventory()

# เป็น
from src.pyshop.storage import load_products, save_products, export_json, write_log
inventory = load_products()

# แล้วเพิ่มเมนูใหม่ใน match choice:
#   case "7": save_products(inventory); write_log(f"บันทึก {len(inventory)} รายการ")
#   case "8": export_json(inventory)
# และเรียก save_products(inventory) ก่อน break ตอนออกจากโปรแกรม
```

> ✅ **ผลลัพธ์ที่คาดหวัง:** เพิ่มสินค้าใหม่ผ่านเมนู 3 แล้วเลือกเมนู 7 เพื่อบันทึก จากนั้น **ปิดโปรแกรมแล้วเปิดใหม่** สินค้าที่เพิ่มต้องยังอยู่ และในโฟลเดอร์ `data/` ต้องมีไฟล์สำรอง `products_2026xxxx_xxxxxx.bak.csv` เกิดขึ้น
>
> 🏋️ **โจทย์ต่อยอด:** เขียนฟังก์ชัน `import_csv(path)` ที่นำเข้าไฟล์ CSV จากภายนอกแล้วรวมกับข้อมูลเดิม โดยถ้ารหัสซ้ำให้ปรับจำนวนแทนการเพิ่มซ้ำ

---

## 📚 Module 8: การเขียนโปรแกรมเชิงวัตถุใน Python (OOP)

### เวลา 10:30-12:00 น.

> 💡 **หัวใจของ Module นี้:** ตอนนี้สินค้าของเราคือ `dict` ซึ่งใครก็เข้าไปแก้ค่าอะไรก็ได้ พิมพ์ชื่อ key ผิดก็ไม่มีใครเตือน **OOP คือการมัดข้อมูลกับพฤติกรรมที่เกี่ยวข้องไว้ด้วยกัน** ทำให้ข้อมูลดูแลตัวเองได้

---

### 8.1 แนวคิดการสร้างโปรแกรมเชิงวัตถุ

```
แบบเดิม (dict + ฟังก์ชันแยก):           แบบ OOP (class):
┌─────────────────────────────┐        ┌─────────────────────────────┐
│ product = {                 │        │ class Product:              │
│   "name": "เมาส์",          │        │   name, price, stock        │ ← ข้อมูล
│   "price": 890,             │  ⟶    │                             │
│ }                           │        │   def stock_value()         │ ← พฤติกรรม
│                             │        │   def restock(qty)          │   อยู่ด้วยกัน
│ def stock_value(product)    │        │   def is_low_stock()        │
│ def restock(product, qty)   │        │                             │
└─────────────────────────────┘        └─────────────────────────────┘
  ข้อมูลกับฟังก์ชันแยกกันอยู่               มัดรวม แก้ค่าผ่านเมธอดที่ควบคุมได้
  พิมพ์ key ผิดไม่มีใครเตือน                 พิมพ์ชื่อผิด Editor เตือนทันที
```

**คำศัพท์ที่ต้องรู้จัก**

| คำศัพท์ | ความหมาย | เปรียบเทียบ |
| --- | --- | --- |
| **Class** | พิมพ์เขียว/แม่แบบ | แบบแปลนบ้าน |
| **Object / Instance** | สิ่งที่สร้างจาก Class | บ้านหลังจริงที่สร้างตามแบบ |
| **Attribute** | ข้อมูลของ Object | สีบ้าน จำนวนห้อง |
| **Method** | ฟังก์ชันของ Object | เปิดประตู เปิดไฟ |
| **Constructor** | เมธอด `__init__` ที่ทำงานตอนสร้าง Object | ขั้นตอนก่อสร้าง |
| **`self`** | ตัวแทนของ Object ตัวที่กำลังทำงานอยู่ | "บ้านหลังนี้" |

### 8.2 การสร้างคลาสและ Constructor

```python
class Product:
    """คลาสแทนสินค้า 1 รายการในระบบ PyShop Mini"""

    # Class Attribute - ใช้ร่วมกันทุก object ของคลาสนี้
    VAT_RATE = 0.07
    LOW_STOCK_LIMIT = 10

    def __init__(
        self,
        code: str,
        name: str,
        price: float,
        stock: int = 0,
        category: str = "ทั่วไป",
    ) -> None:
        """สร้างสินค้าใหม่ (Constructor ทำงานอัตโนมัติตอนสร้าง object)"""
        # Instance Attribute - แต่ละ object มีค่าของตัวเอง
        self.code = code.strip().upper()
        self.name = name.strip()
        self.price = float(price)
        self.stock = int(stock)
        self.category = category.strip() or "ทั่วไป"


# สร้าง Object (Instance)
mouse = Product("PRD-001", "เมาส์ไร้สาย", 890, 25, "อุปกรณ์เสริม")
keyboard = Product("PRD-002", "คีย์บอร์ด", 1290, 8, "อุปกรณ์เสริม")

print(mouse.name)          # เมาส์ไร้สาย
print(keyboard.stock)      # 8
print(Product.VAT_RATE)    # 0.07  เรียกจากคลาสได้เลย
```

> ✅ **`self` คืออะไร:** เมื่อเรียก `mouse.some_method()` Python จะส่ง `mouse` เข้าไปเป็นพารามิเตอร์แรกโดยอัตโนมัติ ซึ่งรับด้วยชื่อ `self` ตามธรรมเนียม พูดง่าย ๆ คือ `self` แปลว่า "ตัวฉันเอง" **ทุกเมธอดของ instance ต้องมี `self` เป็นพารามิเตอร์แรกเสมอ**

### 8.3 Method - พฤติกรรมของวัตถุ

```python
class Product:
    VAT_RATE = 0.07
    LOW_STOCK_LIMIT = 10

    def __init__(self, code, name, price, stock=0, category="ทั่วไป"):
        self.code = code.strip().upper()
        self.name = name.strip()
        self.price = float(price)
        self.stock = int(stock)
        self.category = category

    # --- เมธอดคำนวณ ---
    def stock_value(self) -> float:
        """มูลค่าคงคลังของสินค้ารายการนี้"""
        return self.price * self.stock

    def price_with_vat(self) -> float:
        """ราคาที่รวม VAT แล้ว"""
        return self.price * (1 + self.VAT_RATE)

    def is_low_stock(self) -> bool:
        """ตรวจว่าสินค้าใกล้หมดหรือไม่"""
        return 0 < self.stock < self.LOW_STOCK_LIMIT

    def status(self) -> str:
        """สถานะสินค้าในรูปข้อความ"""
        if self.stock <= 0:
            return "สินค้าหมด"
        if self.is_low_stock():
            return "ใกล้หมด"
        return "ปกติ"

    # --- เมธอดเปลี่ยนสถานะ ---
    def restock(self, qty: int) -> None:
        """เพิ่มจำนวนสินค้าเข้าคลัง"""
        if qty <= 0:
            raise ValueError("จำนวนที่เติมต้องมากกว่า 0")
        self.stock += qty

    def sell(self, qty: int) -> float:
        """ขายสินค้าและคืนยอดเงินที่ได้ (รวม VAT)"""
        if qty <= 0:
            raise ValueError("จำนวนที่ขายต้องมากกว่า 0")
        if qty > self.stock:
            raise ValueError(f"สินค้าไม่พอ คงเหลือเพียง {self.stock} ชิ้น")
        self.stock -= qty
        return self.price_with_vat() * qty

    # --- Magic Method: กำหนดว่า print(object) จะแสดงอะไร ---
    def __str__(self) -> str:
        return f"{self.code} {self.name} ({self.price:,.0f} บาท, คงเหลือ {self.stock})"

    def __repr__(self) -> str:
        return f"Product(code={self.code!r}, name={self.name!r}, price={self.price})"


mouse = Product("PRD-001", "เมาส์ไร้สาย", 890, 25)

print(mouse)                       # PRD-001 เมาส์ไร้สาย (890 บาท, คงเหลือ 25)
print(mouse.stock_value())         # 22250.0
print(mouse.status())              # ปกติ

income = mouse.sell(5)
print(f"ขายได้ {income:,.2f} บาท คงเหลือ {mouse.stock} ชิ้น")
```

| Magic Method | ทำงานเมื่อ | ตัวอย่างการใช้ |
| --- | --- | --- |
| `__init__` | สร้าง object | `Product(...)` |
| `__str__` | แปลงเป็นข้อความให้คนอ่าน | `print(obj)`, `str(obj)` |
| `__repr__` | แสดงให้นักพัฒนาดู (ดีบัก) | พิมพ์ชื่อตัวแปรใน REPL |
| `__eq__` | เปรียบเทียบเท่ากัน | `obj1 == obj2` |
| `__len__` | หาความยาว | `len(obj)` |
| `__lt__` | เปรียบเทียบน้อยกว่า | `sorted(objects)` |

### 8.4 การห่อหุ้มข้อมูล (Encapsulation)

ปัญหาของโค้ดข้างบนคือใครก็ตั้งค่า `mouse.stock = -999` ได้ ซึ่งไม่สมเหตุสมผล Encapsulation คือการควบคุมการเข้าถึงข้อมูล

```python
class Product:
    def __init__(self, code, name, price, stock=0):
        self.code = code
        self.name = name
        self._price = price        # _ นำหน้า = "ภายใน อย่าแตะจากข้างนอก" (ธรรมเนียม)
        self.__stock = stock       # __ นำหน้า = ซ่อนจริง (Name Mangling)

    # --- property: ให้อ่านได้เหมือน attribute ปกติ แต่ควบคุมได้ ---
    @property
    def price(self) -> float:
        """ราคาสินค้า (อ่านผ่าน obj.price ได้เลย ไม่ต้องใส่วงเล็บ)"""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """ตั้งราคาใหม่ พร้อมตรวจสอบความถูกต้อง"""
        if value < 0:
            raise ValueError("ราคาต้องไม่ติดลบ")
        self._price = value

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def stock_value(self) -> float:
        """มูลค่าคงคลัง (คำนวณสด ไม่ต้องเก็บเป็น attribute)"""
        return self._price * self.__stock

    def restock(self, qty: int) -> None:
        if qty <= 0:
            raise ValueError("จำนวนต้องมากกว่า 0")
        self.__stock += qty


p = Product("PRD-001", "เมาส์", 890, 25)

print(p.price)          # 890      เรียกเหมือน attribute
print(p.stock_value)    # 22250.0  คำนวณให้อัตโนมัติ ไม่ต้องใส่วงเล็บ

p.price = 950           # เรียก setter ตรวจค่าให้
# p.price = -100        # ❌ ValueError: ราคาต้องไม่ติดลบ
# p.stock = 999         # ❌ AttributeError เพราะไม่มี setter
p.restock(10)           # ✅ ต้องผ่านเมธอดที่ควบคุมไว้
```

| รูปแบบ | ความหมาย | Python บังคับไหม |
| --- | --- | --- |
| `name` | สาธารณะ ใช้ได้อิสระ | - |
| `_name` | ภายใน ไม่ควรใช้จากข้างนอก | ❌ ไม่บังคับ (เป็นข้อตกลงร่วมกัน) |
| `__name` | ซ่อน (Name Mangling เปลี่ยนชื่อจริงเป็น `_Class__name`) | ⚠️ ยากขึ้นแต่ยังเข้าถึงได้ถ้าตั้งใจ |

> 💡 **ปรัชญาของ Python:** ต่างจาก Java/C# ที่มี `private` บังคับจริง Python เชื่อในหลัก **"We are all consenting adults here"** คือใช้ธรรมเนียม `_` เตือนกันว่าไม่ควรแตะ แทนการบังคับด้วยภาษา จุดสำคัญคือทีมต้องเคารพข้อตกลงนี้ร่วมกัน

### 8.5 การสืบทอด (Inheritance) และการ Override

```python
class Product:
    """คลาสแม่ - สินค้าทั่วไป"""

    def __init__(self, code, name, price, stock=0):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock

    def shipping_fee(self) -> float:
        """ค่าจัดส่งมาตรฐาน"""
        return 50.0

    def describe(self) -> str:
        return f"{self.name} ราคา {self.price:,.0f} บาท"


class DigitalProduct(Product):
    """คลาสลูก - สินค้าดิจิทัล (ไม่มีค่าจัดส่ง ไม่มีสต็อกจำกัด)"""

    def __init__(self, code, name, price, download_url: str):
        super().__init__(code, name, price, stock=999999)   # ★ เรียก __init__ ของแม่
        self.download_url = download_url

    def shipping_fee(self) -> float:      # ★ Override: เขียนทับพฤติกรรมของแม่
        return 0.0

    def describe(self) -> str:            # Override แบบต่อยอดจากของแม่
        return f"{super().describe()} [ดาวน์โหลดได้ทันที]"


class BulkyProduct(Product):
    """คลาสลูก - สินค้าขนาดใหญ่ (ค่าส่งตามน้ำหนัก)"""

    def __init__(self, code, name, price, stock, weight_kg: float):
        super().__init__(code, name, price, stock)
        self.weight_kg = weight_kg

    def shipping_fee(self) -> float:
        return 100.0 + self.weight_kg * 20


items = [
    Product("PRD-001", "เมาส์ไร้สาย", 890, 25),
    DigitalProduct("DIG-001", "ซอฟต์แวร์ตัดต่อ", 2900, "https://example.com/dl"),
    BulkyProduct("BLK-001", "โต๊ะทำงาน", 4900, 3, weight_kg=25),
]

# ★ Polymorphism: เรียกเมธอดชื่อเดียวกัน แต่แต่ละคลาสตอบต่างกัน
for item in items:
    print(f"{item.describe():<50} ค่าส่ง {item.shipping_fee():>8,.2f} บาท")
```

```
ผังการสืบทอด:

              ┌──────────────┐
              │   Product    │  ← คลาสแม่ (Base/Parent Class)
              │  shipping_fee│
              │  describe    │
              └──────┬───────┘
          ┌──────────┴───────────┐
          ▼                      ▼
  ┌────────────────┐    ┌────────────────┐
  │ DigitalProduct │    │  BulkyProduct  │  ← คลาสลูก (Derived/Child Class)
  │ ค่าส่ง = 0      │    │ ค่าส่ง = ตามน้ำหนัก│
  └────────────────┘    └────────────────┘
       ★ สืบทอดทุกอย่างจากแม่ แล้วเขียนทับเฉพาะที่ต่าง
```

```python
# ตรวจสอบความสัมพันธ์
digital = DigitalProduct("DIG-001", "ซอฟต์แวร์", 2900, "url")
print(isinstance(digital, DigitalProduct))    # True
print(isinstance(digital, Product))           # True  ← ลูกก็เป็นแม่ด้วย
print(issubclass(DigitalProduct, Product))    # True
```

> ⚠️ **อย่าใช้ Inheritance พร่ำเพรื่อ:** ใช้เมื่อความสัมพันธ์เป็นแบบ **"is-a"** จริง ๆ (DigitalProduct **เป็น** Product) ถ้าเป็นแบบ **"has-a"** (Order **มี** Product) ให้ใช้การเก็บ object ไว้เป็น attribute แทน ซึ่งเรียกว่า Composition และมักยืดหยุ่นกว่า

### 8.6 Dataclass - เขียนคลาสเก็บข้อมูลแบบกระชับ

สำหรับคลาสที่มีหน้าที่หลักคือ "เก็บข้อมูล" Python มี `@dataclass` ที่สร้าง `__init__`, `__repr__`, `__eq__` ให้อัตโนมัติ

```python
from dataclasses import dataclass, field, asdict


@dataclass
class Product:
    """สินค้า 1 รายการ (เขียนด้วย dataclass สั้นกว่ามาก)"""

    code: str
    name: str
    price: float
    stock: int = 0
    category: str = "ทั่วไป"
    tags: list[str] = field(default_factory=list)   # ★ ค่าเริ่มต้นที่เป็น list ต้องใช้ field

    VAT_RATE = 0.07
    LOW_STOCK_LIMIT = 10

    def __post_init__(self) -> None:
        """ทำงานหลัง __init__ ใช้ตรวจสอบและปรับค่า"""
        self.code = self.code.strip().upper()
        self.name = self.name.strip()
        if self.price < 0:
            raise ValueError("ราคาต้องไม่ติดลบ")

    @property
    def stock_value(self) -> float:
        return self.price * self.stock

    def status(self) -> str:
        if self.stock <= 0:
            return "สินค้าหมด"
        if self.stock < self.LOW_STOCK_LIMIT:
            return "ใกล้หมด"
        return "ปกติ"


p = Product("prd-001", " เมาส์ไร้สาย ", 890, 25, "อุปกรณ์เสริม")

print(p)                  # Product(code='PRD-001', name='เมาส์ไร้สาย', ...)  ← __repr__ ให้ฟรี
print(p.stock_value)      # 22250.0
print(asdict(p))          # แปลงเป็น dict ได้ทันที (สะดวกมากตอนเขียนลง JSON/CSV)

# __eq__ ให้ฟรี: เทียบค่าทุกฟิลด์
p2 = Product("PRD-001", "เมาส์ไร้สาย", 890, 25, "อุปกรณ์เสริม")
print(p == p2)            # True
```

| เขียนเอง | ใช้ `@dataclass` |
| --- | --- |
| ต้องเขียน `__init__` เอง 10 บรรทัด | สร้างให้อัตโนมัติจากการประกาศฟิลด์ |
| ต้องเขียน `__repr__` เอง | ได้ฟรี พร้อมแสดงทุกฟิลด์ |
| ต้องเขียน `__eq__` เอง | ได้ฟรี เทียบทุกฟิลด์ |
| แปลงเป็น dict ต้องทำเอง | `asdict(obj)` |
| ควบคุมทุกอย่างเองได้ละเอียด | เหมาะกับคลาสเก็บข้อมูลเป็นหลัก |

> 💡 **`@dataclass(frozen=True)`** จะทำให้ object แก้ค่าไม่ได้เลยหลังสร้าง (Immutable) เหมาะกับข้อมูลที่ไม่ควรเปลี่ยน เช่น รายการในใบเสร็จที่ออกไปแล้ว

---

### 🧪 Workshop 8.1 - ออกแบบคลาสสำหรับ PyShop Mini

> **เป้าหมาย:** เปลี่ยนจาก `dict` เป็น `class` เต็มรูปแบบ พร้อมคลาส `Inventory` ที่ดูแลรายการสินค้าทั้งหมด

**ไฟล์ `src/pyshop/product.py`**

```python
"""product.py - คลาสสินค้าและคลังสินค้าของ PyShop Mini (OOP)"""

from dataclasses import asdict, dataclass, field


@dataclass
class Product:
    """สินค้า 1 รายการในระบบ"""

    code: str
    name: str
    price: float
    stock: int = 0
    category: str = "ทั่วไป"

    VAT_RATE = 0.07
    LOW_STOCK_LIMIT = 10

    def __post_init__(self) -> None:
        self.code = self.code.strip().upper()
        self.name = self.name.strip()
        self.category = self.category.strip() or "ทั่วไป"
        if self.price < 0:
            raise ValueError(f"ราคาของ {self.name} ต้องไม่ติดลบ")
        if self.stock < 0:
            raise ValueError(f"จำนวนของ {self.name} ต้องไม่ติดลบ")

    # --- ค่าที่คำนวณได้ ---
    @property
    def stock_value(self) -> float:
        """มูลค่าคงคลังของสินค้ารายการนี้"""
        return self.price * self.stock

    @property
    def price_with_vat(self) -> float:
        """ราคาต่อหน่วยที่รวม VAT แล้ว"""
        return self.price * (1 + self.VAT_RATE)

    def status(self) -> str:
        """สถานะคงคลังในรูปข้อความ"""
        if self.stock <= 0:
            return "สินค้าหมด"
        if self.stock < self.LOW_STOCK_LIMIT:
            return "ใกล้หมด"
        return "ปกติ"

    # --- การเปลี่ยนแปลงสถานะ ---
    def restock(self, qty: int) -> None:
        """เติมสินค้าเข้าคลัง"""
        if qty <= 0:
            raise ValueError("จำนวนที่เติมต้องมากกว่า 0")
        self.stock += qty

    def sell(self, qty: int) -> float:
        """ขายสินค้าและคืนยอดเงินรวม VAT"""
        if qty <= 0:
            raise ValueError("จำนวนที่ขายต้องมากกว่า 0")
        if qty > self.stock:
            raise ValueError(f"{self.name} คงเหลือเพียง {self.stock} ชิ้น")
        self.stock -= qty
        return self.price_with_vat * qty

    def to_dict(self) -> dict:
        """แปลงเป็น dict สำหรับบันทึกลงไฟล์หรือฐานข้อมูล"""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        """สร้าง Product จาก dict (เช่นแถวที่อ่านมาจาก CSV)"""
        return cls(
            code=str(data["code"]),
            name=str(data["name"]),
            price=float(data["price"]),
            stock=int(data["stock"]),
            category=str(data.get("category", "ทั่วไป")),
        )

    def __str__(self) -> str:
        return f"{self.code} {self.name} ({self.price:,.0f} บาท x {self.stock})"


@dataclass
class Inventory:
    """คลังสินค้า - ดูแลรายการสินค้าทั้งหมด"""

    items: list[Product] = field(default_factory=list)

    # --- ทำให้ใช้งานเหมือน list ได้ ---
    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    # --- การจัดการรายการ ---
    def add(self, product: Product) -> None:
        """เพิ่มสินค้าใหม่ (ถ้ารหัสซ้ำจะเติมจำนวนแทน)"""
        existing = self.find(product.code)
        if existing:
            existing.restock(product.stock)
            return
        self.items.append(product)

    def remove(self, code: str) -> bool:
        """ลบสินค้าตามรหัส คืน True ถ้าลบสำเร็จ"""
        product = self.find(code)
        if product is None:
            return False
        self.items.remove(product)
        return True

    def find(self, code: str) -> Product | None:
        """ค้นหาสินค้าจากรหัสแบบตรงตัว"""
        target = code.strip().upper()
        return next((p for p in self.items if p.code == target), None)

    def search(self, keyword: str) -> list[Product]:
        """ค้นหาจากคำค้นหา (ตรวจทั้งรหัสและชื่อ)"""
        key = keyword.strip().lower()
        if not key:
            return list(self.items)
        return [p for p in self.items if key in p.name.lower() or key in p.code.lower()]

    # --- รายงานสรุป ---
    @property
    def total_value(self) -> float:
        return sum(p.stock_value for p in self.items)

    @property
    def total_quantity(self) -> int:
        return sum(p.stock for p in self.items)

    def low_stock(self) -> list[Product]:
        return [p for p in self.items if p.stock < Product.LOW_STOCK_LIMIT]

    def by_category(self) -> dict[str, float]:
        summary: dict[str, float] = {}
        for product in self.items:
            summary[product.category] = summary.get(product.category, 0.0) + product.stock_value
        return summary

    def sorted_by(self, key: str = "price", reverse: bool = False) -> list[Product]:
        """เรียงลำดับสินค้าตามฟิลด์ที่ระบุ"""
        return sorted(self.items, key=lambda p: getattr(p, key), reverse=reverse)


if __name__ == "__main__":
    inv = Inventory()
    inv.add(Product("PRD-001", "เมาส์ไร้สาย", 890, 25, "อุปกรณ์เสริม"))
    inv.add(Product("PRD-002", "คีย์บอร์ด", 1290, 8, "อุปกรณ์เสริม"))
    inv.add(Product("PRD-003", "จอภาพ 27 นิ้ว", 6900, 0, "จอแสดงผล"))

    for product in inv:
        print(f"{product}  →  {product.status()}")

    print(f"\nรวม {len(inv)} รายการ มูลค่า {inv.total_value:,.2f} บาท")
    print(f"ต้องสั่งเพิ่ม: {[p.name for p in inv.low_stock()]}")

    income = inv.find("PRD-001").sell(5)
    print(f"ขายเมาส์ 5 ชิ้น ได้ {income:,.2f} บาท (รวม VAT)")
```

**รันทดสอบ**

```powershell
uv run -m src.pyshop.product
```

> ✅ **ผลลัพธ์ที่คาดหวัง:** เห็นรายการสินค้า 3 รายการพร้อมสถานะ, มูลค่ารวม, รายการที่ต้องสั่งเพิ่ม (คีย์บอร์ด, จอภาพ) และผลการขาย
>
> 💡 **สังเกตความต่างจากเมื่อวาน:** `inv.find("PRD-001").sell(5)` อ่านแล้วเข้าใจทันทีว่าทำอะไร ต่างจากเมื่อวานที่ต้องเขียน `product["stock"] = product["stock"] - 5` และไม่มีอะไรกันไม่ให้ขายเกินจำนวนที่มี
>
> 🏋️ **โจทย์ต่อยอด:** สร้างคลาสลูก `DigitalProduct(Product)` ที่ไม่จำกัดสต็อกและไม่มีค่าจัดส่ง แล้วเพิ่มเข้า `Inventory` เดียวกัน สังเกตว่า `Inventory` ทำงานกับทั้งสองคลาสได้โดยไม่ต้องแก้อะไรเลย

---

## 📚 Module 9: การจัดการข้อผิดพลาดของโปรแกรมและการ Debug

### เวลา 13:00-13:45 น.

> 💡 **หัวใจของ Module นี้:** โปรแกรมมืออาชีพไม่ใช่โปรแกรมที่ไม่มีข้อผิดพลาด แต่คือโปรแกรมที่ **รับมือกับข้อผิดพลาดได้อย่างสง่างาม** บอกผู้ใช้ว่าเกิดอะไรขึ้น และไม่ทำให้ข้อมูลเสียหาย

---

### 9.1 ประเภทของ Error ใน Python

```
Error มี 2 ประเภทใหญ่:

  1. Syntax Error (ไวยากรณ์ผิด)        2. Exception (รันไปแล้วเกิดปัญหา)
     - เกิดตอน Python อ่านโค้ด            - เกิดตอนโปรแกรมทำงาน
     - โปรแกรมไม่เริ่มทำงานเลย            - โปรแกรมทำงานไปแล้วส่วนหนึ่ง
     - เช่น ลืม : ลืมวงเล็บ                - เช่น หารด้วยศูนย์, ไฟล์ไม่มี
     - ★ แก้ได้ก่อนรัน                     - ★ ต้องเขียนโค้ดดักไว้
```

| Exception | เกิดเมื่อ | ตัวอย่าง |
| --- | --- | --- |
| `ValueError` | ชนิดถูกแต่ค่าไม่ถูก | `int("abc")` |
| `TypeError` | ชนิดข้อมูลผิด | `"5" + 5` |
| `KeyError` | ไม่มี key ใน dict | `product["brand"]` ทั้งที่ไม่มี |
| `IndexError` | ตำแหน่งเกินขอบเขต | `items[99]` ทั้งที่มี 5 ตัว |
| `FileNotFoundError` | เปิดไฟล์ที่ไม่มี | `open("missing.csv")` |
| `ZeroDivisionError` | หารด้วยศูนย์ | `10 / 0` |
| `AttributeError` | เรียก attribute/method ที่ไม่มี | `"abc".push()` |
| `ImportError` | import ไม่ได้ | ยังไม่ได้ `uv add` |
| `PermissionError` | ไม่มีสิทธิ์เข้าถึงไฟล์ | เขียนไฟล์ที่เปิดอยู่ใน Excel |

### 9.2 try / except / else / finally

```python
try:
    # โค้ดที่อาจเกิดข้อผิดพลาด
    price = float(input("ราคา: "))
    qty = int(input("จำนวน: "))
    total = price * qty

except ValueError as e:
    # ทำงานเมื่อเกิด ValueError
    print(f"  ⚠ กรุณาใส่ตัวเลขเท่านั้น ({e})")

except (TypeError, KeyError) as e:
    # จับหลายชนิดพร้อมกันได้
    print(f"  ⚠ ข้อมูลไม่ถูกต้อง: {e}")

else:
    # ทำงานเมื่อ "ไม่เกิด" ข้อผิดพลาดเลย
    print(f"  ✅ ยอดรวม {total:,.2f} บาท")

finally:
    # ทำงานเสมอ ไม่ว่าจะเกิดหรือไม่เกิดข้อผิดพลาด
    print("  จบการคำนวณ")
```

```
ลำดับการทำงาน:

           ┌─────────┐
           │  try:   │
           └────┬────┘
        ┌───────┴────────┐
   เกิด error        ไม่เกิด error
        │                │
        ▼                ▼
   ┌─────────┐      ┌─────────┐
   │ except: │      │  else:  │
   └────┬────┘      └────┬────┘
        └───────┬────────┘
                ▼
          ┌───────────┐
          │ finally:  │  ← ทำงานเสมอ (ใช้ปิดไฟล์/ปิดการเชื่อมต่อ)
          └───────────┘
```

### 9.3 หลักการเขียน except ที่ถูกต้อง

```python
# ❌ แย่ที่สุด: จับทุกอย่างแล้วเงียบ (บั๊กหายเข้ากลีบเมฆ)
try:
    process_data()
except:
    pass

# ❌ ยังไม่ดี: จับกว้างเกินไป ไม่รู้ว่าเกิดอะไร
try:
    process_data()
except Exception:
    print("เกิดข้อผิดพลาด")

# ✅ ดี: จับเฉพาะที่คาดไว้ และบอกรายละเอียด
try:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"  ⚠ ไม่พบไฟล์ {path} จะเริ่มด้วยข้อมูลว่าง")
    data = []
except json.JSONDecodeError as e:
    print(f"  ⚠ ไฟล์ {path} เสียหายที่บรรทัด {e.lineno}: {e.msg}")
    data = []
```

> ⚠️ **กฎเหล็ก 3 ข้อ:**
>
> 1. **จับให้แคบที่สุดเท่าที่รู้** ระบุชนิด Exception ที่คาดว่าจะเกิด
> 2. **อย่าใช้ `except: pass`** เพราะจะกลืนแม้กระทั่ง `KeyboardInterrupt` ตอนกด Ctrl+C
> 3. **จับแล้วต้องทำอะไรสักอย่าง** ไม่ว่าจะแจ้งผู้ใช้ บันทึก log หรือใช้ค่าสำรอง

### 9.4 การสร้าง Exception ของตนเอง

```python
# --- นิยาม Exception เฉพาะของระบบเรา ---
class PyShopError(Exception):
    """คลาสแม่ของข้อผิดพลาดทั้งหมดใน PyShop Mini"""


class ProductNotFoundError(PyShopError):
    """ไม่พบสินค้าตามรหัสที่ระบุ"""

    def __init__(self, code: str) -> None:
        self.code = code
        super().__init__(f"ไม่พบสินค้ารหัส {code}")


class InsufficientStockError(PyShopError):
    """สินค้าคงเหลือไม่พอสำหรับการขาย"""

    def __init__(self, name: str, requested: int, available: int) -> None:
        self.name = name
        self.requested = requested
        self.available = available
        super().__init__(
            f"{name}: ต้องการ {requested} ชิ้น แต่คงเหลือเพียง {available} ชิ้น"
        )


# --- การใช้งาน ---
def sell_product(inventory, code: str, qty: int) -> float:
    product = inventory.find(code)
    if product is None:
        raise ProductNotFoundError(code)
    if qty > product.stock:
        raise InsufficientStockError(product.name, qty, product.stock)
    return product.sell(qty)


# --- ฝั่งผู้เรียกใช้ ---
try:
    income = sell_product(inv, "PRD-999", 5)
except ProductNotFoundError as e:
    print(f"  ⚠ {e} (รหัสที่ค้นหา: {e.code})")
except InsufficientStockError as e:
    print(f"  ⚠ {e}")
    print(f"     ขายได้สูงสุด {e.available} ชิ้น")
except PyShopError as e:
    print(f"  ⚠ ข้อผิดพลาดของระบบ: {e}")
```

> 💡 **ทำไมต้องสร้าง Exception เอง:** เพราะทำให้ผู้เรียกใช้ **แยกแยะสาเหตุได้อย่างแม่นยำ** และแนบข้อมูลเพิ่มเติมไปด้วยได้ (เช่น `e.available`) การใช้ `ValueError` กับทุกกรณีทำให้แยกไม่ออกว่าผิดพลาดเพราะอะไร

**การ `raise` และการส่งต่อ**

```python
# ส่ง Exception ขึ้นไปพร้อมบอกต้นเหตุเดิม
try:
    value = int(text)
except ValueError as e:
    raise ProductNotFoundError(text) from e     # ★ from e เก็บ traceback เดิมไว้

# จับแล้วส่งต่อโดยไม่แก้ไข
try:
    risky()
except PyShopError:
    write_log("เกิดข้อผิดพลาดในระบบ")
    raise                                        # ส่งต่อตัวเดิมขึ้นไป
```

### 9.5 การใช้ logging แทน print

`print()` เหมาะกับการคุยกับผู้ใช้ แต่ไม่เหมาะกับการบันทึกเหตุการณ์ของระบบ

| ประเด็น | `print()` | `logging` |
| --- | --- | --- |
| ระดับความสำคัญ | ไม่มี | มี 5 ระดับ กรองได้ |
| เวลาที่เกิด | ต้องใส่เอง | มีให้อัตโนมัติ |
| บันทึกลงไฟล์ | ต้องเขียนเอง | ตั้งค่าครั้งเดียว |
| ปิดตอน Production | ต้องไล่ลบทีละบรรทัด | เปลี่ยนระดับเดียวจบ |
| รู้ว่ามาจากไฟล์ไหน | ไม่รู้ | บอกชื่อโมดูลให้ |

```python
import logging
from pathlib import Path

# --- ตั้งค่าครั้งเดียวตอนเริ่มโปรแกรม (ปกติอยู่ใน main.py) ---
LOG_PATH = Path("data/pyshop.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding="utf-8"),   # บันทึกลงไฟล์
        logging.StreamHandler(),                            # แสดงบนหน้าจอด้วย
    ],
)

logger = logging.getLogger(__name__)

# --- การใช้งาน ---
logger.debug("ค่าตัวแปร inventory = %s", inventory)        # รายละเอียดสำหรับดีบัก
logger.info("เริ่มระบบ PyShop Mini")                        # เหตุการณ์ปกติ
logger.warning("สินค้า %s ใกล้หมด (เหลือ %d)", name, stock) # เตือน แต่ยังทำงานได้
logger.error("บันทึกไฟล์ไม่สำเร็จ: %s", path)               # ผิดพลาด ทำงานต่อไม่ได้บางส่วน
logger.critical("เชื่อมต่อฐานข้อมูลไม่ได้ ระบบหยุดทำงาน")     # ร้ายแรงที่สุด

# ★ บันทึก traceback เต็มเมื่ออยู่ในบล็อก except
try:
    risky_operation()
except Exception:
    logger.exception("เกิดข้อผิดพลาดที่ไม่คาดคิด")   # แนบ stack trace ให้อัตโนมัติ
```

| ระดับ | ค่าตัวเลข | ใช้เมื่อ |
| --- | --- | --- |
| `DEBUG` | 10 | รายละเอียดปลีกย่อยตอนพัฒนา |
| `INFO` | 20 | เหตุการณ์ปกติที่ควรบันทึก |
| `WARNING` | 30 | ผิดปกติแต่ยังไปต่อได้ |
| `ERROR` | 40 | ทำงานส่วนนั้นไม่สำเร็จ |
| `CRITICAL` | 50 | ระบบทำงานต่อไม่ได้ |

> 💡 **เคล็ดลับ:** ใช้ `logger.info("ค่า %s", value)` แทน `logger.info(f"ค่า {value}")` เพราะแบบแรกจะไม่เสียเวลาแปลงข้อความหากระดับ log นั้นถูกปิดอยู่

### 9.6 การ Debug ด้วย Visual Studio Code

การใช้ `print()` ไล่หาบั๊กได้ผลแต่ช้า Debugger ให้คุณหยุดโปรแกรมกลางคันแล้วส่องดูค่าทุกตัวแปรพร้อมกัน

**ขั้นตอนการใช้งาน**

| ขั้น | การทำ | ผลที่ได้ |
| --- | --- | --- |
| 1 | คลิกที่ช่องว่างซ้ายเลขบรรทัด จะได้จุดแดง (**Breakpoint**) | โปรแกรมจะหยุดที่บรรทัดนี้ |
| 2 | กด `F5` เลือก `Python File` | เริ่มรันในโหมด Debug |
| 3 | ดูแผง **VARIABLES** ด้านซ้าย | เห็นค่าทุกตัวแปร ณ จุดนั้น |
| 4 | เพิ่มนิพจน์ในแผง **WATCH** | เฝ้าดูค่าที่สนใจโดยเฉพาะ |
| 5 | ใช้ปุ่มควบคุมด้านบน | เดินโปรแกรมทีละก้าว |

**ปุ่มควบคุมที่ต้องรู้**

| ปุ่ม | คีย์ลัด | ทำอะไร |
| --- | --- | --- |
| Continue | `F5` | วิ่งต่อจนถึง Breakpoint ถัดไป |
| Step Over | `F10` | ทำบรรทัดนี้จบแล้วไปบรรทัดถัดไป (ไม่เข้าไปในฟังก์ชัน) |
| Step Into | `F11` | ★ เข้าไปดูข้างในฟังก์ชันที่ถูกเรียก |
| Step Out | `Shift + F11` | ออกจากฟังก์ชันปัจจุบันกลับไปที่ผู้เรียก |
| Restart | `Ctrl + Shift + F5` | เริ่มดีบักใหม่ |
| Stop | `Shift + F5` | หยุด |

**ไฟล์ `.vscode/launch.json` สำหรับโปรเจกต์ที่ใช้ uv**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "PyShop Mini",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/main.py",
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}",
      "justMyCode": true
    }
  ]
}
```

> 💡 **Conditional Breakpoint - เทคนิคที่ช่วยประหยัดเวลามาก:** คลิกขวาที่จุดแดง เลือก `Edit Breakpoint` แล้วใส่เงื่อนไข เช่น `product.stock < 0` โปรแกรมจะหยุดเฉพาะตอนที่เงื่อนไขเป็นจริงเท่านั้น แทนที่จะต้องกด Continue ผ่านข้อมูลปกติเป็นร้อยรอบ

### 9.7 การอ่าน Traceback ให้เป็น

```
Traceback (most recent call last):
  File "main.py", line 45, in <module>
    main()
  File "main.py", line 38, in main
    income = sell_product(inv, "PRD-001", 100)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "src\pyshop\service.py", line 22, in sell_product
    return product.sell(qty)
           ^^^^^^^^^^^^^^^^^
  File "src\pyshop\product.py", line 58, in sell
    raise ValueError(f"{self.name} คงเหลือเพียง {self.stock} ชิ้น")
ValueError: เมาส์ไร้สาย คงเหลือเพียง 25 ชิ้น
```

**วิธีอ่านที่ถูกต้อง**

1. **อ่านบรรทัดล่างสุดก่อน** เพราะบอกชนิดและข้อความของ Error (`ValueError: เมาส์ไร้สาย คงเหลือเพียง 25 ชิ้น`)
2. **ไล่ขึ้นจากล่างไปบน** เพื่อดูว่าโค้ดของเราบรรทัดไหนเป็นต้นเหตุ (`product.py` บรรทัด 58)
3. **บนสุดคือจุดเริ่มต้น** ของสายการเรียก
4. ถ้าบรรทัดล่าง ๆ เป็นไฟล์ในไลบรารีภายนอก ให้ไล่ขึ้นมาหาไฟล์ในโปรเจกต์เราที่อยู่ใกล้ที่สุด นั่นคือจุดที่เราควรแก้

---

### 🧪 Workshop 9.1 - ไล่หาสาเหตุของ Bug ด้วย Debugger

> **เป้าหมาย:** ฝึกใช้ Debugger กับโปรแกรมที่มีบั๊กจริง แทนการเดาด้วย `print()`

**ไฟล์ `workshop9_bug.py` - โปรแกรมที่มีบั๊ก 3 จุด**

```python
"""workshop9_bug.py - โปรแกรมคำนวณส่วนลดที่มีบั๊กซ่อนอยู่ 3 จุด"""

orders = [
    {"code": "PRD-001", "name": "เมาส์ไร้สาย", "price": 890, "qty": 3},
    {"code": "PRD-002", "name": "คีย์บอร์ด", "price": 1290, "qty": 0},
    {"code": "PRD-003", "name": "จอภาพ", "price": "6900", "qty": 1},
    {"code": "PRD-004", "name": "หูฟัง", "price": 1590, "qty": 2},
]


def discount_rate(qty):
    """คืนอัตราส่วนลดตามจำนวนที่ซื้อ"""
    if qty >= 10:
        return 0.15
    elif qty >= 5:
        return 0.10
    elif qty >= 3:
        return 0.05


def calculate_line(order):
    """คำนวณยอดของรายการเดียว"""
    subtotal = order["price"] * order["qty"]
    rate = discount_rate(order["qty"])
    discount = subtotal * rate
    return subtotal - discount


def average_price(orders):
    """ราคาเฉลี่ยต่อชิ้น"""
    total_amount = sum(o["price"] * o["qty"] for o in orders)
    total_qty = sum(o["qty"] for o in orders if o["qty"] > 0)
    return total_amount / total_qty


def main():
    grand_total = 0
    for order in orders:
        line_total = calculate_line(order)
        print(f"{order['name']:<15} {line_total:>12,.2f}")
        grand_total += line_total

    print(f"{'รวมทั้งสิ้น':<15} {grand_total:>12,.2f}")
    print(f"ราคาเฉลี่ยต่อชิ้น {average_price(orders):,.2f}")


if __name__ == "__main__":
    main()
```

**ขั้นตอนการหาบั๊ก**

1. รัน `uv run workshop9_bug.py` แล้วอ่าน Traceback บรรทัดล่างสุด
2. วาง Breakpoint ที่บรรทัดแรกของ `calculate_line()` แล้วกด `F5`
3. กด `F10` ทีละบรรทัด สังเกตค่าของ `subtotal`, `rate`, `discount` ในแผง VARIABLES
4. เมื่อเจอบรรทัดที่ค่าผิดคาด ให้กด `F11` เข้าไปดูข้างในฟังก์ชันนั้น

**เฉลยบั๊กทั้ง 3 จุด**

| จุด | อาการ | สาเหตุ | วิธีแก้ |
| --- | --- | --- | --- |
| 1 | `TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'` ที่รายการคีย์บอร์ด | `discount_rate()` ไม่มี `return` สำหรับกรณี `qty < 3` จึงคืน `None` แล้วถูกนำไปคูณ | เพิ่ม `return 0.0` เป็นบรรทัดสุดท้าย (หรือใช้ `else:`) |
| 2 | แก้บั๊กที่ 1 แล้วรันต่อ เจอ `TypeError: can't multiply sequence by non-int of type 'float'` ที่รายการจอภาพ | `price` ของ PRD-003 เป็น `str` `"6900"` การคูณ str ด้วย int คือการทำซ้ำข้อความ (`"6900" * 2` ได้ `"69006900"`) จึงกลายเป็น str แล้วคูณ float ต่อไม่ได้ | แปลงชนิดตอนอ่านข้อมูล `float(order["price"])` หรือใช้คลาส `Product` ที่ตรวจสอบใน `__post_init__` |
| 3 | ค่าเฉลี่ยผิด (หารด้วยตัวหารที่ไม่ตรงกับตัวตั้ง) | `total_amount` รวมทุกแถวรวมแถวที่ `qty = 0` แต่ `total_qty` กรองแถวนั้นออก | ใช้เงื่อนไขกรองเดียวกันทั้งสองบรรทัด และเพิ่มการกัน `ZeroDivisionError` |

**เวอร์ชันที่แก้แล้ว**

```python
def discount_rate(qty: int) -> float:
    """คืนอัตราส่วนลดตามจำนวนที่ซื้อ (0.0 ถ้าไม่เข้าเงื่อนไข)"""
    if qty >= 10:
        return 0.15
    if qty >= 5:
        return 0.10
    if qty >= 3:
        return 0.05
    return 0.0                       # ★ แก้บั๊กที่ 1


def calculate_line(order: dict) -> float:
    """คำนวณยอดของรายการเดียวหลังหักส่วนลด"""
    try:
        price = float(order["price"])    # ★ แก้บั๊กที่ 2
        qty = int(order["qty"])
    except (ValueError, TypeError, KeyError) as e:
        raise ValueError(f"ข้อมูลรายการ {order.get('code', '?')} ไม่ถูกต้อง") from e

    subtotal = price * qty
    return subtotal * (1 - discount_rate(qty))


def average_price(orders: list[dict]) -> float:
    """ราคาเฉลี่ยต่อชิ้นของรายการที่มีจำนวนมากกว่า 0"""
    valid = [o for o in orders if int(o["qty"]) > 0]      # ★ แก้บั๊กที่ 3
    total_qty = sum(int(o["qty"]) for o in valid)
    if total_qty == 0:
        return 0.0
    total_amount = sum(float(o["price"]) * int(o["qty"]) for o in valid)
    return total_amount / total_qty
```

> ✅ **บทเรียนจาก Workshop นี้:** บั๊กทั้งสามจุดนี้ไม่มีอันไหนที่ Python เตือนตอนเขียนโค้ด แต่ทั้งหมดหาเจอได้ภายในไม่กี่นาทีด้วย Debugger **สังเกตว่าถ้าเราใช้คลาส `Product` จาก Module 8 บั๊กที่ 2 จะไม่มีทางเกิดเลย** เพราะ `__post_init__` แปลงชนิดและตรวจสอบให้ตั้งแต่ตอนสร้าง object

---

## 📚 Module 10: การเขียน Python ติดต่อฐานข้อมูล PostgreSQL

### เวลา 13:45-14:45 น.

> 💡 **หัวใจของ Module นี้:** ไฟล์ CSV ใช้ได้ดีกับข้อมูลไม่กี่ร้อยแถวและคนใช้คนเดียว แต่เมื่อข้อมูลเป็นหมื่นแถว มีหลายคนใช้พร้อมกัน และต้องค้นหาซับซ้อน **ฐานข้อมูลคือคำตอบ** Module นี้จะพาเชื่อม Python เข้ากับ PostgreSQL อย่างถูกวิธีและปลอดภัย

---

### 10.1 ทำไมต้องใช้ฐานข้อมูล

| ประเด็น | ไฟล์ CSV/JSON | ฐานข้อมูล (PostgreSQL) |
| --- | --- | --- |
| ปริมาณข้อมูล | เหมาะกับหลักพันแถว | หลักล้านแถวขึ้นไป |
| ค้นหาเฉพาะแถว | ต้องอ่านทั้งไฟล์ | ใช้ Index ค้นตรงจุด เร็วมาก |
| หลายคนใช้พร้อมกัน | ❌ ทับกันแน่นอน | ✅ จัดการให้ |
| ความถูกต้องของข้อมูล | ต้องตรวจเองทั้งหมด | มี Constraint บังคับให้ |
| ยกเลิกเมื่อผิดพลาดกลางคัน | ทำเองยากมาก | ✅ Transaction |
| ความปลอดภัย | ใครเปิดไฟล์ได้ก็อ่านได้หมด | กำหนดสิทธิ์รายผู้ใช้ |

> 💡 **หลักสูตรนี้เลือก PostgreSQL** เพราะเป็นฐานข้อมูลโอเพนซอร์สที่ทำตามมาตรฐาน SQL ได้ครบถ้วนที่สุด รองรับ JSON ในตัว และเป็นที่นิยมสูงมากในงานสมัยใหม่ ส่วนผู้ที่ใช้ **MySQL** อยู่แล้ว แนวคิดทุกอย่างในโมดูลนี้ใช้ได้เหมือนกัน เปลี่ยนเพียงไลบรารีเป็น `mysql-connector-python` และตัวยึดตำแหน่งค่ายังคงเป็น `%s` เช่นเดียวกัน

### 10.2 การติดตั้ง PostgreSQL

**Windows** ดาวน์โหลดตัวติดตั้งจาก postgresql.org/download/windows แล้วติดตั้งโดยจดจำค่าเหล่านี้ไว้:

| ค่าที่ต้องจำ | ค่าเริ่มต้น | หมายเหตุ |
| --- | --- | --- |
| Port | `5432` | ถ้าถูกใช้อยู่แล้วจะเปลี่ยนเป็น 5433 |
| Username | `postgres` | ผู้ใช้ระดับผู้ดูแลระบบ |
| Password | (ที่คุณตั้งเอง) | ⚠️ **จดไว้ให้ดี ลืมแล้วรีเซ็ตยุ่งยาก** |
| Locale | `Default locale` | |

ตัวติดตั้งจะให้เครื่องมือ **pgAdmin 4** มาด้วย ใช้จัดการฐานข้อมูลผ่านหน้าเว็บได้สะดวก

**ตรวจสอบว่าติดตั้งสำเร็จ** เปิด PowerShell แล้วรัน:

```powershell
psql --version
```

> 💡 **ถ้าคำสั่ง `psql` ใช้ไม่ได้** ให้เพิ่ม `C:\Program Files\PostgreSQL\17\bin` เข้าไปใน Path ของ Environment Variables หรือใช้ pgAdmin แทนก็ได้ (ไม่กระทบกับการเขียน Python)

**สร้างฐานข้อมูลสำหรับหลักสูตร**

```powershell
# เข้าสู่ psql ด้วยผู้ใช้ postgres
psql -U postgres
```

```sql
-- สร้างฐานข้อมูลและผู้ใช้สำหรับโปรเจกต์
CREATE DATABASE pyshop_db;
CREATE USER pyshop_user WITH PASSWORD 'ตั้งรหัสผ่านของคุณเอง';
GRANT ALL PRIVILEGES ON DATABASE pyshop_db TO pyshop_user;

-- เชื่อมต่อเข้าฐานข้อมูลที่สร้าง
\c pyshop_db

-- ให้สิทธิ์บน schema public (จำเป็นตั้งแต่ PostgreSQL 15 ขึ้นไป)
GRANT ALL ON SCHEMA public TO pyshop_user;

-- ออกจาก psql
\q
```

### 10.3 การสร้างตาราง

```sql
CREATE TABLE IF NOT EXISTS products (
    id          SERIAL PRIMARY KEY,
    code        VARCHAR(20)    NOT NULL UNIQUE,
    name        VARCHAR(200)   NOT NULL,
    price       NUMERIC(12, 2) NOT NULL CHECK (price >= 0),
    stock       INTEGER        NOT NULL DEFAULT 0 CHECK (stock >= 0),
    category    VARCHAR(100)   NOT NULL DEFAULT 'ทั่วไป',
    created_at  TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Index ช่วยให้ค้นหาตามหมวดหมู่เร็วขึ้นมากเมื่อข้อมูลเยอะ
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
```

| คำสั่ง/ข้อกำหนด | ความหมาย |
| --- | --- |
| `SERIAL PRIMARY KEY` | เลขลำดับที่เพิ่มอัตโนมัติ และเป็นตัวระบุแถวที่ไม่ซ้ำ |
| `NOT NULL` | ห้ามเว้นว่าง |
| `UNIQUE` | ห้ามซ้ำในตาราง (รหัสสินค้าต้องไม่ซ้ำ) |
| `CHECK (price >= 0)` | ★ ฐานข้อมูลบังคับกฎธุรกิจให้ แม้โปรแกรมเผลอส่งค่าติดลบก็ใส่ไม่ได้ |
| `DEFAULT` | ค่าเริ่มต้นเมื่อไม่ระบุ |
| `NUMERIC(12, 2)` | ตัวเลข 12 หลัก ทศนิยม 2 ตำแหน่ง (แม่นยำกว่า float สำหรับเงิน) |

> 💡 **ทำไมเงินต้องใช้ `NUMERIC` ไม่ใช่ `FLOAT`:** เพราะ float มีความคลาดเคลื่อนในการเก็บทศนิยม (`0.1 + 0.2 != 0.3`) ซึ่งยอมรับไม่ได้ในงานการเงิน `NUMERIC` เก็บค่าแบบแม่นยำเป๊ะ

### 10.4 การติดตั้ง Driver ด้วย uv

```powershell
# psycopg 3 (เวอร์ชันปัจจุบัน) แบบ binary ไม่ต้องคอมไพล์เอง เหมาะกับ Windows
uv add "psycopg[binary]"

# ถ้าต้องการโหลดค่าตั้งค่าจากไฟล์ .env ด้วย
uv add python-dotenv
```

| ฐานข้อมูล | ไลบรารี | คำสั่งติดตั้ง |
| --- | --- | --- |
| PostgreSQL | `psycopg` (v3) | `uv add "psycopg[binary]"` |
| PostgreSQL (เก่า) | `psycopg2-binary` | `uv add psycopg2-binary` |
| MySQL / MariaDB | `mysql-connector-python` | `uv add mysql-connector-python` |
| SQLite | มากับ Python | ไม่ต้องติดตั้ง (`import sqlite3`) |

### 10.5 การเก็บข้อมูลการเชื่อมต่ออย่างปลอดภัย

> ⚠️ **ห้ามเขียนรหัสผ่านลงในโค้ดเด็ดขาด** เพราะโค้ดจะถูกอัปขึ้น Git แล้วรหัสผ่านหลุด ให้เก็บไว้ในไฟล์ `.env` ที่ **ไม่ขึ้น Git**

**ไฟล์ `.env`** (เพิ่มบรรทัด `.env` ลงใน `.gitignore` ทันที)

```ini
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pyshop_db
DB_USER=pyshop_user
DB_PASSWORD=รหัสผ่านของคุณ
```

**ไฟล์ `.env.example`** (อันนี้ขึ้น Git ได้ ให้เพื่อนรู้ว่าต้องตั้งค่าอะไรบ้าง)

```ini
DB_HOST=localhost
DB_PORT=5432
DB_NAME=pyshop_db
DB_USER=your_username
DB_PASSWORD=your_password
```

```python
import os
from dotenv import load_dotenv

load_dotenv()      # อ่านค่าจากไฟล์ .env เข้าสู่ Environment Variables

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "dbname": os.getenv("DB_NAME", "pyshop_db"),
    "user": os.getenv("DB_USER", "pyshop_user"),
    "password": os.getenv("DB_PASSWORD", ""),
}
```

### 10.6 การเชื่อมต่อและสั่งงาน SQL

```python
import psycopg
from psycopg.rows import dict_row

# ★ ใช้ with ทั้งกับ connection และ cursor เพื่อให้ปิดให้อัตโนมัติเสมอ
with psycopg.connect(**DB_CONFIG, row_factory=dict_row) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT code, name, price, stock FROM products ORDER BY code")
        rows = cur.fetchall()

for row in rows:
    print(f"{row['code']} {row['name']} {row['price']:,.2f}")
```

```
ลำดับชั้นของการทำงานกับฐานข้อมูล:

  Connection (การเชื่อมต่อ)          ← เปิดครั้งเดียว ใช้ได้หลายคำสั่ง
      └── Cursor (ตัวชี้)             ← ใช้ส่งคำสั่ง SQL และรับผลลัพธ์
              └── execute()          ← ส่ง SQL 1 คำสั่ง
                      └── fetchall() ← ดึงผลลัพธ์กลับมา
      └── commit() / rollback()      ← ยืนยัน / ยกเลิกการเปลี่ยนแปลง
```

| เมธอด | คืนอะไร | ใช้เมื่อ |
| --- | --- | --- |
| `cur.fetchone()` | 1 แถว หรือ `None` | คาดว่าได้ผลแถวเดียว |
| `cur.fetchall()` | list ของทุกแถว | ผลลัพธ์ไม่มากเกินไป |
| `cur.fetchmany(n)` | list จำนวน n แถว | แบ่งดึงทีละชุด |
| `cur.rowcount` | จำนวนแถวที่กระทบ | ตรวจว่า UPDATE/DELETE โดนกี่แถว |

> 💡 **`row_factory=dict_row` มีประโยชน์มาก:** ปกติ psycopg คืนผลเป็น tuple ต้องอ้างด้วยตำแหน่ง (`row[0]`) ซึ่งอ่านยากและพังง่ายเมื่อลำดับคอลัมน์เปลี่ยน การใช้ `dict_row` ทำให้อ้างด้วยชื่อคอลัมน์ได้ (`row["name"]`)

### 10.7 Parameterized Query - ป้องกัน SQL Injection

**นี่คือหัวข้อที่สำคัญที่สุดของ Module นี้ในแง่ความปลอดภัย**

```python
# ❌❌❌ อันตรายที่สุด: ต่อข้อความ SQL เอง
code = input("รหัสสินค้า: ")
cur.execute(f"SELECT * FROM products WHERE code = '{code}'")

# ถ้าผู้ใช้พิมพ์:  ' OR '1'='1
# SQL จะกลายเป็น: SELECT * FROM products WHERE code = '' OR '1'='1'
#                  → ดึงข้อมูลทั้งตารางออกมา!
#
# ถ้าผู้ใช้พิมพ์:  '; DROP TABLE products; --
#                  → ตารางหายทั้งตาราง!
```

```python
# ✅✅✅ ถูกต้อง: ใช้ %s เป็นตัวยึดตำแหน่ง แล้วส่งค่าเป็น tuple แยกต่างหาก
cur.execute("SELECT * FROM products WHERE code = %s", (code,))
#                                              ↑         ↑
#                                     ตัวยึดตำแหน่ง   ★ ต้องเป็น tuple (มีคอมมา)
```

```
กลไกที่ทำให้ปลอดภัย:

  แบบต่อข้อความเอง:                    แบบ Parameterized:
  ┌────────────────────────┐          ┌────────────────────────┐
  │ ค่าที่ผู้ใช้พิมพ์ กลายเป็น │          │ SQL ถูกส่งไปก่อนแยกต่างหาก│
  │ "ส่วนหนึ่งของคำสั่ง SQL"  │   ⟶     │ ค่าถูกส่งตามทีหลัง        │
  │ → สั่งงานฐานข้อมูลได้     │          │ → ถูกมองเป็น "ข้อมูล"     │
  │                        │          │   เท่านั้น ไม่ใช่คำสั่ง    │
  └────────────────────────┘          └────────────────────────┘
```

```python
# ตัวอย่างการใช้งานที่ถูกต้องในกรณีต่าง ๆ
cur.execute(
    "INSERT INTO products (code, name, price, stock, category) VALUES (%s, %s, %s, %s, %s)",
    (code, name, price, stock, category),
)

cur.execute(
    "UPDATE products SET stock = %s, updated_at = CURRENT_TIMESTAMP WHERE code = %s",
    (new_stock, code),
)

# LIKE ก็ต้องใช้ตัวยึดตำแหน่ง ห้ามต่อข้อความ
cur.execute(
    "SELECT * FROM products WHERE name ILIKE %s",
    (f"%{keyword}%",),          # ★ ใส่ % รอบคำค้นในฝั่ง Python ไม่ใช่ใน SQL
)

# IN (...) หลายค่า
cur.execute(
    "SELECT * FROM products WHERE category = ANY(%s)",
    (["เสียง", "จอแสดงผล"],),
)
```

> ⚠️ **ข้อควรระวังที่พบบ่อย:** `(code)` **ไม่ใช่ tuple** แต่เป็นวงเล็บธรรมดา ต้องเขียน `(code,)` มีคอมมาปิดท้ายเสมอเมื่อมีค่าเดียว มิฉะนั้นจะเกิดข้อผิดพลาดเรื่องจำนวนพารามิเตอร์

### 10.8 Transaction - ทำสำเร็จทั้งหมด หรือไม่ทำเลย

```python
# ตัวอย่างที่ต้องใช้ Transaction: ขายสินค้า = ลดสต็อก + บันทึกใบเสร็จ
# ถ้าลดสต็อกสำเร็จแต่บันทึกใบเสร็จล้มเหลว ข้อมูลจะไม่ตรงกันทันที

conn = psycopg.connect(**DB_CONFIG)
try:
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE products SET stock = stock - %s WHERE code = %s AND stock >= %s",
            (qty, code, qty),
        )
        if cur.rowcount == 0:
            raise ValueError(f"สินค้า {code} คงเหลือไม่พอ")

        cur.execute(
            "INSERT INTO sales (product_code, qty, amount) VALUES (%s, %s, %s)",
            (code, qty, amount),
        )

    conn.commit()          # ★ ยืนยันทั้งสองคำสั่งพร้อมกัน
    print("✅ บันทึกการขายเรียบร้อย")

except Exception as e:
    conn.rollback()        # ★ ย้อนกลับทั้งหมด เหมือนไม่เคยเกิดอะไรขึ้น
    print(f"⚠ ยกเลิกรายการ: {e}")

finally:
    conn.close()
```

> ✅ **ข้อสำคัญของ psycopg 3:** เมื่อใช้ `with psycopg.connect(...) as conn:` ตัวไลบรารีจะ **commit ให้อัตโนมัติเมื่อออกจากบล็อกโดยไม่มีข้อผิดพลาด** และ **rollback ให้อัตโนมัติเมื่อเกิดข้อผิดพลาด** ซึ่งเป็นพฤติกรรมที่ปลอดภัยและสะดวก แต่ในกรณีที่ต้องควบคุมละเอียด (เช่นทำหลายขั้นตอนแล้วตัดสินใจกลางทาง) ให้เขียน `commit()`/`rollback()` เองอย่างชัดเจนดังตัวอย่างข้างบน

### 10.9 การเพิ่มข้อมูลหลายแถวและการรับค่าที่สร้างขึ้น

```python
# เพิ่มหลายแถวในครั้งเดียว (เร็วกว่าวน execute ทีละแถวมาก)
rows = [
    ("PRD-001", "เมาส์ไร้สาย", 890, 25, "อุปกรณ์เสริม"),
    ("PRD-002", "คีย์บอร์ด", 1290, 8, "อุปกรณ์เสริม"),
    ("PRD-003", "จอภาพ 27 นิ้ว", 6900, 0, "จอแสดงผล"),
]

with conn.cursor() as cur:
    cur.executemany(
        """
        INSERT INTO products (code, name, price, stock, category)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (code) DO UPDATE
        SET name = EXCLUDED.name,
            price = EXCLUDED.price,
            stock = EXCLUDED.stock,
            updated_at = CURRENT_TIMESTAMP
        """,
        rows,
    )

# รับค่า id ที่ฐานข้อมูลสร้างให้กลับมา
with conn.cursor() as cur:
    cur.execute(
        "INSERT INTO products (code, name, price) VALUES (%s, %s, %s) RETURNING id",
        ("PRD-006", "ที่วางแล็ปท็อป", 690),
    )
    new_id = cur.fetchone()["id"]
    print(f"เพิ่มสินค้าใหม่ id = {new_id}")
```

> 💡 **`ON CONFLICT ... DO UPDATE`** คือคำสั่งที่มีประโยชน์มาก แปลว่า "ถ้ารหัสนี้มีอยู่แล้วให้อัปเดตแทนการเพิ่มใหม่" ทำให้เขียนสคริปต์นำเข้าข้อมูลซ้ำได้โดยไม่เกิดข้อผิดพลาด (เรียกว่า Upsert)

---

### 🧪 Workshop 10.1 - เชื่อม PyShop Mini เข้ากับ PostgreSQL

> **เป้าหมาย:** สร้างชั้นเข้าถึงข้อมูล (Repository) ที่ทำ CRUD ครบทั้ง 4 คำสั่งกับ PostgreSQL โดยใช้ Parameterized Query ทั้งหมด

**ไฟล์ `src/pyshop/database.py`**

```python
"""database.py - ชั้นเชื่อมต่อฐานข้อมูล PostgreSQL ของ PyShop Mini"""

import logging
import os
from contextlib import contextmanager

import psycopg
from dotenv import load_dotenv
from psycopg.rows import dict_row

from .product import Product

load_dotenv()
logger = logging.getLogger(__name__)

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
    "dbname": os.getenv("DB_NAME", "pyshop_db"),
    "user": os.getenv("DB_USER", "pyshop_user"),
    "password": os.getenv("DB_PASSWORD", ""),
}

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS products (
    id          SERIAL PRIMARY KEY,
    code        VARCHAR(20)    NOT NULL UNIQUE,
    name        VARCHAR(200)   NOT NULL,
    price       NUMERIC(12, 2) NOT NULL CHECK (price >= 0),
    stock       INTEGER        NOT NULL DEFAULT 0 CHECK (stock >= 0),
    category    VARCHAR(100)   NOT NULL DEFAULT 'ทั่วไป',
    created_at  TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP      NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""


@contextmanager
def get_connection():
    """ตัวช่วยเปิด-ปิดการเชื่อมต่อฐานข้อมูลอย่างปลอดภัย

    ใช้งาน:
        with get_connection() as conn:
            ...
    """
    conn = None
    try:
        conn = psycopg.connect(**DB_CONFIG, row_factory=dict_row)
        yield conn
    except psycopg.OperationalError as e:
        logger.error("เชื่อมต่อฐานข้อมูลไม่สำเร็จ: %s", e)
        raise
    finally:
        if conn is not None:
            conn.close()


def init_db() -> None:
    """สร้างตารางหากยังไม่มี"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_SQL)
        conn.commit()
    logger.info("เตรียมฐานข้อมูลเรียบร้อย")


def _to_product(row: dict) -> Product:
    """แปลงแถวจากฐานข้อมูลเป็น object Product"""
    return Product(
        code=row["code"],
        name=row["name"],
        price=float(row["price"]),
        stock=int(row["stock"]),
        category=row["category"],
    )


# ---------- CREATE ----------
def insert_product(product: Product) -> int:
    """เพิ่มสินค้าใหม่ คืนค่า id ที่ฐานข้อมูลสร้างให้"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO products (code, name, price, stock, category)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (product.code, product.name, product.price, product.stock, product.category),
            )
            new_id = cur.fetchone()["id"]
        conn.commit()
    logger.info("เพิ่มสินค้า %s (id=%s)", product.code, new_id)
    return new_id


def upsert_many(products: list[Product]) -> int:
    """นำเข้าสินค้าหลายรายการ ถ้ารหัสซ้ำให้อัปเดตแทน"""
    rows = [(p.code, p.name, p.price, p.stock, p.category) for p in products]
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO products (code, name, price, stock, category)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (code) DO UPDATE
                SET name = EXCLUDED.name,
                    price = EXCLUDED.price,
                    stock = EXCLUDED.stock,
                    category = EXCLUDED.category,
                    updated_at = CURRENT_TIMESTAMP
                """,
                rows,
            )
        conn.commit()
    return len(rows)


# ---------- READ ----------
def fetch_all() -> list[Product]:
    """ดึงสินค้าทั้งหมด เรียงตามรหัส"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM products ORDER BY code")
            return [_to_product(row) for row in cur.fetchall()]


def fetch_by_code(code: str) -> Product | None:
    """ดึงสินค้ารายการเดียวตามรหัส"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM products WHERE code = %s", (code.strip().upper(),))
            row = cur.fetchone()
            return _to_product(row) if row else None


def search_products(keyword: str) -> list[Product]:
    """ค้นหาสินค้าจากรหัสหรือชื่อ (ไม่สนตัวพิมพ์ใหญ่เล็ก)"""
    pattern = f"%{keyword.strip()}%"
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM products
                WHERE code ILIKE %s OR name ILIKE %s
                ORDER BY code
                """,
                (pattern, pattern),
            )
            return [_to_product(row) for row in cur.fetchall()]


def summary_by_category() -> list[dict]:
    """สรุปจำนวนและมูลค่าคงคลังแยกตามหมวดหมู่"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT category,
                       COUNT(*)                AS item_count,
                       SUM(stock)              AS total_stock,
                       SUM(price * stock)      AS total_value
                FROM products
                GROUP BY category
                ORDER BY total_value DESC
                """
            )
            return cur.fetchall()


# ---------- UPDATE ----------
def update_stock(code: str, change: int) -> bool:
    """ปรับจำนวนคงเหลือ (บวกเพิ่ม ลบลด) คืน True เมื่อสำเร็จ

    ใช้ WHERE stock + %s >= 0 เพื่อกันไม่ให้สต็อกติดลบที่ระดับฐานข้อมูล
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE products
                SET stock = stock + %s, updated_at = CURRENT_TIMESTAMP
                WHERE code = %s AND stock + %s >= 0
                """,
                (change, code.strip().upper(), change),
            )
            success = cur.rowcount > 0
        conn.commit()

    if not success:
        logger.warning("ปรับสต็อก %s ไม่สำเร็จ (ไม่พบสินค้าหรือจำนวนไม่พอ)", code)
    return success


def update_price(code: str, new_price: float) -> bool:
    """แก้ไขราคาสินค้า"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE products SET price = %s, updated_at = CURRENT_TIMESTAMP WHERE code = %s",
                (new_price, code.strip().upper()),
            )
            success = cur.rowcount > 0
        conn.commit()
    return success


# ---------- DELETE ----------
def delete_product(code: str) -> bool:
    """ลบสินค้าตามรหัส"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE code = %s", (code.strip().upper(),))
            success = cur.rowcount > 0
        conn.commit()
    if success:
        logger.info("ลบสินค้า %s", code)
    return success
```

**ไฟล์ทดสอบ `workshop10.py`**

```python
"""workshop10.py - ทดสอบการเชื่อมต่อฐานข้อมูลของ PyShop Mini"""

import logging

from src.pyshop.database import (
    delete_product,
    fetch_all,
    fetch_by_code,
    init_db,
    search_products,
    summary_by_category,
    update_stock,
    upsert_many,
)
from src.pyshop.product import Product

logging.basicConfig(level=logging.INFO, format="%(levelname)-8s %(message)s")


def main() -> None:
    # 1) เตรียมตาราง
    init_db()

    # 2) นำเข้าข้อมูลเริ่มต้น (รันซ้ำได้ไม่พัง เพราะใช้ Upsert)
    seed = [
        Product("PRD-001", "เมาส์ไร้สาย", 890, 25, "อุปกรณ์เสริม"),
        Product("PRD-002", "คีย์บอร์ด", 1290, 8, "อุปกรณ์เสริม"),
        Product("PRD-003", "จอภาพ 27 นิ้ว", 6900, 0, "จอแสดงผล"),
        Product("PRD-004", "หูฟัง", 1590, 42, "เสียง"),
        Product("PRD-005", "ลำโพง", 2490, 5, "เสียง"),
    ]
    print(f"นำเข้า {upsert_many(seed)} รายการ")

    # 3) อ่านทั้งหมด
    print("\n📦 สินค้าทั้งหมดในฐานข้อมูล")
    print("-" * 62)
    for p in fetch_all():
        print(f"{p.code:<10}{p.name:<18}{p.price:>10,.0f}{p.stock:>8}  {p.status()}")

    # 4) ค้นหา
    keyword = "เมาส์"
    print(f"\n🔍 ผลการค้นหา '{keyword}'")
    for p in search_products(keyword):
        print(f"   {p}")

    # 5) ปรับสต็อก
    print("\n🔄 ทดสอบปรับสต็อก")
    print(f"   ลดเมาส์ 5 ชิ้น    : {update_stock('PRD-001', -5)}")
    print(f"   ลดจอภาพ 3 ชิ้น    : {update_stock('PRD-003', -3)}  ← ต้องเป็น False (สต็อก 0)")
    print(f"   เติมจอภาพ 10 ชิ้น : {update_stock('PRD-003', 10)}")
    print(f"   ผลลัพธ์เมาส์       : {fetch_by_code('PRD-001')}")

    # 6) รายงานสรุปจากฐานข้อมูลโดยตรง
    print("\n📊 สรุปแยกตามหมวดหมู่ (คำนวณโดย PostgreSQL)")
    print("-" * 62)
    for row in summary_by_category():
        print(
            f"   {row['category']:<14}{row['item_count']:>4} รายการ"
            f"{row['total_stock']:>8} ชิ้น{float(row['total_value']):>14,.2f} บาท"
        )

    # 7) ทดสอบ SQL Injection (ต้องไม่มีอะไรเสียหาย)
    print("\n🛡️  ทดสอบ SQL Injection")
    evil = "' OR '1'='1"
    result = search_products(evil)
    print(f"   ค้นด้วย {evil!r} ได้ {len(result)} รายการ (ต้องเป็น 0)")


if __name__ == "__main__":
    main()
```

**รันด้วย**

```powershell
uv run workshop10.py
```

> ✅ **ผลลัพธ์ที่คาดหวัง:**
>
> - นำเข้า 5 รายการ และ **รันซ้ำอีกครั้งต้องไม่เกิด error** (เพราะใช้ `ON CONFLICT`)
> - `update_stock('PRD-003', -3)` ต้องคืน `False` เพราะสต็อกเป็น 0 อยู่แล้ว ซึ่งพิสูจน์ว่ากฎกันสต็อกติดลบทำงาน
> - การค้นด้วย `' OR '1'='1` ต้องได้ **0 รายการ** ไม่ใช่ทั้งตาราง ซึ่งพิสูจน์ว่า Parameterized Query ป้องกันได้จริง
>
> ⛔ **ถ้าเจอ `psycopg.OperationalError: connection failed`** ให้ตรวจตามลำดับ (1) บริการ PostgreSQL ทำงานอยู่หรือไม่ (เปิด Services แล้วหา `postgresql-x64-17`) (2) ค่าใน `.env` ถูกต้องหรือไม่ (3) Port ตรงกันหรือไม่ (4) ผู้ใช้มีสิทธิ์บนฐานข้อมูลนั้นจริงหรือไม่

---

## 📚 Module 11: การใช้งาน Git Version Control ใน Python

### เวลา 14:45-15:15 น.

> 💡 **หัวใจของ Module นี้:** ทุกคนเคยมีไฟล์ชื่อ `main_final.py`, `main_final_2.py`, `main_final_ใช้ตัวนี้.py` Git คือคำตอบของปัญหานั้น มันเก็บ **ประวัติทุกการเปลี่ยนแปลง** ทำให้ย้อนกลับได้ทุกจุด และทำให้หลายคนแก้ไฟล์เดียวกันได้โดยไม่ทับกัน

---

### 11.1 แนวคิดของ Version Control

```
ไม่มี Git:                              มี Git:
┌────────────────────────┐             ┌──────────────────────────────┐
│ main.py                │             │  ● commit "เพิ่มเมนูค้นหา"     │
│ main_v2.py             │             │  │                           │
│ main_final.py          │     ⟶      │  ● commit "เชื่อมฐานข้อมูล"   │
│ main_final_แก้แล้ว.py    │             │  │                           │
│ main_ใช้ตัวนี้จริง.py     │             │  ● commit "เพิ่มคลาส Product" │
└────────────────────────┘             └──────────────────────────────┘
  ไม่รู้ว่าตัวไหนล่าสุด                      ไฟล์เดียว แต่ย้อนดูได้ทุกจุด
  ไม่รู้ว่าแก้อะไรไปบ้าง                      รู้ว่าใครแก้อะไร เมื่อไร ทำไม
```

| ประโยชน์ | รายละเอียด |
| --- | --- |
| ย้อนกลับได้ | แก้พังแล้วกลับไปเวอร์ชันที่ยังดีได้ทันที |
| รู้ประวัติ | ใครแก้บรรทัดไหน เมื่อไร ด้วยเหตุผลอะไร |
| ทำงานพร้อมกัน | แต่ละคนแยก Branch ทำงาน แล้วรวมทีหลัง |
| สำรองข้อมูล | Push ขึ้น GitHub คือมีสำเนาบนคลาวด์ |
| ทดลองได้อย่างปลอดภัย | สร้าง Branch ทดลอง ถ้าไม่ดีก็ลบทิ้ง |

### 11.2 การติดตั้งและตั้งค่าเริ่มต้น

ดาวน์โหลดจาก git-scm.com แล้วติดตั้ง จากนั้นตั้งค่าตัวตนของเราครั้งเดียว (ชื่อและอีเมลนี้จะปรากฏในทุก commit)

```powershell
git --version

git config --global user.name "Samit Koyom"
git config --global user.email "samitkoyom@gmail.com"

# ตั้งชื่อ branch หลักเป็น main (มาตรฐานปัจจุบัน)
git config --global init.defaultBranch main

# ตั้งค่าการขึ้นบรรทัดใหม่ให้ถูกต้องบน Windows
git config --global core.autocrlf true

# ดูค่าที่ตั้งไว้ทั้งหมด
git config --list
```

### 11.3 แนวคิด 3 พื้นที่ของ Git

```
   Working Directory        Staging Area           Repository
   (ไฟล์ที่คุณแก้อยู่)        (เตรียมจะบันทึก)        (ประวัติถาวร)
   ┌──────────────┐        ┌──────────────┐      ┌──────────────┐
   │  main.py     │        │              │      │  commit #3   │
   │  product.py  │──add──▶│  main.py     │─commit─▶│  commit #2   │
   │  database.py │        │  product.py  │      │  commit #1   │
   └──────────────┘        └──────────────┘      └──────────────┘
                                                        │
                                                      push
                                                        ▼
                                                   ┌──────────┐
                                                   │  GitHub  │
                                                   └──────────┘
```

> 💡 **ทำไมต้องมี Staging Area:** เพื่อให้คุณเลือกได้ว่าจะบันทึกอะไรบ้างใน commit นี้ เช่น แก้ไป 5 ไฟล์ แต่ 3 ไฟล์เป็นเรื่องเดียวกันและอีก 2 ไฟล์เป็นอีกเรื่อง ก็แยก commit ได้ ทำให้ประวัติอ่านเข้าใจง่าย

### 11.4 คำสั่ง Git พื้นฐาน

```powershell
# --- เริ่มต้น ---
git init                        # สร้าง repository ใหม่ (uv init ทำให้แล้วเมื่อวาน)
git status                      # ★ ดูสถานะปัจจุบัน (ใช้บ่อยที่สุด)

# --- บันทึกการเปลี่ยนแปลง ---
git add main.py                 # เพิ่มไฟล์เดียวเข้า staging
git add src/                    # เพิ่มทั้งโฟลเดอร์
git add .                       # เพิ่มทุกไฟล์ที่เปลี่ยน
git commit -m "เพิ่มคลาส Product และ Inventory"

# --- ดูประวัติ ---
git log                         # ประวัติเต็ม
git log --oneline               # ★ ย่อบรรทัดเดียวต่อ commit อ่านง่ายกว่า
git log --oneline --graph --all # เห็นผังกิ่ง branch ด้วย
git show <commit-id>            # ดูรายละเอียดของ commit นั้น

# --- ดูความแตกต่าง ---
git diff                        # เทียบไฟล์ปัจจุบันกับ staging
git diff --staged               # เทียบ staging กับ commit ล่าสุด

# --- ย้อนกลับ ---
git restore main.py             # ทิ้งการแก้ไขในไฟล์นี้ กลับไปเป็นแบบ commit ล่าสุด
git restore --staged main.py    # เอาออกจาก staging (แต่ยังเก็บการแก้ไขไว้)
git revert <commit-id>          # สร้าง commit ใหม่ที่ย้อนผลของ commit เดิม (ปลอดภัย)
```

> ⚠️ **`git restore <ไฟล์>` ลบการแก้ไขที่ยังไม่ commit ทิ้งถาวร** และไม่มีทางกู้คืนได้เพราะ Git ไม่เคยเห็นการแก้ไขนั้นเลย ให้แน่ใจก่อนใช้เสมอ

**การเขียนข้อความ commit ที่ดี**

| ❌ ไม่ดี | ✅ ดี |
| --- | --- |
| `update` | `เพิ่มฟังก์ชันค้นหาสินค้าจากรหัสและชื่อ` |
| `fix bug` | `แก้บั๊ก discount_rate คืน None เมื่อ qty น้อยกว่า 3` |
| `แก้ไขไฟล์` | `เปลี่ยนจาก dict เป็นคลาส Product เพื่อตรวจสอบข้อมูลอัตโนมัติ` |
| `asdfgh` | `เชื่อมต่อ PostgreSQL ด้วย psycopg 3 พร้อม Parameterized Query` |

### 11.5 ไฟล์ .gitignore สำหรับโปรเจกต์ Python

```gitignore
# Virtual Environment
.venv/
venv/
env/

# Python cache
__pycache__/
*.py[cod]
*.egg-info/
.pytest_cache/
.ruff_cache/
.mypy_cache/

# ★ ความลับ - ห้ามขึ้น Git เด็ดขาด
.env
*.key
credentials.json

# ข้อมูลและไฟล์ผลลัพธ์
data/*.bak.csv
data/*.log
*.sqlite3

# ระบบปฏิบัติการ
Thumbs.db
desktop.ini
.DS_Store

# Editor
.vscode/*
!.vscode/settings.json
!.vscode/launch.json
.idea/
```

> ⚠️ **สิ่งที่ห้ามขึ้น Git โดยเด็ดขาด:** ไฟล์ `.env`, รหัสผ่าน, API Key, ไฟล์ Certificate และข้อมูลส่วนบุคคล **เพราะ Git จำทุกอย่างตลอดไป** ต่อให้ลบไฟล์แล้ว commit ใหม่ ประวัติเดิมก็ยังมีข้อมูลนั้นอยู่ ถ้าเผลออัปขึ้น GitHub ไปแล้วต้องถือว่ารหัสผ่านนั้นรั่วไหลและเปลี่ยนทันที
>
> 💡 **สิ่งที่ต้องขึ้น Git:** `pyproject.toml`, `uv.lock`, `.gitignore`, `.env.example` และซอร์สโค้ดทั้งหมด

### 11.6 การทำงานกับ Branch

```powershell
# ดู branch ทั้งหมด
git branch

# สร้างและย้ายไป branch ใหม่พร้อมกัน
git switch -c feature/gui-form

# ...แก้โค้ด แล้ว commit ตามปกติ...
git add .
git commit -m "เพิ่มหน้าจอฟอร์มกรอกข้อมูลด้วย Tkinter"

# กลับไป branch หลัก
git switch main

# รวมงานจาก branch ย่อยเข้ามา
git merge feature/gui-form

# ลบ branch ที่รวมเสร็จแล้ว
git branch -d feature/gui-form
```

```
ผังการทำงานด้วย Branch:

  main    ●───●───●─────────────●  ← รวมงานกลับเข้ามา (merge)
                   ╲           ╱
  feature           ●───●───●     ← ทดลองงานใหม่ได้อย่างอิสระ
                                     ถ้าไม่ดีก็ลบทิ้งได้เลย
```

| คำสั่งใหม่ | คำสั่งเดิม (ยังใช้ได้) | ความหมาย |
| --- | --- | --- |
| `git switch <branch>` | `git checkout <branch>` | ย้าย branch |
| `git switch -c <branch>` | `git checkout -b <branch>` | สร้างและย้าย |
| `git restore <file>` | `git checkout -- <file>` | ทิ้งการแก้ไข |

> 💡 **ถ้าเกิด Merge Conflict:** Git จะแทรกเครื่องหมาย `<<<<<<<`, `=======`, `>>>>>>>` ลงในไฟล์ ให้เปิดไฟล์นั้นใน VS Code ซึ่งจะแสดงปุ่ม `Accept Current Change` / `Accept Incoming Change` / `Accept Both` ให้เลือก จากนั้น `git add` ไฟล์นั้นแล้ว `git commit` เพื่อจบการรวม

### 11.7 การทำงานกับ GitHub

```powershell
# --- ส่งโปรเจกต์ขึ้น GitHub ครั้งแรก ---
# (สร้าง repository เปล่าบน github.com ก่อน โดยไม่ต้องติ๊ก Add README)
git remote add origin https://github.com/your-name/pyshop.git
git branch -M main
git push -u origin main

# --- การใช้งานประจำวัน ---
git push                        # ส่งการเปลี่ยนแปลงขึ้น
git pull                        # ดึงการเปลี่ยนแปลงจากคนอื่นลงมา
git remote -v                   # ดูว่าเชื่อมกับ repo ไหนอยู่
```

**การรับโปรเจกต์ Python จากภายนอกมาใช้งาน**

```powershell
# 1) โคลนโปรเจกต์ลงมา
git clone https://github.com/some-team/some-python-project.git
cd some-python-project

# 2) ★ ติดตั้งไลบรารีทั้งหมดตามที่โปรเจกต์ต้องการ (นี่คือพลังของ uv)
uv sync

# 3) รันได้ทันที
uv run main.py
```

> ✅ **นี่คือเหตุผลที่ `uv.lock` ต้องขึ้น Git:** คนที่โคลนโปรเจกต์ไปจะได้ไลบรารีเวอร์ชันเดียวกันเป๊ะกับเครื่องคุณ ไม่มีปัญหา "เครื่องผมรันไม่ได้" อีกต่อไป

**การนำโมดูลจากภายนอกมาใช้**

```powershell
# วิธีที่แนะนำ: ติดตั้งจาก PyPI ผ่าน uv
uv add rich

# กรณีไลบรารีนั้นยังไม่ขึ้น PyPI หรือต้องการเวอร์ชันจาก branch เฉพาะ
uv add "git+https://github.com/user/some-lib.git"
uv add "git+https://github.com/user/some-lib.git@develop"
```

---

### 🧪 Workshop 11.1 - นำ PyShop Mini ขึ้น GitHub

```powershell
cd C:\PythonTraining\pyshop

# 1) ตรวจสอบว่ามีอะไรจะบันทึกบ้าง
git status

# 2) ★ ตรวจ .gitignore ก่อน push เสมอ ต้องไม่เห็น .venv และ .env ในรายการ
notepad .gitignore

# 3) บันทึกงานทั้งหมดของ 2 วัน
git add .
git commit -m "PyShop Mini: ระบบจัดการสินค้าคงคลัง (Python Basic 2026)"

# 4) ดูประวัติ
git log --oneline

# 5) เชื่อมกับ GitHub แล้วส่งขึ้นไป
git remote add origin https://github.com/your-name/pyshop.git
git branch -M main
git push -u origin main
```

> ✅ **ผลลัพธ์ที่คาดหวัง:** เปิดหน้า repository บน GitHub แล้วเห็นซอร์สโค้ดครบ **แต่ต้องไม่เห็นโฟลเดอร์ `.venv` และไฟล์ `.env`** ถ้าเห็นแสดงว่า `.gitignore` ยังไม่ทำงาน ให้แก้แล้วรัน `git rm -r --cached .venv .env` ก่อน commit ใหม่
>
> 🏋️ **โจทย์ต่อยอด:** ลองจับคู่กับเพื่อนในห้อง ให้เพื่อน `git clone` โปรเจกต์ของคุณแล้วรัน `uv sync` และ `uv run main.py` ถ้าเพื่อนรันได้โดยไม่ต้องถามอะไรเพิ่ม แสดงว่าโปรเจกต์ของคุณสมบูรณ์แล้ว

---

## 📚 Module 12: Python GUI ด้วย Tkinter และ CustomTkinter

### เวลา 15:15-15:45 น.

> 💡 **หัวใจของ Module นี้:** โปรแกรม Console ใช้งานได้ดีสำหรับนักพัฒนา แต่ผู้ใช้ทั่วไปต้องการหน้าต่างที่คลิกได้ **ข่าวดีคือ ถ้าเราแยก Logic ออกจาก UI มาตั้งแต่วันแรก การเปลี่ยนหน้าจอจะแทบไม่ต้องแตะโค้ดตรรกะเลย** วันนี้จะได้พิสูจน์

---

### 12.1 ภาพรวมไลบรารี GUI ในภาษา Python

| ไลบรารี | ข้อดี | ข้อเสีย | เหมาะกับ |
| --- | --- | --- | --- |
| **Tkinter** | มากับ Python ไม่ต้องติดตั้ง เรียนรู้เร็ว | หน้าตาเก่า | เครื่องมือภายในองค์กร โปรแกรมเล็ก |
| **CustomTkinter** | ต่อยอดจาก Tkinter หน้าตาทันสมัย มี Dark Mode | ต้องติดตั้งเพิ่ม | โปรแกรมที่ต้องการความสวยงาม |
| **PyQt / PySide** | ครบเครื่องที่สุด มีเครื่องมือออกแบบ UI | เรียนรู้ยาก ลิขสิทธิ์ต้องตรวจสอบ | แอปเดสก์ท็อประดับมืออาชีพ |
| **Flet** | เขียนครั้งเดียวได้ทั้ง Desktop/Web/Mobile | ยังใหม่ ชุมชนเล็กกว่า | โปรเจกต์ที่ต้องการหลายแพลตฟอร์ม |
| **Streamlit** | ทำ Data Dashboard ได้เร็วมาก | เป็นเว็บ ไม่ใช่แอปเดสก์ท็อป | งาน Data Analytics |

> ✅ **หลักสูตรนี้ใช้ Tkinter เป็นฐาน** เพราะมากับ Python อยู่แล้ว ทุกคนใช้ได้ทันที แล้วแสดงให้เห็นว่า **CustomTkinter** ยกระดับหน้าตาได้อย่างไรด้วยการแก้โค้ดเพียงเล็กน้อย

### 12.2 หน้าต่างแรกด้วย Tkinter

```python
import tkinter as tk

# 1) สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("PyShop Mini")
root.geometry("400x200")          # กว้าง x สูง
root.resizable(True, True)        # ให้ย่อขยายได้ทั้งแนวนอนและแนวตั้ง

# 2) ใส่ Widget
label = tk.Label(root, text="ยินดีต้อนรับสู่ PyShop Mini", font=("Tahoma", 14))
label.pack(pady=20)

button = tk.Button(root, text="ปิดโปรแกรม", command=root.destroy)
button.pack()

# 3) ★ เริ่มลูปรับเหตุการณ์ (ต้องเป็นบรรทัดสุดท้ายเสมอ)
root.mainloop()
```

> ⚠️ **`mainloop()` ต้องอยู่บรรทัดสุดท้าย:** เพราะมันคือลูปที่คอยรับการคลิกและการพิมพ์ของผู้ใช้ โค้ดที่เขียนต่อจากบรรทัดนี้จะทำงานก็ต่อเมื่อผู้ใช้ปิดหน้าต่างแล้วเท่านั้น
>
> 💡 **ฟอนต์ภาษาไทยบน Windows:** ใช้ `"Tahoma"` หรือ `"Leelawadee UI"` จะแสดงภาษาไทยได้สวยและครบทุกสระวรรณยุกต์

### 12.3 Widget ที่ใช้บ่อย

| Widget | หน้าที่ | ตัวอย่าง |
| --- | --- | --- |
| `Label` | แสดงข้อความหรือรูป | หัวข้อ, ป้ายกำกับช่องกรอก |
| `Entry` | ช่องกรอกข้อความบรรทัดเดียว | ชื่อสินค้า, ราคา |
| `Text` | ช่องกรอกหลายบรรทัด | หมายเหตุ |
| `Button` | ปุ่มกด | บันทึก, ค้นหา, ลบ |
| `Combobox` | รายการให้เลือก (ttk) | หมวดหมู่สินค้า |
| `Checkbutton` | ติ๊กเลือก | สถานะเปิด/ปิดการขาย |
| `Radiobutton` | เลือกหนึ่งจากหลายตัวเลือก | ประเภทการเรียงลำดับ |
| `Treeview` | ★ ตารางข้อมูล (ttk) | รายการสินค้า |
| `Frame` | กล่องจัดกลุ่ม Widget | แบ่งหน้าจอเป็นส่วน ๆ |
| `messagebox` | กล่องข้อความแจ้งเตือน | ยืนยันการลบ |

### 12.4 การจัดวาง Layout

Tkinter มีระบบจัดวาง 3 แบบ **ห้ามใช้ปนกันภายใน Frame เดียวกัน**

```python
# 1) pack() - เรียงต่อกันตามทิศทาง (ง่ายที่สุด เหมาะกับ layout ง่าย ๆ)
widget.pack(side="top", fill="x", padx=10, pady=5)
widget.pack(side="left", expand=True, fill="both")

# 2) grid() - จัดเป็นตาราง แถว/คอลัมน์ (★ เหมาะกับฟอร์มมากที่สุด)
tk.Label(root, text="ชื่อสินค้า:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
tk.Entry(root).grid(row=0, column=1, sticky="ew", padx=5, pady=5)
root.columnconfigure(1, weight=1)      # ให้คอลัมน์ 1 ยืดตามหน้าต่าง

# 3) place() - ระบุพิกัดตายตัว (ไม่แนะนำ เพราะไม่ยืดหยุ่นตามขนาดหน้าจอ)
widget.place(x=50, y=100, width=200)
```

| พารามิเตอร์ | ความหมาย |
| --- | --- |
| `padx`, `pady` | ระยะห่างภายนอก (แนวนอน/แนวตั้ง) |
| `sticky` | ยึดติดกับด้านไหนของช่อง (`n`, `s`, `e`, `w`, `ew`, `nsew`) |
| `fill` | ขยายเต็มพื้นที่ (`x`, `y`, `both`) |
| `expand` | ให้แย่งพื้นที่ที่เหลือ (`True`/`False`) |
| `weight` | สัดส่วนการยืดของแถว/คอลัมน์เมื่อขยายหน้าต่าง |

### 12.5 การรับ-ส่งค่าจากฟอร์มและการผูก Event

```python
import tkinter as tk
from tkinter import messagebox, ttk


class ProductForm(tk.Frame):
    """ฟอร์มกรอกข้อมูลสินค้า"""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master, padx=12, pady=12)

        # ★ ตัวแปรพิเศษของ Tkinter ที่ผูกกับ Widget แบบสองทาง
        self.var_code = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_price = tk.StringVar(value="0")
        self.var_stock = tk.StringVar(value="0")
        self.var_category = tk.StringVar(value="ทั่วไป")

        fields = [
            ("รหัสสินค้า", self.var_code),
            ("ชื่อสินค้า", self.var_name),
            ("ราคา", self.var_price),
            ("จำนวน", self.var_stock),
        ]

        for row, (label_text, variable) in enumerate(fields):
            tk.Label(self, text=f"{label_text}:", font=("Tahoma", 10)).grid(
                row=row, column=0, sticky="e", padx=5, pady=4
            )
            tk.Entry(self, textvariable=variable, font=("Tahoma", 10), width=28).grid(
                row=row, column=1, sticky="ew", padx=5, pady=4
            )

        tk.Label(self, text="หมวดหมู่:", font=("Tahoma", 10)).grid(
            row=4, column=0, sticky="e", padx=5, pady=4
        )
        ttk.Combobox(
            self,
            textvariable=self.var_category,
            values=["ทั่วไป", "อุปกรณ์เสริม", "จอแสดงผล", "เสียง"],
            state="readonly",
            width=26,
        ).grid(row=4, column=1, sticky="ew", padx=5, pady=4)

        # ★ ผูก Event: command คือฟังก์ชันที่จะถูกเรียกเมื่อกดปุ่ม
        tk.Button(self, text="บันทึก", command=self.on_save, width=12).grid(
            row=5, column=1, sticky="e", pady=10
        )

        self.columnconfigure(1, weight=1)

        # ผูกคีย์ Enter ให้เท่ากับการกดปุ่มบันทึก
        master.bind("<Return>", lambda event: self.on_save())

    def get_data(self) -> dict:
        """อ่านค่าจากฟอร์มออกมาเป็น dict"""
        return {
            "code": self.var_code.get().strip(),
            "name": self.var_name.get().strip(),
            "price": self.var_price.get().strip(),
            "stock": self.var_stock.get().strip(),
            "category": self.var_category.get(),
        }

    def clear(self) -> None:
        """ล้างฟอร์ม"""
        self.var_code.set("")
        self.var_name.set("")
        self.var_price.set("0")
        self.var_stock.set("0")

    def on_save(self) -> None:
        """ตรวจสอบข้อมูลแล้วแจ้งผล"""
        data = self.get_data()

        if not data["code"] or not data["name"]:
            messagebox.showwarning("ข้อมูลไม่ครบ", "กรุณากรอกรหัสและชื่อสินค้า")
            return

        try:
            price = float(data["price"])
            stock = int(data["stock"])
        except ValueError:
            messagebox.showerror("ข้อมูลผิดพลาด", "ราคาและจำนวนต้องเป็นตัวเลข")
            return

        messagebox.showinfo(
            "บันทึกสำเร็จ",
            f"{data['name']}\nราคา {price:,.2f} บาท\nจำนวน {stock} ชิ้น",
        )
        self.clear()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PyShop Mini - ฟอร์มสินค้า")
    root.geometry("420x260")
    ProductForm(root).pack(fill="both", expand=True)
    root.mainloop()
```

| ตัวแปรพิเศษ | ใช้กับ | เมธอด |
| --- | --- | --- |
| `tk.StringVar()` | ข้อความ | `.get()` / `.set()` |
| `tk.IntVar()` | จำนวนเต็ม | `.get()` / `.set()` |
| `tk.DoubleVar()` | ทศนิยม | `.get()` / `.set()` |
| `tk.BooleanVar()` | ค่าจริง/เท็จ (Checkbutton) | `.get()` / `.set()` |

| กล่องข้อความ | ใช้เมื่อ | คืนค่า |
| --- | --- | --- |
| `messagebox.showinfo()` | แจ้งข้อมูล | `"ok"` |
| `messagebox.showwarning()` | เตือน | `"ok"` |
| `messagebox.showerror()` | แจ้งข้อผิดพลาด | `"ok"` |
| `messagebox.askyesno()` | ★ ถามยืนยันก่อนลบ | `True`/`False` |

### 12.6 CustomTkinter - ยกระดับหน้าตาให้ทันสมัย

```powershell
uv add customtkinter
```

```python
import customtkinter as ctk

ctk.set_appearance_mode("dark")           # "light", "dark", "system"
ctk.set_default_color_theme("blue")       # "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("PyShop Mini")
app.geometry("460x300")

ctk.CTkLabel(app, text="PyShop Mini", font=("Tahoma", 22, "bold")).pack(pady=20)

entry = ctk.CTkEntry(app, placeholder_text="ค้นหาสินค้า...", width=300, height=36)
entry.pack(pady=10)

ctk.CTkButton(app, text="ค้นหา", width=180, height=38,
              command=lambda: print(entry.get())).pack(pady=10)

ctk.CTkSwitch(app, text="โหมดกลางคืน").pack(pady=10)

app.mainloop()
```

| Tkinter | CustomTkinter | ความต่าง |
| --- | --- | --- |
| `tk.Tk()` | `ctk.CTk()` | รองรับ Dark Mode |
| `tk.Label` | `ctk.CTkLabel` | มุมโค้ง สีสวยกว่า |
| `tk.Entry` | `ctk.CTkEntry` | มี `placeholder_text` |
| `tk.Button` | `ctk.CTkButton` | มี hover effect |
| - | `ctk.CTkSwitch` | สวิตช์เปิด/ปิดแบบสมัยใหม่ |

> 💡 **จุดสำคัญ:** CustomTkinter ทำงานบนพื้นฐานของ Tkinter ทั้งหมด ดังนั้นทุกอย่างที่เรียนมา (`grid`, `pack`, `StringVar`, `command`) ใช้ได้เหมือนเดิม เปลี่ยนแค่ชื่อคลาสของ Widget เท่านั้น และยังใช้ `ttk.Treeview` ร่วมกับ CustomTkinter ได้

---

## 🛠️ Module 13: Workshop ปิดท้าย - PyShop Mini v2 (GUI + PostgreSQL)

### เวลา 15:45-16:00 น. (เริ่มในห้อง ทำต่อที่บ้านได้)

> **โจทย์:** ประกอบทุกอย่างจากทั้งสองวันเป็นโปรแกรมเดียว รับข้อมูลจากผู้ใช้ผ่าน GUI ประมวลผลด้วยคลาส `Product` บันทึกลง PostgreSQL และแสดงผลในตาราง พร้อมส่งออกรายงานเป็น CSV

### สถาปัตยกรรมของโปรแกรมที่จะสร้าง

```
┌──────────────────────────────────────────────────────────┐
│  app_gui.py            ← ชั้นแสดงผล (Presentation)        │
│  Tkinter: ฟอร์ม + ตาราง + ปุ่ม                             │
└────────────────────────┬─────────────────────────────────┘
                         │ เรียกใช้
┌────────────────────────▼─────────────────────────────────┐
│  src/pyshop/product.py ← ชั้นตรรกะธุรกิจ (Domain)          │
│  class Product, class Inventory (ตรวจสอบข้อมูล + คำนวณ)   │
└────────────────────────┬─────────────────────────────────┘
                         │ เรียกใช้
┌────────────────────────▼─────────────────────────────────┐
│  src/pyshop/database.py ← ชั้นเข้าถึงข้อมูล (Data Access)  │
│  psycopg → PostgreSQL (CRUD ด้วย Parameterized Query)    │
└──────────────────────────────────────────────────────────┘
        ★ แต่ละชั้นเปลี่ยนได้อิสระ เช่น เปลี่ยนจาก PostgreSQL
          เป็น MySQL แก้แค่ database.py ชั้นอื่นไม่ต้องแตะ
```

### ไฟล์ `app_gui.py`

```python
"""app_gui.py - PyShop Mini v2: หน้าจอจัดการสินค้าคงคลัง (Python Basic 2026)"""

import csv
import logging
import tkinter as tk
from datetime import datetime
from pathlib import Path
from tkinter import messagebox, ttk

from src.pyshop.database import (
    delete_product,
    fetch_all,
    init_db,
    insert_product,
    search_products,
    update_stock,
)
from src.pyshop.product import Product

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[
        logging.FileHandler("data/pyshop.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

FONT = ("Tahoma", 10)
FONT_TITLE = ("Tahoma", 16, "bold")
CATEGORIES = ["ทั่วไป", "อุปกรณ์เสริม", "จอแสดงผล", "เสียง", "สายเชื่อมต่อ"]


class PyShopApp(tk.Tk):
    """หน้าต่างหลักของ PyShop Mini v2"""

    def __init__(self) -> None:
        super().__init__()
        self.title("PyShop Mini v2 - ระบบจัดการสินค้าคงคลัง")
        self.geometry("980x620")
        self.minsize(880, 560)

        self._build_header()
        self._build_form()
        self._build_toolbar()
        self._build_table()
        self._build_statusbar()

        self.refresh()

    # ---------- ส่วนประกอบหน้าจอ ----------
    def _build_header(self) -> None:
        header = tk.Frame(self, bg="#0C1628", height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(
            header,
            text="PyShop Mini",
            font=FONT_TITLE,
            bg="#0C1628",
            fg="white",
        ).pack(side="left", padx=20)
        tk.Label(
            header,
            text="ระบบจัดการสินค้าคงคลัง | Python Basic 2026",
            font=FONT,
            bg="#0C1628",
            fg="#9FB3C8",
        ).pack(side="left")

    def _build_form(self) -> None:
        form = tk.LabelFrame(self, text=" ข้อมูลสินค้า ", font=FONT, padx=12, pady=10)
        form.pack(fill="x", padx=16, pady=12)

        self.var_code = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_price = tk.StringVar(value="0")
        self.var_stock = tk.StringVar(value="0")
        self.var_category = tk.StringVar(value=CATEGORIES[0])

        specs = [
            ("รหัสสินค้า", self.var_code, 0, 0),
            ("ชื่อสินค้า", self.var_name, 0, 2),
            ("ราคา (บาท)", self.var_price, 1, 0),
            ("จำนวนคงเหลือ", self.var_stock, 1, 2),
        ]
        for label_text, variable, row, col in specs:
            tk.Label(form, text=f"{label_text}:", font=FONT).grid(
                row=row, column=col, sticky="e", padx=6, pady=6
            )
            tk.Entry(form, textvariable=variable, font=FONT, width=26).grid(
                row=row, column=col + 1, sticky="ew", padx=6, pady=6
            )

        tk.Label(form, text="หมวดหมู่:", font=FONT).grid(
            row=2, column=0, sticky="e", padx=6, pady=6
        )
        ttk.Combobox(
            form,
            textvariable=self.var_category,
            values=CATEGORIES,
            state="readonly",
            font=FONT,
            width=24,
        ).grid(row=2, column=1, sticky="ew", padx=6, pady=6)

        form.columnconfigure(1, weight=1)
        form.columnconfigure(3, weight=1)

    def _build_toolbar(self) -> None:
        bar = tk.Frame(self)
        bar.pack(fill="x", padx=16)

        buttons = [
            ("➕ เพิ่มสินค้า", self.on_add),
            ("🔄 เติมสต็อก", lambda: self.on_adjust(+1)),
            ("➖ ตัดสต็อก", lambda: self.on_adjust(-1)),
            ("🗑 ลบสินค้า", self.on_delete),
            ("📤 ส่งออก CSV", self.on_export),
            ("↻ รีเฟรช", self.refresh),
        ]
        for text, command in buttons:
            tk.Button(bar, text=text, font=FONT, command=command, width=13).pack(
                side="left", padx=3
            )

        tk.Label(bar, text="ค้นหา:", font=FONT).pack(side="left", padx=(20, 4))
        self.var_search = tk.StringVar()
        entry = tk.Entry(bar, textvariable=self.var_search, font=FONT, width=22)
        entry.pack(side="left")
        entry.bind("<Return>", lambda event: self.on_search())
        tk.Button(bar, text="🔍", font=FONT, command=self.on_search, width=4).pack(
            side="left", padx=3
        )

    def _build_table(self) -> None:
        wrapper = tk.Frame(self)
        wrapper.pack(fill="both", expand=True, padx=16, pady=12)

        columns = ("code", "name", "price", "stock", "value", "category", "status")
        headings = {
            "code": ("รหัส", 90),
            "name": ("ชื่อสินค้า", 220),
            "price": ("ราคา", 100),
            "stock": ("คงเหลือ", 80),
            "value": ("มูลค่า", 120),
            "category": ("หมวดหมู่", 130),
            "status": ("สถานะ", 100),
        }

        self.tree = ttk.Treeview(wrapper, columns=columns, show="headings", height=12)
        for key, (title, width) in headings.items():
            anchor = "e" if key in {"price", "stock", "value"} else "w"
            self.tree.heading(key, text=title)
            self.tree.column(key, width=width, anchor=anchor)

        scroll = ttk.Scrollbar(wrapper, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # ระบายสีตามสถานะ
        self.tree.tag_configure("out", background="#FEE2E2")
        self.tree.tag_configure("low", background="#FEF9C3")

        # คลิกแถวแล้วเติมค่าลงฟอร์มอัตโนมัติ
        self.tree.bind("<<TreeviewSelect>>", self.on_select_row)

    def _build_statusbar(self) -> None:
        self.var_status = tk.StringVar(value="พร้อมใช้งาน")
        tk.Label(
            self,
            textvariable=self.var_status,
            font=FONT,
            anchor="w",
            bd=1,
            relief="sunken",
            padx=10,
        ).pack(fill="x", side="bottom")

    # ---------- ตัวช่วย ----------
    def read_form(self) -> Product | None:
        """อ่านข้อมูลจากฟอร์มแล้วสร้าง Product คืน None ถ้าข้อมูลไม่ถูกต้อง"""
        code = self.var_code.get().strip()
        name = self.var_name.get().strip()

        if not code or not name:
            messagebox.showwarning("ข้อมูลไม่ครบ", "กรุณากรอกรหัสและชื่อสินค้า")
            return None

        try:
            return Product(
                code=code,
                name=name,
                price=float(self.var_price.get()),
                stock=int(self.var_stock.get()),
                category=self.var_category.get(),
            )
        except ValueError as e:
            messagebox.showerror("ข้อมูลไม่ถูกต้อง", str(e))
            return None

    def selected_code(self) -> str | None:
        """คืนรหัสสินค้าของแถวที่เลือกอยู่"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showinfo("ยังไม่ได้เลือก", "กรุณาเลือกสินค้าจากตารางก่อน")
            return None
        return self.tree.item(selection[0], "values")[0]

    def fill_table(self, products: list[Product]) -> None:
        """เติมข้อมูลลงตาราง"""
        self.tree.delete(*self.tree.get_children())

        for product in products:
            tag = ""
            if product.stock <= 0:
                tag = "out"
            elif product.stock < Product.LOW_STOCK_LIMIT:
                tag = "low"

            self.tree.insert(
                "",
                "end",
                values=(
                    product.code,
                    product.name,
                    f"{product.price:,.2f}",
                    product.stock,
                    f"{product.stock_value:,.2f}",
                    product.category,
                    product.status(),
                ),
                tags=(tag,),
            )

        total_value = sum(p.stock_value for p in products)
        total_qty = sum(p.stock for p in products)
        self.var_status.set(
            f"แสดง {len(products)} รายการ | รวม {total_qty:,} ชิ้น "
            f"| มูลค่า {total_value:,.2f} บาท | อัปเดต {datetime.now():%H:%M:%S}"
        )

    # ---------- การกระทำของผู้ใช้ ----------
    def refresh(self) -> None:
        """โหลดข้อมูลใหม่จากฐานข้อมูล"""
        try:
            self.fill_table(fetch_all())
        except Exception as e:
            logger.exception("โหลดข้อมูลไม่สำเร็จ")
            messagebox.showerror("เชื่อมต่อฐานข้อมูลไม่ได้", str(e))

    def on_select_row(self, event: tk.Event) -> None:
        """คลิกแถวแล้วเติมค่าลงฟอร์ม"""
        selection = self.tree.selection()
        if not selection:
            return
        values = self.tree.item(selection[0], "values")
        self.var_code.set(values[0])
        self.var_name.set(values[1])
        self.var_price.set(values[2].replace(",", ""))
        self.var_stock.set(values[3])
        self.var_category.set(values[5])

    def on_add(self) -> None:
        """เพิ่มสินค้าใหม่ลงฐานข้อมูล"""
        product = self.read_form()
        if product is None:
            return
        try:
            insert_product(product)
            messagebox.showinfo("สำเร็จ", f"เพิ่ม {product.name} เรียบร้อยแล้ว")
            self.refresh()
        except Exception as e:
            logger.exception("เพิ่มสินค้าไม่สำเร็จ")
            messagebox.showerror("เพิ่มไม่สำเร็จ", f"อาจมีรหัสนี้อยู่แล้ว\n\n{e}")

    def on_adjust(self, direction: int) -> None:
        """ปรับสต็อกเพิ่มหรือลดตามจำนวนในช่อง 'จำนวนคงเหลือ'"""
        code = self.selected_code()
        if code is None:
            return
        try:
            qty = int(self.var_stock.get())
        except ValueError:
            messagebox.showerror("ข้อมูลผิดพลาด", "จำนวนต้องเป็นตัวเลข")
            return

        if update_stock(code, direction * abs(qty)):
            self.refresh()
        else:
            messagebox.showwarning("ปรับไม่สำเร็จ", "สินค้าคงเหลือไม่พอ หรือไม่พบรหัสนี้")

    def on_delete(self) -> None:
        """ลบสินค้าที่เลือก (ถามยืนยันก่อน)"""
        code = self.selected_code()
        if code is None:
            return
        if not messagebox.askyesno("ยืนยันการลบ", f"ต้องการลบสินค้ารหัส {code} ใช่หรือไม่"):
            return
        if delete_product(code):
            self.refresh()
        else:
            messagebox.showwarning("ลบไม่สำเร็จ", f"ไม่พบสินค้ารหัส {code}")

    def on_search(self) -> None:
        """ค้นหาสินค้าตามคำค้น"""
        keyword = self.var_search.get().strip()
        products = fetch_all() if not keyword else search_products(keyword)
        self.fill_table(products)

    def on_export(self) -> None:
        """ส่งออกข้อมูลที่แสดงอยู่เป็นไฟล์ CSV"""
        out_dir = Path("data")
        out_dir.mkdir(parents=True, exist_ok=True)
        path = out_dir / f"stock_report_{datetime.now():%Y%m%d_%H%M%S}.csv"

        with open(path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["รหัส", "ชื่อสินค้า", "ราคา", "คงเหลือ", "มูลค่า", "หมวดหมู่", "สถานะ"])
            for item_id in self.tree.get_children():
                writer.writerow(self.tree.item(item_id, "values"))

        logger.info("ส่งออกรายงาน %s", path.name)
        messagebox.showinfo("ส่งออกสำเร็จ", f"บันทึกไฟล์แล้วที่\n{path.resolve()}")


def main() -> None:
    Path("data").mkdir(parents=True, exist_ok=True)
    try:
        init_db()
    except Exception as e:
        messagebox.showerror("เชื่อมต่อฐานข้อมูลไม่ได้", f"{e}\n\nกรุณาตรวจสอบไฟล์ .env")
        return
    PyShopApp().mainloop()


if __name__ == "__main__":
    main()
```

**รันด้วย**

```powershell
uv run app_gui.py
```

> ✅ **ผลลัพธ์ที่คาดหวัง:** หน้าต่างขนาด 980x620 พร้อมแถบหัวสีเข้ม ฟอร์มกรอกข้อมูล แถบเครื่องมือ 6 ปุ่ม ตารางสินค้าที่ **ระบายสีแดงสำหรับสินค้าหมดและสีเหลืองสำหรับใกล้หมด** และแถบสถานะด้านล่างที่สรุปจำนวนกับมูลค่ารวม
>
> **ทดสอบให้ครบ:**
>
> 1. เพิ่มสินค้าใหม่ → ตารางอัปเดตทันที และ **ปิดโปรแกรมเปิดใหม่ข้อมูลยังอยู่** (เพราะอยู่ในฐานข้อมูลจริง)
> 2. คลิกแถวในตาราง → ฟอร์มด้านบนเติมค่าให้อัตโนมัติ
> 3. เลือกจอภาพ (สต็อก 0) แล้วกด "ตัดสต็อก" → ต้องขึ้นเตือนว่าสินค้าไม่พอ
> 4. กด "ส่งออก CSV" → ได้ไฟล์ในโฟลเดอร์ `data/` ที่เปิดด้วย Excel แล้วภาษาไทยไม่เพี้ยน
> 5. เพิ่มสินค้าด้วยรหัสที่มีอยู่แล้ว → ต้องขึ้นข้อความแจ้ง ไม่ใช่โปรแกรมพัง

> 🎯 **ข้อสังเกตที่สำคัญที่สุดของหลักสูตรนี้:** ไฟล์ `app_gui.py` **ไม่มีคำสั่ง SQL แม้แต่บรรทัดเดียว** และ **ไม่มีสูตรคำนวณมูลค่าหรือ VAT เลย** มันทำหน้าที่เพียงรับค่าจากผู้ใช้แล้วเรียกใช้ `Product` กับ `database` เท่านั้น นี่คือผลของการแยกชั้นที่เราวางไว้ตั้งแต่ Workshop วันแรก และเป็นเหตุผลที่เราเปลี่ยนจาก Console เป็น GUI ได้โดยไม่ต้องเขียนตรรกะใหม่เลย

### 🏋️ โจทย์ต่อยอดของ Workshop ปิดท้าย

| ระดับ | โจทย์ |
| --- | --- |
| ง่าย | เพิ่มปุ่ม "แก้ไขราคา" ที่เรียก `update_price()` |
| ง่าย | เพิ่มช่องกรองตามหมวดหมู่ด้วย Combobox |
| ปานกลาง | เพิ่มแท็บ "รายงาน" ที่แสดงผลจาก `summary_by_category()` |
| ปานกลาง | เพิ่มการเรียงลำดับเมื่อคลิกที่หัวคอลัมน์ของ Treeview |
| ท้าทาย | เปลี่ยนหน้าตาทั้งหมดเป็น CustomTkinter พร้อมโหมดกลางคืน |
| ท้าทาย | เพิ่มตาราง `sales` แล้วบันทึกประวัติการขายพร้อม Transaction |

---

## 🚀 แนวทางการจัดโครงสร้างโปรเจกต์และการต่อยอด

### โครงสร้างโปรเจกต์ Python ที่เป็นระเบียบ

```
pyshop/
├── .env                    ← ความลับ (ห้ามขึ้น Git)
├── .env.example            ← แม่แบบให้เพื่อนดู (ขึ้น Git ได้)
├── .gitignore
├── .python-version
├── pyproject.toml          ← ★ ชื่อโปรเจกต์ + รายการไลบรารี
├── uv.lock                 ← ★ ตรึงเวอร์ชัน (ขึ้น Git)
├── README.md               ← วิธีติดตั้งและใช้งาน
├── main.py                 ← จุดเริ่มแบบ Console
├── app_gui.py              ← จุดเริ่มแบบ GUI
├── data/                   ← ไฟล์ข้อมูลและ log
│   ├── products.csv
│   ├── products.json
│   └── pyshop.log
├── src/
│   └── pyshop/
│       ├── __init__.py
│       ├── product.py      ← คลาส Product, Inventory
│       ├── storage.py      ← อ่าน/เขียนไฟล์ CSV, JSON
│       ├── database.py     ← เชื่อมต่อ PostgreSQL
│       ├── pricing.py      ← ตรรกะราคาและ VAT
│       └── report.py       ← รายงานแบบข้อความ
└── tests/                  ← การทดสอบอัตโนมัติ (เรียนใน Python Advanced)
    └── test_product.py
```

### แนวทางการใช้ AI Coding Assistant อย่างเหมาะสม

AI อย่าง GitHub Copilot หรือ Claude ช่วยให้เขียนโค้ดเร็วขึ้นมาก แต่ถ้าใช้ผิดวิธีจะทำให้ไม่เกิดการเรียนรู้

| ✅ ใช้อย่างนี้ | ❌ อย่าใช้อย่างนี้ |
| --- | --- |
| "อธิบายว่าโค้ดนี้ทำงานอย่างไรทีละบรรทัด" | "เขียนโปรแกรมทั้งหมดให้หน่อย" แล้วส่งงานเลย |
| "ทำไม error นี้ถึงเกิด และแก้ยังไง" | คัดลอกโค้ดที่ไม่เข้าใจไปวางในงานจริง |
| "มีวิธีเขียนแบบอื่นที่อ่านง่ายกว่านี้ไหม" | ใช้แทนการอ่านเอกสารทางการทั้งหมด |
| "ช่วยเขียน docstring และ type hints ให้โค้ดนี้" | เชื่อทุกอย่างโดยไม่ทดสอบ |
| "ช่วยทบทวนโค้ดนี้ว่ามีช่องโหว่ความปลอดภัยไหม" | ส่งรหัสผ่านหรือข้อมูลลูกค้าเข้าไปใน prompt |

> ⚠️ **กฎเหล็กข้อเดียวที่ควรจำ:** ถ้าคุณอธิบายโค้ดที่ AI เขียนให้เพื่อนฟังไม่ได้ **อย่าเพิ่งใช้โค้ดนั้น** เพราะเมื่อเกิดปัญหาในระบบจริง คนที่ต้องแก้คือคุณ ไม่ใช่ AI

### เส้นทางการเรียนรู้ต่อ

```
Python Basic 2026 (คุณอยู่ตรงนี้ ✅)
   │
   ├─▶ 🌐 Web Application
   │     Flask (เล็ก เรียนง่าย) → FastAPI (เร็ว ทำ API) → Django (ครบวงจร)
   │     + HTML/CSS พื้นฐาน + REST API + Deploy ด้วย Docker
   │
   ├─▶ 📊 Data Analytics
   │     Pandas (จัดการข้อมูลตาราง) → Matplotlib/Plotly (กราฟ)
   │     → SQL เชิงลึก → Power BI / Dashboard
   │
   ├─▶ 🤖 AI / Machine Learning
   │     NumPy → scikit-learn (โมเดลพื้นฐาน) → PyTorch (Deep Learning)
   │
   ├─▶ ⚙️ Automation / Scripting
   │     openpyxl (Excel) → Selenium/Playwright (เว็บอัตโนมัติ)
   │     → schedule / Task Scheduler
   │
   └─▶ 🧪 Python Advanced (หลักสูตรต่อเนื่องที่แนะนำ)
         Decorator, Generator, Context Manager, Async/Await,
         Unit Testing ด้วย pytest, Type Checking, Packaging, Performance
```

### แหล่งเรียนรู้และเอกสารอ้างอิง

| แหล่ง | เนื้อหา |
| --- | --- |
| docs.python.org/3 | ★ เอกสารทางการของภาษา Python (ควรเปิดคู่ไว้เสมอ) |
| docs.astral.sh/uv | เอกสารทางการของ uv |
| peps.python.org/pep-0008 | มาตรฐานการเขียนโค้ด PEP 8 |
| realpython.com | บทความสอน Python เชิงลึกที่มีคุณภาพสูง |
| pypi.org | คลังไลบรารีกลาง ค้นหาไลบรารีที่ต้องการ |
| psycopg.org/psycopg3/docs | เอกสารของ psycopg 3 |
| postgresql.org/docs | เอกสารทางการของ PostgreSQL |
| docs.python.org/3/library/tkinter.html | เอกสาร Tkinter |
| git-scm.com/book/th | หนังสือ Pro Git (มีฉบับแปลไทย) |
| www.itgenius.co.th | หลักสูตรต่อเนื่องของสถาบัน |

---

## ✅ แบบทดสอบหลังเรียน (Python Posttest)

ทำแบบทดสอบหลังเรียนแบบออนไลน์ตามลิงก์ที่วิทยากรแจ้ง เพื่อวัดผลสัมฤทธิ์การเรียนรู้ เปรียบเทียบกับคะแนนก่อนเรียน และรับคำแนะนำแนวทางพัฒนาตนเองรายบุคคล

---

## 📝 สรุปประจำวันที่ 2

| หัวข้อ | สิ่งที่ทำได้แล้ว |
| --- | --- |
| ★ Module 7 - File I/O | อ่าน/เขียน Text, CSV, JSON ด้วย `with` และจัดการ path ด้วย `pathlib` พร้อมสำรองไฟล์ก่อนเขียนทับ |
| ★ Module 8 - OOP | สร้างคลาส `Product` และ `Inventory` ด้วย `@dataclass`, `@property`, Inheritance และ Encapsulation |
| Module 9 - Error/Debug | ใช้ `try/except/else/finally` สร้าง Exception ของตนเอง ใช้ `logging` และ Debugger ของ VS Code |
| ★ Module 10 - Database | เชื่อม PostgreSQL ด้วย `psycopg 3` ทำ CRUD ครบด้วย Parameterized Query และจัดการ Transaction |
| Module 11 - Git | บันทึกประวัติ ทำงานกับ Branch ใช้ `.gitignore` ถูกต้อง และส่งขึ้น GitHub |
| Module 12 - GUI | สร้างหน้าจอด้วย Tkinter/ttk ผูก Event และใช้ `Treeview` แสดงข้อมูล |
| ★ Module 13 - Workshop | ได้ **PyShop Mini v2** ระบบครบวงจร GUI + PostgreSQL + ส่งออกรายงาน |

### 🎓 สรุปภาพรวมทั้งหลักสูตร

```
วันที่ 1: ปูพื้นฐาน                        วันที่ 2: ประยุกต์ใช้จริง
┌────────────────────────────┐          ┌────────────────────────────┐
│ Module 1  ภาพรวม Python     │          │ Module 7  ไฟล์ CSV/JSON     │
│ Module 2  uv + VS Code      │          │ Module 8  OOP               │
│ Module 3  ไวยากรณ์พื้นฐาน     │    ⟶    │ Module 9  Error + Debug     │
│ Module 4  Collections       │          │ Module 10 PostgreSQL        │
│ Module 5  Function          │          │ Module 11 Git + GitHub      │
│ Module 6  Module/Package    │          │ Module 12 GUI               │
│                            │          │ Module 13 Workshop รวม      │
│  → PyShop Mini v1 (Console)│          │  → PyShop Mini v2 (GUI+DB)  │
└────────────────────────────┘          └────────────────────────────┘
```

### ✅ เช็กลิสต์ความสามารถหลังจบหลักสูตร

> ให้ตรวจสอบตนเองว่าทำสิ่งเหล่านี้ได้โดยไม่ต้องเปิดเอกสาร:
>
> - [ ] สร้างโปรเจกต์ Python ใหม่ด้วย `uv init` และติดตั้งไลบรารีด้วย `uv add`
> - [ ] เขียนโปรแกรมที่มีเงื่อนไข ลูป และฟังก์ชันได้อย่างถูกต้องตาม PEP 8
> - [ ] เลือกใช้ List, Tuple, Set, Dictionary ให้เหมาะกับปัญหา
> - [ ] อ่าน-เขียนไฟล์ CSV/JSON ที่มีภาษาไทยโดยไม่เพี้ยน
> - [ ] ออกแบบคลาสที่มี Attribute, Method และตรวจสอบข้อมูลในตัว
> - [ ] จับข้อผิดพลาดด้วย `try/except` โดยระบุชนิดที่ชัดเจน
> - [ ] เชื่อมต่อฐานข้อมูลและเขียน SQL แบบ Parameterized Query
> - [ ] ใช้ Git บันทึกงานและส่งขึ้น GitHub โดยไม่หลุดข้อมูลลับ
> - [ ] อ่าน Traceback แล้วบอกได้ว่าต้องแก้ที่ไฟล์ไหน บรรทัดไหน
> - [ ] อธิบายให้คนอื่นฟังได้ว่าโค้ดที่ตนเองเขียนทำงานอย่างไร

### 🎁 สิ่งที่ควรทำภายใน 7 วันหลังจบอบรม

1. **ทบทวนโค้ดทั้งหมดอีกครั้ง** โดยลองพิมพ์เองใหม่แทนการคัดลอก
2. **หาปัญหาจริงในงานของตัวเองมาแก้ด้วย Python สักหนึ่งอย่าง** เช่น สคริปต์รวมไฟล์ Excel หรือเปลี่ยนชื่อไฟล์เป็นชุด
3. **ทำโจทย์ต่อยอดที่ค้างไว้ให้ครบ** โดยเฉพาะระดับ "ท้าทาย" ของ Workshop ปิดท้าย
4. **Push โค้ดขึ้น GitHub** เพื่อเป็นผลงานชิ้นแรกในโปรไฟล์ของคุณ
5. หากติดขัด สอบถามได้ที่ Line: @itgenius หรืออีเมล contact@itgenius.co.th

---

**💡 คำคมประจำวัน:**

> "โปรแกรมที่ดีไม่ใช่โปรแกรมที่ไม่เคยพัง แต่คือโปรแกรมที่เมื่อพังแล้วบอกได้ว่าพังตรงไหน เพราะอะไร และแก้ได้โดยไม่ทำให้ข้อมูลของผู้ใช้เสียหาย"

---

_เอกสารจัดทำโดย: อาจารย์สามิตร โกยม | IT Genius Engineering Co., Ltd._
_หลักสูตร Python Basic 2026 (พื้นฐานการเขียนโปรแกรมภาษา Python) - วันที่ 2 จาก 2_
_อบรมวันที่ 20-21 สิงหาคม 2569 | สถาบันไอทีจีเนียส เอ็นจิเนียริ่ง_
_ติดต่อ: โทร. 02-570-8449 | Line ID: @itgenius | www.itgenius.co.th_




