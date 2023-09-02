account_kivy = """
<AccountScreen>:
	name: "kv_account_screen"

	MDLabel:
    	id: username
		text: "Username"
		icon_left: "account"
		pos_hint: {"center_x": 0.5, "center_y": 0.7}
		size_hint_x: None
		width: 300

	MDRoundFlatButton:
		text: "Logout"
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		theme_text_color: "Hint"
		#on_release:
		#	self.icon = "eye" if self.icon == "eye-off" else "eye-off"
		#	password.password = False if password.password is True else True
"""