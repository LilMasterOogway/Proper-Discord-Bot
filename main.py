import discord, random
from discord.ext import commands

TOKEN = "MTA3OTg5NTA0NjIyMTk5NjE5Mg.GtlTeH.b1AVCkhtza51xU9GAeQ6R51SV54FTGlUgY5vyY"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.command(name = "roll")
async def roll(ctx, num):
  for i in range(int(num)):
    d = random.randint(1,6)
    await ctx.channel.send(f"Rolling a D6 : {d}")

@bot.command(name = "ask")
async def ask(ctx, *words):
  st= ""
  for word in words:
    st+= word
  if st.startswith("do") or st.startswith("Do") or st.startswith("Are") or st.startswith("are") or st.startswith("Am") or st.startswith("am") and st.endswith("?"):
    a = random.randint(1,2)
    if a == 1:
      s = "Yes"
    elif a == 2:
      s = "No"
    await ctx.channel.send(s)
  elif st.endswith("?"):
    b = random.randint(1,2)
    if b == 1:
      s = "I don't know"
    elif b == 2:
      s = "Maybe"
    await ctx.channel.send(s)
  else:
    await ctx.channel.send("That's not a question.")

#doesnt work below
@bot.command(name = "say")
async def say(ctx, *words):
  st= ""
  for word in words:
    st+= word
  if "something good about me" in st:
    s = "You are cool"
    await ctx.channel.send(s)
  elif "something bad about me" in st:
    s = "You are not cool"
    await ctx.channel.send(s)
  else:
    await ctx.channel.send("I don't understand.")







bot.run(TOKEN)