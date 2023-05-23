import discord
from discord.ext import commands
import openai
import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
openai.api_key = (config.key)

@bot.event
async def on_ready():
    print('Bot online')

@bot.command(name='r')
async def cont(ctx: commands.context, *, args):
    result = str(args)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=result,
        temperature=0.3,
        max_tokens=120,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    await ctx.send(embed=discord.Embed(title=f'{result}', description=response['choices'][0]['text']))

bot.run(config.token)
