from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# URL del database (puoi usare SQLite o PostgreSQL)
DATABASE_URL = "sqlite:///./auth.db"
# DATABASE_URL = "postgresql://user:password@localhost/dbname"

# Creazione del motore di connessione al database
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Creazione della sessione del database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Funzione per ottenere una sessione del database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()