import csv
from tkinter import *
import random

BGCOLOR = "#000080"
CORRECT_COLOR = "#7FFFD4"
WRONG_COLOR = "#F08080"
BTN_COLOR = "#C0C0C0"

with open("eng_quiz_data.csv", "r", encoding="UTF-8-sig") as file:
    questions = list(csv.reader(file))

answer = 0
wrong_count = 0  # 틀린 횟수를 추적하는 변수

# 문제 생성
def next_question():
    global answer, wrong_count

    # 새로운 문제로 넘어갈 때 틀린 횟수 초기화
    wrong_count = 0
    
    for i in range(4):
        buttons[i].config(bg=BTN_COLOR)
    multi_choice = random.sample(questions, 4)
    answer = random.randint(0, 3)
    cur_question = multi_choice[answer][0]

    question_label.config(text=cur_question)
    feedback_label.config(text="")  # 피드백 라벨 초기화

    for i in range(4):
        buttons[i].config(text=multi_choice[i][1])

# 정답 체크
def check_answer(idx): 
    global wrong_count  # 전역 변수로 선언된 wrong_count 사용
    idx = int(idx)
    if answer == idx:
        buttons[idx].config(bg=CORRECT_COLOR)
        feedback_label.config(text="역시 넌 천재야^^", fg=CORRECT_COLOR)
        window.after(1000, next_question)
    else:
        wrong_count += 1  # 틀린 횟수 증가
        buttons[idx].config(bg=WRONG_COLOR)
        if wrong_count == 1:
            feedback_label.config(text="너 바보니?", fg=WRONG_COLOR)
        elif wrong_count == 2:
            feedback_label.config(text="너 진짜 바보구나!", fg=WRONG_COLOR)
        elif wrong_count == 3:
            feedback_label.config(text="바보확정!", fg=WRONG_COLOR)
        else:
            feedback_label.config(text="틀렸어! 다음 문제로 넘어가~", fg=WRONG_COLOR)

window = Tk()
window.title("영어 퀴즈><")
window.config(padx=30, pady=10, bg=BGCOLOR)

question_label = Label(window, width=20, height=2, text="test",
                       font=("나눔바른펜", 25, "bold"), bg=BGCOLOR, fg="white")
question_label.pack(pady=30)

buttons = []
for i in range(4):
    btn = Button(window, text=f"{i}번", width=35, height=2, font=("나눔바른펜", 15, "bold"), 
                 bg=BTN_COLOR, command=lambda idx=i: check_answer(idx))
    btn.pack()
    buttons.append(btn)

# 피드백 메시지를 위한 라벨 추가
feedback_label = Label(window, text="", font=("나눔바른펜", 20, "bold"), bg=BGCOLOR)
feedback_label.pack(pady=20)

next_btn = Button(window, text="다음 문제", width=15, height=2,
                  command=next_question, font=("나눔바른펜", 15, "bold"), bg=CORRECT_COLOR)
next_btn.pack(pady=30)

next_question()

window.mainloop()
