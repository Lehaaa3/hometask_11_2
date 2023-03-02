def entitle(text):
    """
    function return text with eachh letter in word capital
    :return: str
    """
    big_text = text.upper()
    return big_text

def big_first_letter(text):
    """
    function return text with first letter in word capital
    :return: str
    """
    word_list = []
    word_list = text.split(" ")
    new_string = " ".join(word_list).title()
    return new_string

