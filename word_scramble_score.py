# Word Scramble Score
# 
# A popular item in the local paper is the word scramble. In this puzzle, a reader is presented with a series
# of letters that are for a scrambled word, e.g. “rwod” can be unscrambled to “word”. Your job is to write
# a program that will score the difficulty of any particular scrambling of a word. The scores can be not,
# poor, fair or hard, depending on whether or not the scramble is not scrambled, easy to solve, a
# reasonable difficulty to solve or hard to solve, respectively.
# 
# Your solution will be evaluated for correctness, code quality, design & extensibility, and its testability.
# 
# Word scrambles can be judged by a set of heuristics including if the word looks real or if the scramble
# has letters in the correct place. A scramble looks like a real word if the letters alternate between vowels
# and consonants (with ‘Y’ being a vowel for this purpose). However, certain combinations of vowels and
# consonants are allowed:
# 
# AI AY EA EE EO IO OA OO OY YA
# YO YU BL BR CH CK CL CR DR FL
# FR GH GL GR KL KR KW PF PL PR
# SC SCH SCR SH SHR SK SL SM SN SP
# SQ ST SW TH THR TR TW WH WR
# 
# Also, all double consonants are allowed, and, no other combinations are allowed. For instance, SWR
# doesn’t look real even though both SW and WR are independently looking real.
# 
# Word classifications:
# • Not – if the word is not scrambled at all
# • Poor – if the first letter or any two consecutive letters are in the correct place and the word
#          doesn’t look real
# • Hard – if none of the letters are in the correct place and the word looks real
# • Fair – for all other cases
# 
# INPUT
# A list where each element is a scramble followed by a space followed by the actual word. The
# characters are expected to be in upper case.
# 
# OUTPUT
# • For not – “<scrambled> is not a scramble of <word>”
# • For poor – “<scrambled> is a poor scramble of <word>”
# • For fair – “<scrambled> is a fair scramble of <word>”
# • For hard – “<scrambled> is a hard scramble of <word>”
# 
# SAMPLE INPUT:
# MAPS SPAM
# RIONY IRONY
# ONYRI IRONY
# IRONY IRONY
# INOYR IRONY
# IOYRN IRONY
# 
# EXPECTED OUTPUT:
# MAPS is a fair scramble of SPAM
# RIONY is a fair scramble of IRONY
# ONYRI is a hard scramble of IRONY
# IRONY is not a scramble of IRONY
# INOYR is a fair scramble of IRONY
# IOYRN is a poor scramble of IRONY

from collections import Counter

