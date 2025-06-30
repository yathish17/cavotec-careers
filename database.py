from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Build the DB connection string from individual env vars
db_connection_string = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl_ca": "ca.pem"
    })

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        rows = result.fetchall()
        return [dict(row._mapping) for row in rows]
