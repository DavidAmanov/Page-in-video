#Необходимые библиотеки
import cv2 #Необходима для самой работы с видео
import time #Необходима для работы со временем в видео
import os #Необходима для работы с файловой системой компьютера(задание путей, а также присвоение названия файлам)

output_folder = r'C:\Users\David\Desktop\pictres' # Укажите путь, в котором нужно сохранять кадры без движения
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
path = r'C:\Users\David\Desktop\pictres\video_2023-10-27_15-53-11.mp4' #путь к видео файлу
cap = cap = cv2.VideoCapture(path)  # Видеопоток с веб-камеры или путь к видео файлу
#cap.set(3, 1280)  # Установка размера окна при необходимости
#cap.set(4, 700)

ret, frame1 = cap.read() #1 кадр
ret, frame2 = cap.read() #2 кадр


motion_detected = False  # Флаг для отслеживания движения
last_motion_time = time.time()  # Время последнего обнаруженного движения
motion_timeout = 0.5  # Время ожидания без движения в секундах, параметр влияет на точность выполнения кода

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2) #сравнение кадров
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(
                contour)
        if cv2.contourArea(contour) < 1000: # размер контура движения, параметр который влияет на тончость выполнения кода
            continue

        cv2.putText(frame1, "Status: {}".format("Dvigenie"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3,
                    cv2.LINE_AA) #добавляет подпись "движение" на видеопоток
        motion_detected = True
        last_motion_time = time.time()

    if motion_detected and time.time() - last_motion_time >= motion_timeout: # Условие сохранения кадра без движения
        frame_filename = os.path.join(output_folder, f'frame_{time.time()}.jpg') #путь сохранения и создание имени файла
        cv2.imwrite(frame_filename, frame1) #Само сохранение кадра
        motion_detected = False #Возврат флага к положению false
    cv2.imshow("frame1", frame1) #Вывод видеопотока на экран
    frame1 = frame2
    ret, frame2 = cap.read()


    if cv2.waitKey(40) == 27:
        break

cap.release()
cv2.destroyAllWindows()