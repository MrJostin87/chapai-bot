import os
import threading
import discord
from flask import Flask

# 1. Creamos un mini servidor web para que Render detecte actividad
app = Flask('')


@app.route('/')
def home():
  return '¡ChapAI está en línea y protegiendo La Resistencia 🛡️!'


def run_web():
  app.run(host='0.0.0.0', port=8080)


# 2. Configuramos tu bot de Discord normalmente
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'¡Conectado exitosamente como {client.user}!')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hola'):
    await message.channel.send(
        '¡Hola! Soy **ChapAI**, tu asistente oficial en La Resistencia 🛡️⚔️.'
    )


# 3. Ejecutamos ambos al mismo tiempo
if __name__ == '__main__':
  # Arranca el servidor web en segundo plano
  threading.Thread(target=run_web).start()
  # Arranca el bot de Discord usando tu variable segura de entorno
  token = os.getenv('DISCORD_TOKEN')
  client.run(token)
