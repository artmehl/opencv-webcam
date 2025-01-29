import cv2
import os
import time

video_path = 'output/teste.mp4'

if not os.path.exists('frames'):
    os.makedirs('frames')

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Erro ao abrir o vídeo")
    exit()

frame_count = 0

start = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = f'frames/frame_{frame_count:04d}.png'
    cv2.imwrite(frame_filename, frame)
    print(f'Frame {frame_count} salvo em {frame_filename}')
    frame_count += 1
    
cap.release()
print("Extração de frames concluída.")
print(f"levou: {time.time() - start}")
