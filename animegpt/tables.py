from dataclasses import dataclass, fields

class table():
    @property
    def dict(self):
        attr = {
            field.name: getattr(self, field.name)
            for field in fields(self)
            if getattr(self, field.name) is not None
        }
        return attr
    
    def keys(self):
        return [key for key, value in self.dict.items() if value is not None]
    
    def values(self):
        pass