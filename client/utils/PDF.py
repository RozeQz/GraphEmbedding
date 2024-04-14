from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, logo_path, title):
        super().__init__()
        self.add_font('Times New Roman', '',
                      './client/gui/resources/fonts/Times New Roman.ttf',
                      uni=True)
        self.set_font("Times New Roman", size=14)
        # Отступ 2.5см от левого края
        self.set_left_margin(margin=25)
        # Отступ 2см от правого края
        self.set_right_margin(margin=20)
        # Отступ 2см от верхнего края
        self.set_top_margin(margin=20)
        self.logo_path = logo_path
        self.title = title

    def header(self):
        self.set_font("Times New Roman", size=18)
        # Логотип
        self.image(self.logo_path, 10, 8, 33)
        # Title
        self.cell(w=170, h=10, text=self.title, align='C')
        # Line break
        self.ln(h=25)

    def footer(self):
        self.set_font("Times New Roman", size=14)
        # Position at 2 cm from bottom
        self.set_y(-20)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, str(self.page_no()), 0, 0, 'C')

    def tab(self, n=1, tab_size=10):
        for _ in range(n):
            self.cell(w=tab_size, h=10, ln=0)
