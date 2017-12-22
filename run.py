


import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import os
import pickle                        #DON'T TOUCH ANY OF THESE IMPORTS UNLESS YOU KNOW WHAT YOU'RE DOING.
import random
import time
import logging

bot = commands.Bot(command_prefix='!')
client = discord.Client()




#Introduction text for shell opening (Dont need to tamper if you don't wan't too.)
@bot.event
async def on_ready():
    print ("Bot was developed by Rews all of his code was helped by and with Da532 and the forums of reddit and stack overflow")
    print ("ANGLED is running on: " + bot.user.name)
    print ("With the ID of: " + bot.user.id)
    print ("-----------------------------------------------------")
    else:
        print("Incorrect passsword, please retry entering by reloading the shell either through sourcecode.py or startbot.bat")


#Ping command


@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def ping(ctx):
    embed = discord.Embed(title="***Ping***", description=":ping_pong: **I ping you back**", color=0x0000ff)
    embed.set_footer(text="ANGLED™")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule1(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 1: ***", description="*1. No spam, this means sending the same or similar message for 5 times continuously or more.*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule2(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 2: ***", description="*2.  No NSFW what so ever*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule3(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 3: ***", description="*3. All memes and random stuff irrellivent to the text topic is to be posted in #shitpost*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule4(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 4: ***", description="*4. No using the music bot for audio files/music which contain minge/troll material or contents that go against the rules*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule5(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 5: ***", description="*5. No racism what so ever, action will be taken.*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule6(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 6: ***", description="*6. No edgy behaviour towards each other, wether it be arguments or not, it's still cringey*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule7(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 7: ***", description="*7. No advertising of any sort, you may if granted by me or staff*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule8(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 8: ***", description="*8. Speak the language in the designated channels for it.*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule9(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 9: ***", description="*9. Micspam is not tolerated and will instantly result in a 10 minute mute.*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def rule10(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 10: ***", description="*10. Don't use alt accounts to bypass previous bans given on this server*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
@commands.has_role("helping hand")
async def rule11(ctx):
    embed = discord.Embed(title="*** :information_source: Rule 11: ***", description="*11. Don't request ranks that require time.*", color=0x0000ff)
    embed.set_footer(text="Follow all of these at all times!")
    await bot.say(embed=embed)



@bot.event
async def on_user_join(user: discord.Member):
    serverchannel = user.server.default_channel
    msg = "**Welcome!** {0} **To** {1}".format(user.mention, user.server.name)
    await bot.send_message(serverchannel, msg)

#Info command

#Flip command:

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def profile(ctx, user: discord.Member):
    embed = discord.Embed(title="**{}'s info**".format(user.name), description="**Below is the following information I can find:**", color=0x0000ff)
    embed.add_field(name="** :information_source: Name**", value=user.name, inline=True)
    embed.add_field(name="** :information_source: ID**", value=user.id, inline=True)
    embed.add_field(name="** :information_source: Joined**", value=user.joined_at)
    embed.add_field(name="** :information_source: Status**", value=user.status, inline=True)
    embed.add_field(name="** :information_source: Highest role**", value=user.top_role)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await bot.say("** :information_source: I have successfully kicked**, {}. **We wont see that user any time soon!**".format(user.name))
    await bot.kick(user)

#Diceroll command

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def roll(ctx):
    r=random.randrange(1,6)
    embed = discord.Embed(title="*** :game_die: Roll***", description="*You* ***rolled*** *a* " + str(r) + "!", color=0x0000ff)
    embed.set_footer(text="ANGLED™")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def what(ctx):
    embed = discord.Embed(title=" :information_source: **Welcome to ANGLED!**", description="*You are probably wondering how exactly to get into the text and voice channels, and for that you need to type* ***!role member*** *to do so. However, you need to keep a promise, by using that command you are comitting to following all the rules mentioned to you in #welcome, can't wait to see you using our server!*", color=0x0000ff)
    embed.set_footer(text="ANGLED™")
    await bot.say(embed=embed)

roasts = ["%s**?, more like loser!**", "%s, **your hair reminds me of the sea... It makes me feel seasick!**", "%s, **your teeth remind me of the stars, they come out at night!**"]
@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def insult(ctx, *, user: discord.Member = None):
    if user is None:
        await bot.say(ctx.message.author.mention + ":** :no_entry_sign: Error: I can't insult no-one. **")
        return
    if user.id == "268506966521806856":
        await bot.say(ctx.message.author.mention + ":** :no_entry_sign: Error. **")
    if user.id == "245581170664800266":
        await bot.say(ctx.message.author.mention + ":** :no_entry_sign: Error. **")
    elif user.id == ctx.message.author:
        await bot.say(ctx.message.author.mention + ": :no_entry_sign: Error.")
    else:
        random.seed(time.time())
        choice1 = roasts[random.randrange(len(roasts))] % user.mention
        await bot.say(ctx.message.author.mention + ": " + choice1)


killResponses = ["**Looks like %s got nuked, oh deer!**", "**%s ass got kicked too hard**", "**Looks like %s got headshotted by a quickscope!**"]


@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def kill(ctx, *, user: discord.Member = None):
    if user is None:
        await bot.say(ctx.message.author.mention + ":** :information_source: I shall never kill no-one.:dagger: **")
        return
    if user.id == "268506966521806856":
        await bot.say(ctx.message.author.mention + ":** :information_source: I Shall NEVER destroy my mummy:dagger: **")
    if user.id == "245581170664800266":
        await bot.say(ctx.message.author.mention + ":** :information_source: I shall NEVER destory my so called daddy!:dagger: **")
    elif user.id == ctx.message.author:
        await bot.say(ctx.message.author.mention + ": Why shall I kill my master?")
    else:
        random.seed(time.time())
        choice = killResponses[random.randrange(len(killResponses))] % user.mention
        await bot.say(ctx.message.author.mention + ": " + choice)


async def background_loop():
    await bot.wait_until_ready()
    while not bot.is_closed:
        channel = bot.get_channel("374550245847072768")
        messages = ["*:information_source: Be sure to* ***follow*** *the rules at all times!*", "*:information_source: Need help?* ***inform*** *a member of staff by* ***dming*** *them!*", "*:information_source: Make song requests in the* ***#songrequests*** *channel!*"]
        await bot.send_message(channel, random.choice(messages))
        await asyncio.sleep(600)

client.loop.create_task(background_loop())


@bot.command(pass_context = True)
async def clear(ctx, number):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await bot.delete_message(x)
            counter += 1
            await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even






@bot.command(pass_context = True)
async def massclear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)


@bot.command(pass_context = True)
async def msay(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)




@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def spookme(ctx):
    embed = discord.Embed(title="***Be prepared!, I'm sorry but this is what you asked for!***", description="*https://cdn.discordapp.com/attachments/374550245847072768/374646842400702474/manspooksjakepaul.gif*", color=0x0000ff)
    embed.set_footer(text="ANGLED™")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def warn(ctx, user: discord.Member = None):
    if user is None:
        await bot.say(ctx.message.author.mention + ":** :no_entry_sign: Error: I can't warn no-one.**")
        return
    if user.id == "268506966521806856":
        await bot.say(ctx.message.author.mention + ":** :no_entry_sign: **")
    if user.id == "245581170664800266":
        await bot.say(ctx.message.author.mention + ":** :no_entry_sign: **")
    else:
        await bot.say(ctx.message.author.mention + "** :information_source: I have warned {}**".format(user.name))
        await bot.delete_message(ctx.message)



@bot.command()
@commands.cooldown(1, 30, commands.BucketType.user)
@commands.has_permissions(kick_members=True)
async def game(*, game: str):
    await bot.change_presence(game=discord.Game(name=game))
    await bot.say("Game **changed** to: " +game)

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def marry(ctx, user: discord.Member = None):
    if user is None:
        await bot.say(ctx.message.author.mention + ":** :no_entry_sign: Error: You can't marry no-one.**")
        return
    if user.id == "268506966521806856":
        await bot.say(ctx.message.author.mention + ":** :information_source: Im afraid you can't marry {}!**".format(user.name))
    if user.id == "245581170664800266":
        await bot.say(ctx.message.author.mention + ":** :information_source: No.**")
    else:
        await bot.say(ctx.message.author.mention + "** :information_source: You are now married with {}! **".format(user.name))


@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def invite(ctx):
    embed = discord.Embed(title=" :information_source: **Invite link to ANGLED**", description="*Link - https://discord.gg/TwStSZt*", color=0x0000ff)
    embed.set_footer(text="ANGLED™")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def divorce(ctx, user: discord.Member = None):
    if user is None:
        await bot.say(ctx.message.author.mention + ":** :no_entry_sign: Error: You can't divorce no-one.**")
        return
    if user.id == "268506966521806856":
        await bot.say(ctx.message.author.mention + ":** :information_source: Im afraid you can't marry {}!**".format(user.name))
    if user.id == "245581170664800266":
        await bot.say(ctx.message.author.mention + ":** :information_source: No.**")
    else:
        await bot.say(ctx.message.author.mention + "** :information_source: You are now divorced from {}! **".format(user.name))


@bot.event
async def on_message(message):
    if message.content.startswith("!pokemon"):
        await bot.send_message(message.channel, random.choice(["**You have caught a bulbasaur! https://www.pokemon.com/uk/pokedex/bulbasaur**", "**You have caught a charizard! https://www.pokemon.com/uk/pokedex/charizard**", "**You have caught a caterpie! https://www.pokemon.com/uk/pokedex/caterpie**", "**You have caught a butterfree! https://www.pokemon.com/uk/pokedex/butterfree**", "**You have caught a squirtle! https://www.pokemon.com/uk/pokedex/squirtle**", "**You have caught a venusaur! https://www.pokemon.com/uk/pokedex/venusaur**", "**You have caught a metapod! https://www.pokemon.com/uk/pokedex/metapod**", "**You have caught an ekans! https://www.pokemon.com/uk/pokedex/ekans**", "**You have caught a pidgeot! https://www.pokemon.com/uk/pokedex/pidgeot**", "**You have caught a rattata! https://www.pokemon.com/uk/pokedex/rattata**", "**You have caught a stunky! https://www.pokemon.com/uk/pokedex/stunky**", "**You have caught a regice! https://www.pokemon.com/uk/pokedex/regice**", "**You have caught an electabuzz! https://www.pokemon.com/uk/pokedex/electabuzz**", "**You have caught a lapras! https://www.pokemon.com/uk/pokedex/lapras**", "**You have caught a psyduck! https://www.pokemon.com/uk/pokedex/psyduck**", "**You have caught a golbat! https://www.pokemon.com/uk/pokedex/golbat**", "**You have caught a makuhita! https://www.pokemon.com/uk/pokedex/makuhita**", "**You have caught a zorua! https://www.pokemon.com/uk/pokedex/zorua**", "**You have caught a xatu! https://www.pokemon.com/uk/pokedex/xatu**", "**You have caught a mr-mime! https://www.pokemon.com/uk/pokedex/mr-mime**", "**You have caught a zoroark! https://www.pokemon.com/uk/pokedex/zoroark**"]))
    await bot.process_commands(message)
    if message.content.startswith("!flip"):
        await bot.send_message(message.channel, random.choice(["**The coin stands at :speaking_head:**!", "**The coin stands at Tails**"]))
    await bot.process_commands(message)
    if message.content.startswith("!cringeme"):
        await bot.send_message(message.channel, random.choice(["http://s3.thingpic.com/images/Xm/Y1QNT2oZpgENDCAcABCN9eFX.gif", "https://sd.keepcalm-o-matic.co.uk/i/whats-9-plus-10-21.png", "https://images4.sw-cdn.net/product/picture/710x528_7480816_1496035_1459325206.jpg", "http://i1.kym-cdn.com/photos/images/newsfeed/001/112/704/8a8.jpg", "http://i0.kym-cdn.com/photos/images/newsfeed/000/096/044/trollface.jpg?1296494117", "https://media.giphy.com/media/l4KhKUiUI0Hjw4OJi/giphy.gif", "https://media.giphy.com/media/c3tx8BpfFxJN6/source.gif", "http://s2.quickmeme.com/img/9a/9ad6fc939940196a04b357664d49ede04e124c73c02670e66c265c8c1080fece.jpg", "https://memegenerator.net/img/instances/500x/52103908/minecraft-memes-r-so-epik.jpg", "https://i.imgflip.com/1rs0h2.jpg", "http://aspirevapeco.com/wp-content/uploads/2016/08/13e4876ec5551cc2.jpg", "https://i.imgflip.com/wfc0i.jpg", "http://quotationsquotes.com/wp-content/uploads/2015/08/Top-40-Funniest-minions-memes-Funnies-memes.jpg", "https://slm-assets2.secondlife.com/assets/11522413/lightbox/what_are_you_doing_in_my_swamp_by_garretfox93-d8d20hn.jpg?1430365878"]))
    await bot.process_commands(message)
    if message.content.startswith("!slots"):
        await bot.send_message(message.channel, random.choice(["> :apple: :apple: :apple: | **Congratulations!** ", "> :banana: :apple: :apple: | **Congratulations!** ", "> :apple: :banana: :apple: ", "> :apple: :apple: :banana: | **Congratulations!** ", "> :banana: :apple: :banana: ", "> :banana: :banana: :apple: | **Congratulations!** ", "> :banana: :banana: :banana: | **Congratulations!**", "> :pear: :pear: :pear: | **Congratulations!**", "> :banana: :pear: :pear: | **Congratulations!**", "> :pear: :banana: :pear: ", "> :pear: :pear: :banana: | **Congratulations!**", "> :banana: :pear: :banana: ", "> :banana: :banana: :pear: | **Congratulations!**", "> :apple: :pear: :pear: | **Congratulations!**", "> :pear: :apple: :pear: ", "> :pear: :pear: :apple: | **Congratulations!**", "> :pear: :pear: :apple: | **Congratulations!**", "> :pear: :pear: :pear: | **Congratulations!**", "> :apple: :pear: :apple: ", "> :apple: :apple: :pear: | **Congratulations!**", "> :pear: :apple: :apple: | **Congratulations!**", "> :pear: :banana: :banana: | **Congratulations!**", "> :pear: :banana: :banana: | **Congratulations!**", "> :pear: :banana: :pear: ", "> :banana: :pear: :pear: | **Congratulations!**", "> :pear: :apple: :apple: | **Congratulations!**", "> :apple: :pear: :apple:", "> :apple: :apple: :pear: | **Congratulations!**", "> :pear: :pear: :apple: | **Congratulations!**", "> :apple: :pear: :pear: | **Congratulations!**", "> :apple: :pear: :banana:", "> :pear: :banana: :apple:", "> :banana: :pear: :apple:", "> :pear: :apple: :banana:", "> :apple: :pear: :banana:", "> :pear: :banana: :apple:", "> :banana: :pear: :apple:", "> :pear: :apple: :banana:", "> :apple: :pear: :banana:", "> :pear: :banana: :apple:", "> :banana: :pear: :apple:", "> :pear: :apple: :banana:"]))
    await bot.process_commands(message)
    if message.content.startswith("!role"):
        team_list = ["member", "vip"]
        entered_team = message.content[6:].lower()
        role = discord.utils.get(message.server.roles, name=entered_team)
        roles = [
            # IDs of the roles for the teams
            "392736497771610122",
        ]
        for r in message.author.roles:
            if r.id in roles:
                # If a role in the user's list of roles matches one of those we're checking
                await bot.send_message(message.channel, "** :no_entry_sign: Error: You already have a team role. If you want to switch, message a moderator.**")
                return
        if role is None or role.name not in team_list:
            # If the role wasn't found by discord.utils.get() or is a role that we don't want to add:
            await bot.send_message(message.channel, "** :no_entry_sign: Error:Team doesn't exist.**")
            return
        elif role in message.author.roles:
            # If they already have the role
            await bot.send_message(message.channel, "** :no_entry_sign: Error: You already have this role.**")
        else:
            try:
                await bot.add_roles(message.author, role)
                await bot.send_message(message.channel, "** :information_source: Successfully added role {0}**".format(role.name))
            except discord.Forbidden:
                await bot.send_message(message.channel, "** :no_entry_sign: Error: I don't have perms to add roles. **")
    if message.content.startswith("!poll"):
        await bot.add_reaction(message, "👍")
        await bot.add_reaction(message, "👎")



bot.run(env.process.BOT_TOKEN)

