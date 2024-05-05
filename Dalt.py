from tkinter import*
import cv2
import numpy as np
def Cam ():
    def change_saturation(frame, saturation_factor):
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv_frame[:, :, 1] = np.clip(hsv_frame[:, :, 1] * saturation_factor, 0, 255).astype(np.uint8)
        modified_frame = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)
        return modified_frame

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if ret:
            saturated_frame = change_saturation(frame, 3.5)
            cv2.imshow('DALTONICO', saturated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


root = Tk()

root.title('DALTONICO')
root.geometry('331x741')
root.resizable(width = 'False', height = 'False')

root.image = PhotoImage(file="fonn.png")
bg_image = Label(root, image=root.image)
bg_image.pack()

root.menuImage = PhotoImage(file='menuu.png')
menu = Button(root, image=root.menuImage, borderwidth=0, bg = 'black',activebackground='black',activeforeground='black')
menu.place(x = 17, y = 265)

root.buttonImage = PhotoImage(file="knopka.png")
roundedbutton = Button(root, bg = 'white', image=root.buttonImage, command= Cam, borderwidth=0)
roundedbutton.place(x = 10 , y = 575)

root.mainloop()