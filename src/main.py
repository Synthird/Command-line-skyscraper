def ask_question(question: str, prompt: str) -> str:
    print(f"--- {question} ---")
    try:
        answer: int = int(input(f"{prompt}: "))
        return answer
    except:
        print("Cannot print a skyscraper!")
        print("Probably because you entered:")
        print("a) Decimals\nb) Letters\nc) Symbols\nd) Spaces between numbers")
        raise SystemExit


def print_multiple_times(message: str, iterations: int) -> None:
    for _ in range(iterations):
        print(message)


floors: int = ask_question(
    "How many floors do you want in your skyscraper?", "Floors")

rod_dots: int = ask_question(
    "How tall do you want your lightning rod to be?", "Number of dots for the rod")

print_multiple_times("   .", rod_dots)
print_multiple_times(".......", floors)
