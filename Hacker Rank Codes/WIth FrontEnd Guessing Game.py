import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QLineEdit, QMessageBox, QComboBox
)

class GuessGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Guessing Game")
        self.setGeometry(300, 200, 400, 250)

        # Game variables
        self.num = None
        self.attempts = 0
        self.remaining = 0

        # Difficulty selection
        self.diff_label = QLabel("Choose Difficulty:")
        self.diff_box = QComboBox()
        self.diff_box.addItems(["Easy", "Medium", "Hard"])

        self.start_btn = QPushButton("Start Game")
        self.start_btn.clicked.connect(self.start_game)

        # Guess input
        self.guess_label = QLabel("Enter a number (1-100):")
        self.guess_input = QLineEdit()
        self.check_btn = QPushButton("Check Guess")
        self.check_btn.clicked.connect(self.check_guess)
        self.check_btn.setEnabled(False)

        # Result display
        self.result_label = QLabel("")

        # Layouts
        vbox = QVBoxLayout()
        vbox.addWidget(self.diff_label)
        vbox.addWidget(self.diff_box)
        vbox.addWidget(self.start_btn)
        vbox.addWidget(self.guess_label)
        vbox.addWidget(self.guess_input)
        vbox.addWidget(self.check_btn)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)

    def start_game(self):
        choice = self.diff_box.currentText()
        if choice == "Easy":
            self.attempts = 10
        elif choice == "Medium":
            self.attempts = 7
        else:
            self.attempts = 5

        self.num = random.randint(1, 100)
        self.remaining = self.attempts
        self.result_label.setText(f"Game started! You have {self.attempts} attempts.")
        self.check_btn.setEnabled(True)

    def check_guess(self):
        if not self.guess_input.text().isdigit():
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
            return

        guess = int(self.guess_input.text())
        self.remaining -= 1

        if guess == self.num:
            QMessageBox.information(self, "Winner!", f"🎉 Correct! You won in {self.attempts - self.remaining} attempts.")
            self.reset_game()
        elif self.remaining == 0:
            QMessageBox.information(self, "Game Over", f"😢 You lost! The number was {self.num}.")
            self.reset_game()
        elif guess < self.num:
            if guess >= self.num - 5:
                self.result_label.setText(f"Low but close! Attempts left: {self.remaining}")
            else:
                self.result_label.setText(f"Too low! Attempts left: {self.remaining}")
        else:
            if guess <= self.num + 5:
                self.result_label.setText(f"High but close! Attempts left: {self.remaining}")
            else:
                self.result_label.setText(f"Too high! Attempts left: {self.remaining}")

    def reset_game(self):
        self.check_btn.setEnabled(False)
        self.guess_input.clear()
        self.result_label.setText("Game Over! Start again.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GuessGame()
    window.show()
    sys.exit(app.exec_())
