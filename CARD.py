import telebot
import requests,json

token = "7022253924:AAFTeQyhjLFWwdA1qmnKId7bF-AkX-T9Mus"
bot = telebot.TeleBot(token)
us = bot.get_me().username


@bot.message_handler(commands=['start'])
def send_start_message(message):
    bot.reply_to(message,''' إرسال بطاقة الشحن  : 
 py :   @HIKR7''')

@bot.message_handler(func=lambda message: True)
def send_info(message):
    username = message.text.strip()
    url = "https://odpapp.asiacell.com/api/v1/top-up"
    params = {
  'lang': "ar"
}
    payload = json.dumps({
  "msisdn": "07763816651",
  "rechargeType": 1,
  "voucher": username
})
    headers = {
  'User-Agent': "okhttp/5.0.0-alpha.2",
  'Connection': "Keep-Alive",
  'Accept-Encoding': "gzip",
  'Content-Type': "application/json",
  'X-ODP-API-KEY': "1ccbc4c913bc4ce785a0a2de444aa0d6",
  'DeviceID': "a7df99df-a975-4f2a-b3cf-b3f3fb54e1a2",
  'X-OS-Version': "11",
  'X-Device-Type': "[Android][realme][RMX2189 11] [R]",
  'X-ODP-APP-VERSION': "3.8.0",
  'X-FROM-APP': "odp",
  'X-ODP-CHANNEL': "mobile",
  'X-SCREEN-TYPE': "MOBILE",
  'Authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzZXNzaW9uSUQiOjQzMTYzNjQsImV4cCI6MTcxNTMxOTMxMH0.kUXn10H91UI2MMrjKgZ7zL85bdvtALe8OVB6lmd9V7XW5kCGwAZGKzTRND7xlGDoWkzS9PFBTWvYCxMOdY85uw",
  'Cache-Control': "private, max-age=240"
}
    response = requests.post(url, params=params, data=payload, headers=headers).text
    if '''{"success":false,"message":"عذرا ، الرقم الذي أدخلته خاطئ. يرجى إدخال رقم بطاقة الشحن الصالحة والمحاولة مرة أخرى.","title":"","analyticData":{"event":"Recharge other_Recharge completed","params":{"Rcharge method":"Balance","Recharge Mode":"VOUCHER-CODE","B party number":"07763816651","Recaharge amount":"N/A","Status":"Fail","Status Description":"عذرا ، الرقم الذي أدخلته خاطئ. يرجى إدخال رقم بطاقة الشحن الصالحة والمحاولة مرة أخرى."}}}''' in response:
    
        bot.send_message(message.chat.id,f'''
--------------------erorr---------------
The balance has not been recharged 
----------------

        ''')
    else:
    	bot.send_message(message.message.chat.id,f'''
------------------------
The balance has been recharged 
----------------------
	''')

bot.polling()