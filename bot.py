
import telepot
import pymysql

# تأكد من استبدال هذه القيم بمعلومات الاتصال الصحيحة
db = pymysql.connect(host="localhost", user="root", password="", database="student_results")
cursor = db.cursor()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, "مرحبًا! الرجاء إدخال رقم الجامعة الخاص بك للحصول على النتائج.")
        else:
            university_id = msg['text']
            cursor.execute(f"SELECT * FROM students WHERE university_id = '{university_id}'")
            student = cursor.fetchone()
            if student:
                result_message = f"الاسم الكامل: {student[2]}\nالقسم: {student[3]}\nالمرحلة: {student[4]}\n" \
                                 f"معالجة اشارة رقمية: {student[5]}\nالاتصالات: {student[6]}\nالشبكات: {student[7]}\n" \
                                 f"منظومات زمن حقيقي: {student[8]}\nالرياضيات: {student[9]}\nالإنجليزية: {student[10]}\n" \
                                 f"قواعد البيانات: {student[11]}\nالتحكم: {student[12]}"
                bot.sendMessage(chat_id, result_message)
            else:
                bot.sendMessage(chat_id, "الطالب غير موجود. الرجاء إدخال رقم جامعي صحيح.")

TOKEN = '6830009269:AAHzJqkHj-fScnESlXkGnVY_CXNymrz4xos'
bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print('Listening ...')

import time
while 1:
    time.sleep(10)
