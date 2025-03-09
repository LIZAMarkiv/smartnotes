from PyQt6.QtWidgets import*
from file_meneger import*

notes = read_from_file()
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
notes_list.addItems(notes)
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


def show_notes():
    key = notes_list.currentItem().text()
    notes_text.setText(notes[key]["текст"])
    notes_list2.clear()
    notes_list2.addItems(notes[key]["теги"])


def add_note():
    note_name, ok = QInputDialog.getText(window, "Нова нотатка", "Введіть назву нотатки")
    if ok == True:
        notes[note_name] = {
            "текст": "",
            "теги": [

            ]
        }
        notes_list.clear()
        notes_list.addItems(notes)
        write_in_file(notes)

def save_note_funk():
    text = notes_text.toPlainText()
    note_key = notes_list.currentItem().text()
    notes[note_key]["текст"] = text
    write_in_file(notes)



def add_teg():
    teg_name, ok = QInputDialog.getText(window, "Новий тег", "Введіть назву тегу")
    if ok == True:
        notes[teg_name] = {
            "текст": "",
            "теги": [

            ]
        }
        


def delete_note():

    note_key = notes_list.currentItem().text()
    notes.pop(note_key)
    notes_list.clear()
    notes_list.addItems(notes)
    write_in_file(notes)



knopka2.clicked.connect(delete_note)
knopka3.clicked.connect(save_note_funk)
knopka4.clicked.connect(add_note)
notes_list.itemClicked.connect(show_notes)

window.setLayout(main_line)
window.show()
app.exec()

