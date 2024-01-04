import time
import random
import string
def generate_random_text(length):
    return ''.join(random.choices(string.ascii_letters+string.whitespace,k=length))
def calculate_words_per_minute(text,typed_text,elapsed_time):
    words_typed=len(typed_text.split())
    minutes=elapsed_time/60
    words_per_minute=words_typed/minutes if minutes>0 else 0
    return round(words_per_minute)
def typing_speed_test():
    print("Welcome to the Typing Speed Tester!!!")
    print("You will be presented with a random sentence to type..")
    print("Type the sentance as soon as possible")
    print("Press Enter when You're ready to start...")
    input("")
    random_text=generate_random_text(30)
    print(f"\n Type this: {random_text}\n")
    start_time=time.time()
    typed_text=input("Start Typing here:")
    end_time=time.time()
    elapsed_time=end_time-start_time
    words_per_minute=calculate_words_per_minute(random_text,typed_text,elapsed_time)
    print(f"\n You typed at {words_per_minute} words per minute.")
if __name__=="__main__":
    typing_speed_test()