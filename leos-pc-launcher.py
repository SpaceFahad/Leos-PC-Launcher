import asyncio
import os
import discord
import yaml
from discord import app_commands
from discord.app_commands import Choice
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
LOGS_CHANNEL_ID = int(os.getenv("LOGS_CHANNEL_ID"))

# Embed config
embed = discord.Embed(color=0xA08007, title="Leo's PC Launcher")
embed.set_thumbnail(url="https://i.imgur.com/lK0PyZ0.png")
embed.set_footer(text="",icon_url="https://i.imgur.com/LUrtTgs.png")
embed.add_field(name="Github" ,value="[Leo's PC Launcher](https://github.com/SpaceFahad/Leos-PC-Launcher)", inline=False)

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


class CustomClient(discord.Client):
    tree: app_commands.CommandTree

    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        """Syncs the slash command."""

        await self.tree.sync()


client = CustomClient()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    channel = client.get_channel(LOGS_CHANNEL_ID)
    embed.description = "### Bot Status \n\n**Bot is Online**"
    await channel.send(embed=embed)


@client.tree.command()
@app_commands.describe(command="Select from the list above")
@app_commands.choices(
    command=[
        Choice(name="Training Server", value="subserver"),
        Choice(name="Main Server", value="mainserver"),
        Choice(name="Quit Arma 3 Instances", value="qa3"),
        Choice(name="Start TS3 Server", value="ts3"),
    ]
)
async def run(interaction: discord.Interaction, command: Choice[str]):
    """Launch a file/application on the host computer"""

    server_config = config["commands"][command.value]

    allowed_roles = server_config["allowed_roles"]
    file_path = server_config["file_path"]
    allowed_channels = server_config["allowed_channels"]

    if interaction.channel.id not in allowed_channels:
        embed.description = f"{interaction.user.mention} This command is not allowed in this channel!"
        return await interaction.response.send_message(embed=embed)

    if not any(role.id in allowed_roles for role in interaction.user.roles):
        embed.description = f"{interaction.user.mention} Permission Denied, this Command is not enabled for your role!"
        return await interaction.response.send_message(embed=embed)

    if not os.path.exists(file_path) or not (file_path.endswith(".bat") or file_path.endswith(".lnk")):
        embed.description = f"{interaction.user.mention} The specified file does not exist or has an invalid extension."
        return await interaction.response.send_message(embed=embed)

    try:
        process = await asyncio.create_subprocess_shell(
            file_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        for response in server_config["responses"]:

            embed.description = interaction.user.mention + ' ' + response["message"]
            if interaction.response.is_done():
                await interaction.followup.send(embed=embed)
            else:
                await interaction.response.send_message(embed=embed)

            delay = response.get("delay")
            if delay:
                await asyncio.sleep(delay)

        logs_channel = client.get_channel(LOGS_CHANNEL_ID)
        if logs_channel is not None:
            timestamp = discord.utils.format_dt(discord.utils.utcnow(), 'F')
            embed.description = f"### Leo's PC Launcher Logs \nUser: {interaction.user.mention}\n Executed: **[{command.name}]** \n Date/Time: {timestamp}"
            try:
                await logs_channel.send(embed=embed)
            except discord.HTTPException:
                print('Error: Can\'t send a message in the logs channel!')

        stdout, stderr = await process.communicate()

        if stdout:
            embed.description = stdout.decode("utf-8")
            await interaction.followup.send(embed=embed)
        if stderr:
            embed.description = stderr.decode("utf-8")
            await interaction.followup.send(embed=embed)
    except Exception as e:
        embed.description = f"{interaction.user.mention} An error occurred: {e}"
        if interaction.response.is_done():
            await interaction.followup.send(embed=embed)
        else:
            await interaction.response.send_message(embed=embed)


client.run(TOKEN)
