from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ساخت Engine و اتصال به دیتابیس SQLite
engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# تعریف مدل جدول
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# ساخت جدول در دیتابیس
Base.metadata.create_all(engine)

# اضافه کردن رکورد جدید
new_user = User(name="Ali", age=22)
session.add(new_user)
session.commit()

# خواندن داده‌ها
for user in session.query(User).all():
    print(user.name, user.age)
