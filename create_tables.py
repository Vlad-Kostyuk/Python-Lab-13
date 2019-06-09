from app.config import app
from app.models import db

print("Creating tables")
app.app_context().push()
db.create_all()
