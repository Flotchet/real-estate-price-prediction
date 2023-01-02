import re
import pandas as pd
import matplotlib as plt 
from lorem_text import lorem
from nltk.corpus import stopwords

def clean_text_by_regex(text : str , regex_list : str or list[str]) -> str:
    """
    clean a text by a list of regex
    takes a text and a list of regex
    return the text cleaned
    """

    if type(regex_list) == str:
        regex_list = [regex_list]

    for regex in regex_list:
        pattern = re.compile(regex)
        text = re.sub(pattern, "", text)

    return text

def ctbr(text : str , regex_list : str or list[str]) -> str:
    """
    clean a text by a list of regex
    takes a text and a list of regex
    return the text cleaned
    """

    return clean_text_by_regex(text, regex_list)

def remove_html_tags_from_text(text : str) -> str:
    """
    remove all the html tags from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"<.*?>")

def rtft(text : str) -> str:
    """
    remove all the html tags from a text
    takes a text
    return the text cleaned
    """

    return remove_html_tags_from_text(text)

def remove_parenthesis_from_text(text : str) -> str:
    """
    remove all the parenthesis from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"\(.*?\)")

def rpft(text : str) -> str:
    """
    remove all the parenthesis from a text
    takes a text
    return the text cleaned
    """

    return remove_parenthesis_from_text(text)

def remove_braces_from_text(text : str) -> str:
    """
    remove all the braces from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"\{.*?\}")

def rbft(text : str) -> str:
    """
    remove all the braces from a text
    takes a text
    return the text cleaned
    """

    return remove_braces_from_text(text)

def remove_brackets_from_text(text : str) -> str:
    """
    remove all the brackets from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"\[.*?\]")

def rbktft(text : str) -> str:
    """
    remove all the brackets from a text
    takes a text
    return the text cleaned
    """

    return remove_brackets_from_text(text)

def remove_all_types_of_brackets_fror_text(text : str) -> str:
    """
    remove all the brackets from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"\(.*?\)|\[.*?\]|\{.*?\}")

def rabft(text : str) -> str:
    """
    remove all the brackets from a text
    takes a text
    return the text cleaned
    """

    return remove_all_types_of_brackets_fror_text(text)

def remove_new_line_from_text(text : str) -> str:
    """
    remove all the new line from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[\n")

def rnlft(text : str) -> str:
    """
    remove all the new line from a text
    takes a text
    return the text cleaned
    """

    return remove_new_line_from_text(text)

def remove_carriage_return_from_text(text : str) -> str:
    """
    remove all the carriage return from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[\r]")

def rcrft(text : str) -> str:
    """
    remove all the carriage return from a text
    takes a text
    return the text cleaned
    """

    return remove_carriage_return_from_text(text)

def remove_carriage_return_line_feed_from_text(text : str) -> str:
    """
    remove all the carriage return line feed from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[\r\n]")

def rcrnlft(text : str) -> str:
    """
    remove all the carriage return line feed from a text
    takes a text
    return the text cleaned
    """

    return remove_carriage_return_line_feed_from_text(text)

def remove_tab_from_text(text : str) -> str:
    """
    remove all the tab from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[\t]")

def rtabft(text : str) -> str:
    """
    remove all the tab from a text
    takes a text
    return the text cleaned
    """

    return remove_tab_from_text(text)

def remove_non_breaking_space_from_text(text : str) -> str:
    """
    remove all the non breaking space from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[\xa0]")

def rnbsft(text : str) -> str:
    """
    remove all the non breaking space from a text
    takes a text
    return the text cleaned
    """

    return remove_non_breaking_space_from_text(text)

def remove_non_breaking_hyphen_from_text(text : str) -> str:
    """
    remove all the non breaking hyphen from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[\xad]")

def rnbfhft(text : str) -> str:
    """
    remove all the non breaking hyphen from a text
    takes a text
    return the text cleaned
    """

    return remove_non_breaking_hyphen_from_text(text)

def remove_punctuation_characters_from_text(text : str) -> str:
    """
    remove all the punctuation characters from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[^\w\s]")

def rpcft(text : str) -> str:
    """
    remove all the punctuation characters from a text
    takes a text
    return the text cleaned
    """

    return remove_punctuation_characters_from_text(text)

def remove_numbers_from_text(text : str) -> str:
    """
    remove all the numbers from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"\d")

def rnumft(text : str) -> str:
    """
    remove all the numbers from a text
    takes a text
    return the text cleaned
    """

    return remove_numbers_from_text(text)

def remove_multiple_spaces_from_text(text : str) -> str:
    """
    remove all the multiple spaces from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"\s+")

