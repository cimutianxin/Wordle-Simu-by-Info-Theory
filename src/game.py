import random


# 加载单词列表
def load_words(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()


# 生成反馈
def generate_feedback(guess, target):
    feedback = []
    for g_char, t_char in zip(guess, target):
        if g_char == t_char:
            feedback.append("g")
        elif g_char in target:
            feedback.append("y")
        else:
            feedback.append("-")
    return "".join(feedback)


# 彩色显示反馈
def colorful_feedback(feedback, guess):
    colored_result = ""
    for char, fb in zip(guess, feedback):
        if fb == "g":
            colored_result += f"\033[38;2;0;255;0m{char}\033[0m"  # 绿色 RGB (0, 255, 0)
        elif fb == "y":
            colored_result += f"\033[38;2;255;255;0m{char}\033[0m"  # 黄色 RGB (255, 255, 0)
        else:
            colored_result += f"\033[38;2;0;0;0;0m{char}\033[0m"  # 红色 RGB (255, 0, 0)
    return colored_result


# 控制台版 Wordle 游戏
def play_wordle(word_list):
    target = random.choice(word_list)
    max_attempts = 99
    attempts = 0

    print("Welcome to Wordle!")
    print(f"You have {max_attempts} attempts to guess the 5-letter word.\n")

    while attempts < max_attempts:
        guess = input("Enter your guess: ").strip().lower()

        if len(guess) != 5 or guess not in word_list:
            print("Invalid guess. Please enter a 5-letter word from the word list.\n")
            continue

        attempts += 1
        feedback = generate_feedback(guess, target)
        feedback = colorful_feedback(feedback, guess)
        print(f"Feedback: {feedback}\n")

        if feedback == "ggggg":
            print(f"Congratulations! You've guessed the word '{target}' in {attempts} attempts.")
            return

    print(f"Sorry, you've used all your attempts. The word was '{target}'.")


if __name__ == "__main__":
    # 使用短单词列表测试
    word_list_file = "data/allowed_words.txt"
    word_list = load_words(word_list_file)
    play_wordle(word_list)
