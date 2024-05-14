import json
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import concatenate_videoclips, VideoFileClip

# Путь к JSON-файлу и видеофайлу
json_file_path = 'combined_output.json'
video_file_path = 'test1.mp4'

# Загрузка данных из JSON-файла
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Извлечение таймлайна ходов
timelines = data['timeline']

# Функция для объединения близких таймингов
def merge_close_timings(timelines, threshold=4):
    merged_timelines = []
    for timeline in timelines:
        merged_timeline = []
        current_start = timeline[0] - 4  # Начало первого хода с вычетом 4 секунд
        current_end = timeline[0]
        
        for timestamp in timeline[1:]:
            if timestamp - current_end <= threshold:
                current_end = timestamp
            else:
                merged_timeline.append((current_start, current_end + 0.5))
                current_start = timestamp - 4
                current_end = timestamp
        merged_timeline.append((current_start, current_end + 0.5))
        merged_timelines.append(merged_timeline)
    
    return merged_timelines

# Функция для нарезки видео на основе объединенных таймингов
def cut_video_blocks(merged_timelines, video_file_path):
    block_filenames = []
    for i, timeline in enumerate(merged_timelines):
        block_files = []
        for j, (start, end) in enumerate(timeline):
            start_time = max(0, start)  # Начало момента
            end_time = end  # Конец момента
            output_filename = f'combination_{i+1}_block_{j+1}.mp4'
            ffmpeg_extract_subclip(video_file_path, start_time, end_time, targetname=output_filename)
            print(f"Saved {output_filename}")
            block_files.append(output_filename)
        block_filenames.append(block_files)
    return block_filenames

# Функция для объединения блоков в итоговые комбинации
def concatenate_combination_blocks(block_filenames):
    for i, block_files in enumerate(block_filenames):
        if len(block_files) > 1:
            clips = [VideoFileClip(filename) for filename in block_files]
            final_clip = concatenate_videoclips(clips, method="compose")
            output_filename = f'final_combination_{i+1}.mp4'
            final_clip.write_videofile(output_filename, codec='libx264')
            print(f"Saved {output_filename}")
        else:
            # If there's only one block, rename it to the final combination name
            block_filename = block_files[0]
            output_filename = f'final_combination_{i+1}.mp4'
            os.rename(block_filename, output_filename)
            print(f"Saved {output_filename}")

# Объединение близких таймингов
merged_timelines = merge_close_timings(timelines)

# Нарезка видео на блоки
block_filenames = cut_video_blocks(merged_timelines, video_file_path)

# Объединение блоков в итоговые комбинации
concatenate_combination_blocks(block_filenames)
