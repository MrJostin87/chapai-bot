import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"¡Conectado con éxito como {bot.user}!")

@bot.command()
async def hola(ctx):
    await ctx.send(f"¡Hola {ctx.author.mention}! Saludos desde el estudio. 🚀")

# Usamos una variable de entorno segura para el token
bot.run(os.getenv("DISCORD_TOKEN"))
