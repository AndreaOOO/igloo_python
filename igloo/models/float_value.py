
from aiodataloader import DataLoader


class FloatValueLoader(DataLoader):
    def __init__(self, client, id):
        super().__init__()
        self.client = client
        self._id = id

    async def batch_load_fn(self, keys):
        fields = " ".join(set(keys))
        res = await self.client.query('{floatValue(id:"%s"){%s}}' % (self._id, fields), keys=["floatValue"])

        # if fetching object the key will be the first part of the field
        # e.g. when fetching device{id} the result is in the device key
        resolvedValues = [res[key.split("{")[0]] for key in keys]

        return resolvedValues


class FloatValue:
    def __init__(self, client, id):
        self.client = client
        self._id = id
        self.loader = FloatValueLoader(client, id)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        if self.client.asyncio:
            return self.loader.load("name")
        else:
            return self.client.query('{floatValue(id:"%s"){name}}' % self._id, keys=[
                "floatValue", "name"])

    @name.setter
    def name(self, newName):
        self.client.mutation(
            'mutation{floatValue(id:"%s", name:"%s"){id}}' % (self._id, newName), asyncio=False)

    @property
    def visibility(self):
        if self.client.asyncio:
            return self.loader.load("visibility")
        else:
            return self.client.query('{floatValue(id:"%s"){visibility}}' % self._id, keys=[
                "floatValue", "visibility"])

    @visibility.setter
    def visibility(self, newValue):
        self.client.mutation(
            'mutation{floatValue(id:"%s", visibility:%s){id}}' % (self._id, newValue), asyncio=False)

    @property
    def cardSize(self):
        if self.client.asyncio:
            return self.loader.load("cardSize")
        else:
            return self.client.query('{floatValue(id:"%s"){cardSize}}' % self._id, keys=[
                "floatValue", "cardSize"])

    @cardSize.setter
    def cardSize(self, newValue):
        self.client.mutation(
            'mutation{floatValue(id:"%s", cardSize:%s){id}}' % (self._id, newValue), asyncio=False)

    @property
    def index(self):
        if self.client.asyncio:
            return self.loader.load("index")
        else:
            return self.client.query('{floatValue(id:"%s"){index}}' % self._id, keys=[
                "floatValue", "index"])

    @index.setter
    def index(self, newValue):
        self.client.mutation(
            'mutation{floatValue(id:"%s", index:%s){id}}' % (self._id, newValue), asyncio=False)

    @property
    def myRole(self):
        if self.client.asyncio:
            return self.loader.load("myRole")
        else:
            return self.client.query('{floatValue(id:"%s"){myRole}}' % self._id, keys=[
                "floatValue", "myRole"])

    @property
    def createdAt(self):
        if self.client.asyncio:
            return self.loader.load("createdAt")
        else:
            return self.client.query('{floatValue(id:"%s"){createdAt}}' % self._id, keys=[
                "floatValue", "createdAt"])

    @property
    def updatedAt(self):
        if self.client.asyncio:
            return self.loader.load("updatedAt")
        else:
            return self.client.query('{floatValue(id:"%s"){updatedAt}}' % self._id, keys=[
                "floatValue", "updatedAt"])

    async def _async_load_device(self):
        id = await self.loader.load("device{id}")["id"]

        from .device import Device
        return Device(self.client, id)

    @property
    def device(self):
        if self.client.asyncio:
            return self._async_load_device()
        else:
            id = self.client.query('{floatValue(id:"%s"){device{id}}}' % self._id, keys=[
                "floatValue", "device", "id"])

            from .device import Device
            return Device(self.client, id)

    @property
    def permission(self):
        if self.client.asyncio:
            return self.loader.load("permission")
        else:
            return self.client.query('{floatValue(id:"%s"){permission}}' % self._id, keys=[
                "floatValue", "permission"])

    @permission.setter
    def permission(self, newValue):
        self.client.mutation(
            'mutation{floatValue(id:"%s", permission:%s){id}}' % (self._id, newValue), asyncio=False)

    @property
    def value(self):
        if self.client.asyncio:
            return self.loader.load("value")
        else:
            return self.client.query('{floatValue(id:"%s"){value}}' % self._id, keys=[
                "floatValue", "value"])

    @value.setter
    def value(self, newValue):
        self.client.mutation(
            'mutation{floatValue(id:"%s", value:%s){id}}' % (self._id, newValue), asyncio=False)

    @property
    def precision(self):
        if self.client.asyncio:
            return self.loader.load("precision")
        else:
            return self.client.query('{floatValue(id:"%s"){precision}}' % self._id, keys=[
                "floatValue", "precision"])

    @precision.setter
    def precision(self, newValue):
        self.client.mutation(
            'mutation{floatValue(id:"%s", precision:%s){id}}' % (self._id, newValue), asyncio=False)

    @property
    def min(self):
        if self.client.asyncio:
            return self.loader.load("min")
        else:
            return self.client.query('{floatValue(id:"%s"){min}}' % self._id, keys=[
                "floatValue", "min"])

    @min.setter
    def min(self, newValue):
        self.client.mutation(
            'mutation{floatValue(id:"%s", min:%s){id}}' % (self._id, newValue), asyncio=False)

    @property
    def max(self):
        if self.client.asyncio:
            return self.loader.load("max")
        else:
            return self.client.query('{floatValue(id:"%s"){max}}' % self._id, keys=[
                "floatValue", "max"])

    @max.setter
    def max(self, newValue):
        self.client.mutation(
            'mutation{floatValue(id:"%s", max:%s){id}}' % (self._id, newValue), asyncio=False)

    @property
    def unitOfMeasurement(self):
        if self.client.asyncio:
            return self.loader.load("unitOfMeasurement")
        else:
            return self.client.query('{floatValue(id:"%s"){unitOfMeasurement}}' % self._id, keys=[
                "floatValue", "unitOfMeasurement"])

    @unitOfMeasurement.setter
    def unitOfMeasurement(self, newValue):
        self.client.mutation(
            'mutation{floatValue(id:"%s", unitOfMeasurement:"%s"){id}}' % (self._id, newValue), asyncio=False)
