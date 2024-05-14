# Case-Friflex-MAI-2024-team-Smeshariki
# Целевое решение:

Образ результата представляет собой видеоролик из фрагмента партии, содержащего не более 9 полуходов, сопровождаемый комментарием chatgpt (аудиодорожка + субтитры) в контекстах разных целевых аудиторий.

Пробная целевая аудитория - гонщики. На перспективу планируется подбор ~5-10 целевых аудиторий.

# Архитектура:

PGN файл дается на вход промту, промт прокидывается в чат ГТП через АПИ, на выходе сеть генерирует JSON файл, содержащий информацию о четырех ходах, предшествующих интересному полуходу в процессе игры, и самом интересном полуходе: время окончания полухода, значение полухода и общий комментарий (до 450 символов) к ходу игры, предшествующему полуходу, признанному сетью интересным. Комментарий стилизован для выделенной целевой аудитории.

Предобрабатывающий питон-модуль получает на вход таймкод начала игры, PGN-файл и JSON-файл, сгенерированный ГПТ. Во всем JSON-файле ts перерабатывается в фактические таймкоды исходного видеоролика. 

Переработанный JSON-файл передается на вход парсинг модулю. На выходе из модуля получаем словарь, содержащий данные из переработанного JSON’а (тайм-коды). 

Словарь и видеозапись партии передаются на вход питон модулю, который по тайм-кодам производит извлечение фрагментов видеозаписи (каждый из тайм кодов минимум 3,5 секунды), содержащие перемещение фигуры по доске. 

Вспомогательный питон модуль генерирует аудио дорожку на основании текста комментария, содержащегося в переработанном JSON-файле и экспортирует ее в формате .wav. 

Все исходные части (JSON, аудиодорожка и видео фрагмент) соединяются в последнем модуле, где происходит формирование субтитров и наложение их на видеодорожку. Аудиодорожка накладыватеся на полученный видео фрагмен длиной не более 40 секунд.

![Диаграмма без названия2 drawio](https://github.com/MartinIJL7/Case-Friflex-MAI-2024-team-Smeshariki/assets/146389168/441e84f7-5f36-4e0d-b7e2-c4ee6a97bb55)

# Работа с проектом

Чтобы создать ответ от chatGPT с интересными ходами партии, нужно запустить файл request.py, который находится в папке codes. Для этого в любой среде разработки нужно открыть и запустить файл request.py. Для вставки партии необходимо в промте для gpt (в переменной multiline_query) поменять текст партии в формате .pgn на новую (вручную). Для подключения chatGPT можно пополнить баланс на сайте proxyapi.ru и создать ключ.

![image](https://github.com/MartinIJL7/Case-Friflex-MAI-2024-team-Smeshariki/assets/146389168/0d2d7c5c-4730-40d2-9212-f12445b95f97)
![image](https://github.com/MartinIJL7/Case-Friflex-MAI-2024-team-Smeshariki/assets/146389168/2096be56-d415-4ff6-ac3b-caf20d97d63e)



ПРЕДОБРАБАТЫВАЮЩИЙ ПИТОН МОДУЛЬ.............


Парсинг модуль. Берем JSON-файл, полученный из предобрабатывающего питон-модуля. Заходим в файл Timestamps.py, который находится по адресу pythonproject/Timestamps/. В 14 строчке кода меняем аргумент функции parsing на название JSON-файла, полученного из предобрабатывающего питон-модуля.
![парсинг](https://github.com/MartinIJL7/Case-Friflex-MAI-2024-team-Smeshariki/assets/169812958/959b5b18-05e3-4844-b73f-3de736e8d68a)

Запускаем программу. Получает словарь с тайм-кодами, который выводится в терминал.
![image](https://github.com/MartinIJL7/Case-Friflex-MAI-2024-team-Smeshariki/assets/169812958/aa943c4c-3a3a-4dde-b092-da7f8546f155)


ЕЩЕ ПИТОН МОДУЛЬ..............

Вспомогательный питон модуль. Берем JSON-файл, полученный из предобрабатывающего питон-модуля. Заходим в файл text-to-speech.py, который находится по адресу pythonproject/Text-to-speech/. В 30 строчке кода меняем аргумент функции making_audio на название JSON-файла, полученного из предобрабатывающего питон-модуля.
![к моему модулю картинку](https://github.com/MartinIJL7/Case-Friflex-MAI-2024-team-Smeshariki/assets/169812958/81641cfc-0331-414d-9b32-89d069ea090d)
Запускаем программу. На выходе получаем комментарии к каждому интересному моменту.

![image](https://github.com/MartinIJL7/Case-Friflex-MAI-2024-team-Smeshariki/assets/169812958/b3a9c037-711c-4ecf-9904-9547512a9121)


ПОСЛЕДНИЙ МОДУЛЬ.................
