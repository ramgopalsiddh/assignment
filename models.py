from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Bank(Base):
    __tablename__ = 'banks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Branch(Base):
    __tablename__ = 'branches'
    id = Column(Integer, primary_key=True, index=True)
    ifsc = Column(String, index=True)
    branch = Column(String, index=True)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)
    bank_id = Column(Integer, ForeignKey('banks.id'))
    bank = relationship("Bank", back_populates="branches")

Bank.branches = relationship("Branch", order_by=Branch.id, back_populates="bank")
