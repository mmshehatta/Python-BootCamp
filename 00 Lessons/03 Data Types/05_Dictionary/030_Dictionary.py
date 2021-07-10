
# 00 Lesson
# >> 03 Data Types
# >> 03 dictionary
# >> 030_dictionary.py

from icecream import ic

# -----------------------------
# [1] dictionary items enclosed in Curly Braces
# [2] dict are contains key : value
# [3] dict key need to be immutable=>(Number , String , Tuble) list not allowed
# [4] dict value is any data type
# [5] dict key must be unique
# [6] dict items not ordered , and can access by key
# -----------------------------

# dictionary:
# [1] dictionary items enclosed in Curly Braces
# [2] dict are contains key : value
user = {
    'name': 'Mahmoud',
    'age': 35,
    'country': 'Egypt'
}

# [3] dict key need to be immutable=>(Number , String , Tuble) list not allowed
dict1 = {
    'name': 'Mahmoud',
    'age': 35,
    'country': 'Egypt',
    (1, 2): ("one", "two"),  # Allowed
    # [1, 2]: ["one", "two"]  # Not Allowed
}


# [4] dict value is any data type
dict2 = {
    'name': 'Mahmoud',  # string
    'age': 35,  # number
    'country': 'Egypt',  # string
    (1, 2): ("one", "two"),  # tuble
}


# [5] dict key must be unique
dict3 = {
    'name': 'Mahmoud',  # taked because is first
    'age': 35,
    'country': 'Egypt',
    'name': 'Amr',  # not taked

}

# [6] dict items not ordered , and can access by key
dict4 = {
    'name': 'Mahmoud',
    'age': 35,
    'country': 'Egypt',
}


ic(dict4['name'])       #ic| dict4['name']: 'Mahmoud'
ic(dict4['age'])        #ic| dict4['age']: 35
ic(dict4.get('country'))#ic| dict4.get('country'): 'Egypt'

# all key and values:
ic(dict4.keys())    #ic| dict4.keys(): dict_keys(['name', 'age', 'country'])
ic(dict4.values())  #ic| dict4.values(): dict_values(['Mahmoud', 35, 'Egypt'])


# 2D dictinary:
prog_languages={
    'one':{
        'name':'css',
        'progress':'90%',
    },
    'two':{
        'name':'js',
        'progress':'70%',
    }
}

ic(prog_languages)  #ic| prog_languages: {'one': {'name': 'css', 'progress': '90%'}, 'two': {'name': 'js', 'progress': 70%'}}
ic(prog_languages['one'])             #ic| prog_languages['one']: {'name': 'css', 'progress': '90%'}
ic(prog_languages['one']['name'])     #ic| prog_languages['one']['name']: 'css'
ic(prog_languages['one']['progress']) #ic| prog_languages['one']['progress']: '90%'

ic(prog_languages['two'])             #ic| prog_languages['two']: {'name': 'js', 'progress': '70%'}
ic(prog_languages['two']['name'])     #ic| prog_languages['two']['name']: 'js'
ic(prog_languages['two']['progress']) #ic| prog_languages['two']['progress']: '70%'


ic(prog_languages.get('one'))   #ic| prog_languages.get('one'): {'name': 'css', 'progress': '90%'}
ic(prog_languages.get('two'))   #ic| prog_languages.get('two'): {'name': 'js', 'progress': '70%'}
ic(prog_languages.get('one').get('name'))   #ic| prog_languages.get('one').get('name'): 'css'
ic(prog_languages.get('two').get('name'))   #ic| prog_languages.get('two').get('name'): 'js'

ic(prog_languages.get('one').get('progress')) #ic| prog_languages.get('one').get('progress'): '90%'
ic(prog_languages.get('two').get('progress')) #ic| prog_languages.get('two').get('progress'): '70%'


# to check dist len:number of elements
ic(len(prog_languages))        #ic| len(prog_languages): 2
ic(len(prog_languages['one'])) #ic| len(prog_languages['one']): 2
ic(len(prog_languages['two'])) #ic| len(prog_languages['two']): 2




# more than one dict need to collect in one wrapper dict:
framework1={
    'name':'Vue.js',
    'progress':'50%',
}


framework2={
    'name':'React.js',
    'progress':'70%',
}
framework3={
    'name':'Angular.js',
    'progress':'80%',
}


all_js_frameworks={
    'one':'framework1',
    'two':'framework2',
    'three':'framework3',
}

ic(all_js_frameworks)   #ic| all_js_frameworks: {'one': 'framework1', 'three': 'framework3', 'two': 'framework2'}

