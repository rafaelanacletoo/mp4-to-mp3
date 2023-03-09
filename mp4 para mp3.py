from moviepy.editor import *
import os

# Defina o diretório que contém os arquivos MP4
directory = input(
    "Digite o caminho da pasta com arquivos mp4 que deseja converter para mp3: ")

# Para cada arquivo na pasta
for filename in os.listdir(directory):
    if filename.endswith(".mp4"):
        # Caminho completo do arquivo MP4
        video_path = os.path.join(directory, filename)

        # Nome do arquivo MP3 (mesmo nome do arquivo MP4, mas com extensão .mp3)
        audio_path = os.path.join(
            directory, os.path.splitext(filename)[0] + '.mp3')

        # Carrega o arquivo de vídeo
        video = VideoFileClip(video_path)

        # Extrai o áudio do arquivo de vídeo
        audio = video.audio

        # Salva o arquivo de áudio como um arquivo MP3
        audio.write_audiofile(audio_path)

        # Fecha o arquivo de vídeo
        video.close()
