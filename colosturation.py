import cv2
import numpy as np

# Функция для изменения изображения
def change_saturation(frame, saturation_factor):
    # Преобразование в цветовое пространство HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Изменение 
    hsv_frame[:, :, 1] = np.clip(hsv_frame[:, :, 1] * saturation_factor, 0, 255).astype(np.uint8)

    # Преобразование обратно в цветовое пространство BGR
    modified_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)
    return modified_frame

# Захват видеопотока с веб-камеры
cap = cv2.VideoCapture(0)

while True:
    # Считывание кадра из видеопотока
    ret, frame = cap.read()

    if ret:
        # Изменение изображения
        saturated_frame = change_saturation(frame, 2.0)

        # Отображение кадра с изменениями
        cv2.imshow('Saturated Video', saturated_frame)

    # Для выхода - 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
