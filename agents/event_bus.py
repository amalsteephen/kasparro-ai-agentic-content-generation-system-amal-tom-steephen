class EventBus:
    def __init__(self):
        self.events = {}

    def publish(self, key, value):
        self.events[key] = value

    def read(self, key):
        return self.events.get(key)

    def exists(self, key):
        return key in self.events

    def has(self, key):
        return key in self.events
