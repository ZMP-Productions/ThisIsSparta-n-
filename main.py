import discord
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
i=discord.Intents.all()
client=commands.Bot(intents=i)
def secret(secret: str):  return os.environ.get(secret)
@client.event
async def on_message(ctx):
  content = ctx.content
  if "```" in content: content.replace("```", "")
  alertChannel=client.get_guild(secret("alertChannel"))
  if ctx.channel.id == secret("consoleChannel"):
    lines = []
    lines.append(content.split("\n"))
    for line in lines:
      if "[Spartan]" in line:
        try:
          when, sep, after = line.partition("]")
          before, sep, when = when.partition(" ")
          when, sep, after = when.partition(" ")
          before, sep, user = line.partition("n] ")
          user, sep, after = user.partition(" is ")
          likelihood, sep, after = after.partition(" ")
          before, sep, hack = after.partition("using ")
          hack, sep, after = hack.partition(" ")
          before, sep, count = after.partition(" x")
          count, sep, after = count.partition("")
          before, sep, length = line.partition(" | ")
          length, sep, after = length.partition(" | ")
          tps, sep, after = after.partition(" TPS | ")
          await alertChannel.send(f"User: {user}\nTime: {when}\nLikelihood: {likelihood}\nTimeframe: {length}\nTimes used within timeframe: {cont}\nTPS: {tps}\nMore info:\n{after}")
         except Exception as e: await alertChannel.send(f"Could not parse data: {e}\nSending raw:\n\n```{line}```")
@client.event
async def on_message_edit(ctx, before, after):
  content = ctx.content
  alertChannel=client.get_guild(secret("alertChannel"))
  if ctx.channel.id == secret("consoleChannel"):
    before, sep, difference = after.partition(after)
    lines = []
    lines.append(difference.split("\n"))
    for line in lines:
      if "[Spartan]" in line:
        try:
          when, sep, after = line.partition("]")
          before, sep, when = when.partition(" ")
          when, sep, after = when.partition(" ")
          before, sep, user = line.partition("n] ")
          user, sep, after = user.partition(" is ")
          likelihood, sep, after = after.partition(" ")
          before, sep, hack = after.partition("using ")
          hack, sep, after = hack.partition(" ")
          before, sep, count = after.partition(" x")
          count, sep, after = count.partition("")
          before, sep, length = line.partition(" | ")
          length, sep, after = length.partition(" | ")
          tps, sep, after = after.partition(" TPS | ")
          await alertChannel.send(f"User: {user}\nTime: {when}\nLikelihood: {likelihood}\nTimeframe: {length}\nTimes used within timeframe: {cont}\nTPS: {tps}\nMore info:\n{after}")
         except Exception as e: await alertChannel.send(f"Could not parse data: {e}\nSending raw:\n\n```{line}```")
await client.run(secret("token"))
