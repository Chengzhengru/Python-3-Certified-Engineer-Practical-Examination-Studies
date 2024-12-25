class User:
    user_type = None  

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def increment_age(self):
        self.age += 1

    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]  
        else:
            return ""

class User2:
    user_type = None  

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"<User2 id:{id(self)} name:{self.name}>"

    def increment_age(self):
        self.age += 1

    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]  
        else:
            return ""
        
class User3:
    user_type = None  

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"<User3 id:{id(self)} name:{self.name}>"
    
    def __len__(self):
        return len(self.name)

    def increment_age(self):
        self.age += 1

    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]  
        else:
            return ""     

class User4:
    user_type = None  

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"<User4 id:{id(self)} name:{self.name}>"
    
    def __len__(self):
        return len(self.name)
    
    def __eq__(self, other):
        if isinstance(other, User4):
            return self.age == other.age
        return NotImplemented

    def increment_age(self):
        self.age += 1

    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]  
        else:
            return ""  

class User5:
    user_type = None  

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"<User5 id:{id(self)} name:{self.name}>"

    def increment_age(self):
        self.age += 1

    @property
    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]  
        else:
            return ""
