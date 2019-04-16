from .device import EnvironmentDeviceList
from .user import User
from .utils import wrapWith
from .pending_environment_share import EnvironmentPendingEnvironmentShareList
from .pending_owner_change import EnvironmentPendingOwnerChangeList
from aiodataloader import DataLoader


class EnvironmentLoader(DataLoader):
    def __init__(self, client, id):
        super().__init__()
        self.client = client
        self._id = id

    async def batch_load_fn(self, keys):
        fields = " ".join(set(keys))
        res = await self.client.query('{environment(id:"%s"){%s}}' % (self._id, fields), keys=["environment"])

        resolvedValues = [res[key.split("{")[0]] for key in keys]

        return resolvedValues


class Environment:
    def __init__(self, client, id):
        self.client = client
        self._id = id
        self.loader = EnvironmentLoader(client, id)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        if self.client.asyncio:
            return self.loader.load("name")
        else:
            return self.client.query('{environment(id:"%s"){name}}' % self._id, keys=[
                "environment", "name"])

    @name.setter
    def name(self, newName):
        self.client.mutation(
            'mutation{environment(id:"%s", name:"%s"){id}}' % (self._id, newName), asyncio=False)

    @property
    def owner(self):
        if self.client.asyncio:
            res = self.loader.load("owner{id}")
        else:
            res = self.client.query('{environment(id:"%s"){owner{id}}}' % self._id, keys=[
                "environment", "owner"])

        def wrapper(res):
            res = User(self.client, res["id"])

            return res

        return wrapWith(res, wrapper)

    @property
    def myRole(self):
        if self.client.asyncio:
            return self.loader.load("myRole")
        else:
            return self.client.query('{environment(id:"%s"){myRole}}' % self._id, keys=[
                "environment", "myRole"])

    @property
    def picture(self):
        if self.client.asyncio:
            return self.loader.load("picture")
        else:
            return self.client.query('{environment(id:"%s"){picture}}' % self._id, keys=[
                "environment", "picture"])

    @picture.setter
    def picture(self, newPicture):
        self.client.mutation(
            'mutation{environment(id:"%s", picture:"%s"){id}}' % (self._id, newPicture), asyncio=False)

    @property
    def uniqueFirmwares(self):
        if self.client.asyncio:
            return self.loader.load("uniqueFirmwares")
        else:
            return self.client.query('{environment(id:"%s"){uniqueFirmwares}}' % self._id, keys=[
                "environment", "uniqueFirmwares"])

    @property
    def index(self):
        if self.client.asyncio:
            return self.loader.load("index")
        else:
            return self.client.query('{environment(id:"%s"){index}}' % self._id, keys=[
                "environment", "index"])

    @index.setter
    def index(self, newIndex):
        self.client.mutation(
            'mutation{environment(id:"%s", index:%s){id}}' % (self._id, newIndex), asyncio=False)

    @property
    def muted(self):
        if self.client.asyncio:
            return self.loader.load("muted")
        else:
            return self.client.query('{environment(id:"%s"){muted}}' % self._id, keys=[
                "environment", "muted"])

    @muted.setter
    def muted(self, newMuted):
        self.client.mutation(
            'mutation{environment(id:"%s", muted:%s){id}}' % (self._id, "true" if newMuted else "false"), asyncio=False)

    @property
    def devices(self):
        return EnvironmentDeviceList(self.client, self._id)

    @property
    def pendingEnvironmentShares(self):
        return EnvironmentPendingEnvironmentShareList(self.client, self._id)

    @property
    def pendingOwnerChanges(self):
        return EnvironmentPendingOwnerChangeList(self.client, self._id)


class EnvironmentList:
    def __init__(self, client):
        self.client = client
        self.current = 0

    def __len__(self):
        res = self.client.query('{user{environmentCount}}', keys=[
                                "user", "environmentCount"])
        return res

    def __getitem__(self, i):
        if isinstance(i, int):
            res = self.client.query(
                '{user{environments(limit:1, offset:%d){id}}}' % i)
            if len(res["user"]["environments"]) != 1:
                raise IndexError()
            return Environment(self.client, res["user"]["environments"][0]["id"])
        elif isinstance(i, slice):
            start, end, _ = i.indices(len(self))
            res = self.client.query(
                '{user{environments(offset:%d, limit:%d){id}}}' % (start, end-start))
            return [Environment(self.client, environment["id"]) for environment in res["user"]["environments"]]
        else:
            print("i", type(i))
            raise TypeError("Unexpected type {} passed as index".format(i))

    def __iter__(self):
        return self

    def __next__(self):
        res = self.client.query(
            '{user{environments(limit:1, offset:%d){id}}}' % self.current)

        if len(res["user"]["environments"]) != 1:
            raise StopIteration

        self.current += 1
        return Environment(self.client, res["user"]["environments"][0]["id"])

    def next(self):
        return self.__next__()
