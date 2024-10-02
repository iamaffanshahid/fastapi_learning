# # -*- coding: utf-8 -*-


# from module import helper as hl

# from module.helper import calculate_homework

# homework_assignment_grades = {

# "home_work_1" : 85,
# "home_work_2" : 100,
# "home_work_3" : 81

# }

# hl.calculate_homework(homework_assignment_grades)


import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)