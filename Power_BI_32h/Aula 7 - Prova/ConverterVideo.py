from moviepy.editor import VideoFileClip

def convert_mov_to_mp4(input_path, output_path):
    # Carrega o vídeo .MOV
    video_clip = VideoFileClip(input_path)
    
    # Especifica o caminho de saída e converte para .MP4
    video_clip.write_videofile(output_path, codec='libx264')

# Caminho do arquivo .MOV de entrada
input_path = 'D:\IMG_6059.MOV'

# Caminho do arquivo .MP4 de saída
output_path = 'D:\Videos Convertidos/video.mp4'

# Converte o vídeo
convert_mov_to_mp4(input_path, output_path)