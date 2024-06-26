class TextMessages():
	def __init__(s, lang):
		# create command
		s.PROJECTS_DOES_NOT_EXISTS = {
			"fr": ":x: Ce project n'existe pas !",
			"en": ":x: This project doesn't exist!"
		}
		s.GROUP_ALREADY_EXISTS = {
			"en": ":x: You already created a group for this project!"
		}
		s.HAS_NOT_MINIMUM_SIZE = {
			"en": ":x: The size limit must be upper than 1!"
		}

		# list command
		s.CURRENT_GROUPS_EMBED_TITLE = {
			"en": "Current Groups"
		}
		s.CONFIRMED_GROUPS_EMBED_TITLE = {
			"en": "Confirmed Groups"
		}
		s.PROJECT_NOT_FOUND = {
			"en": "No project found."
		}
		s.LIST_CONTENT = {
			"en": "**%s** %s\n"
		}

		# join group button
		s.ALREADY_IN_GROUP = {
			"en": ":x: You are already in this group!"
		}
		s.GROUP_LOCKED_CANT_JOIN = {
			"en": ":lock: This group is locked, you cannot join it!"
		}
		s.GROUP_IS_FULL = {
			"en": ":x: This group is full!"
		}
		s.USER_JOIN_GROUP_TO_LEADER = { #1
			"en": "%s joined your group **%s**! %s"
		}
		s.GROUP_IS_FULL_TO_LEADER = { #2
			"en": "\nYour group is now full!"
		}
		s.USER_JOIN_GROUP = {
			"en": "You have joined **%s**."
		}

		# leave group button
		s.GROUP_LOCKED_CANT_LEAVE = {
			"en": ":lock: This group is locked, it seems that you are stuck!"
		}
		s.DELETE_EMPTY_GROUP = {
			"en": ":cry: No one left in the group, it has been deleted."
		}
		s.USER_LEFT_GROUP_TO_LEADER = {
			"en": "%s left your group **%s**! %s"
		}
		s.NEW_GROUP_LEADER = {
			"en": "You are now the new group leader of **%s**! %s"
		}
		s.USER_LEFT_GROUP = {
			"en": "You have left **%s**."
		}

		# confirm group button
		s.CONFIRM_GROUP_MINIMUM_SIZE = {
			"en": ":x: You can only confirm a group with a minimum of 2 people!"
		}
		s.CONFIRM_GROUP_NOT_AUTHORIZED = {
			"en": ":x: Only the group leader can confirm the group!"
		}
		s.CONFIRM_GROUP_TO_MEMBERS = {
			"en": "%s confirmed the group for **%s**! %s"
		}
		s.CONFIRM_GROUP = {
			"en": "You have %s the group **%s**."
		}

		# delete group button
		s.DELETE_GROUP_NOT_AUTHORIZE = {
			"en": ":x: Only the leader can delete the group!"
		}
		# group modal
		s.DELETE_GROUP = {
			"en": "You have deleted the group **%s**."
		}
		s.DELETE_GROUP_TO_MEMBERS = {
			"en": "%s has deleted the group **%s**!"
		}

		s.NOT_IN_GROUP = {
			"en": ":x: You are not part of this group!"
		}

		# assign language to every dict attributes
		for attr_name in vars(s):
			attr_value = getattr(s, attr_name)
			if isinstance(attr_value, dict):
				setattr(s, attr_name, attr_value.get(lang, attr_value.get("en")))

