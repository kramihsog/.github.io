import tkinter as tk
from tkinter import messagebox
import random



class HitAndBlow(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.configure(bg="blue")
        self.secret = random.sample(range(10),4)
        self.attempts = 0

        tk.Label(self,text="0-9の重複しない4桁の数字を入力").pack(pady=10)
        self.entry = tk.Entry(self, font=("Arial",14))
        self.entry.pack(pady=5)
        
        self.button = tk.Button(self, text="判定",command=self.check)
        self.button.pack(pady=5)

        self.giveup_button = tk.Button(self,text="ギブアップ",command=self.show_answer,bg="#ffcccc")
        self.giveup_button.pack(pady=5)

        self.bind("<Return>", self.check)

        self.history_list = tk.Listbox(self,height=8,width=30)
        self.history_list.pack(pady=10)
        
    def check(self, event = None):
        guess_str = self.entry.get()

        if len(guess_str) !=4 or not guess_str.isdigit() or len(set(guess_str)) != 4:
            messagebox.showwarning("エラー","重複しない数字を入力してください")
            return

        guess = [int(d) for d in guess_str]
        self.attempts += 1

        hits = sum(1 for i in range(4) if guess[i] == self.secret[i])
        blows = sum(1 for i in range(4) if guess[i] in self.secret and guess[i] != self.secret[i])

        result_text = f"{self.attempts}回目:{guess_str} -> {hits}Hit,{blows}Blow"
        self.history_list.insert(tk.END,result_text)
        self.history_list.see(tk.END)

        self.entry.delete(0,tk.END)
        if hits == 4:
            messagebox.showinfo("クリア！",f"おめでとうございます！{self.attempts}回で正解しました！")
            self.destroy()

    def show_answer(self):
        answer_str = "".join(map(str,self.secret))
        messagebox.showinfo("ギブアップ",f"正解:{answer_str}")
        self.quit()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ヒットアンドブロー")
        self.geometry("400x250")

        self.container = tk.Frame(self)
        self.container.pack(fill="both",expand=True)

        self.start_frame = tk.Frame(self.container,bg="blue")
        self.start_frame.place(relx=0,rely=0,relwidth=1,relheight=1)
        tk.Label(self.start_frame,text="ヒットアンドブロー",fg="green").pack(pady=20)
        tk.Button(self.start_frame,text="スタート",command=self.show_game).pack(pady=20)

        self.game_frame = HitAndBlow(self.container)
        self.game_frame.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.start_frame.tkraise()

    def show_game(self):
        self.game_frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
