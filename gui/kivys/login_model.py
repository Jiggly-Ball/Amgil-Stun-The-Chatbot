login_kivy = """
<LoginScreen>:
	name: "kv_login_screen"
    
	MDTextField:
    	id: username
        required: True
		hint_text: "Enter username"
		icon_left: "account"
		pos_hint: {"center_x": 0.5, "center_y": 0.7}
		size_hint_x: None
		width: 300

	MDTextField:
		id: password
        required: True
		hint_text: "Enter password"
		icon_left: "key-variant"
        password: True
        
		pos_hint: {"center_x": 0.5, "center_y": 0.6}
		size_hint_x: None
		width: 300

	MDIconButton:
		icon: "eye-off"
		pos_hint: {"center_x": 0.69, "center_y": 0.61}
		pos: password.width - self.width + dp(8), 0
		theme_text_color: "Hint"
		on_release:
			self.icon = "eye" if self.icon == "eye-off" else "eye-off"
			password.password = False if password.password is True else True

	MDLabel:
		id: remember
		text: "Remember me"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
		font_size: 20
		halign: "center"
		size_hint_y: None
		height: self.texture_size[1]
		padding_y: 15

            
	MDFloatLayout:
		MDCheckbox:
			size_hint: None, None
			size: "48dp", "48dp"
			pos_hint: {'center_x': 0.69, 'center_y': 0.51}

	MDLabel:
		id: log_label
		text: ""
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
		font_size: 15
		halign: "center"
		size_hint_y: None
		height: self.texture_size[1]
		padding_y: 15
"""