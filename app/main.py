import json

import requests
from pydantic import BaseModel, Field
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import engine, get_db


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_questions(questions_num: int):
    url = "https://jservice.io/api/random?count={}".format(questions_num)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))


class Request(BaseModel):
    questions_num: int = Field(1, gt=0, description="Number of questions")


@app.post("/")
async def store_questions(request: Request, db: Session = Depends(get_db)):

    response = []
    questions_num = request.questions_num

    while questions_num > 0:
        questions = get_questions(1)

        if questions is None:
            continue

        question = questions[0]

        quiz = db.query(models.Quiz) \
            .filter(models.Quiz.id == question['id']) \
            .first()

        if quiz is None:
            quiz_model = models.Quiz()
            quiz_model.id = question['id'],
            quiz_model.question = question['question'],
            quiz_model.answer = question['answer'],
            quiz_model.created_at = question['created_at']
            db.add(quiz_model)
            db.commit()
            questions_num -= 1

            if questions_num == 1:
                response = {
                    'id': quiz_model.id,
                    'question': quiz_model.question,
                    'answer': quiz_model.answer,
                    'created_at': quiz_model.created_at
                }

    return response
