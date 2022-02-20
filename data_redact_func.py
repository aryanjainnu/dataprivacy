import nltk
import requests
import en_core_web_sm


nlp = en_core_web_sm.load()


def main():
    input_str = input("Please input a string: ")
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

            response = requests.get(url="https://en.wikipedia.org/wiki/" + person_name, )
            if not response.status_code == 200:
                nn = person_name.replace("_", " ")
                input_str = input_str.replace(nn, "REDACT")
        elif nlp_str[i][3] == 'GPE' or nlp_str[i][1] == 'NUM':
            input_str = input_str.replace(nlp_str[i][0], "REDACT")
        i += 1
    print("final: ", input_str)


main()
