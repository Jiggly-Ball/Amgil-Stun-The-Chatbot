account_kivy = """
<AccountScreen>:
	name: "kv_account_screen"

	MDIcon:
		icon: "account-circle-outline"
		font_size : 75
		pos_hint: {"center_x": .5, "center_y": .9}

	MDLabel:
		text: "Username"
		pos_hint: {"center_x": 0.2, "center_y": 0.7}
		halign: "center"
		size_hint_x: None
		height: self.texture_size[1]
		padding_y: 15
		width: 300

	MDLabel:
		text: "Password"
		pos_hint: {"center_x": 0.2, "center_y": 0.6}
		halign: "center"
		size_hint_x: None
		height: self.texture_size[1]
		padding_y: 15
		width: 300
		
	MDLabel:
		id: username
		text: app.username #self.parent.username
		pos_hint: {"center_x": 0.5, "center_y": 0.7}
		font_size: 20
		halign: "center"
		size_hint_x: None
		height: self.texture_size[1]
		padding_y: 15
		width: 300

	MDLabel:
		id: password
		text: app.password # self.parent.password
		pos_hint: {"center_x": 0.5, "center_y": 0.6}
		halign: "center"
		size_hint_x: None
		height: self.texture_size[1]
		padding_y: 15
		width: 300


	MDRoundFlatButton:
		text: "Logout"
		pos_hint: {"center_x": 0.5, "center_y": 0.5}
		theme_text_color: "Hint"
		on_release:
			self.parent.logout()
			self.parent.manager.current = "kv_login_screen"

	MDIconButton:
		icon: "close-circle"
		pos_hint: {"center_x": 0.9, "center_y": 0.9}
		theme_text_color: "Hint"
		on_release: self.parent.manager.current = "kv_chat_screen"
"""