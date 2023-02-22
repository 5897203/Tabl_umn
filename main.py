import random
import pyttsx3
import speech_recognition as sr

# Инициализация движка озвучивания
engine = pyttsx3.init()

# Инициализация объекта распознавания речи
recognizer = sr.Recognizer()

# Генерация 5 примеров
problems = [(i, j) for i in range(2, 10) for j in range(2, 10)]
random.shuffle(problems)
problems = problems[:5]

# Цикл, в котором будут задаваться примеры
while problems:
    # Выбор случайного примера из массива
    problem = random.choice(problems)
    num1, num2 = problem
    correct_answer = num1 * num2

    # Озвучивание и вывод примера на экран
    problem_text = f"{num1} умножить на {num2} равно: "
    print(problem_text)
    engine.say(problem_text)
    engine.runAndWait()

    # Получение ответа от пользователя с помощью распознавания голоса
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        user_answer = int(recognizer.recognize_google(audio, language="ru-RU"))
    except sr.UnknownValueError:
        print("Извините, не удалось распознать ваш ответ.")
        engine.say("Извините, не удалось распознать ваш ответ.")
        engine.runAndWait()
        continue
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания речи: {e}")
        engine.say("Извините, возникла ошибка при распознавании вашего ответа.")
        engine.runAndWait()
        continue

    # Проверка ответа
    if user_answer == correct_answer:
        print("Правильно!")
        engine.say("Правильно!")
        engine.runAndWait()

        # Удаление примера из массива
        problems.remove(problem)
    else:
        print("Неправильно.")
        engine.say(f"Неправильно. Правильный ответ: {correct_answer}")
        engine.runAndWait()

        # Добавление примера в массив еще раз
        problems.append(problem)

        # Озвучивание правильного ответа
#        correct_answer_text = f"Правильный ответ: {correct_answer}"
#        print(correct_answer_text)
#        engine.say(correct_answer_text)
#        engine.runAndWait()

print("Поздравляем, вы решили все примеры!")
engine.say("Поздравляем, вы решили все примеры!")
engine.runAndWait()

# Закрытие движка озвучивания
engine.stop()
engine.runAndWait()
