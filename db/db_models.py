from sqlalchemy import Column, Integer, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default='now()')


class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    class_id = Column(Integer, ForeignKey('char_classes.id'))
    name = Column(Text, nullable=False)
    level = Column(Integer, nullable=False)
    health = Column(Float, default=100)
    mana = Column(Float, default=100)
    phys_dmg = Column(Float, default=10)
    magic_dmg = Column(Float, default=10)
    phys_def = Column(Float, default=10)
    magic_def = Column(Float, default=10)
    gold = Column(Float)
    user = relationship('User')
# ADD BACKREF


class Char_Class(Base):
    __tablename__ = 'char_classes'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    health = Column(Float)
    mana = Column(Float)
    phys_dmg_mod = Column(Float)
    magic_dmg_mod = Column(Float)
    phys_def_mod = Column(Float)
    magic_def_mod = Column(Float)
    weapon_class = Column(Text, nullable=False)


class Armor(Base):
    __tablename__ = 'armors'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    phys_def_mod = Column(Float)
    magic_def_mod = Column(Float)
    defense = Column(Float)
    type = Column(Text, nullable=False)


class Weapon(Base):
    __tablename__ = 'weapons'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    phys_dmg_mod = Column(Float)
    magic_dmg_mod = Column(Float)
    damage = Column(Float)
    type = Column(Text, nullable=False)


class CharacterEquipment(Base):
    __tablename__ = 'character_equipment'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    helmet = Column(Integer, ForeignKey('armors.id'))
    boots = Column(Integer, ForeignKey('armors.id'))
    chest = Column(Integer, ForeignKey('armors.id'))
    gloves = Column(Integer, ForeignKey('armors.id'))
    leggings = Column(Integer, ForeignKey('armors.id'))
    main_hand = Column(Integer, ForeignKey('weapons.id'))
    off_hand = Column(Integer, ForeignKey('weapons.id'))
    character = relationship('Character')


class Achievement(Base):
    __tablename__ = 'achievements'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    buff_stat = Column(Text, nullable=False)
    buff_amount = Column(Integer, nullable=False)


class UserAchievement(Base):
    __tablename__ = 'user_achievements'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    achievement_id = Column(Integer, ForeignKey(
        'achievements.id'), primary_key=True)
    user = relationship('User')
    achievement = relationship('Achievement')
