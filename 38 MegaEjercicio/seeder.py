from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models import Answer, Question, Test

if __name__ == "__main__":
    engine = create_engine("sqlite:///C:\\Users\\frjoma\\python-learning\\curso-dimas\\38 MegaEjercicio\\testdb\\tests.db", echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    # 
    questions = [
        Question(
            question_text = "¿Cómo se define una lista?",
            answers = [
                Answer(
                    answer_text="lista = [1,2,3]",
                    is_correct=True
                ), 
                Answer(
                    answer_text="lista(1,2,3,)",
                    is_correct=False
                ), 
                Answer(
                    answer_text="iter(1,2,3,)",
                    is_correct=False
                ),
            ]            
        ),
        Question(
            question_text = "¿Qué excepcion lanza un Iterador?",
            answers = [
                Answer(
                    answer_text="Stopiteration",
                    is_correct=True
                ), 
                Answer(
                    answer_text="ZeroDivision",
                    is_correct=False
                ), 
                 Answer(
                    answer_text="SyntaxError",
                    is_correct=False
                ),
            ]            
        )   
    ]

    #Lo anterior es los mismo que hacer lo siguiente que pongo abajo.
 #   questions = []
 #   ans1 = Answer(answer_text="respuesta 1", is_correct=True)
 #   ans2 = Answer(answer_text="respuesta 2", is_correct=False)
 #   ans = [ans1, ans2]
 #   q1 = Question(question_text = "Que respuesta es la buena", answers=ans)
 #   questions.append(q1)

    test = Test(test_name = "Python", questions = questions)
    session.add(test)
    session.commit()