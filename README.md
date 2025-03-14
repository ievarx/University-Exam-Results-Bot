
### **📌 University Exam Results Bot - Database Project (2023-2024) ✅**  

This repository contains the **University Exam Results Bot**, a **university database project** that allows students to check their exam results via Telegram. The bot retrieves student grades from a **MySQL** database based on their student ID. **Q2.txt** contains sample data for testing purposes.  

📌 **This project was developed as a mandatory university assignment for the 2023-2024 academic year.**  

#### **📂 Project Files:**  
- **`Query.txt`** → Contains SQL queries to create the exam results database.  
- **`Q2.txt`** → Contains sample data for testing the bot's functionality.  
- **`bot.py`** → The main script for running the Telegram results bot.  

#### **🚀 Features:**  
- Developed as a **mandatory university assignment**.  
- Retrieves exam results from a **MySQL** database.  
- Students can enter their **student ID** to get their grades instantly.  
- **Q2.txt** provides sample data for testing purposes.  

#### **⚙️ How to Install & Run:**  
1. **Clone the repository:**  
   ```bash
   git clone https://github.com/ievarx/University-Exam-Results-Bot.git
   ```  
2. **Install dependencies:**  
   Run the following commands:  
   ```bash
   pip install python-telegram-bot==13.7.0  
   pip install mysql-connector-python  
   ```  
3. **Create the database:**  
   - Open **MySQL** and execute the queries from **`Query.txt`** to create the database.  
4. **Add sample data (optional for testing):**  
   - Use **`Q2.txt`** to insert test data into the database for testing purposes.  
5. **Run the bot:**  
   ```bash
   python bot.py  
   ```  

💡 **Notes:**  
- Ensure that your **Telegram bot token** is correctly configured inside `bot.py`.  
- The bot must have permission to send and receive messages.  
- Feel free to contribute or suggest improvements! 😊  

---
