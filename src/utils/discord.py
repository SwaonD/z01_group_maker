from discord import Interaction
from src.settings.variables import NOTIF_MSG_TIMEOUT

async def send_quick_response(ctx: Interaction, msg: str):
	await ctx.response.send_message(msg,
			ephemeral=True, delete_after=NOTIF_MSG_TIMEOUT)
