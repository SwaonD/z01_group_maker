from discord import Interaction
from src.settings.variables import NOTIF_MSG_TIMEOUT

async def send_quick_response(ctx: Interaction, \
		msg: str, timeout: int = NOTIF_MSG_TIMEOUT):
	await ctx.response.send_message(msg,
			ephemeral=True, delete_after=timeout)
