# Case-Friflex-MAI-2024-team-Smeshariki
# Целевое решение:

Образ результата представляет собой видеоролик из фрагмента партии, содержащего не более 9 полуходов, сопровождаемый комментарием chatgpt (аудиодорожка + субтитры) в контекстах разных целевых аудиторий.

Пробная целевая аудитория - гонщики. На перспективу планируется подбор ~5-10 целевых аудиторий.

# Архитектура:

PGN файл дается на вход промту, промт прокидывается в чат ГТП через АПИ, на выходе сеть генерирует JSON файл, содержащий информацию о четырех ходах, предшествующих интересному полуходу в процессе игры, и самом интересном полуходе: время окончания полухода, значение полухода и общий комментарий (до 450 символов) к ходу игры, предшествующему полуходу, признанному сетью интересным. Комментарий стилизован для выделенной целевой аудитории.

Предобрабатывающий питон-модуль получает на вход таймкод начала игры, PGN-файл и JSON-файл, сгенерированный ГПТ. Во всем JSON-файле ts перерабатывается в фактические таймкоды исходного видеоролика. 

Переработанный JSON-файл передается на вход парсинг модулю. На выходе из модуля получаем словарь, содержащий все данные из  переработанного JSON’а (тайм-коды и комментарий к фрагменту партии). 

Словарь и видеозапись партии передаются на вход питон модулю, который по тайм-кодам производит извлечение фрагментов видеозаписи (каждый из тайм кодов минимум 3,5 секунды), содержащие перемещение фигуры по доске. 

Вспомогательный питон модуль генерирует аудио дорожку на основании текста комментария, содержащегося в переработанном JSON-файле и экспортирует ее в формате .wav. 

Все исходные части (JSON, аудиодорожка и видео фрагмент) соединяются в последнем модуле, где происходит формирование субтитров и наложение их на видеодорожку. Аудиодорожка накладыватеся на полученный видео фрагмен длиной не более 40 секунд.
![Диаграмма без названия2 drawio](https://github.com/MartinIJL7/Case-Friflex-MAI-2024-team-Smeshariki/assets/146389168/441e84f7-5f36-4e0d-b7e2-c4ee6a97bb55)

# Работа с проектом

Чтобы создать ответ от chatGPT с интересными ходами партии, нужно запустить файл request.py. Для этого в любой среде разработки нужно открыть и запустить файл request.py. Для вставки партии необходимо в промте для gpt (в переменной multiline_query) поменять текст партии в формате .pgn на новую (вручную).

