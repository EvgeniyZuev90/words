import random


with open('words.txt', 'r', encoding='utf-8') as f:
    words_list = f.read().splitlines()

while True:
    word = random.choice(words_list)
    length_word = len(word)
    display_word = ['_'] * length_word
    print("Загаданное слово:", " ".join(display_word))

    print("Выберите уровень сложности:")
    print("1 — Легкий (10 жизней)")
    print("2 — Средний (6 жизней)")
    print("3 — Хардкор (3 жизни)")

    choice = input("Введите номер уровня: ")

    if choice == '1':
        lives = 10
    elif choice == '2':
        lives = 6
    elif choice == '3':
        lives = 3
    else:
        print("Неверный ввод, по умолчанию выбрано 6 жизней.")
        lives = 6

        
    used_letters = []


    while lives > 0 and '_' in display_word:
        print(f'\nОсталось жизней: {lives}')
        print(' '.join(display_word))

        guess = input('Введите букву: ').lower()
        
        if guess == '?':
            if lives < 1:
                print('Вы не можете взять подсказку, у вас не хватает жизней')
                continue

            indices = []
            for i in range (len(word)):
                if display_word[i] == '_':
                    indices.append(i)
            if indices:        
                random_index = random.choice(indices)
                display_word[random_index] = word[random_index]
                lives = lives - 1
                used_letters.append(word[random_index])
                print('Подсказка использована!')
                continue    
        
        
        if not guess.isalpha():
            print('Ошибка, нужно ввести букву')
            continue
        if len(guess)!=1:
            print('Ошибка, можно ввести только одну букву')
            continue
        



        if guess in used_letters:
            print('Вы уже вводили эту букву')
            print(used_letters)
            continue
        else:
            used_letters.append(guess)

        if guess not in word:
            lives = lives - 1
            print('Такой буквы нет в этом слове')

        else:
            for i in range(len(word)):
                if guess == word[i]:
                    display_word[i] = guess



    if '_' not in display_word:
        print(f'Поздравляю вы отгдали слово: {word}')

    else:
        print('К сожалению вы проиграли')

    play_again = input("\nХотите сыграть еще раз? (да/нет): ").lower()
    if play_again != 'да':
        print("Спасибо за игру! До встречи.")
        break
            
