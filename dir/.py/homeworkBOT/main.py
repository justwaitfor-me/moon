import discord
from discord.ext import commands
from discord import app_commands
import interactions
from discord.ext.forms import Form

message = None

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Log in...")
    await bot.change_presence(activity=discord.Game(name="/help | by JustWait"))
    try:
        synced = await bot.tree.sync()
        print("Synced...")
    except Exception as e:
        print(e)
        
@bot.tree.command(name="setup", description="setup your Server.")
@app_commands.describe(user = 'select a user (@user)')
async def levent(interaction: discord.Interaction, user: str):
    ...

class MyView(discord.ui.View):
    @discord.ui.button(label='Click me!')
    async def on_button_click(self, button: discord.ui.Button, interaction: discord.Interaction):
        await message.edit(content='You clicked the button!', view=None)

@bot.command()
async def button(ctx):
    view = MyView()
    global message
    message = await ctx.send('This message has a button!', view=view)
    
@bot.command()
async def testform(ctx):
    form = Form(ctx,'Title')
    form.add_question('Question 1','first')
    form.add_question('Question 2','second')
    form.add_question('Question 3','third')
    result = await form.start()
    print(result)
    return result

bot.run("MTE0OTQyNDk3Mzc3NDA2OTc5MQ.Gxj_LB.xyWhle075w2pLwpEAw2mr9c_KEwUGiyFrzoNDw")