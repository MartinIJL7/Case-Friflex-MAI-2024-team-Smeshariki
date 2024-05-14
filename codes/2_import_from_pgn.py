import re
import json

def read_pgn_from_file(file_path):
    """
    Читает содержимое PGN файла.

    Args:
        file_path (str): Путь к файлу PGN.

    Returns:
        str: Содержимое файла в виде строки.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_timestamps_from_pgn(pgn_content):
    """
    Извлекает таймкоды из содержимого PGN.

    Args:
        pgn_content (str): Строка с содержимым файла PGN.

    Returns:
        list: Список меток времени в миллисекундах.
    """
    pattern = r"\[%ts (\d+)\]"  # Регулярное выражение для поиска таймкодов
    timestamps = re.findall(pattern, pgn_content)
    return [int(ts) for ts in timestamps]

def convert_timestamps_to_video_seconds(timestamps, video_start_time):
    """
    Преобразует список UNIX-меток времени в секунды относительно первого таймкода и добавляет время начала видео.

    Args:
        timestamps (list): Список меток времени в миллисекундах.
        video_start_time (float): Время начала видео в секундах.

    Returns:
        list: Список секунд относительно первого таймкода с добавленным временем начала видео.
    """
    base_time = timestamps[0]  # Устанавливаем первый таймкод как начальное время
    seconds_from_base = [(ts - base_time) / 1000 + video_start_time for ts in timestamps]
    return seconds_from_base

def save_to_json(filename, data):
    """
    Сохраняет данные в файл JSON.

    Args:
        filename (str): Имя файла для сохранения.8
        data (dict): Данные для сохранения.
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

# Путь к файлу PGN, который необходимо считать
file_path = 'test.pgn'

# Ввод времени начала видео пользователем
video_start_time = float(input("Введите время начала видео в секундах: "))

# Чтение PGN контента из файла
pgn_content = read_pgn_from_file(file_path)

# Извлечение таймкодов из PGN
timestamps = extract_timestamps_from_pgn(pgn_content)

# Конвертация таймкодов в секунды видео с учётом времени начала видео
video_seconds = convert_timestamps_to_video_seconds(timestamps, video_start_time)

# Формирование данных для сохранения
output_data = {
    'ts': timestamps,
    'timeline': video_seconds
}

# Сохранение данных в файл JSON
json_filename = 'output.json'
save_to_json(json_filename, output_data)

print(f"Data has been saved to {json_filename}.")