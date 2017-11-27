def ask_user():
    while True:
        user_say = input('Какой у Вас вопрос? \n')
        if user_say == "Пока!":
            break
        else:
            answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
            def  get_answer():
                question = user_say
                return answers[question].lower()  
            print(get_answer())
ask_user()

 