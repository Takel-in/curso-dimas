from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models import Answer, Question, Test
from sqlite3 import ProgrammingError


class Controller:
    def __init__(self) -> None:
        engine = create_engine("sqlite:///C:\\Users\\frjoma\\python-learning\\curso-dimas\\38 MegaEjercicio\\testdb\\tests.db", echo=True)
        session = sessionmaker(bind=engine)
        self.session = session()

    def create_empty_test(self, _test_name):
        test = self.session.query(Test).filter(Test.test_name == _test_name).first()
        if test == None:
            new_test = Test(test_name = _test_name)
            self.session.add(new_test)       
            self.session.commit()
        else:
            raise ProgrammingError("Test ya existe")
        
         


