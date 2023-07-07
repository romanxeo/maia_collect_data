from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Float, ARRAY
from sqlalchemy.sql.functions import func

Base = declarative_base()


class CollectDataModel(Base):
    __tablename__ = 'collect_data'

    id = Column('id', Integer, primary_key=True, index=True)
    input = Column(ARRAY(Float), nullable=False)
    output = Column(ARRAY(Float), nullable=False)
    symbol = Column(String, nullable=True)
    price = Column(Float, default='', nullable=True)
    time = Column(DateTime(timezone=True), server_default=func.now())
    first_signal = Column(String, default='', nullable=True)
