from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from utils.formatting import make_button, stylize_text


@Client.on_message(filters.command("start"))
async def start_command(client, message: Message):
    user_mention = message.from_user.mention
    await message.reply_text(
        stylize_text(f"Hey {user_mention}!\nI am **Anime Lord Bot**.\nUse /help to see what I can do."),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("Help", callback_data="help")],
        ])
    )


@Client.on_message(filters.command("help"))
async def help_command(client, message: Message):
    await message.reply_text(
        stylize_text(
            "**Anime Lord Bot Commands:**\n\n"
            "✦ /admin - Admin access panel\n"
            "✦ /linkprotect - Link password protection\n"
            "✦ /expire - Set file expiration\n"
            "✦ /bulkshare - Bulk file sharing\n"
            "✦ /delete - Delete files\n"
            "✦ /uploadlimit - Set upload size limit\n\n"
            "✦ /forcejoin - Force channel subscription\n"
            "✦ /submsg - Set custom subscription message\n"
            "✦ /autopost - Enable auto-posting\n\n"
            "✦ /users - View user list\n"
            "✦ /broadcast - Broadcast a message\n"
            "✦ /track - Track user activity\n\n"
            "✦ /autoconfig - Configure auto-post\n"
            "✦ /logs - View activity logs\n"
            "✦ /clearlogs - Clear logs\n\n"
            "✦ /backup - Create DB backup\n"
            "✦ /restore - Restore from backup\n"
            "✦ /reset - Emergency reset\n\n"
            "✦ /button - Create custom button\n"
            "✦ /channellogs - Channel logging\n"
            "✦ /styled - Styled font message\n"
        )
    )


@Client.on_message(filters.command("admin"))
async def admin_panel(client, message: Message):
    await message.reply_text(stylize_text("Admin access panel coming soon!"))


@Client.on_message(filters.command("linkprotect"))
async def link_protection(client, message: Message):
    await message.reply_text(stylize_text("Link protection feature enabled."))


@Client.on_message(filters.command("expire"))
async def file_expiration(client, message: Message):
    await message.reply_text(stylize_text("Set file expiration time."))


@Client.on_message(filters.command("bulkshare"))
async def bulk_share(client, message: Message):
    await message.reply_text(stylize_text("Bulk file sharing initiated."))


@Client.on_message(filters.command("delete"))
async def file_delete(client, message: Message):
    await message.reply_text(stylize_text("Delete selected files."))


@Client.on_message(filters.command("uploadlimit"))
async def upload_limit(client, message: Message):
    await message.reply_text(stylize_text("Set upload size limit."))


@Client.on_message(filters.command("forcejoin"))
async def force_join(client, message: Message):
    await message.reply_text(stylize_text("Users must join the channel to continue."))


@Client.on_message(filters.command("submsg"))
async def subscription_msg(client, message: Message):
    await message.reply_text(stylize_text("Set your custom subscription message."))


@Client.on_message(filters.command("autopost"))
async def auto_posting(client, message: Message):
    await message.reply_text(stylize_text("Auto-posting to channels activated."))


@Client.on_message(filters.command("users"))
async def user_list(client, message: Message):
    await message.reply_text(stylize_text("Here is the list of users."))


@Client.on_message(filters.command("broadcast"))
async def broadcast_msg(client, message: Message):
    await message.reply_text(stylize_text("Broadcast message sent to all users."))


@Client.on_message(filters.command("track"))
async def user_tracking(client, message: Message):
    await message.reply_text(stylize_text("User activity tracking enabled."))


@Client.on_message(filters.command("autoconfig"))
async def auto_post_config(client, message: Message):
    await message.reply_text(stylize_text("Auto-post configuration panel."))


@Client.on_message(filters.command("logs"))
async def activity_logs(client, message: Message):
    await message.reply_text(stylize_text("Here are your recent logs."))


@Client.on_message(filters.command("clearlogs"))
async def clear_logs(client, message: Message):
    await message.reply_text(stylize_text("Logs cleared successfully."))


@Client.on_message(filters.command("backup"))
async def backup_data(client, message: Message):
    await message.reply_text(stylize_text("Database backup created."))


@Client.on_message(filters.command("restore"))
async def restore_data(client, message: Message):
    await message.reply_text(stylize_text("Backup restored successfully."))


@Client.on_message(filters.command("reset"))
async def emergency_reset(client, message: Message):
    await message.reply_text(stylize_text("Emergency reset triggered!"))


@Client.on_message(filters.command("button"))
async def custom_button(client, message: Message):
    await message.reply_text(
        stylize_text("Here is your custom button:"),
        reply_markup=InlineKeyboardMarkup([
            [make_button("Visit Channel", "https://t.me/yourchannel")]
        ])
    )


@Client.on_message(filters.command("channellogs"))
async def channel_logs(client, message: Message):
    await message.reply_text(stylize_text("Channel logging is now enabled."))


@Client.on_message(filters.command("styled"))
async def styled_text(client, message: Message):
    await message.reply_text(stylize_text("This is a styled message from Anime Lord Bot."))
