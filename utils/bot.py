import discord
import responses
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

async def send_message(message, user_message, is_private):
    try:
        if response == "unknown command, ignoring":
            pass
        else:
            response = responses.handle_responses(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as error:
        print(error)

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

def run_bot():
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is online and ready')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' in ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
    