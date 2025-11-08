def word_frequencies(words):
    """Count how many times each word appears."""
    counts = {}
    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1
    return counts

def top_words(counts, number=10):
    """Return the top N most common words."""
    items = list(counts.items())

    items.sort(key=lambda x: x[1], reverse=True)
    return items[:number]

def summary(words, sentences):
    """Give simple info about the text."""
    total_words = len(words)
    unique_words = len(set(words))
    average_word_length = sum(len(w) for w in words) / total_words
    average_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)

    stats = {
        "Total words": total_words,
        "Unique words": unique_words,
        "Average word length": round(average_word_length, 2),
        "Average sentence length": round(average_sentence_length, 2)
    }
    return stats

def compare_books(counts1, counts2):
    """Compare how similar two books are using simple word overlap."""
    # Get the sets of words from both books
    words1 = set(counts1.keys())
    words2 = set(counts2.keys())

    # Count how many words appear in both books
    common_words = words1.intersection(words2)
    total_words = len(words1.union(words2))

    # Compute a simple similarity score (percentage)
    similarity = (len(common_words) / total_words) * 100

    print("\n--- Comparison Between the Two Books ---")
    print("Words in first book:", len(words1))
    print("Words in second book:", len(words2))
    print("Words in common:", len(common_words))
    print(f"Similarity: {similarity:.2f}%")
