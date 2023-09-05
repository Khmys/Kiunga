import os
from pyrogram import Client, filters
import feedfinder2
import re

app = Client("FeedFinder")

mfano = '''
1. Mfano,  in group au private:
 ✍ /check_feed http://www.alhidaaya.com/sw/homepage  kisha tuma, 
 
 Au /check_feed alhidaaya.com/sw/homepage
 

2. Mfano wa pili: 
✍ /tf http://firqatunnajia.com/
✍ /tf https://islamhouse.com/sw/main/

3. Kama ni private siyo kwenye group au Channel Tuma link bila Command:
📋  https://uongofu.com/

📋 https://www.al-feqh.com/sw

Kama una link **Copy** kisha **Paste** Bot atakuangalizia kama URL Yako ina RSS
 


'''


# Function to send a message with the title and URL to the user
def send_blog_post(chat_id, title, url):
    message = f"{title}\n{url}"
    app.send_message(chat_id=chat_id, text=message)

# Function to find RSS feed URL from the given URL
def find_rss_url(url):
    rss_urls = feedfinder2.find_feeds(url)
    return rss_urls
    
# Handler for /start command
@app.on_message(filters.command(["start", "rss", "feed"]) & (filters.private))
def start(_, message):
    message.reply_text("Karibu Tuma URL Nikutafutie **RSS, Feeds** \n\nAutuma /tf or /check_feed na **URL** ili kuchunguza kama ina **RSS feed.**\n\nHauja elewa gusa 👣👉 /example 👀")

# Handler for /check_feed command
@app.on_message(filters.regex(r"(?P<url>https?://[^\s]+)") & filters.private)
def check_feed(client, message):
    chat_id = message.chat.id
    url_match = message.matches[0].group("url") if message.matches else None

    if url_match:
        rss_urls = find_rss_url(url_match)
        if rss_urls:
            response = "➊ Feeds:\nTovuti ina RSS feed!\n" + "\n".join(rss_urls)
            client.send_message(chat_id, response)
        else:
            client.send_message(chat_id, f"➊ Tovuti hii {url_match} haipatikani au haina RSS feed.\n\n⚠ Musaada hapa  /example")
    else:
        client.send_message(chat_id, "➊ Tuma URL ya tovuti unayotaka kuchunguza.")
        
        
@app.on_message(filters.command(["tf", "check_feed"]))
def check_kiunga(client, message):
    chat_id = message.chat.id
    if len(message.command) > 1:
        url = message.command[1]
        rss_urls = find_rss_url(url)
        if rss_urls:
            response = "➋ Feeds:\nTovuti ina RSS feed!\n" + "\n".join(rss_urls)
            client.send_message(chat_id, response)
        else:
            client.send_message(chat_id, "➋ Tovuti hii {mesaage_user}  haipatikani au haina RSS feed.\n\n⚠ Musaada hapa /example")
    else:
        client.send_message(chat_id, "➋ Tuma /tf au /check_feed na URL ya tovuti unayotaka kuchunguza.")

@app.on_message(filters.command(["mfano", "example"]))
def musaada(_, message):
    message.reply_text(mfano, disable_web_page_preview=True)

# Start the bot
print("finder feed")
app.run()