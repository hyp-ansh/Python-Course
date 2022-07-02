from PyDictionary import PyDictionary
dictionary = PyDictionary()
word = input("Write the word : ")
meaning = dictionary.meaning(word, disable_errors=True)
result = f"Word : {word}\n"
try:
    for a, b in meaning.items():
        result += f"{a}\n"
        for i in b:
            result += f"{i}"
            print(result)
            break
except Exception:
    print("Either spelling is wrong or the word is not in dictionary.")
