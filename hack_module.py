from telethon import events
import os

@client.on(events.NewMessage(pattern=r"\.hack"))
async def hack_video(event):
    # Уведомляем пользователя, что процесс начался
    await event.edit("🛠 Starting the hacking sequence...")

    # Текст для видео
    hack_text = """
        SYSTEM BREACHED!
        Accessing mainframe...
        Downloading sensitive data...
        💻 HACK COMPLETE!
        Status: SUCCESS ✅
        Target: COMPROMISED
        """

    # Путь к видео
    video_path = "hack_video.mp4"

    # Проверяем, существует ли файл
    if not os.path.exists(video_path):
        await event.edit("⚠️ Video file not found! Make sure 'hack_video.mp4' is in the bot's directory.")
        return

    # Отправляем видео с текстом
    await client.send_file(event.chat_id, video_path, caption=hack_text)

    # Удаляем исходное сообщение
    await event.delete()
