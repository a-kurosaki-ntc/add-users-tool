from sqlalchemy import Column, DateTime, text
from sqlalchemy.dialects.mysql import NVARCHAR, BIGINT, BOOLEAN
from db.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    subject_id = Column(NVARCHAR(50), nullable=False)
    display_name = Column(NVARCHAR(50), nullable=False)
    email = Column(NVARCHAR(100), nullable=False, unique=True)
    is_admin = Column(BOOLEAN, nullable=False, server_default='false')
    created_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    updated_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'), nullable=False)

    def __init__(self, subject_id, display_name, email, is_admin=False):
        self.subject_id = subject_id
        self.display_name = display_name
        self.email = email
        self.is_admin = is_admin
        