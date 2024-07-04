from discord import Interaction, Member, errors
from src.settings.variables import NOTIF_MSG_TIMEOUT
from src.utils.log import LOGGER

async def send_quick_response(ctx: Interaction, \
		msg: str, timeout: int = NOTIF_MSG_TIMEOUT):
	await ctx.response.send_message(msg,
			ephemeral=True, delete_after=timeout)

async def send_private_message(member: Member, \
		msg: str, timeout: int = NOTIF_MSG_TIMEOUT):
	try:
		await member.send(msg, suppress_embeds=True)
	except errors.Forbidden:
		LOGGER.msg(f"Could not send message to {member.name}")
