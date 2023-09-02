setting_kivy = """
<SettingsScreen>:
	name: "kv_settings_screen"
	id: settings

	MDLabel:
		
		text: "Theme"
        pos_hint: {"center_x": 0.2, "center_y": 0.8}
		font_size: 20
		halign: "center"
		size_hint_y: None
		height: self.texture_size[1]
		padding_y: 15

	MDRaisedButton:
		id: theme_button
		text: app.theme_cls.theme_style
		pos_hint: {"center_x": 0.4, "center_y": 0.8}
		on_release:
			app.theme_menu(*args)

	MDLabel:
		text: "Primary Palette Colour"
        pos_hint: {"center_x": 0.2, "center_y": 0.7}
		font_size: 20
		halign: "center"
		size_hint_y: None
		height: self.texture_size[1]
		padding_y: 15

	MDRaisedButton:
		id: primary_palette_button
		text: app.theme_cls.primary_palette
		pos_hint: {"center_x": 0.4, "center_y": 0.7}
		on_release:
			app.primary_palette_menu(*args)

	MDLabel:
		id: setting_log
		text: "A restart is required when you make a change to the settings."
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
		font_size: 15
		halign: "center"
		size_hint_y: None
		height: self.texture_size[1]
		padding_y: 15

	MDIconButton:
		
		icon: "close-circle"
		pos_hint: {"center_x": 0.9, "center_y": 0.9}
		theme_text_color: "Hint"
		on_release: self.parent.manager.current = "kv_chat_screen"

		#MDNavigationLayout:
		#	MDNavigationDrawer:
		#		MDNavigationDrawerIconButton:
		#			text: "Dark"
		#			on_release: app.theme_cls.theme_style = "Dark"
		#			on_release: app.save_settings(*args)
#
		#		MDNavigationDrawerIconButton:
		#			text: "Light"
		#			on_release: app.theme_cls.theme_style = "Light"
		#			on_release: app.save_settings(*args)

"""