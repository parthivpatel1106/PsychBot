import discord
from discord.ext import commands
from PsychBotToken import token,channel_id
import os
import random
#client (our bot)
client = commands.Bot(command_prefix='!!')
@client.command(name='info')
async def bot_info(ctx):
    embed_info=discord.Embed(title="About PsychBot", description= "Hello my name is Psych. I am a bot who plays Stone, Paper, Scissor game with you. just type command '!!game' to play with me. Don't forget to use  '!!' before start command. you don't have to use '!!' during game. You can also use '!!stone', '!!paper', '!!scissor' or 'play' with '!!' to start game. '!!join' command is use to see if bot is online or not. You can also contribute to this bot. This bot is created by [Parthiv](https://github.com/parthivpatel1106).")
    await ctx.send(embed=embed_info)
@client.command(name='join')
async def bot_join(ctx):
    gen_channel= client.get_channel(channel_id) #your channel id
    await ctx.send("Let's Play Dude!")
@client.command('game', aliases=['play','stone','paper','scissor'])
async def mygame(ctx):
    #global times_used
    #gen_channel= client.get_channel(channel_id)
    que=str(""" ```css\n How many time you wanna play? \n you can stop your game by using "stop" command``` """)
    await ctx.send(que)
    def check(msg):
        return msg.author == ctx.author and msg.channel==ctx.channel
    
    response = await client.wait_for('message',check=check)
    if (response.content.isdigit()):
        await ctx.send("let's start")
    else:
        await ctx.send("""```css\n please choose digits for range!\n re-type the command for restart the game!```""")
    pscore=[]
    uscore=[]
    p=random.randrange(0,2)

    if(p==0):
        x='stone'
    elif(p==1):
        x='paper'
    else:
        x='scissor'

    num=response.content
    for i in range(int(num)):
        choose=str(""" ```css\n choose: stone, paper or scissor``` """)
        await ctx.send(choose)
        def chk(m):
            return m.author== ctx.author and m.channel==ctx.channel
        res= await client.wait_for('message',check=chk)
        if(res.content.lower()=='stone' or res.content.lower()=='paper' or res.content.lower()=='scissor'):
            await ctx.send(x)
            if(res.content.lower()==x.lower()):
                await ctx.send("""```css\n tie```""")
                pflag=0
                uflag=0
                pscore.append(pflag)
                uscore.append(uflag) 
            elif(res.content.lower()!=x.lower()):
                if(res.content.lower()=='stone' and x.lower()=='paper'):
                    await ctx.send("""```css\n Psych won```""")
                    pflag=1
                    uflag=0
                    pscore.append(pflag)
                    uscore.append(uflag) 
                elif(res.content.lower()=='stone' and x.lower()=='scissor'):
                    await ctx.send("""```css\n You won```""")
                    uflag=1
                    pflag=0
                elif(res.content.lower()=='paper' and x.lower()=='stone'):
                    await ctx.send("""```css\n You won```""")
                    uflag=1
                    pflag=0
                    pscore.append(pflag)
                    uscore.append(uflag) 
                elif(res.content.lower()=='paper' and x.lower()=='scissor'):
                    await ctx.send("""```css\n Psych won```""")
                    uflag=0
                    pflag=1
                    pscore.append(pflag)
                    uscore.append(uflag) 
                elif(res.content.lower()=='scissor' and x.lower()=='paper'):
                    await ctx.send("""```css\n You won```""")
                    uflag=1
                    pflag=0
                    pscore.append(pflag)
                    uscore.append(uflag) 
                elif(res.content.lower()=='scissor' and x.lower()=='stone'):
                    await ctx.send('Psych won')
                    pflag=1
                    uflag=0
                    pscore.append(pflag)
                    uscore.append(uflag) 
                    #psych+=1
                else:
                    await ctx.send("""```css\n Something wrong!```""")
        elif(res.content.lower()=='stop'):
            await ctx.send("""```css\n Stopping....```""")
            break
        elif(res.content.lower()!='stone' or res.content.lower()!='paper' or res.content.lower()!='scissor'):
            await ctx.send("""```css\n You are already looser! please check your input```""")
            await ctx.send("""```css\n Psych is winner!```""")
            pflag=1
            uflag=0
            pscore.append(pflag)
            uscore.append(uflag)
        else:
            await ctx.send("""```css\n Something wrong!```""")
            
        
            
    a=sum(pscore)
    b=sum(uscore)
    if(a>b):
        win="winner is Psych"
    elif(a==b):
        win="tie game"
    else:
        win="winner is You"
    embed_game=discord.Embed(title='Final scoreboard', description="""```css\n {}```""".format(win),color=0xee82ee)
    embed_game.add_field(name="Psych's result:", value=pscore, inline=False)
    embed_game.add_field(name="total",value=a)
    embed_game.add_field(name="Your result:",value=uscore,inline=False)
    embed_game.add_field(name="total",value=b)
    await ctx.send(embed=embed_game)


client.run(token) #your discord bot token