from enum import Enum, auto

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Producer(Enum):
    USA = auto()
    EUROPE = auto()
    ASIA = auto()


class Season(Enum):
    WINTER = "WINTER"
    AUTUM = "AUTUM"
    SUMMER = "SUMMER"
    ALL_SEASON = "ALL_SEASON"


class Sex(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Size(Enum):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"
    XXXL = "XXXL"


class FishingSetType(Enum):
    FISHINGRODS = auto()
    FISHINGNET = auto()
    CLOTHING = auto()
    BAIT = auto()


class Clothing(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    price = db.Column(db.Integer, default=0)
    name = db.Column(db.String(100), default='name')
    material = db.Column(db.String(50), default='material')

    producer = db.Column(
        db.Enum(Producer), default=Producer.EUROPE
    )

    guarantee = db.Column(db.Integer, default=0)
    color = db.Column(db.String(20), default='color')
    season = db.Column(db.Enum(Season), default=Season.ALL_SEASON)
    fishing_set_type = db.Column(db.Enum(FishingSetType), default=FishingSetType.FISHINGNET)
    size = db.Column(db.Enum(Size), default=Size.XL)
    sex = db.Column(db.Enum(Sex), default=Sex.MALE)

    def __str__(self):
        return str(self.price) + " " + str(self.name) + " " + str(self.masa) + " " + str(self.material) + \
               " " + str(self.guarantee) + " " + str(self.color) + str(self.producer) + " " + str(self.season.value) \
               + " " + str(self.fishingSetType.value) + " " + str(self.size) + " " + str(self.sex)
