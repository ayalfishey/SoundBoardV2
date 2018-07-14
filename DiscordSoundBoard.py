from discord.ext.commands import Bot

BOT_PREFIX='!'

TOKEN = 'MjM4OTExMzkbsn436JVN'

## TODO: propogate SOUNDLIST from cloud service
SOUNDLIST= ['test1', 'test2']

client = Bot(command_prefix=BOT_PREFIX)

#Creates a unique command for each file based on name
for file in SOUNDLIST:
    @client.command(name=file)
    async def playsound():
            ## TODO: join channel
            #await play voice clip
            await client.say(msg)


@client.event
async def on_ready():
    print('Sound Board on')

client.run(TOKEN)
