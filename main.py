from data_source import fetch_text
from text_edit import full_clean
from text_analysis import word_frequencies, top_words, summary
from text_visualization import show_bar_chart

def main():
    # The two books chosen from Project Gutenberg
    pride_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
    oliver_url = "https://www.gutenberg.org/cache/epub/730/pg730.txt"

    # Downloading books
    print("Downloading books...")
    pride_text = fetch_text(pride_url)
    oliver_text = fetch_text(oliver_url)

    # Text cleaning
    pride_words, pride_sentences = full_clean(pride_text)
    oliver_words, oliver_sentences = full_clean(oliver_text)

    # book analysis
    pride_counts = word_frequencies(pride_words)
    oliver_counts = word_frequencies(oliver_words)

    # Visualization
    print("\n--- Pride and Prejudice ---")
    pride_stats = summary(pride_words, pride_sentences)
    print(pride_stats)
    show_bar_chart(top_words(pride_counts, 10))

    print("\n--- Oliver Twist ---")
    oliver_stats = summary(oliver_words, oliver_sentences)
    print(oliver_stats)
    show_bar_chart(top_words(oliver_counts, 10))
    
    #Comparing the two books
    from text_analysis import compare_books
    compare_books(pride_counts, oliver_counts)

if __name__ == "__main__":
    main()
