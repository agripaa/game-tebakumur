import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QWidget,
    QRadioButton,
    QPushButton,
    QButtonGroup,
    QMessageBox,
)


class AgeGuessingGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game Penebak Umur")
        self.setGeometry(100, 100, 400, 300)

        self.questions = [
            {
                "question": "Apa jenis musik kesukaan Anda?",
                "options": ["Pop", "Rock", "Jazz"],
                "points": [1, 2, 3],
            },
            {
                "question": "Apa hobi Anda?",
                "options": ["Membaca", "Olahraga", "Menonton Film"],
                "points": [2, 1, 3],
            },
            {
                "question": "Apa makanan kesukaan Anda?",
                "options": ["Pizza", "Sushi", "Burger"],
                "points": [1, 3, 2],
            },
            {
                "question": "Apa genre film kesukaan Anda?",
                "options": ["Komedi", "Horor", "Drama"],
                "points": [1, 3, 2],
            },
            {
                "question": "Apa minuman kesukaan Anda?",
                "options": ["Teh", "Kopi", "Jus"],
                "points": [2, 3, 1],
            },
            {
                "question": "Apa warna favorit Anda?",
                "options": ["Merah", "Biru", "Hijau"],
                "points": [2, 1, 3],
            },
            {
                "question": "Apa yang Anda lakukan di waktu luang?",
                "options": ["Berkumpul dengan teman", "Bermain game", "Berkebun"],
                "points": [1, 2, 3],
            },
            {
                "question": "Hewan peliharaan apa yang Anda sukai?",
                "options": ["Kucing", "Anjing", "Burung"],
                "points": [2, 3, 1],
            },
            {
                "question": "Apa genre buku kesukaan Anda?",
                "options": ["Fiksi", "Non-fiksi", "Fantasi"],
                "points": [1, 2, 3],
            },
            {
                "question": "Olahraga apa yang Anda sukai?",
                "options": ["Sepak bola", "Berenang", "Lari"],
                "points": [3, 2, 1],
            },
        ]

        self.points = 0
        self.current_question = 0

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.question_label = QLabel(self.questions[self.current_question]["question"])
        self.layout.addWidget(self.question_label)

        self.options_group = QButtonGroup()
        for option in self.questions[self.current_question]["options"]:
            radio_button = QRadioButton(option)
            self.layout.addWidget(radio_button)
            self.options_group.addButton(radio_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next_question)
        self.layout.addWidget(self.next_button)

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def next_question(self):
        selected_button = self.options_group.checkedButton()
        if selected_button:
            selected_option = selected_button.text()
            index = self.questions[self.current_question]["options"].index(
                selected_option
            )
            self.points += self.questions[self.current_question]["points"][index]
            self.current_question += 1
            if self.current_question < len(self.questions):
                self.update_question()
            else:
                self.guess_age()
        else:
            QMessageBox.warning(self, "Peringatan", "Pilih salah satu opsi!")

    def update_question(self):
        self.question_label.setText(self.questions[self.current_question]["question"])
        self.options_group = QButtonGroup()
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QRadioButton):
                self.layout.removeWidget(widget)
                widget.deleteLater()

        for option in self.questions[self.current_question]["options"]:
            radio_button = QRadioButton(option)
            self.layout.addWidget(radio_button)
            self.options_group.addButton(radio_button)

    def guess_age(self):
        age = self.calculate_age()

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setWindowTitle("Hasil Tebakan")
        msg_box.setText(f"Saya menebak umur Anda adalah {age} tahun. Apakah benar?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg_box.exec_()

        if result == QMessageBox.Yes:
            QMessageBox.information(self, "Hasil", "Umur Anda benar.")
            self.close()
        else:
            self.retry()

    def calculate_age(self):
        # mengkalkulasikan point yang didapat
        if self.points <= 10:
            return 15
        elif self.points <= 20:
            return 20
        elif self.points <= 25:
            return 25
        else:
            return 30

    def retry(self):
        self.points = 0
        self.current_question = 0
        self.initUI()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgeGuessingGame()
    window.show()
    sys.exit(app.exec_())
