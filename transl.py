from googletrans import Translator
import hgtk

print("This script will take English words, find their Korean translation, then re-type them in English for a password suggestion.")
print("You’ll enter two English words and a symbol, and we’ll convert them to Korean typing on a US keyboard layout.")
print("I reccomend words that are not so common (such as dog, for example) and that try to get creative!")
print("Let's get started!\n")



# Mapping of jamo characters to English keyboard layout
jamo_to_keyboard = {
    'ㄱ': 'r', 'ㄲ': 'R', 'ㄴ': 's', 'ㄷ': 'e', 'ㄸ': 'E', 'ㄹ': 'f', 'ㅁ': 'a', 'ㅂ': 'q', 'ㅃ': 'Q',
    'ㅅ': 't', 'ㅆ': 'T', 'ㅇ': 'd', 'ㅈ': 'w', 'ㅉ': 'W', 'ㅊ': 'c', 'ㅋ': 'z', 'ㅌ': 'x', 'ㅍ': 'v', 'ㅎ': 'g',
    'ㅏ': 'k', 'ㅐ': 'o', 'ㅑ': 'i', 'ㅒ': 'O', 'ㅓ': 'j', 'ㅔ': 'p', 'ㅕ': 'u', 'ㅖ': 'P', 'ㅗ': 'h',
    'ㅘ': 'hk', 'ㅙ': 'ho', 'ㅚ': 'hl', 'ㅛ': 'y', 'ㅜ': 'n', 'ㅝ': 'nj', 'ㅞ': 'np', 'ㅟ': 'nl', 'ㅠ': 'b',
    'ㅡ': 'm', 'ㅢ': 'ml', 'ㅣ': 'l'
}

def translate_to_korean(word):
    translator = Translator()
    result = translator.translate(word, src='en', dest='ko')
    return result.text

def korean_to_keyboard_typing(hangul_text):
    us_keyboard_text = []
    for syllable in hangul_text:
        if hgtk.checker.is_hangul(syllable):
            # Decompose Hangul syllable into its jamo components
            initial, medial, final = hgtk.letter.decompose(syllable)
            # Map each jamo component to the corresponding US keyboard character
            us_keyboard_text.append(jamo_to_keyboard.get(initial, initial))
            us_keyboard_text.append(jamo_to_keyboard.get(medial, medial))
            if final:  # Final jamo may be absent
                us_keyboard_text.append(jamo_to_keyboard.get(final, final))
        else:
            us_keyboard_text.append(syllable)  # Non-Hangul characters are added as-is
    return ''.join(us_keyboard_text)

# Prompt for input
word1 = input("Enter the first English word: ")
symbol = input("Enter a symbol (e.g., #): ")
word2 = input("Enter the second English word: ")

# Translate words to Korean
korean_word1 = translate_to_korean(word1)
korean_word2 = translate_to_korean(word2)

# Convert Korean to US keyboard typing format
keyboard_typing_word1 = korean_to_keyboard_typing(korean_word1)
keyboard_typing_word2 = korean_to_keyboard_typing(korean_word2)

# Output the results
print(f"{korean_word1}, {symbol}, {korean_word2}")
print(f"Your Korean-to-English password is: {keyboard_typing_word1}{symbol}{keyboard_typing_word2}")

