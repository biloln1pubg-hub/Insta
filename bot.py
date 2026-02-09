import telebot
import yt_dlp
import os

TOKEN = "8527945906:AAGGvFw3NAiZpCTXDkWNls94p5peNwAx9j0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_link(message):
    url = message.text
    if "http" not in url: return

    status = bot.reply_to(message, "Yuklanmoqda... ⏳")
    file_name = f"video_{message.chat.id}.mp4"

    ydl_opts = {
        'format': 'best',
        'outtmpl': file_name,
        'quiet': True,
        'no_warnings': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        with open(file_name, 'rb') as video:
            bot.send_video(message.chat.id, video, caption="Tayyor! ✅")
        
        os.remove(file_name)
        bot.delete_message(message.chat.id, status.message_id)
        
    except Exception as e:
        bot.reply_to(message, "Xatolik: Video juda katta yoki linkda xato bor.")
        if os.path.exists(file_name): os.remove(file_name)

print("Bot yoqildi...")
bot.polling()

