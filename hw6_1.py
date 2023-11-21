string = input('Введите строку: ')
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
new_str = ''
for i in range(len(string)):
    if string[i] in small_letters:
        for j in range(len(small_letters)):
            if string[i] == small_letters[j]:
                new_str += big_letters[j]
                break
    else:
        new_str += string[i]

print('Прописные буквы преобразованы в строчные:', new_str)

