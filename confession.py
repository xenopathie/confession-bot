import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio
from keep_alive import keep_alive

async def start_bot_and_flask():
    
    keep_alive()

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
CONFESSION_CHANNEL_ID = 1267532294910902303
LOG_CHANNEL_ID = 1281545719630794827

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

class ConfessionPanel(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Envoyer une confession", style=discord.ButtonStyle.primary)
    async def send_confession(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "📩 Envoie-moi ta confession en message privé.", ephemeral=True
        )
        await interaction.user.send("🌟 Merci de m'envoyer ta confession en MP.")
        def check(msg):
            return msg.author == interaction.user and isinstance(msg.channel, discord.DMChannel)
        try:
            msg = await bot.wait_for('message', check=check, timeout=300)
            confession = msg.content
            channel = bot.get_channel(CONFESSION_CHANNEL_ID)
            if channel:
                embed = discord.Embed(
                    title="**Confession Anonyme**",
                    description=f"**{confession}**",
                    color=discord.Color.blue()
                )
                embed.set_footer(text="⚠️ Les signalements abusifs entraîneront des sanctions.")
                
                sent_message = await channel.send(embed=embed)
                view = SignalerPanel(sent_message)
                await sent_message.edit(view=view)
                await interaction.user.send("✅ Ta confession a été envoyée anonymement !")
                
                view = ConfessionPanel()
                await interaction.channel.send("📢 **Envoyez une autre confession !**", view=view)
            else:
                await interaction.user.send("⚠️ Le salon de confessions est introuvable.")
        except asyncio.TimeoutError:
            await interaction.user.send("⏳ Désolé, tu as pris trop de temps pour envoyer ta confession.")

class SignalerPanel(discord.ui.View):
    def __init__(self, message):
        super().__init__(timeout=None)
        self.message = message

    @discord.ui.button(label="🚨 Signaler", style=discord.ButtonStyle.danger)
    async def signaler_confession(self, interaction: discord.Interaction, button: discord.ui.Button):
        log_channel = bot.get_channel(LOG_CHANNEL_ID)
        if log_channel:
            await log_channel.send(f"🚨 Signalement d'une confession :\n{self.message.content}\nSignalé par: {interaction.user}")
            await interaction.response.send_message("⚠️ Cette confession a été signalée.", ephemeral=True)
        else:
            await interaction.response.send_message("⚠️ Le salon de logs est introuvable.", ephemeral=True)

@bot.command()
async def setup_confession(ctx):
    """Commande pour afficher le panel de confession dans le salon actuel"""
    view = ConfessionPanel()
    await ctx.send("📢 **Envoyez une confession anonyme !**\nCliquez sur le bouton ci-dessous :", view=view)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")
    print(f"Commandes chargées: {list(bot.commands)}")
    await bot.tree.sync()

print("Token OK, lancement du bot...")
try:
    bot.run(token=token)
except Exception as e:
    print(f"❌ Une erreur est survenue au lancement du bot : {e}")

asyncio.run(start_bot_and_flask())
