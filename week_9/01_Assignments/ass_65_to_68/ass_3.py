# التكليف 03

word_count = 0
lines_number = 0
char_count = 0
letter_count = 0
with open("file_1.txt", "r") as f:
    print("-" * 30)
    file_lines = f.readlines()
    lines_number = len(file_lines)
    print(f"lines_number: {lines_number}")
    for line in file_lines:
        words = line.split()
        word_count += len(words)
        for w in words:
            char_count += len(w)
            for ch in w:
                if ch.lower() == "l":
                    letter_count += 1

    print(f"word_count: {word_count}")
    print(f"char_count: {char_count}")
    print(f"letter_count: {letter_count}")
