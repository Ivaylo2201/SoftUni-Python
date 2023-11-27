from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

DATABASE_URL = 'postgresql+psycopg2://postgres:5432@127.0.0.1/postgres'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

# CRUD

with Session() as session:
    session.add(
        User(username="username", password="password")
    )
    session.commit()

with Session() as session:
    users = session.query(User).all()  # = User.objects.all() -> List of Users
    print(users)
    for u in users:
        print(u.username, u.password)

with Session() as session:
    # filter_by = filter() from Django
    user = session.query(User).filter_by(username="username").order_by(User.id.desc())
    user.username = "new username"
    session.commit()

with Session() as session:
    # Gets the first user and deletes it
    user = session.query(User).first()
    session.delete(user)
    session.commit()

with Session() as session:
    session.add_all([
        User(username="user1", password="password1"),
        User(username="user2", password="password2"),
    ])
    session.commit()
