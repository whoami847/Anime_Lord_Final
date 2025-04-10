from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ফন্ট স্টাইল (Anime Lord স্টাইল)
def stylize_text(text: str) -> str:
    fancy_font_map = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    return text.translate(fancy_font_map)

# সাধারণ টেক্সট ফরম্যাটিং (bold, italic)
def format_text(text: str, style: str = "bold") -> str:
    if style == "bold":
        return f"**{text}**"
    elif style == "italic":
        return f"__{text}__"
    elif style == "code":
        return f"`{text}`"
    else:
        return text

# একক ইনলাইন বাটন (text, url দিয়ে)
def make_button(text: str, url: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(text=text, url=url)

# মাল্টি বাটন ইনলাইন কিবোর্ড (list of rows)
def create_buttons(buttons: list) -> InlineKeyboardMarkup:
    keyboard = []
    for row in buttons:
        btn_row = [
            InlineKeyboardButton(
                text=btn["text"],
                url=btn.get("url", ""),
                callback_data=btn.get("callback")
            ) for btn in row
        ]
        keyboard.append(btn_row)
    return InlineKeyboardMarkup(keyboard)
