# 📖 Rubrica desktop-app

## 📌 Overview
**Rubrica** is a Python-based desktop app that allows users to manage contacts. 

## 🏗 Project Structure
```
📂 Rubrica/
│── 📂 src/
│   │── 📂 models/             # Contact entity
│   │   │── contact.py       
│   │── 📂 storage/            # Storage implementations
│   │   │── contact_storage.py       
│   │   │── sql_database.py      
│   │   │── file_storage.py  
│   │── 📂 application/        # Business logic
│   │   │── contact_controller.py  
│   │   │── view_controller.py     
│   │── 📂 views/                  
│   │   │── main_view.py           
│   │   │── add_edit_view.py
│   │── 📂 test/               # Pytests                  
│   │── main.py                    # Entry point
```

## 🛠️ Installation & Setup
### **Prerequisites**
Ensure you have **Python 3.12** installed. Lowers versions of Python have not been tested.
Tested on:
  - Windows 10
  - Linux

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/simoneorlando/rubrica.git
cd rubrica
```

### **2️⃣ Install Dependencies**
This project has no external dependencies, all the python modules used are in the standard
python library.

NOTE: the UI is based on the the tkinter package, the standard Python Interface.
On some systems you may need to install some packages to make it work.
More info at: https://tkdocs.com/tutorial/install.html

### **3️⃣ Run the Application**
```sh
python src/main.py
```

## 📜 License
This project is licensed under the **MIT License**.

