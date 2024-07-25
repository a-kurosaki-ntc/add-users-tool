from sqlalchemy import Column, DateTime, text, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql import BIGINT
from db.database import Base

class UserUsecase(Base):
    __tablename__ = 'users_usecases'

    user_id = Column(BIGINT(unsigned=True), nullable=False)
    usecase_id = Column(BIGINT(unsigned=True), nullable=False)
    created_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    updated_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'usecase_id'),
    )