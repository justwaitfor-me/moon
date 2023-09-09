import json, discord, interactions
from discord.ext import commands
from discord.ui import InputText, Modal
import os

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client = discord.Bot()
#data = {}"guild" : None,"guild_id" : None,"icon" : None,"owner" : None,"setup": {"check" : False,"class" : "","school" : "","roles"  : [],"admin" : [],"duration" : ""}}

def get_json(guild):
    with open(f'json/{guild}.json', 'r') as file:
        data = json.load(file)
        return data
    
def get_form(data, ctx):
    x = data
    filename = f'json/{ctx}.json'
    with open(filename, 'r') as f:
        data = json.load(f)
        data['setup']['check'] = True # <--- add `id` value.

    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        

class MyModal(Modal):
    def __init__(self, ctx) -> None:
        data = get_json(ctx.guild)
        titel = data["guild"]
        super().__init__(title=str(titel)) #title of the modal up top
        self.add_item(InputText(label="Short Input", placeholder="Placeholder")) 
        self.add_item(
            InputText(
                label= "Long Input", 
                value= "Default", #sort of like a default
                style=discord.InputTextStyle.long, #long/short
            )
        )
        
            
    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Your Modal Results", color=discord.Color.blurple())
        embed.add_field(name="First Input", value=self.children[0].value, inline=False)
        embed.add_field(name="Second Input", value=self.children[1].value, inline=False)
        await interaction.response.send_message(embeds=[embed])
        print(interaction.guild.name)
        get_form(data = [self.children[0].value, self.children[1].value], ctx = interaction.guild.name)


@bot.event
async def on_ready():
    print("Log in...")
    await bot.change_presence(activity=discord.Game(name="/help | by JustWait"))
    try:
        synced = await bot.tree.sync()
        print(f"We have logged in as {bot.user}")
    except Exception as e:
        print(e)
        
@bot.event
async def on_guild_join(guild):
    data = {
        "guild" : str(guild),
        "guild_id" : str(guild.id),
        "icon" : str(guild.icon),
        "owner" : str(guild.owner),
        "setup": {
            "check" : False,
            "class" : "",
            "school" : "",
            "roles"  : [],
            "admin" : [],
            "duration" : ""
        }
    }
    with open(f"json/{guild.name}.json", "w") as file:
        json.dump(data, file)     
        
@bot.slash_command(name= "setup" , description="setup your Server")
async def test(ctx):
    modal = MyModal(ctx)
    #print(modal.data)
    await ctx.interaction.response.send_modal(modal)   


bot.run("MTE0OTQyNDk3Mzc3NDA2OTc5MQ.Gxj_LB.xyWhle075w2pLwpEAw2mr9c_KEwUGiyFrzoNDw")