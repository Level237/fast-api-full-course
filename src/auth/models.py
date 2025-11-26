from sqlmodel import SQLModel,Field,Column
from sqlalchemy.dialects.postgresql import UUID as pgUUID
import uuid
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
  
class User(SQLModel,table=True):
    
    __tablename__ = "users"

    uid:uuid.UUID = Field(
        sa_column=Column(
            pgUUID(as_uuid=True),
            nullable=False,
            primary_key=True,
            default=uuid.uuid4,
        )
    )
    username:str
    email : str
    first_name : str
    last_name : str
    is_verified : bool = Field(default=False)
    created_at: datetime=Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now()))
    updated_at: datetime=Field(sa_column=Column(pg.TIMESTAMP,default=datetime.now()))
    
    def __repr__(self):
        return f"<User {self.username}>"