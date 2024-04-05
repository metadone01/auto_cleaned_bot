from telethon.sync import TelegramClient, functions, types

api_id = ''
api_hash = ''
phone_number = '+'

with TelegramClient('tam_syam', api_id, api_hash) as client:
    # Unsubscribe from all channels
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        if isinstance(dialog.entity, types.Channel):
            client(functions.channels.LeaveChannelRequest(dialog.entity))

    # Block all bots
    bots = client.get_dialogs()
    for bot in bots:
        if isinstance(bot.entity, types.User) and bot.entity.bot:
            client(functions.contacts.BlockRequest(bot.entity.id))

    # Delete all bots
    bots = client.get_dialogs()
    for bot in bots:
        if isinstance(bot.entity, types.User) and bot.entity.bot:
            client(functions.contacts.DeleteContactsRequest([bot.entity.id]))

    # Delete all dialogs
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        client(functions.messages.DeleteHistoryRequest(peer=dialog.entity, max_id=0, just_clear=True))
