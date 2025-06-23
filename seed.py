
from app import create_app, db
from app.models import Subject

app = create_app()
app.app_context().push()

db.create_all()

initial_subjects = [
    "Mathematics I",
    "Physics",
    "Chemistry",
    "Mathematics II",
    "PPS",
    "FPL",
    "Engg. Graphics",
    "Mechanics",
    "BXE",
    "BEE"
]

for name in initial_subjects:
    sub = Subject(name=name)
    db.session.add(sub)


db.session.commit()

