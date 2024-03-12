from src import MaleSinger, Melody


def main() -> None:
    melody = Melody.random_from_words(
        "Danielle, My Love, I want you to know that I love you very much!")
    MaleSinger().sing(melody)


if __name__ == "__main__":
    main()
