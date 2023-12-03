color_dict = {
    "red": "красный",
    "blue": "синий",
    "violet": "фиолетовый",
    "pink": "розовый",
    "green": "зелёный",
    "yellow": "жёлтый",
    "orange": "оранжевый",
    "gray": "серый",
    "white": "белый",
    "black": "чёрный"
}
print("Словарь перевода цветов:")
for key in color_dict:
    print(key,"=", color_dict[key])
last_color = list(color_dict.keys())[-1]
print(f"Перевод последнего слова в словаре:", color_dict[last_color])