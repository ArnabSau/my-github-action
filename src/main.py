import random

def tell_a_joke():
    jokes = [
        "Why did the computer show up at work late? It had a hard drive!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the Python programmer wear glasses? Because they couldn't C!",
        "How do you comfort a JavaScript bug? You console it.",
        "Why was the math book sad? Because it had too many problems."
    ]
    print(random.choice(jokes))

if __name__ == "__main__":
    tell_a_joke()