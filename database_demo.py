from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Базовый класс
Base = declarative_base()
#Модель
class Task(Base):
    __tablename__="tasks"
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, index = True)
    completed = Column(Boolean, default=False)

#Движок и сессия 
engine = create_engine("sqlite:///./tasks.db")
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#Добавление задачи
db=SessionLocal()
new_task = Task(title="Первая задача в базе",completed=False)
db.add(new_task)
db.commit()
db.refresh(new_task)
print(f"Создана задача: ID={new_task.id},Название='{new_task.title}'")

#Получение всех задач
tasks = db.query(Task).all()
print("\nВсе задачи:")
for task in tasks:
    print(f"-{task.id}:{task.title}(Выполнено:{task.completed})")
    
db.close()
