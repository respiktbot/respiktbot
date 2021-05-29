import discord
import requests
import os
client = discord.Client()
@client.event
async def on_ready():
    print("Listening for respects")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('+rep'):
        actual_message = message.content.replace("+rep","")
        a=0
        user = ""
        for i in actual_message:
               if(i=='<'):
                     a = 1
               if(a==1):
                     user = user+i
                     if(i=='>'):
                          break
        reciever = user.replace("<@","").replace(">","").strip()
        channel = client.get_channel(777225766668730419)
        giver = str(message.author.id).strip()
        try:
          trial_1 = int(giver)
          trial_2 = int(reciever)
          if(trial_1==trial_2):
                     int("Throw error")
          else:
              req = requests.post("https://respiktbot.000webhostapp.com/add.php",data={"reciever":reciever}).text.strip()
              if(req=='200'):
                 await message.add_reaction('\U0001F44D')
              else:
                 int("Throw Error")
        except:
           await message.add_reaction('\U0000274C')


    if message.content.startswith('+checkrep'):
        actual_message = message.content.replace("+checkrep","")
        a=0
        user = ""
        for i in actual_message:
               if(i=='<'):
                     a = 1
               if(a==1):
                     user = user+i
                     if(i=='>'):
                          break
        inquirer = user.replace("<@","").replace(">","").strip()
        channel = client.get_channel(777225766668730419)
        try:
           trial = int(inquirer)
           req = requests.post("https://respiktbot.000webhostapp.com/inquire.php",data={"inquirer":inquirer}).text.strip()
           if(req=='404'):
                await message.add_reaction("\U0000274C")
           else:
                q = "<@" +inquirer+"> has "
                await channel.send(str(q+req+"  Respikts"))
                await message.add_reaction('\U0001F44D')
        except:
           await message.add_reaction('\U0000274C')    
        
        
       

    if message.content=='+myrep':
        channel = client.get_channel(777225766668730419)
        inquirer = str(message.author.id).strip()
        try:
           trial = int(inquirer)
           req = requests.post("https://respiktbot.000webhostapp.com/inquire.php",data={"inquirer":inquirer}).text.strip()
           if(req=='404'):
                await message.add_reaction("\U0000274C")
           else:
                req = req + "   <@" +inquirer+">"
                await channel.send(str("Respikt Point : "+req))
                await message.add_reaction('\U0001F44D')
        except:
           await message.add_reaction('\U0000274C')


    if message.content=="+leaderboard":
        reciever = message.content.replace("+rep","").replace("<@","").replace(">","").strip()
        channel = client.get_channel(847814059062984749)
        giver = str(message.author.id).strip()
        try:
           trial = int(giver)
           trial = int(reciever)
           await message.add_reaction('\U0001F44D')
        except:
           await message.add_reaction('\U0000274C')

client.run("ODQ3ODA2ODkyMjgxNDMwMDk3.YLDbsg.cyA0_28Bx5KPmO81DdwRhIt8sbI")
