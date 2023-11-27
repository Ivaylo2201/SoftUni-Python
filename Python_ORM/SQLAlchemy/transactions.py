from main import Session, User

session = Session()

try:
    session.begin()
    # Actions
    session.query(User).delete()

    session.commit()
except Exception as e:
    session.rollback()
finally:
    session.close()
