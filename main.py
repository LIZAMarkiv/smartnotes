from PyQt6.QtWidgets import*

app = QApplication([])
window = QWidget()
notes_text = QTextEdit()
app.setStyleSheet("""
   QWidget {
            background-color: #2E3440;
            color: #D8DEE9;
            font-family: Arial;
            font-size: 14px;
        }

        QLabel {
            font-weight: bold;
        }

        QPushButton {
            background-color: #5E81AC;
            color: white;
            border-radius: 5px;
            padding: 6px;
        }

        QPushButton:hover {
            background-color: #81A1C1;
        }

        QLineEdit, QTextEdit, QListWidget {
            background-color: #3B4252;
            border: 1px solid #4C566A;
            border-radius: 3px;
            padding: 4px;
        }
    """)


notes_list_lbl = QLabel("список заміток")
notes_list = QListWidget()
notes_list2 = QListWidget()
knopka1 = QPushButton("Створити замітку")
knopka2 = QPushButton("Видалити замітку")
knopka3 = QPushButton("Зберегти замітку")
nadpus = QLabel("Список тегів")
knopka4 = QPushButton("Додати до замітки")
knopka5 = QPushButton("Відкріпити від замітки")
knopka6 = QPushButton("шукати замітки по тегу")
text = QLineEdit()
text.setPlaceholderText("Введіть тег...")
main_line = QHBoxLayout()
v1 = QVBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
main_line.addWidget(notes_text)
v1.addWidget(notes_list_lbl)
v1.addWidget(notes_list)
h2.addWidget(knopka1)
h2.addWidget(knopka2)


v1.addLayout(h2)
v1.addWidget(knopka3)
v1.addWidget(nadpus)
v1.addWidget(notes_list2)
v1.addWidget(text)


h3.addWidget(knopka4)
h3.addWidget(knopka5)
v1.addLayout(h3)
v1.addWidget(knopka6)




main_line.addLayout(v1)


window.setLayout(main_line)
window.show()
app.exec()

