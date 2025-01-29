import cv2
import time

duration = 30
fps = 10.0
width = 1280
height = 720
filename = "output/teste.mp4"
limit_n_frames = (fps * duration)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

n_frames = 0
start_time = time.time()

while (n_frames < limit_n_frames):
    print(f"Frame - {n_frames}")
    ret, frame = cap.read()
    if not ret:
        print("Erro ao capturar o frame.")
        break
    out.write(frame)
    n_frames+=1

cap.release()
out.release()

end_time = time.time()
print(f"Levou: {end_time - start_time}")
print(f"Video salvo em {filename}.")
