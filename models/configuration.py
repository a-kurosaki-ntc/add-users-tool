from sqlalchemy import Column
from sqlalchemy.dialects.mysql import NVARCHAR
from db.database import Base

class Configuration(Base):
    __tablename__ = 'configurations'

    key = Column(NVARCHAR(50), primary_key=True)
    value = Column(NVARCHAR(500), nullable=False)