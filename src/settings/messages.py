class TextMessages():
	def __init__(s, lang):
		# create command
		s.PROJECTS_DOES_NOT_EXISTS = {
			"fr": ":x: Ce project n'existe pas !",
			"en": ":x: This project doesn't exist!"
		}
		s.GROUP_ALREADY_EXISTS = {
			"fr": ":x: Tu as déjà crée un group pour ce projet !",
			"en": ":x: You already created a group for this project!"
		}
		s.HAS_NOT_MINIMUM_SIZE = {
			"fr": ":x: La taille limite doit être supérieure à 1 !",
			"en": ":x: The size limit must be upper than 1!"
		}

		# list command
		s.CURRENT_GROUPS_EMBED_TITLE = {
			"fr": "Groupes en formation",
			"en": "Current groups"
		}
		s.CONFIRMED_GROUPS_EMBED_TITLE = {
			"fr": "Groupes confirmés",
			"en": "Confirmed groups"
		}
		s.PROJECT_NOT_FOUND = {
			"fr": "Aucun projet trouvé.",
			"en": "No project found."
		}
		s.LIST_CONTENT = {
			"en": "**%s** %s\n"
		}

		# join group button
		s.ALREADY_IN_GROUP = {
			"fr": ":x: Tu fait déjà partie de ce groupe !",
			"en": ":x: You are already in this group!"
		}
		s.GROUP_LOCKED_CANT_JOIN = {
			"fr": ":lock: Ce groupe est fermé, tu ne peux pas le rejoindre !",
			"en": ":lock: This group is locked, you cannot join it!"
		}
		s.GROUP_IS_FULL = {
			"fr": ":x: Ce group est complet !",
			"en": ":x: This group is full!"
		}
		s.USER_JOIN_GROUP_TO_LEADER = { #1
			"fr": "%s a rejoint ton groupe **%s** ! %s",
			"en": "%s joined your group **%s**! %s"
		}
		s.GROUP_IS_FULL_TO_LEADER = { #2
			"fr": "Vous êtes maintenant au complet !",
			"en": "Your group is now full!"
		}
		s.USER_JOIN_GROUP = {
			"fr": "Tu as rejoins **%s**",
			"en": "You have joined **%s**."
		}

		# leave group button
		s.GROUP_LOCKED_CANT_LEAVE = {
			"fr": ":lock: Ce groupe est fermé, il semblerait que tu sois coincé ! :smirk:",
			"en": ":lock: This group is locked, it seems that you are stuck! :smirk:"
		}
		s.DELETE_EMPTY_GROUP = {
			"fr": ":cry: Il n'y a plus personne dans le groupe, celui-ci a donc été supprimé.",
			"en": ":cry: No one left in the group, it has been deleted."
		}
		s.USER_LEFT_GROUP_TO_LEADER = {
			"fr": "%s a quitté ton groupe **%s** ! %s",
			"en": "%s left your group **%s**! %s"
		}
		s.NEW_GROUP_LEADER = {
			"fr": "Tu es maitenant le nouveau chef de groupe de **%s** ! %s",
			"en": "You are now the new group leader of **%s**! %s"
		}
		s.USER_LEFT_GROUP = {
			"fr": "Tu as quitté **%s**.",
			"en": "You have left **%s**."
		}

		# confirm group button
		s.CONFIRM_GROUP_MINIMUM_SIZE = {
			"fr": ":x: Tu ne peux confirmer un groupe qu'avec un minimum de 2 personnes !",
			"en": ":x: You can only confirm a group with a minimum of 2 people!"
		}
		s.CONFIRM_GROUP_NOT_AUTHORIZED = {
			"fr": ":x: Seulement le chef de groupe peut confirmer le groupe !",
			"en": ":x: Only the group leader can confirm the group!"
		}
		s.CONFIRM_GROUP_TO_MEMBERS = {
			"fr": "%s a confirmé le groupe **%s** ! %s",
			"en": "%s confirmed the group **%s**! %s"
		}
		s.CONFIRM_GROUP = { #1
			"fr": "Tu as %s le groupe **%s**.",
			"en": "You have %s the group **%s**."
		}
		s.CONFIRM_GROUP_STATUS_UNLOCKED = { #2
			"fr": "ouvert",
			"en": "opened"
		}
		s.CONFIRM_GROUP_STATUS_CONFIRMED = { #2
			"fr": "confirmé",
			"en": "confirmed"
		}

		# delete group button
		s.DELETE_GROUP_NOT_AUTHORIZE = {
			"fr": ":x: Seulement le chef de groupe peut supprimer le groupe !",
			"en": ":x: Only the leader can delete the group!"
		}
		# group modal
		s.DELETE_GROUP = {
			"fr": "Le groupe **%s** as été supprimé.",
			"en": "The group **%s** has been deleted."
		}
		s.DELETE_GROUP_TO_MEMBERS = {
			"fr": "%s a supprimé le groupe **%s** !",
			"en": "%s has deleted the group **%s**!"
		}

		s.NOT_IN_GROUP = {
			"fr": ":x: de quoi je me mèles ?",
			"en": ":x: You are not part of this group!"
		}

		# assign language to every dict attributes
		for attr_name in vars(s):
			attr_value = getattr(s, attr_name)
			if isinstance(attr_value, dict):
				setattr(s, attr_name, attr_value.get(lang, attr_value.get("en")))

