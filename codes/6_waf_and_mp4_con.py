from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def merge_video_and_audio(video_path, audio_path, output_path):
    
    video_clip = VideoFileClip(video_path)
    
    
    additional_audio_clip = AudioFileClip(audio_path)
    
    
    original_audio = video_clip.audio
    
    
    final_audio = CompositeAudioClip([original_audio, additional_audio_clip])
    
    
    video_clip = video_clip.set_audio(final_audio)
    
    
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')


merge_video_and_audio('output_video_without_sub.mp4', 'comment.wav', 'output_video.mp4')