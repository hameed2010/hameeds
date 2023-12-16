import telebot
from telebot import types
bot = telebot.TeleBot("6594487166:AAHRg285W0JtRqW9COs7GyENgpY-tgfI_ys")
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
sheet=client.open("amsdr").sheet1
name = ""
age = ""
emali=""
address=""
Employment=""

Delivery_Service=""
Product_details=""
Service_details=""
Navigate_province=""
Service_field=""
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "مرحبًا بك! الرجاء إدخال اسمك.")
    
        
    bot.register_next_step_handler(message, get_name)

# يتم استدعاء هذه الدالة للحصول على اسم المستخدم
def get_name(message):
    global name
    chat_id = message.chat.id
    name = message.text
    bot.send_message(chat_id, "اسمك هو: " + name)
    bot.send_message(chat_id, "الرجاء إدخال عمرك.")
    
    bot.register_next_step_handler(message, get_age)

# يتم استدعاء هذه الدالة للحصول على عمر المستخدم
def get_age(message):
    global age
    chat_id = message.chat.id
    age = message.text
    bot.send_message(chat_id, "عمرك هو: " + age)
    bot.send_message(chat_id, "الرجاء إدخال البريد الاكتروني.")
    bot.register_next_step_handler(message, emali_bot)
def emali_bot(message):
    global emali
    chat_id = message.chat.id
    emali = message.text
    bot.send_message(chat_id, "البريد الاكتروني هو: " + emali)
    bot.send_message(chat_id, "الرجاء إدخال العنوان .")
    bot.register_next_step_handler(message, get_address)
#     insert_data(name,age)
def get_address(message):
    global address
    chat_id = message.chat.id
    address = message.text
    bot.send_message(chat_id, "العنوان هو: " + address)
    
    reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_yes = telebot.types.KeyboardButton('منتج')
    button_no = telebot.types.KeyboardButton('خدمة')
    reply_markup.add(button_yes, button_no)
    bot.send_message(chat_id, "هل لديك منتج او خدمة ", reply_markup=reply_markup)
    bot.register_next_step_handler(message, get_product_or_service)
def get_product_or_service(message):
    global product_or_service
    chat_id = message.chat.id
    product_or_service = message.text
    if product_or_service=="منتج":
        reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_yes = telebot.types.KeyboardButton('جملة')
        button_no = telebot.types.KeyboardButton('تجزئة')
        reply_markup.add(button_yes, button_no)
        bot.send_message(chat_id, "مجال العمل (جملة  -  تجزئة) ", reply_markup=reply_markup)
        
        bot.register_next_step_handler(message, get_Employment)
    elif product_or_service=="خدمة":
        reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        button_yes = telebot.types.KeyboardButton('رقمية')
        button_no = telebot.types.KeyboardButton('يدوية')
        reply_markup.add(button_yes, button_no)
        bot.send_message(chat_id, "مجال الخدمة (رقمية  -  يدوية) ", reply_markup=reply_markup)
        
        bot.register_next_step_handler(message, get_Service_field)
        

def get_Employment(message):
    global Employment
    chat_id = message.chat.id
    Employment = message.text
    bot.send_message(chat_id, "مجال العمل هو: " + Employment)
    reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button_yes = telebot.types.KeyboardButton('نعم')
    button_no = telebot.types.KeyboardButton('لا')
    reply_markup.add(button_yes, button_no)
    bot.send_message(chat_id, "هل لديك  خدمة توصيل ", reply_markup=reply_markup)
    bot.send_message(chat_id, "  هل لديك  خدمة توصيل  .")
    bot.register_next_step_handler(message, get_Delivery_Service)  
def get_Delivery_Service(message):
    global Delivery_Service
    chat_id = message.chat.id
    Delivery_Service = message.text
    bot.send_message(chat_id, "خدمة التوصيل هو: " + Delivery_Service)
    bot.send_message(chat_id, " تفاصيل المنتج المعروضة  .")
    bot.register_next_step_handler(message, get_Product_details)  
def get_Product_details(message):
    global Product_details
    chat_id = message.chat.id
    Product_details = message.text
    bot.send_message(chat_id, "تفاصيل المنتج  هو: " + Product_details)
    insert_data(name, age,emali,address,Employment,Delivery_Service,Product_details)

###############################################################################
  
def get_Service_field(message):
    global Service_field
    chat_id = message.chat.id
    Service_field = message.text
    bot.send_message(chat_id, "مجال الخدمة هو: " + Service_field)
    bot.send_message(chat_id, "  هل مستعد للتنقل في محافظتك لتقديم خدماتك ام داخل المنطقة السنكنية فقط .")
    bot.register_next_step_handler(message, get_Navigate_province)     
def get_Navigate_province(message):
    global Navigate_province
    chat_id = message.chat.id
    Navigate_province = message.text
    bot.send_message(chat_id, " التنقل في محافظتك  هو: " + Navigate_province)
    bot.send_message(chat_id, "  تفاصيل الخدمة   التي تقدمها .")
    bot.register_next_step_handler(message, get_Service_details)  
def get_Service_details(message):
    global Service_details
    chat_id = message.chat.id
    Service_details = message.text
    bot.send_message(chat_id, "تفاصيل الخدمة  هو: " + Service_details)
    insert_data(name, age,emali,address,Service_field,Navigate_province,Service_details)


def insert_data(name, age,emali,address,Employment,Delivery_Service,Product_details):
    new_row = [name, age,emali,address,Employment,Delivery_Service,Product_details]
    num_rows = sheet.get_all_values()
    sheet.insert_row(new_row, len(num_rows) + 1)
bot.polling()