import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')     # A variável "client" está recebendo a instância do bot, que será
                                                # ativada quando for digitado um texto começando com "!"

@client.event                                   # @: chamada de funções de bibliotecas/frameworks
async def on_ready():                           # Quando o bot estiver pronto para receber comandos
    print("The bot is now ready for use!")
    print("-----------------------------")

@client.command()
async def hello(ctx):                           # Pegar inputs do discord
    await ctx.send("Hello, I am a bearDev bot")

client.run('')                                # Sempre ao final do código existe um comando para fazê-lo rodar
