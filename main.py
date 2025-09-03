import sys
from stats import get_num_words, get_char_counts, sort_char_counts


def get_book_text(filepath):
	with open(filepath, "r") as f:
		return f.read()


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)


	filepath = sys.argv[1]
	book_text = get_book_text(filepath)

	num_words = get_num_words(book_text)

	char_counts = get_char_counts(book_text)
	sorted_counts = sort_char_counts(char_counts)

	print("=========== BOOKBOT ===========")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for entry in sorted_counts:
		print(f"{entry['char']}: {entry['num']}")
	print("============= END ===============")


if __name__ == "__main__":
    main()
