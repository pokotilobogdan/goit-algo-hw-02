from queue import Queue
import random
import keyboard
import time

queue = Queue()

def generate_request():
    # Створюватимемо від 0 до 2 запитів, щоб цікавіше було. В середньому все одно 1 запит, але так є шанси побачити повідомлення про порожню чергу
    n = random.randint(0, 2)
    for _ in range(n):
        new_request = hash(random.random())
        queue.put(new_request)

def process_request():
    if queue.empty() == False:
        print("Обслуговуємо заявку {}".format(queue.get()))
        print(f"Requests left: {queue.qsize()}\n")
    else:
        print("queue is empty\n")

while True:
    
#     Щоб вийти з циклу, необхідно натискати кнопку Esc протягом 1 секунди!

    if keyboard.is_pressed('Esc'):
        break
    else:
        time.sleep(0.5)
        generate_request()
        time.sleep(0.5)
        process_request()
