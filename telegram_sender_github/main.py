#____________________________________________________________________________________________________________________________________#
# --------------------------------------------<\>| Information list for script Telegram Sender |<\>----------------------------------#
#                                                 _____________________________________________                                      #
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#                        __________________________________________________________________________________________                  #
# ---------------------| This script for fast end mass mailing on groups/channels in Telegram from your account/s |------------------#
#                       __________________________________________________________________________________________                   #
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#                       ______________________________________________________________________________________________               #
# ---------------------| Coments on use whis script writed with code on this file(Main file), etc. read in "Readme.md" |-------------#
#                      ________________________________________________________________________________________________              # 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#           ___________________________________________________________________________________________________________________      #
#----------| <\> IMPORTANT INFO <\> YOU NEED READ "Readme.md" before use this script! THIS IS NECESSARY! <\> IMPORTANT INFO <\> |----#
#____________________________________________________________________________________________________________________________________#


# ------------------- Imports -------------------
import asyncio 
import random 
import logging 
import warnings 
from aiohttp_socks import ProxyConnector # For proxy info
import os
import socks # For proxy working
from datetime import datetime, timedelta, time
from telethon import TelegramClient, errors

# ------------------- Logging in -------------------
LOGFILE = "logs/run.log"
LOG_LEVEL = "INFO" # DEBUG - detailed log. | INFO - common log. | WARNING - only warnings. | ERROR - errors. | CRITICAL - critical errors. (recommended INFO)
os.makedirs("logs", exist_ok=True) 

logging.basicConfig(
    filename=LOGFILE,
    level=getattr(logging, LOG_LEVEL),
    format='[%(asctime)s] %(levelname)s: %(message)s'
)
console = logging.StreamHandler()
console.setLevel(getattr(logging, LOG_LEVEL))
warnings.filterwarnings("ignore", message="Using async sessions support is an experimental feature") # ignore the warning 
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)
logger = logging.getLogger("main")

# ------------------- Work schedule -------------------
WORK_START = time(12, 0) # Hour and min., of the start working script
WORK_END = time(8, 0) # And end working script
MAX_PER_HOUR = 80
MIN_DELAY = 9 # Min. del. between messages in seconds
MAX_DELAY = 19 # And max. del. 
SAVED_MODE = "last"  # 'last' | 'random' | 'tag' (your messages on Saved Messages telegram. Whear you need mailing on groups. last saved message, random or with tag)
SAVED_TAG = "#send" # if SAVED_MODE is 'tag', you need use this tag in your Saved Message if you want to send it
SAVED_RANDOM_LIMIT = 20

# ------------------- Account config -------------------
ACCOUNTS = [
    {
        "name": "account1",
        "api_id": 654321, # Replace with your actual API ID
        "api_hash": "123456abcdef", # Replace with your actual API hash
        "session": "accounts/account1.session",
        "texts_file": "texts/account1.txt",
        "groups": [
            # Use name, link or ID of the group/channel. Interval - time between messages to this group in seconds
            {"name": "Test Channel", "id": None, "interval": 120}, # You can use the channel name
            {"name": "https://t.me/testchannel", "id": None, "interval": 90}, # Or a link to the channel
            {"name": -1001234567890, "id": None, "interval": 60} # Or directly the channel ID
            # Add more groups as needed
            
            ],
        #Read "Readme.md", how to use a proxy(TorExpert) in your account (if you need). If you don't need a proxy, set "proxy": None
        "proxy": (socks.SOCKS5, "127.0.0.1", 9150) # or None
    },
    #{
    #    "name": "account2",
    #    "api_id": 654321,
    #    "api_hash": "123456abcdef",
    #    "session": "accounts/account2.session",
    #    "texts_file": "texts/account2.txt",
    #    "groups": [
    #       {"name": "Test Channel", "id": None, "interval": 5},

    #       ],
    #    "proxy": (socks.SOCKS5, "127.0.0.1", 9152) # None
    #},
    #{
    #    "name": "account3",
    #    "api_id": 654321,
    #    "api_hash": "123456abcdef",
    #    "session": "accounts/account3.session",
    #    "texts_file": "texts/account3.txt",
    #    "groups": [
    #        {"name": "Test Channel", "id": None, "interval": 5}
    #        
    #        ],
    #    "proxy": (socks.SOCKS5, "127.0.0.1", 9154) # None
    #}
]

# ------------------- Functions -------------------
def random_delay():
    return random.randint(MIN_DELAY, MAX_DELAY)

def can_send_now():
    t = datetime.now().time()
    if WORK_START < WORK_END:
        # Normal interval within one day
        return WORK_START <= t <= WORK_END
    else:
        # If the interval crosses the north
        return t >= WORK_START or t <= WORK_END

def read_texts(file_path):
    if not os.path.exists(file_path):
        logger.warning("Texts file not found: %s", file_path)
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # Divide into blocks by '---'
    blocks = [block.strip("\n") for block in content.split("---") if block.strip()]

    return blocks

