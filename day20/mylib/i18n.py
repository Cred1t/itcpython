
config ='работает как модуль'


languages = {
    'ru': {
        'go': 'идти',
        'think': 'Думать',
        'friend': 'Друг',
        'we': 'Мы',
        'edit': 'Изменить',
        'view': 'просмотр',
        'run': 'Бегать',
        'room': 'комната',
        'i': 'я',
        'number': 'число',
        'it': 'оно',
        'she': 'Она',
        'he': 'Он',
    },
    'en': {
        'идти': 'Go'
    },
    'kg': {
        'go': 'басуу',
        'think': 'Ойлонуу',
        'friend': 'Друг',
        'we': 'Биз',
        'edit': 'Озгортуу',
        'view': 'Коруу',
        'run': 'Чуркоо',
        'room': 'Болмо',
        'i': 'Мен',
        'number': 'Сан',
        'it': 'бул',
        'she': 'Аял',
        'he': 'Эркек',
    }
}





# def to_translate(word,code):
#     word_to_lower = word.lower()
#     if code in languages:
#         if word in languages[code]:
#             print(word,'на',code,'языке',
#             languages[code][word_to_lower]
                
                
#             )



def to_translate(word, code):
    word_to_lower = word.lower()
    if code in languages:
       if word in languages[code]:
            print(
                word, 
                'На', code, 'языке', 
                languages[code][word_to_lower]
            )
def to_translate_many(*args, **kwargs):
    for a in args:
        to_translate(a, kwargs['lang'])

# def to_translate(word,language):
#     if language == 'ru':
#         word_to_lower = word.lower()
#         print(word,'на русском языке: ',ru[word_to_lower])


# def kg_translate(word,language):
#     if language == 'kg':
#         word_to_lower = word.lower()
#         print(word,'на кыргызском языке: ',kg[word_to_lower])


# def en_translate(word,language):
#     if language == 'en':
#         word_to_lower = word.lower()
#         print(word,'на англиском языке: ',en[word_to_lower])