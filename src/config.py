# for tortoise-orm

TORTOISE = {
    "connections": {
        "default": "postgres://avnadmin:AVNS_HfeI9yXZnDEfiIGhce9@stxrz-scrimsbot.j.aivencloud.com:28636/defaultdb",  # Change to PostgreSQL/MySQL if needed
    },
    "apps": {
        "models": {
            "models": [
                "models.esports.scrims",
                "models.esports.tagcheck",  
                "models.esports.slotm",  
                "models.esports.reserve",
                "models.esports.ptable", 
                "models.esports.ssverify", 
                "models.esports.tourney", 
                "models.misc.User",  
                "models.misc.Votes",  
                "models.misc.Timer",
                "models.misc.alerts", 
                "models.misc.AutoPurge", 
                "models.misc.Autorole", 
                "models.misc.block", 
                "models.misc.Commands", 
                "models.misc.guild", 
                "models.misc.Lockdown", 
                "models.misc.premium", 
                "models.misc.Snipe", 
                "models.misc.Tag",
                "aerich.models", 
            ],
            "default_connection": "default",
        }
    }
}

POSTGRESQL = {
    "user": "avnadmin",
    "password": "AVNS_HfeI9yXZnDEfiIGhce9",
    "host": "stxrz-scrimsbot.j.aivencloud.com",
    "port": 28636,
    "database": "defaultdb",
    "url": "postgres://avnadmin:AVNS_HfeI9yXZnDEfiIGhce9@stxrz-scrimsbot.j.aivencloud.com:28636/defaultdb",
}

EXTENSIONS = [
    "cogs.events", 
    "cogs.esports", 
    "cogs.mod", 
    "cogs.utility",
    "cogs.quomisc",
    "cogs.reminder", 
    "cogs.premium", 
]

DISCORD_TOKEN = "MTM4MDA2NjMzOTM2ODA3OTM5MQ.Gb7g6N.kZWOWiBxRjEaYe22_mRcBB0s8TTtQxbA7QiT_0"

COLOR = 0x00FFB3

FOOTER = "HyperQ Development!"

PREFIX = "hq"

SERVER_LINK = "https://discord.gg/hjSV93j93j"

BOT_INVITE = "https://discord.com/oauth2/authorize?client_id=1380066339368079391&permissions=8&integration_type=0&scope=bot"

WEBSITE = "https://kranton-prime.vercel.app/"

REPOSITORY = "https://github.com/Sagexdd/quotient.git"

DEVS = ()

# LOGS
SHARD_LOG = ""
ERROR_LOG = ""
PUBLIC_LOG = ""
