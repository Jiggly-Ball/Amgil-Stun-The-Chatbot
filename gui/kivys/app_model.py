from gui.kivys.login_model import login_kivy
from gui.kivys.chat_model import chat_kivy
from gui.kivys.setting_model import setting_kivy
from gui.kivys.account_model import account_kivy
from local.data import Data

app_kivy = f"""
    
{login_kivy}

{chat_kivy}

{setting_kivy}

{account_kivy}

ScreenManager:
	id: screen_manager
	{"LoginScreen" if not Data.login_allow else "ChatScreen"}:
    {"LoginScreen" if Data.login_allow else "ChatScreen"}:
	SettingsScreen:
	AccountScreen:
"""