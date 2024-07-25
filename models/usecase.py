from sqlalchemy import Column, DateTime, Text, text
from sqlalchemy.dialects.mysql import NVARCHAR, BIGINT, BOOLEAN
from db.database import Base

class Usecase(Base):
    __tablename__ = 'usecases'

    id = Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    title = Column(NVARCHAR(50), nullable=False)
    storage_name = Column(NVARCHAR(30), nullable=False)
    storage_container_name = Column(NVARCHAR(50), nullable=False)
    search_service_name = Column(NVARCHAR(60), nullable=False)
    search_service_index_name = Column(NVARCHAR(50), nullable=False)
    summary_prompt = Column(Text, nullable=False)
    status = Column(NVARCHAR(30), nullable=False)
    expiry_time = Column(DateTime)
    is_public = Column(BOOLEAN, nullable=False, server_default='true')
    created_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), nullable=False)
    updated_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'), nullable=False)