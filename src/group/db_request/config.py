from discord import TextChannel, Guild
from src.settings.tables import GROUPS_CONFIG

async def get_group_channel(guild: Guild) -> TextChannel | None:
	data = GROUPS_CONFIG.get_data(f"{GROUPS_CONFIG.guild_id} = {guild.id}", \
			GROUPS_CONFIG.group_channel_id)
	if len(data) == 0:
		return None
	group_channel_id = data[0][0]
	group_channel: TextChannel = guild.get_channel(group_channel_id)
	if group_channel is None:
		group_channel: TextChannel = \
				await guild.fetch_channel(group_channel_id)
	return group_channel
