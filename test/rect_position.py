import os
import sys
import time
from tkinter import *

import pyautogui
from PIL import Image

root = Tk()
output_box = Text(root)
output_box.pack(fill='both', expand=True)

x1 = None
before_word = None

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


    curpos = pyautogui.position()
    canvas.delete("rect")
    canvas.create_rectangle(pos1.x, pos1.y, curpos.x, curpos.y, outline='red', tags="rect", width=2)
    canvas.update()
    time.sleep(0.01)
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

    # img = Image.open("C:/Users/ilike/Pictures/IU_400x400.jpg")
    img = Image.open(crop_img_path)
    img.show()





# keyboard.add_hotkey('ctrl+alt+s', start)
start()
mainloop()
