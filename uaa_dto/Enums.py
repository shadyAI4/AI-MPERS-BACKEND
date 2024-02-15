import enum

import graphene


class UserTypeInum(enum.Enum):
    GAME_MANAGER = 'GAME_MANAGER'
    ACCOUNTANT= 'ACCOUNTANT'
    CUSTOMER_CARE = 'CUSTOMER_CARE'
    PLAYER= 'PLAYER'
    ADMIN = 'ADMIN'
    
class GenderTypenum(enum.Enum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

UserEnum = graphene.Enum.from_enum(UserTypeInum)
GenderEnum = graphene.Enum.from_enum(GenderTypenum)