class WordScrambleScore(object):

    VOWELS = ['A', 'E', 'I', 'O', 'U', 'Y']
    CONSONANTS = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', \
            'S', 'T', 'V', 'W', 'X', 'Z']
    ALLOWED_VOWEL_COMBINATIONS = ['AI', 'AY', 'EA', 'EE', 'EO', 'IO', 'OA', 'OO', 'OY', 'YA', \
            'YO', 'YU']
    ALLOWED_2_CONSONANT_COMBINATIONS = ['BL', 'BR', 'CH', 'CK', 'CL', 'CR', 'DR', 'FL', 'FR', \
            'GH', 'GL', 'GR', 'KL', 'KR', 'KW', 'PF', 'PL', 'PR', 'SC', 'SH', 'SK', 'SL', 'SM', \
            'SN', 'SP', 'SQ', 'ST', 'SW', 'TH', 'TR', 'TW', 'WH', 'WR']
    ALLOWED_3_CONSONANT_COMBINATIONS = ['SCH', 'SCR', 'SHR', 'THR']
    CONSONANT = 'consonant'
    VOWEL = 'vowel'

    def __init__(self):
        self.word = ''
        self.scrambled = ''
        self.looks_like_real_word = False

    def score(self, scrambled:str, word:str) -> None:
        """Given a word and a scrambled instance of word, outputs a difficulty rating for solving the scrambled word.

           The output is a string printed to STDOUT assessing the difficulty of unscrambling the scrambled 
           word. The categories of difficulty are: 'not', 'poor', 'fair', or 'hard'

           scrambled - the scrambled variation of the word which is being assessed for difficulty
           word - the unscrambled word
           return - None
        """
        if not isinstance(word, str) or not isinstance(scrambled, str):
            print('Invalid arguments: method signature is WordScrambleScore.score(str, str)')
            return None

        self.word = word.upper()
        self.scrambled = scrambled.upper()

        self.looks_like_real_word = self._is_vowels_consonants_alternating()
        difficulty = self._score_scrambled_word()
        self._print_difficulty(difficulty)

        return None

    def _score_scrambled_word(self):
        if self._is_not_scramble():
            return 'not'
        if self._is_poor_scramble():
            return 'poor'
        if self._is_hard_scramble():
            return 'hard'
        return 'fair'

    def _is_not_scramble(self):
        if self._word_and_scrambled_are_identical() or self._word_and_scrambled_are_different_words():
            return True

        return False

    def _is_poor_scramble(self):
        # If scrambled looks like a real word then it doesn't meet the requirement for score 'poor'
        if self.looks_like_real_word:
            return False

        # If the first letters of word and scrambled are the same, score as 'poor'
        if self.scrambled[0] == self.word[0]:
            return True

        # If two consecutive letters are in the same place in word and scrambled, score as 'poor'
        i = 1
        while i < len(self.word):
            if self.word[i:i+2] == self.scrambled[i:i+2]:
                return True
            i += 1

        return False

    def _is_hard_scramble(self):
        # If scrambled doesn't look like a real word then it doesn't meet the requirement for score 'hard'
        if not self.looks_like_real_word:
            return False

        # If no letters are in the same place in word and scrambled, score as 'hard'
        i = 0
        while i < len(self.word):
            if self.word[i] == self.scrambled[i]:
                return False
            i += 1

        return True

    def _word_and_scrambled_are_identical(self):
        # Checks if the unscrambled word and scrambled word are the same.
        # return - True if word and scrambled are identical strings, False otherwise.
        if self.word == self.scrambled:
            return True
        else:
            return False

    def _word_and_scrambled_are_different_words(self):
        # The problem statement does not guarantee that the word pairs will be the same word. Since the
        # input pairs could be different words, this function checks to see if the word pairs contain
        # the same letters and the same count of each letter.
        # return - True if word and scrambled are different words, False otherwise.
        word_letter_count = Counter(self.word)
        scrambled_letter_count = Counter(self.scrambled)

        if word_letter_count != scrambled_letter_count:
            return True
        else:
            return False

    def _is_vowels_consonants_alternating(self):
        # Checks if the scrambled word looks like a 'real' word, where vowel and consonant letters
        # alternate. Accounts for allowed vowel and consonant combinations, and for consecutive
        # consonant letters.
        # return - Ture if scrambled follows the heuristic, False otherwise.
        # import ipdb; ipdb.set_trace()
        if self.scrambled[0] in self.VOWELS:
            current_type = self.VOWEL
        else:
            current_type = self.CONSONANT

        i = 0
        while i < len(self.scrambled):
            if current_type == self.VOWEL:
                if self.scrambled[i] not in self.VOWELS:
                    return False
                # Move the index i to the next consonant, accounting for allowed vowel letter combinations
                if self.scrambled[i:i+2] in self.ALLOWED_VOWEL_COMBINATIONS:
                    i += 2
                else:
                    i += 1
                current_type = self.CONSONANT
            else:
                if self.scrambled[i] not in self.CONSONANTS:
                    return False
                # Move the index i to the next vowel, accounting for allowed consonant letter combinations
                if i+3 < len(self.scrambled) and self.scrambled[i:i+3] in self.ALLOWED_3_CONSONANT_COMBINATIONS:
                    i += 3
                elif i+2 < len(self.scrambled) and self.scrambled[i:i+2] in self.ALLOWED_2_CONSONANT_COMBINATIONS:
                    i += 2
                elif i+1 < len(self.scrambled) and self.scrambled[i] == self.scrambled[i+1]:
                    i += 2
                else:
                    i += 1
                current_type = self.VOWEL

        return True

    def _print_difficulty(self, difficulty):
        if difficulty == 'not':
            print('{scrambled} is not a scramble of {word}'.format(
                scrambled=self.scrambled,
                word=self.word
                ))
        else:
            print('{scrambled} is a {difficulty} scramble of {word}'.format(
                scrambled=self.scrambled,
                difficulty=difficulty,
                word=self.word
                ))


if __name__ == '__main__':
    scorer = WordScrambleScore()

    import sys
    import io
    from contextlib import redirect_stdout

    for line in sys.stdin:
        scorer_inputs = line.split()

        if len(scorer_inputs) == 2:             # Standard format of a word scramble file: SCRAMBLE WORD
            scrambled, word = scorer_inputs
            scorer.score(scrambled, word)

        elif len(scorer_inputs) == 3:           # Test case format of a word scramble file: SCRAMBLE WORD CORRECT_SCORE
            scrambled, word, correct_score = scorer_inputs

            f = io.StringIO()
            with redirect_stdout(f):
                scorer.score(scrambled, word)
                score_result = f.getvalue()[:-1]

                pass_fail = '** TEST FAILED **'
                if correct_score == 'NOT' and 'NOT A SCRAMBLE' in score_result.upper():
                    pass_fail = 'TEST PASSED'
                elif correct_score.upper() + ' SCRAMBLE' in score_result.upper():
                    pass_fail = 'TEST PASSED'

            print('{score_result}\t[ {pass_fail} ]'.format(score_result=score_result, pass_fail=pass_fail))

