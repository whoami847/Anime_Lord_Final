from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ফন্ট স্টাইল (Anime Lord স্টাইল)
def stylize(text: str) -> str:
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

# ইনলাইন বাটন জেনারেটর
def create_buttons(buttons: list) -> InlineKeyboardMarkup:
    keyboard = []
    for row in buttons:
        btn_row = [InlineKeyboardButton(text=btn["text"], url=btn.get("url", ""), callback_data=btn.get("callback")) for btn in row]
        keyboard.append(btn_row)
    return InlineKeyboardMarkup(keyboard)
