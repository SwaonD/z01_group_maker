from discord import Interaction
from src.settings.variables import Variables as V

async def send_quick_response(ctx: Interaction, \
		msg: str, timeout: int = V.NOTIF_MSG_TIMEOUT):
	await ctx.response.send_message(msg,
			ephemeral=True, delete_after=timeout)
