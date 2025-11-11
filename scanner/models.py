from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ScanResult(Base):
    __tablename__ = "scan_results"

    id = Column(Integer, primary_key=True, index=True)
    component_name = Column(String(255), nullable=False)
    vulnerability_id = Column(String(100), nullable=False)
    severity = Column(String(50))
    description = Column(Text)
    fixed_in_version = Column(String(100))
    resolved = Column(Boolean, default=False)
    detected_at = Column(DateTime, default=func.now())
