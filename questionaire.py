import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import numpy as np

class BinaryQuestionApp:
    def __init__(self, master):
        self.master = master
        self.selected_file_path = None
        self.question_answers = None
        self.scale_factor = None

        self.master.title("Image Interpolater")
        self.custom_font = ("Courier", 14)

        self.master.configure(bg="#282c34")
        self.master.resizable(False, False)

        self.frame = tk.Frame(self.master, relief='flat', bd=1, bg="#282c34")
        self.frame.pack(expand=False, padx=15, pady=15, fill="both")

        heading_label = tk.Label(self.frame, text="Choose which best describes your image", font=("Courier", 16, "bold"), fg="white", bg="#282c34")
        heading_label.grid(row=0, column=0, columnspan=2, pady=10)

        questions = [
            'Q1. Is the image primarily made up of sharp edges and distinct boundaries?\t',
            'Q2. Does the image contain a lot of fine details or textures?\t',
            'Q3. Is computational speed a significant concern for you?\t',
            'Q4. Is the image of a natural scene or a photograph?\t',
            'Q5. Do you want the output to be visually smooth, even if it sacrifices some fine details?\t',
            'Q6. Are you willing to invest more computational resources for better quality?\t',
            'Q7. Is the image black-and-white?\t'
        ]

        # Question variables
        self.question_vars = [tk.StringVar() for _ in questions]
        
        # Set default answers
        for var in self.question_vars:
            var.set("No")

        # File path variable
        self.file_path_var = tk.StringVar()
        self.file_path_var.set("No file selected")


        self.create_widgets(questions)

    def create_widgets(self, questions):
        # Set padding
        padding = 5

        # Create question labels and checkbuttons
        for i, question in enumerate(questions):
            question_label = tk.Label(self.frame, text=question, font=self.custom_font, fg="white", bg="#282c34")
            question_label.grid(row=i + 1, column=0, sticky="w", pady=padding)

            yes_checkbutton = tk.Checkbutton(self.frame, text="Yes", variable=self.question_vars[i], onvalue="Yes",
                                             offvalue="No", font=self.custom_font, fg="white", bg="#282c34",
                                             selectcolor="#282c34")
            yes_checkbutton.grid(row=i + 1, column=1, sticky="w", pady=padding)

        # File path label
        file_path_label = tk.Label(self.frame, text="Browse your Image:", font=self.custom_font, fg="white", bg="#282c34")
        file_path_label.grid(row=len(questions) + 1, column=0, columnspan=2, sticky="w", pady=padding*4)

        # File path entry
        file_path_entry = tk.Entry(self.frame, readonlybackground="#282c34", textvariable=self.file_path_var, width=40,
                                   font=self.custom_font, fg="white", state="readonly")
        file_path_entry.grid(row=len(questions) + 3, column=0, columnspan=2, pady=padding*2)

        # Browse button
        browse_button = tk.Button(self.frame, text="Browse", command=self.browse_file,
                                  font=self.custom_font, fg="white", bg="#61dafb")
        browse_button.grid(row=len(questions) + 1, column=1, columnspan=2, pady=padding*4)

        self.scaling = tk.DoubleVar()
        self.scaling.set(0.0)

        # Scaling label
        self.scaling_label = tk.Label(self.frame, text="Scaling:", font=self.custom_font, fg="white", bg="#282c34")
        self.scaling_label.grid(row=len(questions) + 2, column=0, columnspan=2, sticky="w", pady=padding*4)

        # Scaling entry
        scaling_entry = tk.Entry(self.frame, textvariable=self.scaling, width=10,
                                 font=self.custom_font, fg="white", bg="#282c34")
        scaling_entry.grid(row=len(questions) + 2, column=1, columnspan=2, pady=5)

        # Submit button
        submit_button = tk.Button(self.frame, text="Submit", command=self.submit,
                                  font=self.custom_font, fg="white", bg="#61dafb")
        submit_button.grid(row=len(questions) + 4, column=0, columnspan=2, pady=padding)

    def browse_file(self):
        f_types = [("Image Files", "*.png;*.gif;*.ppm;*.pgm;*.pbm;*.pgm;*.tif;*.tiff;*.jpg;*.jpeg")]
        file_path = filedialog.askopenfilename(filetypes=f_types)
        if file_path:
            self.file_path_var.set(file_path)

    def submit(self):
        self.question_answers = list(map(lambda x: 0 if x == 'No' else 1, [var.get() for var in self.question_vars]))
        self.selected_file_path = self.file_path_var.get()
        self.scale_factor = self.scaling.get()

        if self.selected_file_path == "No file selected":
            # Raise a popup if the file path is not selected
            messagebox.showerror("Error", "Please select a file.")
        else:
            self.master.destroy()


def get_config () -> tuple :

    def calculate_scores (answers : list = []) -> np.ndarray :
        
        scores = np.zeros(4)
        answer_results = np.array([
            (2,1,0,-1),
            (-1,0,2,2),
            (1,2,0,-1),
            (0,0,1,2),
            (0,2,1,1),
            (0,0,1,2),
            (2,-1,-1,-1)
        ])

        frac_denom = answer_results.sum(axis=0)

        no_scores = np.vectorize(lambda x : {-1:2, 0:1, 1:0, 2:-1}[x])

        for idx, answer in enumerate(answers) :
            if answer : scores += answer_results[idx]
            else : scores += no_scores(answer_results[idx])

        print(scores, frac_denom, scores/frac_denom) # Remove before Deployment
        return scores/frac_denom

    root = tk.Tk()
    app = BinaryQuestionApp(root)
    root.mainloop()
    
    score_percentage = calculate_scores(app.question_answers)
    return (score_percentage.argmax(), app.selected_file_path, float(app.scale_factor))

if __name__ == "__main__":
    print(get_config())