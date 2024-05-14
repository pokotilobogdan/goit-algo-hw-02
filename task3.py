# Відповідні дужки стоять на відповідних місцях в рядку. Це потрібно для перевірки на симетричність

left_brakets = r"([{"
right_brakets = r")]}"

def is_brakets_sym(string):
    
    stack_left = []     # Додаємо сюди тільки ліві дужки. Якщо з'являється непарна права, то дужки несиметричні
    
    for char in string:
        if char in left_brakets+right_brakets:
        
            # Обробляємо перший символ (можливо вдасться цього позбутись)

            if len(stack_left) == 0 and char in right_brakets:
                return "Несиметрично"
            elif len(stack_left) == 0 and char in left_brakets:
                stack_left.append(char)
                continue
        
            # Перевіряємо дужка права чи ліва:
        
                # Якщо ліва, то додаємо до стеку.
                # Якщо права і симетрична останній в стеку, то видаляємо відповідну зі стеку.
                # Якщо несиметрична, повертаємо результат.
        
            if char in left_brakets:
                stack_left.append(char)
                continue
            elif char in right_brakets and left_brakets.index(stack_left[-1]) == right_brakets.index(char):
                stack_left.pop()
                continue
            else:
                return "Несиметрично"
        
        # Якщо в кінці стек порожній, то всі дужки виявились симетричними. Інакше - несиметричними
        
    if len(stack_left) == 0:
        return "Симетрично"
    else:
        return "Несиметрично"

while True:
    string = input("Введіть рядок з дужками та іншими символами: ")

    if string in ["exit", "quit", "close"]:
        break
    else:
        print(is_brakets_sym(string))
        print()
