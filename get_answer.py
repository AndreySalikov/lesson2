answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
def  get_answer():
    question = input()
    return answers[question].lower()
print(get_answer())