def rmspft(text : str) -> str:
    """
    remove all the multiple spaces from a text
    takes a text
    return the text cleaned
    """

    return remove_multiple_spaces_from_text(text)

def remove_special_character_from_text(text : str) -> str:
    """
    remove all the special character from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[^a-zA-Z0-9]")

def rscft(text : str) -> str:
    """
    remove all the special character from a text
    takes a text
    return the text cleaned
    """

    return remove_special_character_from_text(text)

def remove_control_character_from_text(text : str) -> str:
    """
    remove all the control character from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[\x00-\x1F\x7F]")

def rccft(text : str) -> str:
    """
    remove all the control character from a text
    takes a text
    return the text cleaned
    """

    return remove_control_character_from_text(text)

def remove_all_non_alphanumeric_characters_from_text(text : str) -> str:
    """
    remove all the non alphanumeric characters from a text
    takes a text
    return the text cleaned
    """

    return clean_text_by_regex(text, r"[^a-zA-Z0-9\s]")

def rnaacft(text : str) -> str:
    """
    remove all the non alphanumeric characters from a text
    takes a text
    return the text cleaned
    """

    return remove_all_non_alphanumeric_characters_from_text(text)

def remove_stop_words_from_text(text : str, stop_words : list[str]) -> str:
    """
    remove all the stop words from a text
    takes a text and a list of stop words
    return the text cleaned
    """

    return " ".join([word for word in text.split() if word not in stop_words])

def rswft(text : str, stop_words : list[str]) -> str:
    """
    remove all the stop words from a text
    takes a text and a list of stop words
    return the text cleaned
    """

    return remove_stop_words_from_text(text, stop_words)

def get_stop_words(language : str) -> list[str]:
    """
    get the stop words of a language
    takes a language
    return a list of stop words
    """

    return stopwords.words(language)

def remove_stop_words_from_text_by_language(text : str, language : str) -> str:
    """
    remove all the stop words from a text by language
    takes a text and a language
    return the text cleaned
    """

    return remove_stop_words_from_text(text, get_stop_words(language))

def rswftbl(text : str, language : str) -> str:
    """
    remove all the stop words from a text by language
    takes a text and a language
    return the text cleaned
    """

    return remove_stop_words_from_text_by_language(text, language)

def dictionary_of_frequency_of_words(text : str) -> dict[str : int]:
    """
    return a dictionary of the frequency of words in a cleaned text
    takes a text
    return a dictionary
    """

    return dict(pd.Series(text.split()).value_counts())

def dict_of_w_f(text : str) -> dict[str : int]:
    """
    return a dictionary of the frequency of words in a cleaned text
    takes a text
    return a dictionary
    """

    return dictionary_of_frequency_of_words(text)

def dictionary_of_frequency_of_words_in_a_list_of_text(
    list_of_text : list[str]) -> dict[str : int]:
    """
    return a dictionary of the frequency of words in a list of cleaned text
    takes a list of text
    return a dictionary
    """

    return dictionary_of_frequency_of_words(" ".join(list_of_text))

def dict_of_w_f_in_a_lot(text : list[str]) -> dict[str : int]:
    """
    return a dictionary of the frequency of words in a list of cleaned text
    takes a list of text
    return a dictionary
    """

    return dictionary_of_frequency_of_words_in_a_list_of_text(text)

def bar_plot_of_words_frequencies(
    words : dict[str : int] or list[list[str], list[int]]) -> None:
    """
    plot a bar plot of the frequency of words
    takes a dictionary of words and their frequency 
    or a list of words and a list of their frequency
    return a bar plot
    """

    if type(words) == dict:
        words = list(words.items())

    words = sorted(words, key=lambda x: x[1], reverse=True)

    words = list(zip(*words))

    plt.bar(words[0], words[1])

    return None

def main():
    lorem_text = lorem.words(10_000)
    list_of_lorem_text = [lorem.words(10_000) for _ in range(10)]

    #test functions
    print(rtft(lorem_text))
    print(rnumft(lorem_text))
    print(rmspft(lorem_text))
    print(rscft(lorem_text))
    print(rccft(lorem_text))
    print(rnaacft(lorem_text))
    print(rswft(lorem_text, get_stop_words("english")))
    print(rswftbl(lorem_text, "english"))
    print(dict_of_w_f(lorem_text))
    print(dict_of_w_f_in_a_lot(list_of_lorem_text))
    bar_plot_of_words_frequencies(dict_of_w_f(lorem_text))

if __name__ == "__main__":
    main()



    





