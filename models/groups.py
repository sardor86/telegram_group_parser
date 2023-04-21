from config import gino_db
from .base import Base


class Groups(Base):
    class GroupsTable(gino_db.Model):
        __tablename__ = 'users'

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

    async def get_all_group(self) -> list:
        return await self.GroupsTable.query.gino.all()

    async def delete_group(self, group_link: str) -> bool:
        if not self.check_in_db(group_link):
            return False
        group = await self.GroupsTable.query.where(self.GroupsTable.group_link == group_link).gino.firts()
        await group.delete()
