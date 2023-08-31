chat_kivy = """

<ChatScreen>:
	name: "kv_chat_screen"

	#MDTopAppBar:
	#	md_bg_colour: app.theme_cls.primary_color
	#	elevation: 1
	#	title: "Chat with Lua"

	MDBoxLayout:
		#padding: 30

		MDScrollView:
			MDList:
				id: chat_data

	MDTextField:
		id: text_data
		hint_text: "Enter your text"
		mode: "fill"
		fill_color: 0, 0, 0, .4
        size_hint_x: None
        width: 700
        pos_hint: {"center_x": 0.4, "center_y": 0.1}

	MDRoundFlatButton:
		text: "Send"
		font_size: 12
		pos_hint: {"center_x":0.8, "center_y":0.1}
		on_press: self.parent.send_chat()
"""