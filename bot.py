import os
import asyncio
from threading import Thread
from flask import Flask
import discord
from discord import app_commands

# 1. Configurar el mini servidor web para mantener vivo a Render
app = Flask('')


@app.route('/')
def home():
  return "¡ChapAI está en línea y funcionando perfectamente!"


def run_flask():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run_flask)
  t.start()


# 2. Configurar el bot de Discord con los Intents necesarios
intents = discord.Intents.default()
intents.message_content = (
    True  # Necesario si también quieres usar comandos de texto clásico
)


class ChapAIClient(discord.Client):

  def __init__(self):
    super().__init__(intents=intents)
    self.tree = app_commands.CommandTree(self)

  async def setup_hook(self):
    # Sincroniza los comandos de barra con Discord globalmente o en tus servidores
    await self.tree.sync()
    print("¡Comandos de barra sincronizados con éxito!")


bot = ChapAIClient()


# 3. Definir tu primer comando de barra: /hola
@bot.tree.command(
    name="hola",
    description="Saluda a ChapAI, tu asistente oficial en La Resistencia",
)
async def hola(interaction: discord.Response):  # o interaction: discord.Interaction
  pass


# Corrección limpia para la respuesta de interacción de barra:
@bot.tree.command(
    name="hola",
    description="Saluda a ChapAI, tu asistente oficial en La Resistencia",
)
async def hola_command(interaction: discord.Interaction):
  await interaction.response.send_message(
      "¡Hola! Soy **ChapAI**, tu asistente oficial en La Resistencia 🛡️⚔️."
  )


@bot.event
async def on_ready():
  print(f'¡Conectado como {bot.user} (ID: {bot.user.id})!')
  print('¡ChapAI está listo para la acción!')


# 4. Arrancar el servidor Flask y luego encender el bot de Discord
keep_alive()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
