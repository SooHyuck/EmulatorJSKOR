import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, Menu
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import imageio
import threading

class GifMakerApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.title("GIF Maker")
        self.geometry("800x630")

        # 변수 초기화
        self.file_list = []
        self.preview_images = []
        self.frame_interval = 1.0  # 기본 1초
        self.scale_factor = 1.0  # 이미지 확대 배율
        self.output_path = os.path.join(os.getcwd(), "output.gif")

        # UI 구성
        self.create_widgets()
        self.configure_drag_and_drop()

    def create_widgets(self):
        # 프레임 좌우 배치
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 왼쪽: 파일 리스트 + 삭제 등
        left_frame = ttk.Frame(main_frame, width=300)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)

        lbl_files = ttk.Label(left_frame, text="이미지 파일 목록")
        lbl_files.pack(anchor="w")

        self.listbox = tk.Listbox(left_frame, selectmode=tk.EXTENDED, height=25)
        self.listbox.pack(fill=tk.Y, expand=True)
        self.listbox.bind("<Delete>", self.delete_selected)
        self.listbox.bind("<Button-3>", self.show_context_menu)  # 우클릭 메뉴

        # 우클릭 메뉴
        self.context_menu = Menu(self, tearoff=0)
        self.context_menu.add_command(label="선택 항목 삭제", command=self.delete_selected)

        btn_del = ttk.Button(left_frame, text="선택 삭제", command=self.delete_selected)
        btn_del.pack(fill=tk.X, pady=5)

        # 오른쪽: 이미지 미리보기 + 설정 + GIF 만들기
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10,0))

        # 이미지 미리보기
        preview_lbl = ttk.Label(right_frame, text="선택된 이미지 미리보기")
        preview_lbl.pack(anchor="w")

        preview_height = 400
        preview_width = 450
        self.preview_canvas = tk.Canvas(right_frame, width=preview_width, height=preview_height, bg="white", relief=tk.SUNKEN, borderwidth=1)
        self.preview_canvas.pack()

        self.preview_canvas_img_id = None

        # 프레임 간격 조절 슬라이더
        frame_interval_frame = ttk.Frame(right_frame)
        frame_interval_frame.pack(fill=tk.X, pady=(10,0))

        ttk.Label(frame_interval_frame, text="프레임 간격 (초):").pack(side=tk.LEFT)
        self.frame_slider = ttk.Scale(frame_interval_frame, from_=0.05, to=5.0, value=self.frame_interval,
                                      orient=tk.HORIZONTAL, command=self.on_frame_slider_change)
        self.frame_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.frame_value_lbl = ttk.Label(frame_interval_frame, text=f"{self.frame_interval:.2f}s")
        self.frame_value_lbl.pack(side=tk.LEFT)

        # 이미지 확대 배율 선택
        scale_frame = ttk.Frame(right_frame)
        scale_frame.pack(fill=tk.X, pady=(10,0))

        ttk.Label(scale_frame, text="이미지 확대 배율:").pack(side=tk.LEFT)
        self.scale_var = tk.StringVar(value="1.0")
        scale_options = ["1.0", "2.0", "0.5", "사용자 입력"]
        self.scale_combo = ttk.Combobox(scale_frame, values=scale_options, textvariable=self.scale_var, state="readonly", width=10)
        self.scale_combo.pack(side=tk.LEFT, padx=5)
        self.scale_combo.bind("<<ComboboxSelected>>", self.on_scale_option_changed)

        self.custom_scale_entry = ttk.Entry(scale_frame, width=8)
        self.custom_scale_entry.pack(side=tk.LEFT)
        self.custom_scale_entry.insert(0, "1.0")
        self.custom_scale_entry.config(state=tk.DISABLED)
        self.custom_scale_entry.bind("<Return>", self.on_custom_scale_entered)

        # 출력 파일 지정
        output_frame = ttk.Frame(right_frame)
        output_frame.pack(fill=tk.X, pady=(10,0))

        ttk.Label(output_frame, text="출력 GIF 파일명:").pack(side=tk.LEFT)
        self.output_entry = ttk.Entry(output_frame)
        self.output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.output_entry.insert(0, self.output_path)

        btn_browse = ttk.Button(output_frame, text="찾아보기", command=self.browse_output_file)
        btn_browse.pack(side=tk.LEFT)

        # 진행바
        progress_frame = ttk.Frame(right_frame)
        progress_frame.pack(fill=tk.X, pady=(10,0))

        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100)
        self.progress_bar.pack(fill=tk.X)

        # GIF 만들기 버튼
        self.make_gif_btn = ttk.Button(right_frame, text="GIF 만들기", command=self.start_make_gif_thread)
        self.make_gif_btn.pack(pady=10)

    def configure_drag_and_drop(self):
        # 리스트박스에 드래그 앤 드롭 파일 추가 지원
        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind("<<Drop>>", self.drop_files)

        # 리스트박스 선택시 미리보기 업데이트
        self.listbox.bind("<<ListboxSelect>>", self.update_preview)

    def drop_files(self, event):
        files = self.split_drop_files(event.data)
        new_files = []
        for f in files:
            if f.lower().endswith((".png", ".jpg", ".jpeg")) and f not in self.file_list:
                self.file_list.append(f)
                new_files.append(f)
        self.update_file_listbox()
        if new_files:
            self.listbox.selection_clear(0, tk.END)
            # 새로 추가된 파일들 선택 후 미리보기 업데이트
            for f in new_files:
                idx = self.file_list.index(f)
                self.listbox.selection_set(idx)
            self.update_preview()

    def split_drop_files(self, data):
        # 여러 파일이 공백으로 구분되어 들어옴, 경로에 공백 있으면 중복될 수 있어 "{" "}" 처리 고려
        if data.startswith("{") and data.endswith("}"):
            # 중괄호 묶음 여러개로 분할
            parts = []
            temp = ""
            in_brace = False
            for c in data:
                if c == "{":
                    in_brace = True
                    temp = ""
                elif c == "}":
                    in_brace = False
                    parts.append(temp)
                elif in_brace:
                    temp += c
                elif c == " " and not in_brace:
                    continue
                else:
                    temp += c
            return parts
        else:
            return data.split()

    def update_file_listbox(self):
        self.listbox.delete(0, tk.END)
        for f in self.file_list:
            self.listbox.insert(tk.END, f)

    def delete_selected(self, event=None):
        selected_indices = list(self.listbox.curselection())
        if not selected_indices:
            return
        for index in reversed(selected_indices):
            del self.file_list[index]
        self.update_file_listbox()
        self.update_preview()

    def show_context_menu(self, event):
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

    def update_preview(self, event=None):
        selected = self.listbox.curselection()
        if not selected:
            self.preview_canvas.delete("all")
            return
        index = selected[0]
        filepath = self.file_list[index]
        try:
            img = Image.open(filepath)
            # 이미지 확대 배율 적용
            scale = self.scale_factor
            w, h = img.size
            new_w, new_h = int(w * scale), int(h * scale)

            # 캔버스 크기 고려해서 세로 높이 고정, 너비는 맞추기
            canvas_w = self.preview_canvas.winfo_width()
            canvas_h = self.preview_canvas.winfo_height()

            # 높이 최대한 캔버스 세로 크기로 맞춤
            if new_h > canvas_h:
                scale = canvas_h / h
                new_w, new_h = int(w * scale), canvas_h

            img = img.resize((new_w, new_h), Image.LANCZOS)
            self.preview_imgtk = ImageTk.PhotoImage(img)

            self.preview_canvas.delete("all")
            x = (canvas_w - new_w) // 2 if canvas_w > new_w else 0
            y = (canvas_h - new_h) // 2 if canvas_h > new_h else 0
            self.preview_canvas.create_image(x, y, anchor="nw", image=self.preview_imgtk)
        except Exception as e:
            self.preview_canvas.delete("all")
            self.preview_canvas.create_text(10, 10, anchor="nw", text=f"이미지 미리보기 실패:\n{e}", fill="red")

    def on_frame_slider_change(self, value):
        try:
            self.frame_interval = float(value)
            self.frame_value_lbl.config(text=f"{self.frame_interval:.2f}s")
        except ValueError:
            pass

    def on_scale_option_changed(self, event=None):
        val = self.scale_var.get()
        if val == "사용자 입력":
            self.custom_scale_entry.config(state=tk.NORMAL)
        else:
            self.custom_scale_entry.config(state=tk.DISABLED)
            try:
                self.scale_factor = float(val)
            except ValueError:
                self.scale_factor = 1.0
            self.update_preview()

    def on_custom_scale_entered(self, event=None):
        val = self.custom_scale_entry.get()
        try:
            f = float(val)
            if f <= 0:
                raise ValueError
            self.scale_factor = f
            self.update_preview()
        except ValueError:
            messagebox.showerror("오류", "올바른 숫자를 입력하세요.")

    def browse_output_file(self):
        f = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files","*.gif")], initialfile="output.gif")
        if f:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, f)
            self.output_path = f

    def start_make_gif_thread(self):
        if not self.file_list:
            messagebox.showwarning("경고", "이미지 파일을 하나 이상 추가하세요.")
            return
        output_path = self.output_entry.get().strip()
        if not output_path:
            messagebox.showwarning("경고", "출력 파일명을 지정하세요.")
            return

        self.output_path = output_path

        # GIF 생성 중복 방지
        self.make_gif_btn.config(state=tk.DISABLED)
        self.progress_var.set(0)
        
        threading.Thread(target=self.make_gif).start()

    def make_gif(self):
        try:
            frames = []
            scale = self.scale_factor
            for i, file in enumerate(self.file_list):
                img = Image.open(file).convert("RGBA")
                if scale != 1.0:
                    w, h = img.size
                    img = img.resize((int(w*scale), int(h*scale)), Image.LANCZOS)
                frames.append(img)

                progress = (i + 1) / len(self.file_list) * 100
                self.progress_var.set(progress)

            # duration은 프레임당 ms 단위, frame_interval은 초 단위
            duration_ms = int(self.frame_interval * 1000)

            # 첫 번째 프레임 저장, append_images로 나머지 프레임 추가
            frames[0].save(self.output_path, save_all=True, append_images=frames[1:], optimize=False, duration=duration_ms, loop=0)

            messagebox.showinfo("완료", f"GIF가 성공적으로 저장되었습니다:\n{self.output_path}")

        except Exception as e:
            messagebox.showerror("오류", f"GIF 생성 중 오류가 발생했습니다:\n{e}")
        finally:
            self.make_gif_btn.config(state=tk.NORMAL)
            self.progress_var.set(0)

if __name__ == "__main__":
    app = GifMakerApp()
    app.mainloop()