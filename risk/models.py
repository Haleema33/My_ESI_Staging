from sqlalchemy import Column, Integer, String, Float, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RiskAssessment(Base):
    __tablename__ = "risk_assessments"

    id = Column(Integer, primary_key=True, index=True)
    component_name = Column(String(255), nullable=False)
    overall_score = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)
    recommendation = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())