# word-scramble-score
A simple scoring script which rates the difficulty of solving a word scramble implemented in Python 3.6.

This script implements the word scramble scoring requirements outlined in `Word Scramble Test.pdf`.

## Word scramble file format
Word scrambles must take the form:

SCRAMBLED WORD
  
For example, the following is a valid scramble file with 3 scrambles of the word IRONY:

RIONY IRONY

ONYRI IRONY

IRONY IRONY

## Test case file format
The script implements a variation of the word scramble file format to enable the execution of test cases. Test cases must take the form:

SCRAMBLED WORD CORRECT_SCORE

For example, the following is a valid test case file with 3 scrambles of the word IRONY:

RIONY IRONY FAIR

ONYRI IRONY HARD

IRONY IRONY NOT

## Execution
A list of scrambled words and their unscrambled equivalent can be passed to the script by redirecting stdin to the script:
```
python3 word_scramble_score.py < word_scramble_inputs.txt
```

Output matches that specified in `Word Scramble Test.pdf`.

The script will automatically detect if the input file contains test cases. To execute the provided test case file, simply run:
```
python3 word_scramble_score.py < test_case_inputs.txt
```

Test case output appears as:
```
RIONY is a fair scramble of IRONY	[ TEST PASSED ]
ONYRI is a hard scramble of IRONY	[ TEST PASSED ]
IRONY is not a scramble of IRONY	[ TEST PASSED ]
```