# ------------------- Worker -------------------
class AccountWorker:
    def __init__(self, conf, use_saved=True, use_file=False):
        self.name = conf["name"]
        self.api_id = conf["api_id"]
        self.api_hash = conf["api_hash"]
        self.session = conf["session"]
        self.groups = conf["groups"]
        self.texts_file = conf.get("texts_file")
        self.texts = read_texts(self.texts_file) if self.texts_file else []
        self.hourly_sent = []
        self.use_saved = use_saved
        self.use_file = use_file
        self.proxy = conf.get("proxy", None)

    """your actual IP SOCKS"""
    async def get_me_ip(self):
        if not self.proxy:
            return None
        host, port = self.proxy[1], self.proxy[2]
        connector = ProxyConnector.from_url(f'socks5://{host}:{port}')
        try:
            import aiohttp
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get("http://api.ipify.org") as resp:
                    ip = await resp.text()
                    return ip
        except Exception as e:
            logger.warning("[%s] IP not received: %s", self.name, e)
            return None

    async def start(self):
        try:
            async with TelegramClient(self.session, self.api_id, self.api_hash, proxy=self.proxy) as client:
                logger.info("[%s] ✅ Connected to Telegram", self.name) # Successfully connected to Telegram
                
                current_ip = await self.get_me_ip()
                logger.info("[%s] Current IP via proxy: %s", self.name, current_ip)


                dialogs = await client.get_dialogs()
                for g in self.groups:
                        if g.get("entity") is None:
                            name = g["name"]
                            try:
                                if isinstance(name, str) and ("t.me" in name or name.startswith("http")):
                                    entity = await client.get_entity(name)
                                    g["entity"] = entity
                                    g["id"] = entity.id
                                    logger.info("[%s] Found group by link %s: %s", self.name, name, g["id"])

                                elif isinstance(name, int) or (isinstance(name, str) and name.lstrip("-").isdigit()):
                                    # If directly ID
                                    entity = await client.get_entity(int(name))
                                    g["entity"] = entity
                                    g["id"] = entity.id
                                    logger.info("[%s] Found group by ID %s", self.name, g["id"])

                                else:
                                    # If we search by name
                                    for d in dialogs:
                                        if d.name == name:
                                            g["entity"] = d.entity
                                            g["id"] = d.id
                                            logger.info("[%s] Found a group by name %s: %s", self.name, name, g["id"])
                                            break
                                    else:
                                        logger.warning("[%s] No group found %s", self.name, name)

                            except Exception as e:
                                logger.warning("[%s] Error getting group %s: %s", self.name, name, e)


                while True:
                    now = datetime.now()

                    new_ip = await self.get_me_ip() # Audit IP
                    if hasattr(self, 'last_ip'):
                        if new_ip != self.last_ip:
                            logger.info("[%s] Has changed IP: %s -> %s", self.name, self.last_ip, new_ip)
                    self.last_ip = new_ip

                    if not can_send_now():
                        await asyncio.sleep(110) # Sleep 110 seconds if not working time
                        continue

                    threshold = now - timedelta(hours=1)
                    self.hourly_sent = [t for t in self.hourly_sent if t > threshold]

                    for g in self.groups:
                        if len(self.hourly_sent) >= MAX_PER_HOUR:
                            logger.info("[%s] Hourly message limit reached", self.name)
                            break

                        group_id = g.get("id") 
                        if not group_id:
                            continue

                        msg_text = None
                        saved_msg = None

                        if self.use_saved:
                            try:
                                messages = await client.get_messages("me", limit=SAVED_RANDOM_LIMIT)
                                if messages:
                                    if SAVED_MODE == "last":
                                        saved_msg = messages[0]
                                    elif SAVED_MODE == "random":
                                        saved_msg = random.choice(messages)
                                    elif SAVED_MODE == "tag":
                                        tagged = [m for m in messages if m.text and SAVED_TAG in m.text]
                                        if tagged:
                                            saved_msg = random.choice(tagged)
                                if saved_msg:
                                    msg_text = saved_msg.text
                            except Exception as e:
                                logger.warning("[%s] Error retrieving Saved Messages: %s", self.name, e)

                        if self.use_file and not msg_text:
                            if self.texts:
                                msg_text = random.choice(self.texts)

                        if not msg_text:
                            logger.warning("[%s] No text to send", self.name)
                            continue

                        try:
                            short_text = (msg_text[:22] + "...") if len(msg_text) > 22 else msg_text # 22 characters at the beginning of the sent text
                            logger.info("[%s] We send to %s: %s", self.name, g["name"], short_text)
                            await client.send_message(g["entity"], msg_text)
                            self.hourly_sent.append(datetime.now())
                        except errors.FloodWaitError as e:
                            logger.warning("[%s] FloodWait %s seconds", self.name, e.seconds)
                            await asyncio.sleep(e.seconds + 1)
                        except Exception as e:
                            logger.exception("[%s] Error sending: %s", self.name, e)

                        # Basic sending interval
                        base_interval = g.get("interval", random_delay())

                        # Add +10% to the interval
                        base_interval = int(base_interval * 1.1)

                        # We make a small spread (+/- 15%)
                        delta = int(base_interval * 0.15)
                        sleep_time = base_interval + random.randint(-delta, delta)

                        if sleep_time < 1:
                            sleep_time = 1

                        await asyncio.sleep(sleep_time)

        except Exception as e:
            logger.exception("[%s] Unsuccessful connection attempt: %s", self.name, e)

# ------------------- Start all accounts -------------------
async def start_all(use_saved=True, use_file=False):
    tasks = []
    for acc in ACCOUNTS:
        worker = AccountWorker(acc, use_saved=use_saved, use_file=use_file)
        tasks.append(asyncio.create_task(worker.start()))
    await asyncio.gather(*tasks)

# ------------------- CLI -------------------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    # Command line arguments. Use "python main.py --saved" or "python main.py --file" on CLI to start this script
    parser.add_argument("--saved", action="store_true", help="Use Saved Messages from Telegram") # Use this flag to send texts from Sv. Msgs. Tg
    parser.add_argument("--file", action="store_true", help="Use texts from a file") # Or use this flag to send texts from a file on folder texts
    args = parser.parse_args()

    try:
        asyncio.run(start_all(use_saved=args.saved, use_file=args.file))
    except KeyboardInterrupt:
        logger.info("Stop by Ctrl+C") # Curefully stopped this script