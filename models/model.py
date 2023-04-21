from config import gino_db
from models.base import Base


class Users(Base):
    class UsersTable(gino_db.Model):
        __tablename__ = 'users'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        user_id = gino_db.Column(gino_db.BigInteger(), nullable=False)
        username = gino_db.Column(gino_db.String())
        group = gino_db.Column(gino_db.String(), gino_db.ForeignKey("groups.group_link"))

        def __str__(self) -> str:
            return f'<User {self.user_id}>'

        def __repr__(self) -> str:
            return f'<User {self.user_id}>'

    async def check_user(self, user_id: int, group_link: str) -> bool:
        return not await self.UsersTable.query.where(self.UsersTable.user_id == user_id and
                                                     self.UsersTable.group == group_link).gino.firsts() is None

    async def add_user(self,
                       user_id: int,
                       username: str,
                       group) -> bool:

        if self.check_user(user_id, group) or not Groups().check_in_db(group):
            return False

        user = self.UsersTable(
                               user_id=user_id,
                               username=username,
                               group=group
                              )
        await user.create()
        return True

    async def get_all_user(self, group_link: str) -> list:
        return await self.UsersTable.query.where(self.UsersTable.group == group_link).gino.all()

    async def delete_group(self, group_link: str) -> None:
        for user in await self.get_all_user(group_link):
            await user.delete()


class Groups(Base):
    class GroupsTable(gino_db.Model):
        __tablename__ = 'groups'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        group_link = gino_db.Column(gino_db.String(), unique=True, nullable=False)

        def __str__(self) -> str:
            return f'<Group {self.user_id}>'

        def __repr__(self) -> str:
            return f'<Group {self.user_id}>'

    async def check_in_db(self, group_link: str) -> bool:
        return not await self.GroupsTable.query.where(self.GroupsTable.group_link == group_link).gino.firts() is None

    async def add_group(self, group_link: str) -> bool:
        if await self.check_in_db(group_link):
            return False
        group = self.GroupsTable(group_link=group_link)

        await group.create()
        return True

    async def get_all_group(self) -> list:
        return await self.GroupsTable.query.gino.all()

    async def delete_group(self, group_link: str) -> bool:
        if not self.check_in_db(group_link):
            return False
        group = await self.GroupsTable.query.where(self.GroupsTable.group_link == group_link).gino.firts()
        await group.delete()
        return True


class Words(Base):
    class WordsTable(gino_db.Model):
        __tablename__ = 'words'

        id = gino_db.Column(gino_db.Integer(), primary_key=True)
        words = gino_db.Column(gino_db.String(), unique=True, nullable=False)

        def __str__(self) -> str:
            return f'<Group {self.user_id}>'

        def __repr__(self) -> str:
            return f'<Group {self.user_id}>'

    async def check_in_db(self, word: str) -> bool:
        return not await self.WordsTable.query.where(self.WordsTable.words == word).gino.firts() is None

    async def add_word(self, word: str) -> bool:
        if await self.check_in_db(word):
            return False
        word = self.WordsTable(words=word)

        await word.create()
        return True

    async def get_all_words(self) -> list:
        return await self.WordsTable.query.gino.all()

    async def delete_word(self, word: str) -> bool:
        if not self.check_in_db(word):
            return False
        word = await self.WordsTable.query.where(self.WordsTable.words == word).gino.firts()
        await word.delete()
        return True

