print("© 2020 https://github.com/Stikyboi")
print("by Stikyboi")

import discord
import time
import random
import json
import asyncio
import os
from discord.ext import commands

# Variables

token ="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
bot = commands.Bot(command_prefix="/", description="by dev. Chef")

# Connexions

@bot.event
async def on_ready():
    print("bot lancé")

# Commandes

@bot.command()
async def test(ctx):
    print("Test bien prêt")
    await ctx.send("Test bien effectué")

@bot.command()
async def ServeurInfos(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"```Le serveur {serverName} contient {numberOfPerson} membres.\n La desrcription du serveur {serverDescription}. \n Ce serveur contient {numberOfTextChannels} salon(s) textuels,et {numberOfVoiceChannels} salon(s) vocaux.```"
    await ctx.send(message)

@bot.command()
async def dis(ctx, *texte):
    await ctx.send(" ".join(texte))

@bot.command()
async def disB(ctx, *text):
	chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
	chineseText = []
	for word in text:
		for char in word:
			if char.isalpha():
				index = ord(char) - ord("a")
				transformed = chineseChar[index]
				chineseText.append(transformed)
			else:
				chineseText.append(char)
		chineseText.append("  ")
	await ctx.send("".join(chineseText))

@bot.command()
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"```{user} à été ban pour la raison suivante : {reason}.```")

@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"```{user} à été unban.```")
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"```L'utilisateur {user} n'est pas dans la liste des bans```")

@bot.command()
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"```{user} à été kick.```")

@bot.command()
async def clear(ctx, nombre : int):
	messages = await ctx.channel.history(limit = nombre + 1).flatten()
	for message in messages:
		await message.delete()
bot.run(token)