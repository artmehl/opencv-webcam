import cv2
import time

duration = 30
fps = 10.0
width = 1280
height = 720
filename = "output/teste.mp4"
limit_n_frames = (fps * duration)

# Inicializa a captura de vídeo (0 normalmente é a câmera padrão)
cap = cv2.VideoCapture(0)

# Verifica se a câmera foi aberta com sucesso
if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

# Define a largura e altura do vídeo
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Define o codec e cria o objeto VideoWriter
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
    
# End recording
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Gravação finalizada e salva como {filename}.")
print(f"Levou: {time.time() - start_time}")
