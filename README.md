1. Project Overview

For this project, I explored how to analyze text using Python by working with two public-domain books from Project Gutenberg: Pride and Prejudice by Jane Austen and Oliver Twist by Charles Dickens. I wanted to learn how to get real text from the internet, clean it, and use Python to find patterns. My main goal was to count word frequencies, show the most common words, and compare the two books to see how similar their vocabularies are. I also wanted to understand how simple code can be used to find meaningful insights from large pieces of writing.

2. Implementation

I built this project using only basic Python, without relying on heavy external libraries. The system has a few small files that each handle a specific task:
data_source.py downloads the text from Project Gutenberg using urllib.

* text_edit.py lowercases the text, removes punctuation and common stopwords, and splits it into words and sentences.

* text_analysis.py counts how many times each word appears, finds top words, and calculates statistics such as total words, unique words, and average word length. It also includes a simple book comparison feature that measures how many words both books share.

* text_visualization.py prints easy-to-read bar charts using stars (*) to represent word frequencies.

* main.py brings everything together and runs the full analysis.

I used dictionaries for word counting because they are simple and fast for storing and updating counts. Lists were used for storing words and sentences. One design choice I made was to avoid using libraries like NLTK or pandas because the goal was to practice writing basic logic in pure Python. This made the code easier to understand and run without setup issues.
During development, I used AI tools like ChatGPT to help me learn how to organize multiple files, handle cleaning steps, and fix errors when something didn’t run correctly. I also learned how to write clear comments and test functions step by step.

3. Results

When I ran the program, I was able to:
Download both books directly from the web.

Clean and process each book into a list of words and sentences.

Print statistics such as the total number of words, unique words, and average word and sentence lengths.

Show the top 10 most frequent words in each book with star bar charts.
The two novels shared about 36% of their vocabulary, showing that while both are written in similar English, they have many differences in style, topics, and characters. This simple metric helped me see that word analysis can capture real differences between authors.

4. Reflection

* Process reflection:

Overall, the project went very smoothly once I understood how to break it into smaller files. The hardest part was cleaning the text and removing stopwords correctly without any libraries. I solved this by testing small pieces of code and printing results often. It was rewarding to see that even with very basic tools, Python can process large amounts of text and reveal meaningful patterns.

If I had more time, I would try adding more books and maybe build a small graph comparing all their similarities. I also learned how important it is to test after each change instead of writing everything at once.
Learning reflection:
 
My biggest takeaway was that you don’t need advanced tools to start doing data analysis because logic and structure matter can help a lot more as well. This project helped me understand how data moves step by step: From downloading to cleaning to analyzing and then visualizing. AI tools like ChatGPT helped me learn faster, especially when I got stuck with syntax errors or needed help explaining new concepts. I also learned to verify the code and understand every line instead of just copying it. Going forward, I plan to use these same techniques for other projects that involve reading and analyzing text or data from the web.


