import cv2
import os
import time

# Caminho do vídeo
video_path = 'output/teste.mp4'

# Cria a pasta 'frames' caso não exista
if not os.path.exists('frames'):
    os.makedirs('frames')

# Abre o vídeo
cap = cv2.VideoCapture(video_path)

# Verifica se o vídeo foi aberto corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    exit()

frame_count = 0

start = time.time()

while True:
    # Captura o frame do vídeo
    ret, frame = cap.read()

    # Se não houver mais frames, encerra o loop
    if not ret:
        break
    
    # Salva o frame como uma imagem PNG
    frame_filename = f'frames/frame_{frame_count:04d}.png'
    cv2.imwrite(frame_filename, frame)
    
    # Exibe uma mensagem para acompanhar o progresso
    print(f'Frame {frame_count} salvo em {frame_filename}')
    
    # Incrementa o contador de frames
    frame_count += 1

# Libera os recursos e fecha as janelas
cap.release()
print("Extração de frames concluída.")
print(f"levou: {time.time() - start}")
