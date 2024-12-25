from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    address: str

@dataclass(frozen=True)
class FrozenUser:
    name: str
    age: int
    address: str

@dataclass
class User2:
    name: str
    age: int
    address: str
    active: bool = False
