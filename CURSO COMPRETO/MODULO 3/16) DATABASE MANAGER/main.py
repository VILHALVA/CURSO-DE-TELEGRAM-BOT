import json
import logging
import os

from decouple import config
from redis import Redis
from redis.exceptions import ConnectionError
from telethon import Button, TelegramClient, events

logging.basicConfig(level=logging.INFO)

senders_data = {}


class ENV:
    API_ID = config("API_ID", default=6, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e", cast=str)
    BOT_TOKEN = config("BOT_TOKEN", default="", cast=str)


try:
    client = TelegramClient(None, api_id=ENV.API_ID, api_hash=ENV.API_HASH).start(
        bot_token=ENV.BOT_TOKEN
    )
except Exception as ex:
    print(str(type(ex)) + ": " + str(ex))
    exit()


DEFAULT_HELP = (
    "Help menu for managing your **Redis Database**\n\n"
    + "`/help` - **Will open this menu**\n"
    + "`/set key value` - **Will SET with given key and value in the database**\n"
    + "`/get key` - **Will GET data of given key from the database**\n"
    + "`/delete key` - **Will DELETE value of give key from the database**\n"
    + "`/backup` - **Will take BACKUP of whole redis database**\n"
    + "`/restore` - **Will RESTORE database of replied json file in your database**\n"
    + "`/abort` - **Will remove your REDIS CREDENTIALS from memory**\n"
    + "`/allkeys` - **Will give list of all KEYS in your Database**\n"
    + "`/flushall` - **Will clear REDIS DATABASE**\n"
    + "`/login` - **Will be used to login to your REDIS database**"
)


def redis_connection(redis_uri, redis_port, redis_password):
    try:
        connection = Redis(
            host=redis_uri,
            port=redis_port,
            password=redis_password,
            decode_responses=True,
        )
        if connection.ping():
            return connection
        else:
            return None
    except ConnectionError:
        return False


def perform_redis_action(
    connection,
    method,
    key,
    value=None,
):
    if method not in ["get", "set", "delete"]:
        return False, "Wrong Method"
    if method == "set" and value is not None:
        message = connection.set(key, value)
        if message:
            return True, "Success"
    elif method == "get":
        message = connection.get(key)
        if message:
            return True, message
        else:
            return False, "No such key"
    elif method == "delete":
        delete_it = connection.delete(key)
        if delete_it == 1:
            return True, "Success"
        elif delete_it == 0:
            return False, "Key not found"
        else:
            return None, "Error :("
    else:
        pass  # todo


def redis_backup(connection, userid):
    filename = "redis-" + str(userid) + ".json"
    redis_data = {}
    for keys in connection.keys():
        redis_data.update({keys: connection.get(keys)})
    with open(filename, "w") as z:
        z.write(json.dumps(redis_data, indent=4))
    return filename


def redis_restore(connection, data):
    for keys in data.keys():
        connection.set(str(keys), str(data[keys]))


@client.on(
    events.NewMessage(
        pattern="^/start$",
        func=lambda event: not event.fwd_from and not event.via_bot_id,
    ),
)
async def start(event):
    await event.reply(
        "<b>Hello and welcome to <a href=https://redislabs.com>[Redis Database Manager]</a>!\n"
        + "Check out /help menu\n"
        + "and the below button👇.</b>",
        buttons=Button.url("Other Bots", "t.me/ultroidbots"),
        parse_mode="html",
    )


@client.on(
    events.NewMessage(
        pattern="^/flushall$",
        func=lambda event: not event.fwd_from and not event.via_bot_id,
    ),
)
async def flush(event):
    if event.sender_id not in senders_data.keys():
        return await event.reply("You have not sent me your Redis credentials")
    redis_data = senders_data[event.chat_id]
    connection = redis_connection(
        redis_data["redis_uri"], redis_data["redis_port"], redis_data["redis_password"]
    )
    if not connection:
        return await event.reply("Can't connect to redis database :(")
    await event.reply(
        "**⚠️ This will clear your whole Redis Database!\nDo you want to proceed?**",
        buttons=[Button.inline("Yes"), Button.inline("No")],
    )


@client.on(
    events.CallbackQuery(
        pattern="(.*)",
    ),
)
async def callback(event):
    if event.sender_id not in senders_data.keys():
        return await event.answer(
            "You have not sent me your Redis credentials", alert=True
        )
    redis_data = senders_data[event.chat_id]
    connection = redis_connection(
        redis_data["redis_uri"], redis_data["redis_port"], redis_data["redis_password"]
    )
    if not connection:
        return await event.reply("Can't connect to redis database :(", alert=True)
    match = (event.data_match.group(1)).decode("utf-8")
    if match == "Yes":
        if connection.flushall():
            await event.answer("Cleared Redis Database.", alert=True)
        else:
            await event.answer("Something went wrong!", alert=True)
    else:
        await event.delete()
        await event.answer("Aborted!", alert=True)


@client.on(
    events.NewMessage(
        pattern="^/help$",
        func=lambda event: not event.fwd_from and not event.via_bot_id,
    ),
)
async def help(event):
    await event.reply(DEFAULT_HELP)


@client.on(
    events.NewMessage(
        pattern="^/backup$",
        func=lambda event: not event.fwd_from and not event.via_bot_id,
    ),
)
async def backup(event):
    if event.sender_id not in senders_data.keys():
        return await event.reply("You have not sent me your Redis credentials")
    redis_data = senders_data[event.chat_id]
    connection = redis_connection(
        redis_data["redis_uri"], redis_data["redis_port"], redis_data["redis_password"]
    )
    if not connection:
        return await event.reply("Can't connect to redis database :(")
    msg = await event.reply("Creating backup!")
    file = redis_backup(connection, event.chat_id)
    await client.send_file(event.chat, file, caption="Your Redis Database backup")
    await msg.delete()
    os.remove(file)


@client.on(
    events.NewMessage(
        pattern="^/restore$",
        func=lambda event: not event.fwd_from and not event.via_bot_id,
    ),
)
async def restore(event):
    if event.sender_id not in senders_data.keys():
        return await event.reply("You have not sent me your Redis credentials")
    redis_data = senders_data[event.chat_id]
    connection = redis_connection(
        redis_data["redis_uri"], redis_data["redis_port"], redis_data["redis_password"]
    )
    if not connection:
        return await event.reply("Can't connect to redis database :(")
    reply = await event.get_reply_message()
    if not reply:
        return await event.reply("Reply to a json file")
    json_file = await reply.download_media()
    try:
        with open(json_file, "r") as file:
            data = json.loads(file.read())
    except Exception as ex:
        return await event.reply(str(ex))
    redis_restore(connection, data)
    await event.reply("Restored successfully!")


@client.on(
    events.NewMessage(
        func=lambda event: not event.fwd_from and not event.via_bot_id,
        pattern="^/login$",
    ),
)
async def redis_action(event):
    async with event.client.conversation(event.sender_id) as conv:
        await conv.send_message(
            "Send your REDIS_URI.\n\n`ex. redis.....redislabs.com:12345`"
        )
        redis_cred = await conv.get_response()
        if not redis_cred.message.startswith("redis"):
            await conv.send_message(
                "REDIS_URI should start with redis. Send /login again."
            )
            return await conv.cancel()
        await conv.send_message("Send your REDIS_PASSWORD.")
        redis_password = await conv.get_response()
        if redis_password.message.startswith("/"):
            await conv.send_message(
                "REDIS_PASSWORD shouldn't start with /. Send /login again."
            )
            return await conv.cancel()
    try:
        some = redis_cred.message.split(":")
        redis_uri = some[0]
        redis_port = some[1]
    except IndexError:
        return await event.reply("I can't find port number. Send /login again.")
    senders_data[event.sender_id] = {
        "redis_uri": redis_uri,
        "redis_port": int(redis_port),
        "redis_password": redis_password.message,
    }

    connection = redis_connection(redis_uri, int(redis_port), redis_password.message)
    if not connection:
        return await event.reply("Failed to connect to redis database :(")
    await event.reply("Connected to your redis database")


@client.on(
    events.NewMessage(
        func=lambda event: not event.fwd_from and not event.via_bot_id,
        pattern="^/(set|get|delete)",
    ),
)
async def some_actions(event):
    if event.sender_id not in senders_data.keys():
        return await event.reply("You have not sent me your Redis credentials")
    method = event.pattern_match.group(1)
    redis_data = senders_data[event.sender_id]
    try:
        something = event.text.split(" ", maxsplit=2)
        key = something[1]
    except IndexError:
        return await event.reply("Give atleast a key.")
    value = None
    if method == "set":
        try:
            value = something[2]
        except IndexError:
            return await event.reply("Give value for the key. You Dumbo :(")
    connection = redis_connection(
        redis_data["redis_uri"], redis_data["redis_port"], redis_data["redis_password"]
    )
    status, message = perform_redis_action(connection, method, key, value)
    await event.reply(f"**{status}**\n\n```{message}```")


@client.on(
    events.NewMessage(
        func=lambda event: not event.fwd_from and not event.via_bot_id,
        pattern="^/abort$",
    ),
)
async def _(event):
    if event.sender_id not in senders_data.keys():
        return await event.reply("You have not sent me your Redis credentials")
    del senders_data[event.sender_id]
    await event.reply("Redis credentials successfully removed from memory")


@client.on(
    events.NewMessage(
        func=lambda event: not event.fwd_from and not event.via_bot_id,
        pattern="^/allkeys$",
    ),
)
async def keys(event):
    if event.sender_id not in senders_data.keys():
        return await event.reply("You have not sent me your Redis credentials")
    redis_data = senders_data[event.sender_id]
    connection = redis_connection(
        redis_data["redis_uri"], redis_data["redis_port"], redis_data["redis_password"]
    )
    message = "**All Keys in your Redis Database**\n\n"
    for key in sorted(connection.keys()):
        message += f"• `{key}`\n"
    await event.reply(message)


client.run_until_disconnected()
