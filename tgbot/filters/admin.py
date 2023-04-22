from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, obj):
        if self.is_admin:
            return obj.from_user.id == int(obj.bot.get('config').tgbot.admin)
        return False
