from sqlalchemy import Column, Integer, String, DateTime, Text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SBOMEntry(Base):
    __tablename__ = "sbom_entries"

    id = Column(Integer, primary_key=True, index=True)
    component_name = Column(String(255), nullable=False)
    version = Column(String(100), nullable=False)
    license = Column(String(255))
    description = Column(Text)
    created_at = Column(DateTime, default=func.now())
