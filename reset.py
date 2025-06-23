from app.models import Subject
from app import db, create_app

app = create_app()
with app.app_context():
    try:
        Subject.query.update({Subject.rating: 1400.0})
        db.session.commit()
        print("✅ All subject ratings have been reset to 1400.")
    
    except Exception as e:
        db.session.rollback()
        print(f"❌ Error resetting ratings: {e}")