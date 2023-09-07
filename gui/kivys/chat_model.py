chat_kivy = """
<ChatScreen>:
	name: "kv_chat_screen"

	MDBoxLayout:
		padding: 95

		MDScrollView:
			id: scroll
			
			MDList:
				id: chat_data
				
	MDTextField:
		id: text_data
		hint_text: "Enter your text"
		mode: "fill"
		fill_color: 0, 0, 0, .4
        size_hint_x: None
        width: 800
        pos_hint: {"center_x": 0.4, "center_y": 0.07}

	MDRoundFlatButton:
		id: send
		text: "Send"
		font_size: 12
		pos_hint: {"center_x":0.8, "center_y":0.07}
		on_press: self.parent.send_chat()

	MDBoxLayout:
		padding: "12dp"
		pos_hint: {"center_x": 1.4}

		MDNavigationRail:
			#md_bg_color: app.theme_cls.primary_palette
			anchor: "center"

			MDNavigationRailMenuButton:
				icon: "cog"
				text: "Settings"
				pos_hint: {"center_x": 0.47, "center_y": 0.9}
				on_release: self.parent.parent.parent.parent.manager.current = "kv_settings_screen"

			MDNavigationRailMenuButton:
				icon: "account"
				text: "Account"
				pos_hint: {"center_x": 0.47, "center_y": 0.8}
				on_release: self.parent.parent.parent.parent.manager.current = "kv_account_screen"
"""