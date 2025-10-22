import re

SNAKE_RULE = re.compile(r"[a-z]+(_[a-z]+)*")
CAMEL_RULE = re.compile(r"[A-Z][a-zA-Z]*")

class CaseHelper:

    @staticmethod
    def is_snake(string):
        return bool(SNAKE_RULE.fullmatch(string))
    
    @staticmethod
    def is_upper_camel(string):
        return bool(CAMEL_RULE.fullmatch(string))
    
    @staticmethod
    def to_snake(string):
        res = re.sub(r"(?=[A-Z])", "_", string)
        return res.lower()
    
    @staticmethod
    def to_upper_camel(string):
        return "".join(word.capitalize() for word in string.split("_"))
    
print(CaseHelper.is_snake('beegeek')) 
print(CaseHelper.is_snake('bee_geek')) 
print(CaseHelper.is_snake('Beegeek')) 
print(CaseHelper.is_snake('BeeGeek')) 

print(CaseHelper.is_upper_camel('beegeek')) 
print(CaseHelper.is_upper_camel('bee_geek')) 
print(CaseHelper.is_upper_camel('Beegeek')) 
print(CaseHelper.is_upper_camel('BeeGeek')) 

print(CaseHelper.to_snake('Beegeek')) 
print(CaseHelper.to_snake('BeeGeek'))

print(CaseHelper.to_upper_camel('beegeek')) 
print(CaseHelper.to_upper_camel('bee_geek')) 