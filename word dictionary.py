import json;
from difflib import get_close_matches;
from IPython.display import clear_output;
dic = json.load(open("original.json"));
def dictionary(word):
    if word == "":
        clear_output();
        c = False;
        return c;
    elif word in dic:
        return dic[word];
    elif word.lower() in dic:
        return dic[word.lower()];
    elif word.upper() in dic:
        return dic[word.upper()];
    elif word not in dic:
        similar = get_close_matches(word,dic);
        for j in similar:
            print("Do you mean: ",j);
            ans = input();
            if ans == ("yes" or "Yes" or "YES"):
                return dic[j];
            if j == similar[len(similar)-1]:
                return "word not found";
if __name__ == "__main__":
    c = True;
    while c:
        word = input("enter word: ");
        meaning = dictionary(word);
        if type(meaning) == list:
            for m in meaning:
                print(m);
        elif meaning == False:
            break;
        else:
            print(meaning);
        print("______________________________________________________________________________________________________________");