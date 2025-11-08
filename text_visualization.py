def show_bar_chart(items):
    """Print bars made of stars for the top words."""
    print("Word Frequency Chart:")
    for word, count in items:
        bar = "*" * (count // 10)
        print(f"{word:>12}: {bar}")
