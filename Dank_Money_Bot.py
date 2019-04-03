#INIT
import discord
import asyncio as asyncio
import time
import threading
client = discord.Client()


#ONREADY
@client.event
@asyncio.coroutine
def on_ready():
	print("Bot Online")
	print("Name: {}".format(client.user.name))
	print("ID: {}".format(client.user.id))
	print("\n \n")

	
async def beg_for_money():
	await client.wait_until_ready()
	while not client.is_closed:
		await client.send_message(discord.Object(id="562991872679608321"), "pls beg")
		await asyncio.sleep(65)
	

#t = threading.Timer(5, Kontroll_Check)
#t.start()
client.loop.create_task(beg_for_money())
client.run('discord@grumpf.at', 'DIS7!abc')
#Original NDEwMTE1MDUzNTg5ODg5MDI0.DalD8A.JW95HioOZBaChHrY3bq5Oqxa4Ms