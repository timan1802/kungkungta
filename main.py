import sys

import pyautogui
import os
from tkinter import *
import time
import mouse
import keyboard
import easyocr
import findword

# ocr 초기화
reader = easyocr.Reader(['ko'], gpu=False)

root = Tk()
output_box = Text(root)
output_box.pack(fill='both', expand=True)

# global 변수
x1 = None
history_word_list = []


# 저장/불러오기 경로 : 실행파일과 같은 폴더
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("..")
    return os.path.join(base_path, relative_path)


# 화면창 띄우기, 마우스 우 클릭으로 포지션 설정
def start():
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
def repeat():
    if x1 is None:
        print("마우스 포지션 설정 먼저 하세요.")
        return
    else:
        while True:
            absx = abs(x2 - x1)
            absy = abs(y2 - y1)
            crop_img_path = resource_path('textimage.png')
            pyautogui.screenshot(crop_img_path, region=(min(x1, x2) + 1, min(y1, y2) + 1, absx - 2, absy - 2))
            text_out()
            time.sleep(0.1)


def text_out():
    global history_word_list
    result = reader.readtext(resource_path('textimage.png'), detail=0)
    print('ocr 인식 : ', result)
    if len(result) != 1:
        return
    result = result[0]

    history_word_list.append(result)

    output_box.delete("1.0", END)
    output_box.insert(END, findword.find_word(result))


def history_clear():
    global history_word_list
    history_word_list = []


keyboard.add_hotkey('ctrl+e', start)
keyboard.add_hotkey('ctrl+r', repeat)
keyboard.add_hotkey('ctrl+t', history_clear)
mainloop()
