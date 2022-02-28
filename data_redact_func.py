import nltk
import requests
import en_core_web_sm
import re

nlp = en_core_web_sm.load()
regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
regex_phone = re.compile("^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$", re.IGNORECASE)
regex_zip = re.compile("(^\d{5}$)|(^\d{9}$)|(^\d{5}-\d{4}$)", re.IGNORECASE)


def remove_phone_zip(input_str):
    str_arr = input_str.split()
    for i in range(len(str_arr)):
        if re.match(regex_phone, str_arr[i]) or re.match(regex_zip, str_arr[i]):
            str_arr[i] = "REDACT"
    str_return = " ".join(str_arr)
    return str_return


def main(input_str):
    nlp_str = [(x.orth_, x.pos_, x.lemma_, x.ent_type_) for x in [y
                                                                  for y
                                                                  in nlp(input_str)]]
    n = len(nlp_str)
    i = 0
    while i < n:
        if nlp_str[i][3] == 'PERSON':
            person_name = nlp_str[i][0].capitalize()
            k = 0
            for j in range(i + 1, len(nlp_str)):
                if nlp_str[j][3] == 'PERSON':
                    person_name += "_" + nlp_str[j][0].capitalize()
                    k += 1
                else:
                    i = j - 1
                    break

            response = requests.get(url="https://en.wikipedia.org/wiki/" + person_name)
            if not response.status_code == 200:
                nn = person_name.replace("_", " ")
                input_str = input_str.replace(nn, "REDACT")
        elif nlp_str[i][3] == 'GPE':
            input_str = input_str.replace(nlp_str[i][0], "REDACT")
        elif "@" in nlp_str[i][0]:
            if re.fullmatch(regex_email, nlp_str[i][0]):
                input_str = input_str.replace(nlp_str[i][0], "REDACT")
        i += 1
    input_str = remove_phone_zip(input_str)
    print("final: ", input_str)


main()
