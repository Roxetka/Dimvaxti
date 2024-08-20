from pyrogram import Client, filters
from datetime import datetime, timedelta

# Botunuzun məlumatlarını daxil edin
api_id = "27745006"
api_hash = "99c2ff6828e7e73ad1614c572c43e3c4"
bot_token = "7290881276:AAEFO4yXUrekI3_Ji_Nq7XtEugzwjj4xtbY"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("vaxt"))
async def vaxt(client, message):
    # Bakı vaxtı ilə 21 avqust 21:00 üçün datetime obyektini yaradın
    target_time = datetime(2024, 8, 21, 21, 0, 0)

    # Cari vaxtı UTC+4 Bakı saatına uyğun əldə edin
    now = datetime.utcnow() + timedelta(hours=4)

    # Qalan vaxtı hesablayın
    remaining_time = target_time - now
    
    # Vaxt formatında hissələrə ayırın
    hours, remainder = divmod(remaining_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    # Nəticəni formatlayın
    time_str = f"{int(hours)} saat {int(minutes)} dəqiqə {int(seconds)} saniyə"

    # Cavab göndərin
    await message.reply_text(time_str)
print(“IWLEYIREM QARDAWIM”)
app.run()
