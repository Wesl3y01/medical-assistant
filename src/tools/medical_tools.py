from src.database import SessionLocal, MedicalRecords, User
from langchain.tools import tool

class MedicalTools:
    
    @tool("get_my_medical_history")
    def get_my_medical_history(patient_id: int):
        """
        Utile per recuperare la storia medica e le diagnosi del paziente corrente.
        L'input deve essere l'ID del paziente loggato.
        """
        session = SessionLocal()
        try:
            # LOGICA DI SICUREZZA: 
            # In un sistema reale, patient_id verrebbe dalla sessione sicura,
            # non dall'input dell'LLM. Qui simuliamo il controllo.
            
            results = session.query(MedicalRecords).filter(
                MedicalRecords.patient_id == patient_id
            ).all()
            
            if not results:
                return "Non sono stati trovati record medici per il tuo profilo."
            
            history = []
            for record in results:
                history.append(f"Data: {record.date_created}, Diagnosi: {record.diagnosis}, Trattamento: {record.treatment}")
            
            return "\n".join(history)
        
        except Exception as e:
            return f"Errore durante il recupero dei dati: {str(e)}"
        finally:
            session.close()

    @tool("book_appointment")
    def book_appointment(patient_id: int, date_str: str, reason: str):
        """
        Prenota un nuovo appuntamento. 
        date_str deve essere in formato 'YYYY-MM-DD HH:MM'.
        """
        # Qui aggiungeremo la logica per scrivere nel DB
        pass