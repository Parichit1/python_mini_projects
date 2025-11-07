import random

common_french_words = [
    {"french": "le", "english": "the (masc.)"},
    {"french": "la", "english": "the (fem.)"},
    {"french": "les", "english": "the (plural)"},
    {"french": "un", "english": "a/an (masc.)"},
    {"french": "une", "english": "a/an (fem.)"},
    {"french": "et", "english": "and"},
    {"french": "ou", "english": "or"},
    {"french": "mais", "english": "but"},
    {"french": "oui", "english": "yes"},
    {"french": "non", "english": "no"},
    {"french": "je", "english": "I"},
    {"french": "tu", "english": "you (informal)"},
    {"french": "il", "english": "he"},
    {"french": "elle", "english": "she"},
    {"french": "nous", "english": "we"},
    {"french": "vous", "english": "you"},
    {"french": "ils", "english": "they (masc.)"},
    {"french": "elles", "english": "they (fem.)"},
    {"french": "être", "english": "to be"},
    {"french": "avoir", "english": "to have"},
    {"french": "aller", "english": "to go"},
    {"french": "faire", "english": "to do / make"},
    {"french": "dire", "english": "to say"},
    {"french": "voir", "english": "to see"},
    {"french": "venir", "english": "to come"},
    {"french": "prendre", "english": "to take"},
    {"french": "donner", "english": "to give"},
    {"french": "manger", "english": "to eat"},
    {"french": "boire", "english": "to drink"},
    {"french": "savoir", "english": "to know"},
    {"french": "voudre", "english": "to want"},
    {"french": "pouvoir", "english": "to be able to"},
    {"french": "devoir", "english": ["to have to", "must"]},
    {"french": "parler", "english": "to speak"},
    {"french": "aimer", "english": ["to like", "love"]},
    {"french": "penser", "english": "to think"},
    {"french": "mettre", "english": "to put"},
    {"french": "trouver", "english": "to find"},
    {"french": "donc", "english": ["so", "therefore"]},
    {"french": "parce que", "english": "because"},
    {"french": "quand", "english": "when"},
    {"french": "où", "english": "where"},
    {"french": "comment", "english": "how"},
    {"french": "pourquoi", "english": "why"},
    {"french": "avec", "english": "with"},
    {"french": "sans", "english": "without"},
    {"french": "sous", "english": "under"},
    {"french": "sur", "english": ["on", "over"]},
    {"french": "dans", "english": "in"},
    {"french": "entre", "english": "between"},
    {"french": "avant", "english": "before"},
    {"french": "après", "english": "after"},
    {"french": "toujours", "english": "always"},
    {"french": "souvent", "english": "often"},
    {"french": "jamais", "english": "never"},
    {"french": "maintenant", "english": "now"},
    {"french": "aujourd'hui", "english": "today"},
    {"french": "demain", "english": "tomorrow"},
    {"french": "hier", "english": "yesterday"},
    {"french": "très", "english": "very"},
    {"french": "beaucoup", "english": "a lot"},
    {"french": "peu", "english": "a little"},
    {"french": "plus", "english": "more"},
    {"french": "moins", "english": "less"},
    {"french": "bon", "english": "good"},
    {"french": "mauvais", "english": "bad"},
    {"french": "grand", "english": ["big", "tall"]},
    {"french": "petit", "english": ["small ", " little"]},
    {"french": "jeune", "english": "young"},
    {"french": "vieux", "english": "old"},
    {"french": "nouveau", "english": "new"},
    {"french": "premier", "english": "first"},
    {"french": "dernier", "english": "last"},
    {"french": "homme", "english": "man"},
    {"french": "femme", "english": "woman"},
    {"french": "garçon", "english": "boy"},
    {"french": "fille", "english": "girl"},
    {"french": "ami", "english": "friend"},
    {"french": "amour", "english": "love"},
    {"french": "famille", "english": "family"},
    {"french": "maison", "english": "house"},
    {"french": "école", "english": "school"},
    {"french": "travail", "english": ["work", "job"]},
    {"french": "ville", "english": "city"},
    {"french": "rue", "english": "street"},
    {"french": "voiture", "english": "car"},
    {"french": "livre", "english": "book"},
    {"french": "eau", "english": "water"},
    {"french": "pain", "english": "bread"},
    {"french": "fromage", "english": "cheese"},
    {"french": "café", "english": "coffee"},
    {"french": "thé", "english": "tea"},
    {"french": "lait", "english": "milk"},
    {"french": "temps", "english": ["time", "weather"]},
    {"french": "jour", "english": "day"},
    {"french": "nuit", "english": "night"},
    {"french": "matin", "english": "morning"},
    {"french": "soir", "english": "evening"},
    {"french": "année", "english": "year"},
    {"french": "semaine", "english": "week"},
    {"french": "heure", "english": "hour"},
    {"french": "minute", "english": "minute"}
]


def quiz():
    print("How many questions you would like to get?")
    question_asked = int(input("Your answer: "))

    selected_words = random.sample(common_french_words, question_asked)
    score = 0
    for word in selected_words:
        print(
            f"What is the english tanslation of {word['french']} ?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word["english"].lower()

        if user_answer == correct_answer:
            print("That was correct!")
            score += 1
        else:
            print(
                f"That was incorrect, the correct answer was {word['english']}")

    print(f"Your total score is {score}/ {question_asked}")


def main():
    print("Hello and Welcome to French quiz, \n Here we will be asking you most common 100 french words")
    quiz()


main()
