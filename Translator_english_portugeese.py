# Question: Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using the following
# dictionary as a vocabulary source.
# d = dict(weather = "clima", earth = "terra", rain = "chuva")
# Expected output:
# Enter word: earth
# terra

# d = dict(weather="clima", earth="terra", rain="chuva")
#
#
# def translator(user_input):
#     try:
#         return d[user_input]
#     except:
#         return "not exist"
#
#
# user_input = input("enter word to translate. weather/earth/rain ...    ")
# print("The portuguese word for the english word ", user_input, "is: ", translator(user_input))


# Question: Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using the following dictionary
# as a vocabulary source. Also, return the message, "We couldn't find that word!"
# when the user enters a word that is not in the dictionary. Also, make the program non-case-sensitive,
# meaning that, for example, both earth and Earth should return the translation correctly for that word.

d1 = dict(weather="clima", earth="terra", rain="chuva")


def translator_ignore_case(user_input1):
    try:
        return d1[user_input1]
    except:
        return "not exist"


user_input1 = input("enter word to translate. weather/earth/rain ...    ").lower()
print("The portuguese word for the english word ", user_input1, "is: ", translator_ignore_case(user_input1))
