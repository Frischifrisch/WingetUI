from lang.lang_tools import languageReference

lang = {}
englang = {}
languages = {
    key: f"lang_{key}.json"
    for key in languageReference.keys()
    if (key != "default")
}
debugLang = False
