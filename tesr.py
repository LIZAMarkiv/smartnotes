notes = {
    "Замітка 1": {
        "текст": "певний текст",
        "теги": [
            "тег1",
            "тег2"
        ]
    },
    "Замітка 2": {
        "текст": "певний",
        "теги": [
            "тег3",
            "тег4"
        ]
    }
}
notes["Замітка 1"]["теги"].remove()

print(notes["Замітка 2"]["текст"])