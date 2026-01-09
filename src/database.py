from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    role = Column(String(20), nullable=False)
    
class MedicalRecords(Base):
    __tablename__ = 'medical_records'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('users.id'))
    doctor_id = Column(Integer, ForeignKey('users.id'))
    diagnosis = Column(Text)
    treatment = Column(Text)
    date_created = Column(DateTime)    
    
class Appointments(Base):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('users.id'))
    doctor_id = Column(Integer, ForeignKey('users.id'))
    appointment_date = Column(DateTime)
    reason = Column(Text)
    
engine = create_engine('sqlite:///data/medical_practice.db')
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
    session = SessionLocal()
    if session.query(User).count() == 0:
        admin = User(name='Admin User', role='admin')
        doctor = User(name='Dr. Smith', role='doctor')
        patient = User(name='John Doe', role='patient')
        session.add_all([admin, doctor, patient])
        session.commit()
        record_john = MedicalRecords(patient_id=patient.id, doctor_id=doctor.id, diagnosis='Flu', treatment='Rest, hydration')
        session.add(record_john)
        appointment_john = Appointments(patient_id=patient.id, doctor_id=doctor.id, appointment_date=datetime.datetime.now(), reason='Routine check-up')
        session.add(appointment_john)
        session.commit()
    session.close()
    
if __name__ == "__main__":
    init_db()
    print("Database initialized with sample data.")
