from gui.kivys.login_model import login_kivy
from gui.kivys.chat_model import chat_kivy

app_kivy = f"""
    
{login_kivy}

{chat_kivy}

ScreenManager:
	LoginScreen:
    ChatScreen:
    
"""