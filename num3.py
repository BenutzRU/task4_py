#Создайте функцию, которая принимает аргументы «текст» и «имя файла». Функция должна записать в файл (если файла не существует, то создать его) текст с новой строки.
# Выведите информацию из четных строк файла.


def ent(text, filename):

    with open(filename, "a+") as f:
        words = text.split()


        for word in words:
            f.write(word + "\n")


def pin(filename):
    with open(filename, "r") as f:


        line_num = 0


        for line in f:
            if line_num % 2 == 0:
                print(line.strip())
            line_num += 1

text = input("Text: ")



while True:
    filename = input("File name (.txt): ")
    if filename.endswith(".txt"):
        break
    else:
        print("Error. Имя файла должно оканчиваться на .txt.")

ent(text, filename)
pin(filename)
