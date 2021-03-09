from django.shortcuts import render
from PyDictionary import PyDictionary


# Create your views here.


def index(request):
    return render(request, "index.html", {})


def word(request):
    search = request.GET.get("search")
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonym = dictionary.synonym(search)
    antonym = dictionary.antonym(search)
    if len(synonym) > 5:
        synonym = synonym[:5]

    if len(antonym) > 5:
        antonym = antonym[:5]
    if "Verb" in meaning:
        meaning = meaning["Verb"][0]
    elif "Noun" in meaning:
        meaning = meaning["Noun"][0]
    elif "Adjective" in meaning:
        meaning = meaning["Adjective"][0]
    context = {
        "meaning": meaning,
        "synonyms": synonym,
        "antonyms": antonym
    }
    return render(request, "word.html", context)
