

class PossibilitiesGenerator:

    LETTERS = 28
    NUMBERS = 10

    @staticmethod
    def generate(nb_characters, lower_case = False, upper_case = False, numbers = False):
        nb_possibilities = 0
        if lower_case:
            for i in range(0, nb_characters):
                nb_possibilities += PossibilitiesGenerator.LETTERS
        if upper_case:
            for i in range(0, nb_characters):
                nb_possibilities += PossibilitiesGenerator.LETTERS
        if numbers:
            for i in range(0, nb_characters):
                nb_possibilities += PossibilitiesGenerator.NUMBERS

        return nb_possibilities


