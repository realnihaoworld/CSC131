import tkinter as tk
import cv2

class WebcamApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Webcam App")

        self.cap = cv2.VideoCapture(0)

        self.canvas = tk.Canvas(self.root, width=640, height=480)
        self.canvas.pack()

        self.loop()

    def loop(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = image.fromarray(frame)
            photo = ImageTk.PhotoImage(image)
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)

        self.root.after(1, self.loop)

if __name__ == "__main__":
    app = WebcamApp()
    app.root.mainloop()