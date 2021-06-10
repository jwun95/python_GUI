from tkinter import *
import os


root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") # 가로 * 세로
#root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

root.resizable(True, True) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

# 파일 입출력
filename = "mynote.txt"


def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, "w", encoding="UTF8") as file:
        file.write(txt.get("1.0", END)) 

# 메뉴 관리부분

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")
root.config(menu=menu)

# 스크롤바 관리 부분
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트 관리 부분

txt = Text(root, yscrollcommand=scrollbar.set) 
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.mainloop()