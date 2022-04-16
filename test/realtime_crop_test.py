import pyautogui
# import pytesseract
import os
from tkinter import *
import cv2
import time
import mouse
import keyboard
from PIL import Image
import easyocr

reader = easyocr.Reader(['ko'], gpu=True)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
root = Tk()
output_box = Text(root)
output_box.pack(fill='both', expand=True)



x1 = None


# 저장/불러오기 경로 : 실행파일과 같은 폴더
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# 텍스트 위치의 이미지 crop
def crop_image():
    global x1, y1, x2, y2

    # 투명한 캔버스 띄우기
    toplevel = Toplevel(root)

    canvas = Canvas(toplevel, highlightthickness=0, bd=0, relief='ridge', bg='white')
    canvas.master.wm_attributes('-transparentcolor', 'white')
    canvas.pack(expand=True, fill="both")

    # 화면 반짝거림 줄이기
    toplevel.update()

    # 전체화면, 맨위, 창 상단바 없애기
    toplevel.attributes('-fullscreen', True)
    toplevel.wm_attributes('-topmost', True)
    toplevel.focus_force()
    toplevel.overrideredirect(True)
    toplevel.update()

    # Crop할 부분 사각형 처리 및 좌표 가져오기 (마우스 왼쪽 버튼 클릭)
    pos1 = pyautogui.position()
    canvas.create_rectangle(0, 0, 0, 0, tags="rect")
    while True:
        curpos = pyautogui.position()
        canvas.delete("rect")
        canvas.create_rectangle(pos1.x, pos1.y, curpos.x, curpos.y, outline='red', tags="rect", width=2)
        canvas.update()
        time.sleep(0.01)
        if mouse.is_pressed("left"):
            pos2 = pyautogui.position()

            # 위에서 얻은 좌표로 이미지 Crop하기
            x1, y1 = pos1.x, pos1.y
            x2, y2 = pos2.x, pos2.y
            absx = abs(x2 - x1)
            absy = abs(y2 - y1)
            crop_img_path = resource_path('textimage.png')
            pyautogui.screenshot(crop_img_path, region=(min(x1, x2) + 1, min(y1, y2) + 1, absx - 2, absy - 2))

            toplevel.destroy()
            toplevel.update()
            break
    text_out()


# 같은 위치 또 crop
def crop_image_again():
    if x1 is None:
        print("Error")
    else:
        absx = abs(x2 - x1)
        absy = abs(y2 - y1)
        crop_img_path = resource_path('textimage.png')
        pyautogui.screenshot(crop_img_path, region=(min(x1, x2) + 1, min(y1, y2) + 1, absx - 2, absy - 2))
        text_out()


# 위에서 얻은 이미지로 OCR 후 프로그램에 출력
# ocr_lang = 'kor'
ocr_lang = 'eng'


# ocr_lang = 'jpn+jpn_vert'
def text_out():
    img = resource_path('textimage.png')
    img_gray = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('gray', img_gray)
    img_gray = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # cv2.imshow('gray', img_gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    result = reader.readtext('textimage.png', detail=0)
    output_box.delete("1.0", END)
    output_box.insert(END, result)

    # text_ocr = pytesseract.image_to_string(img_gray, lang=ocr_lang)[:-1].strip()
    # text_output = ''
    # if ocr_lang == 'jpn+jpn_vert':
    #     for t in text_ocr:
    #         if t != ' ' and t != '\n':
    #             text_output += t
    # else:
    #     text_output = text_ocr.replace('\n', ' ')
    #
    # output_box.delete("1.0", END)
    # output_box.insert(END, text_output)


keyboard.add_hotkey('ctrl+q', crop_image)
keyboard.add_hotkey('ctrl+r', crop_image_again)
mainloop()