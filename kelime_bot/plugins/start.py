from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun, rating
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *
from kelime_bot import USERNAME



keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕𝐌ə𝐧𝐢 𝐪𝐫𝐮𝐩𝐚 ə𝐥𝐚𝐯ə 𝐞𝐭➕", url=f"http://t.me/XAOS_Gamebot?startgroup=new")
    ],
    [
        InlineKeyboardButton(" 𝐎𝐰𝐧𝐞𝐫 🇦🇿 ", url="t.me/sesizKOLGE"),
        InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="t.me/XaosResmii"),
    ]
])
 
 
START = """
**👋 Salam 𝕏𝔸𝕆𝕊 𝔾𝔸𝕄𝔼 Söz Oyun Botuna xoş gəldin.**\n🤖** Bu Bot İlə Qarışıq Həriflərdən İbarət Söz Tapmaq Oyunu Oynaya Bilərsiniz..**
 
➤ Oyun Qaydaları üçün 👉 /help Üzərinə Klikləyin. 📚 Əmrlər Asan və Sadədir.
"""
 
HELP = """
** Əmrlər menyusuna xoş gəldin.**
 
 
✅ /start - Botu Başladar..
🎮 /oyna - Söz Tap Oyunu Başladar.. 
➡️ /kec - Növbəti Sözə Keçər..
🏆 /reyting - Qruplar Üzrə Oyunçu Reyrinqi
⛔ /dayan - Söz Tap Oyununu Sonlandırar
"""
 
# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/7770592d74a8bf3236382.jpg",caption=START,reply_markup=keyboard)
 
@Client.on_message(filters.command("help", [".", "!", "/", "@"]))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/7770592d74a8bf3236382.jpg",caption=HELP) 
 
# Oyunu başlat. 
@Client.on_message(filters.command("oyna", ["!", "/", "@", "."])) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False
 
    if aktif:
        await m.reply("**❗ Hal-Hazırda Qrupunuzda  Oyun Davam Edir ✍🏻 \n Oyunu Sonlandırmaq Üçün /dayan Əmrindəm İsdifadə Edin")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfindən! \nSöz Tapma Oyunu Başladı .\n\nUğurlar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/100 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığın Xal: 50
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 
 
✏️ Qarışıq Hərflərdən İbarət Sözü Tapın 
        """
        await c.send_message(m.chat.id, text)
        
        
        
@Client.on_message(filters.command("data") & filters.user("realjihokimin")) 
async def data(c:Client, m):
    await m.reply(oyun)
    await m.reply(rating
    
    
    
@Client.on_message(filters.command("kec", ["!", "/", "@"]) & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False
 
    if aktif:
        if oyun[m.chat.id]["kec"] < 30:
            oyun[m.chat.id]["kec"] += 1
            await c.send_message(m.chat.id,f"✅ Sizin Tam Yol Haqqınız Var!\n➡️ Növbəti sözə Keçdim !\n✏️ Doğru söz : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/100 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığın Xal : 50
🔎 İ𝗉𝗎𝖼𝗎 : 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 𝖴𝗓𝗎𝗇𝗅uq: {int(len(kelime_list)/2)} 
 
✏️ Qarışıq Hərflərdən İbarət Sözü Tapın 
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>**❗ Keçid Düzgün Saxlanıldı! </code> \n Oyunu dayandırmaq üçün  /dayan yaza bilərsiniz ✍🏻**")
    else:
        await m.reply(f"❗ **Qrupumuzda aktiv oyun yoxdur!\n Yeni oyuna başlamaq üçün /oyna yaza bilərsiniz ✍🏻**")
        
        
        
@Client.on_message(filters.command("reyting"))
async def ratingsa(c:Client, m:Message):
    global rating
    metin = """🏆 Qlobal Qrup Reytinqi :
 
"""
    eklenen = 0
    puanlar = []
    for kisi in rating:
        puanlar.append(rating[kisi])
    puanlar.sort(reverse = True)
    for puan in puanlar:
        for kisi in rating:
            if puan == rating[kisi]:
                metin += f"**{kisi}** : {puan}  puan\n"
                eklenen += 50
                if eklenen == 30:
                    break
                
    await c.send_message(m.chat.id, metin)    
   
@Client.on_message(filters.command("dayan") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f"{i}   :   {oyun[m.chat.id]['oyuncular'][i]} Bal")
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**{m.from_user.mention}** Tərəfindən Oyun sonlandırıldı\n\nYeni Oyuna Başlamaq Üçün /oyna Yaza Bilərsən\n\n 📝 Xallar səyfəsi  :\n\n{siralama_text}")
    oyun[m.chat.id] = {}
         
        
@Client.on_message(filters.text & ~filters.private & ~filters.channel)
async def buldu(c:Client, m:Message):
    global oyun
    global rating
    try:
        if m.chat.id in oyun:
            if m.text.lower() == oyun[m.chat.id]["kelime"]:
                await c.send_message(m.chat.id,f"✨ Tebrikler !\n**{m.from_user.mention}** \n**<code>{oyun[m.chat.id]['kelime']}</code>** , Sözünü Tapdi ✅")
                if f"{m.from_user.mention}" in rating:
                    rating[f"{m.from_user.mention}"] += 50
                else:
                    rating[f"{m.from_user.mention}"] = 50
                
                try:
                    puan = oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)]
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] +=50
                except KeyError:
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] = 50
                
                
                oyun[m.chat.id]["kelime"] = kelime_sec()
                oyun[m.chat.id]["round"] = oyun[m.chat.id]["round"] + 1
                
                if not oyun[m.chat.id]["round"] <= 100:
                    siralama = []
                    for i in oyun[m.chat.id]["oyuncular"]:
                        siralama.append(f"{i} :   {oyun[m.chat.id]['oyuncular'][i]}  Bal")
                    siralama.sort(reverse=True)
                    siralama_text = ""
                    for i in siralama:
                        siralama_text += i + "\n"
                    
                    return await c.send_message(m.chat.id,f"✅ Oyun Bitti✓ \n\n📝 Puan :\n\n{siralama_text}\n\n Yeni Oyuna Başlamaq Üçün /oyna Yaza Bilərsiniz !")
                
                
                
                kelime_list = ""
                kelime = list(oyun[m.chat.id]['kelime'])
                shuffle(kelime)
                for harf in kelime:
                    kelime_list+= harf + " "
            
                text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/100 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığın Xal : 50
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 
 
✏️ Qarışıq hərflərdən ibarət sözü tapın 
                        """
                await c.send_message(m.chat.id, text)
    except KeyError:
        pass
    
    
gonderilmedi = True
data_message = None
EKLENEN_CHATS = []
@Client.on_message()
async def data(c:Client, m:Message):
    global EKLENEN_CHATS
    global gonderilmedi
    global data_message
    
    chat_id = str(m.chat.id)
    
    if chat_id in EKLENEN_CHATS:
        return
 
    if gonderilmedi:
        data_message= await c.send_message(OWNER_ID, f"{OWNER_ID}")
        gonderilmedi = False
        
    
    else:
        chats = await c.get_messages(OWNER_ID, data_message.message_id)
        chats = chats.text.split()
        
        if chat_id in chats:
            pass
        else:
            chats.append(chat_id)
            EKLENEN_CHATS.append(chat_id)
            data_text = ""
            for i in chats:
                data_text += i + " "
            await c.edit_message_text(OWNER_ID, data_message.message_id, data_text)
            
                 
        
        








