import discord
TOKEN = "MTE0OTQyNDk3Mzc3NDA2OTc5MQ.Gxj_LB.xyWhle075w2pLwpEAw2mr9c_KEwUGiyFrzoNDw"
bot = discord.Client(intents=discord.Intents.default()) # Create a bot object

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

@bot.slash_command() # Create a slash command
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button

bot.run(TOKEN) # Run the bot