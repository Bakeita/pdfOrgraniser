import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF

class PDFThumbnailViewer(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("PDF Thumbnail Viewer")

        self.pdf_path = ""
        self.pdf_document = None
        self.current_page = 0

        self.label_thumbnail = tk.Label(self, text="Thumbnail will appear here")
        self.label_thumbnail.pack(padx=10, pady=10)

        open_button = tk.Button(self, text="Open PDF", command=self.open_pdf)
        open_button.pack(pady=10)

        next_page_button = tk.Button(self, text="Next Page", command=self.show_next_page)
        next_page_button.pack(pady=5)

        prev_page_button = tk.Button(self, text="Previous Page", command=self.show_previous_page)
        prev_page_button.pack(pady=5)

    def open_pdf(self):
        self.pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

        if self.pdf_path:
            self.pdf_document = fitz.open(self.pdf_path)
            self.show_page_thumbnail()

    def show_page_thumbnail(self):
        if self.pdf_document and 0 <= self.current_page < self.pdf_document.page_count():
            page = self.pdf_document.load_page(self.current_page)
            pix = page.get_pixmap()
            img_data = pix.image
            img = tk.PhotoImage(data=img_data)
            self.label_thumbnail.config(image=img)
            self.label_thumbnail.image = img

    def show_next_page(self):
        if self.pdf_document and self.current_page < self.pdf_document.page_count() - 1:
            self.current_page += 1
            self.show_page_thumbnail()

    def show_previous_page(self):
        if self.pdf_document and self.current_page > 0:
            self.current_page -= 1
            self.show_page_thumbnail()


if __name__ == "__main__":
    app = PDFThumbnailViewer()
    app.mainloop()
