def word_replacement():
    str = "hi, this is panjagala speaking with you, hi hi hi"

    Target_word_to_replace = input("enter target word to replace:")
    Replace_word = input("enter the word you want to replace with:")
    updated_string = str.replace(Target_word_to_replace, Replace_word)
    print(updated_string)

word_replacement()