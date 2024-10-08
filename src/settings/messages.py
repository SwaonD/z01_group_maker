class TextMessages():
	def __init__(s, lang):

		# event on ready
		s.CHANNEL_COMMAND_ONLY = {
			"fr": "Seulement les commandes sont autorisées dans %s.",
			"en": "Only commands are allowed in %s"
		}

		# create command
		s.GROUP_CHANNEL_NOT_CONFIGURED = {
			"fr": "Aucun channel de group n'a été configuré, utilisez la commande /config en tant qu'administrateur pour l'ajouter.",
			"en": "No group channel configured, pls use /config as an administrator"
		}
		s.PROJECTS_DOES_NOT_EXISTS = {
			"fr": ":x: Ce project n'existe pas !",
			"en": ":x: This project doesn't exist!"
		}
		s.GROUP_ALREADY_EXISTS = {
			"fr": ":x: Tu as déjà crée un group pour ce projet !",
			"en": ":x: You already created a group for this project!"
		}
		s.GROUP_HAS_NOT_MIN_SIZE = {
			"fr": ":x: La taille limite du groupe doit être supérieure à 1 !",
			"en": ":x: The size limit of the group must be upper than 1!"
		}
		s.GROUP_OVER_MAX_SIZE = {
			"fr": ":x: La taille limite du groupe est de %s !",
			"en": ":x: The size limit of the group is %s !"
		}
		s.GROUP_DESCRIPTION_OVER_MAX_CHARS = {
			"fr": ":x: Le nombre de charactères maximum pour la description est de %s !",
			"en": ":x: The chars limit for the description is %s !"
		}
		s.GROUP_CREATED = {
			"fr": "Le groupe **%s** a été créé. %s",
			"en": "Group **%s** created. %s"
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
			"en": "**%s** %s %s\n"
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
		s.USER_JOIN_GROUP_TO_LEADER = {  # 1
			"fr": "%s a rejoint ton groupe **%s** ! %s",
			"en": "%s joined your group **%s**! %s"
		}
		s.GROUP_IS_FULL_TO_LEADER = {  # 2
			"fr": "Vous êtes maintenant au complet ! Tu peux maintenant confirmer le groupe pour notifier les autres membres.",
			"en": "Your group is now full! You can now confirm it to notify the other members."
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
		s.CONFIRM_GROUP = {  # 1
			"fr": "Tu as %s le groupe **%s**.",
			"en": "You have %s the group **%s**."
		}
		s.CONFIRM_GROUP_STATUS_UNLOCKED = {  # 2
			"fr": "ouvert",
			"en": "opened"
		}
		s.CONFIRM_GROUP_STATUS_CONFIRMED = {  # 2
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
		s.DELETE_GROUP_MODAL_TITLE = {
			"fr": "Supprimer %s ?",
			"en": "Delete %s ?"
		}

		s.NOT_IN_GROUP = {
			"fr": ":x: De quoi je me mèles ?",
			"en": ":x: You are not part of this group!"
		}
		s.GROUP_NOT_FOUND = {
			"fr": ":x: Aucun groupe trouvé !",
			"en": ":x: Group not found!"
		}

		s.GROUP_CHANNEL_CONFIGURED = {
			"fr": "%s est le nouveau channel de groupe.",
			"en": "%s is the new default group channel."
		}
		s.GROUP_CHANNEL_CONFIG_NOT_AUTHORIZED = {
			"fr": "Seulement un administrateur peut configurer le channel de groupe",
			"en": "Only an administrator can setup the group channel."
		}

		# Kick messages
		s.MEMBER_KICKED_CHANNEL = {
			"fr": "%s a bien été exclu du groupe **%s**",
			"en": "%s has been kicked from **%s**"
		}

		s.MEMBER_KICKED_PM = {
			"fr": "%s vous a exclu du groupe **%s**",
			"en": "%s kicked you from **%s**"
		}

		s.NOT_LEADER = {
			"fr": ":x: Nuh uh, tu n'es pas le leader",
			"en": ":x: Nuh uh, you ain't the leader"
		}

		s.CANT_KICK_LEADER = {
			"fr": ":x: N'abandonne pas ton équipe comme ça !",
			"en": ":x: Don't leave your group comrades !"
		}

		# Welcome message
		s.WELCOME_TITLE = {
			"en": "Hello There !"
		}
		s.WELCOME_DESCRIPTION = {
			"en": """
					This bot helps creating groups to work together !
					For a given project, it is possible to create a group with the /create command. This way, everyone will be able to join your group if they are interested.

					Here is a list of the commands available:
				""",
			"fr": """
					Ce bot vous aide à créer des groupes pour travailler ensemble !
					Pour un projet donné, il est possible de créer un groupe via la commande /create. Ainsi tout le monde pourra rejoindre votre groupe s'il est intéressé.

					Voici une liste des commandes disponibles:
				"""
		}
		s.WELCOME_CREATE_CMD = {
			"en": "Create a group for a given project.",
			"fr": "Créer un groupe pour un projet donné."
		}

		s.WELCOME_LIST_CMD = {
			"en": "Lists every group available. You can filter by user or project name.",
			"fr": "Donne une liste de chaque groupe disponible. Il est possible de filtrer les projets par utilisateur ou nom de projet."
		}

		s.WELCOME_STATUS_CMD = {
			"en": "Displays all the current groups you are in.",
			"fr": "Affiche tout les groupes dans lesquels vous êtes."
		}

		s.WELCOME_CONFIG_CMD = {
			"en": "Configure the group channel to use.",
			"fr": "Configure le channel à utiliser."
		}

		s.WELCOME_KICK_CMD = {
			"en": "Kicks someone from a group whose leader is you.",
			"fr": "Exclure quelqu'un d'un groupe dont vous êtes le chef."
		}

		# assign language to every dict attributes
		for attr_name in vars(s):
			attr_value = getattr(s, attr_name)
			if isinstance(attr_value, dict):
				setattr(s, attr_name, attr_value.get(
						lang, attr_value.get("en")))
