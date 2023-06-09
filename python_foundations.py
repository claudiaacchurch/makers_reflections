# Review of basic programming and python fundamentals:

'''Command Line:
pwd = print working dir
ls Parameter = show contents of specified dir
cd / cd.. = move into child / out to parent dir
mkdir new_dir = new dir
touch new_file = new file
cp new_file copy_file = copies file

move:
mv new_file ../ = moves up to parent dir
mv new_file ../NewDir = moves into a new dir in parent dir
mv Reflections python_foundations = Reflections goes into python_foundations
OR * python_foundation doesn't exist*
Reflections will be renamed python_foundations

remove:
rmdir new_dir 
OR *Directory not empty*
rm -r new_dir = removes dir and contents in it


cmnds with flags:
ls -A = shows all files inlcuding hidden(.) a.k.a dotfiles
ls -l = shows long format with file details
ls -lA = shows long format of all files (inc. hidden)

git & github:
echo "hello" > README.md = writes text to new (or existing) file 
rm -rf .git = removes an init call inside dir
git log = history of commits 
'''

#Python foundations, final password manager:

from datetime import datetime
class PasswordManager2():
    
    def __init__(self):
        self.dictionary = {}
    
    def add(self, service_name, password):
        symbols = ["!", "@", "$", "%", "&"]
        all_passwords = [password['password'] for password in self.dictionary.values()]
        if len(password) > 7 and any(symbol in password for symbol in symbols) and password not in all_passwords:
            self.dictionary[service_name] = {'password': password, 'added_on': datetime.now()}
        return None
    
    def remove(self, service_name):
        if service_name in self.dictionary:
            del self.dictionary[service_name]
        return None

    def update(self, service_name, password):
        self.add(service_name, password)
        return None
    
    def list_services(self):
        return [item for item in self.dictionary.keys()]

    def sort_services_by(self, string, reverse_arg=False):
        if string == "service":
            sorted_dict = sorted(self.dictionary.items(), key = lambda item: item[0], reverse = bool(reverse_arg))
        elif string == "added_on":
            sorted_dict = sorted(self.dictionary.items(), key = lambda item: item[1]['added_on'], reverse = bool(reverse_arg))
        return [item[0] for item in sorted_dict]
    
    def get_for_service(self, service_name):
        if service_name in self.dictionary:
            return self.dictionary[service_name]['password']
        else:
            return None

#1. Which data structure did you choose and why?
# Dictionaries preferred choice to store key: value(s). there are lots of ways of accessing dictionary vals. This extended to contain a nested dictionary:
my_dict = {
    "facebook": {"password": "123", "date_added": 12/12/2022},
    "makers": {"password": "456", "date_added": 13/8/2023}
    }

for item in my_dict:
    print(item) #facebook, makers, good for getting the keys.

for item in my_dict.items():
    # print(item) #('facebook', {'password': '123', "date_added" : "12/12/2022"}) \n ('makers', {"password": "456", "date_added": 13/8/2023})
    print(item[0]) #facebook
    print(item[1]) #{'password': '123', "date_added" : "12/12/2022"}
    print(item[1]["password"]) #456
    # dictionaries.items() return tuples so you can access the key / value through indexing, would be the same as:
for k, v in my_dict.items():
    print(k, v) 

for item in my_dict.values():
    print(item) #values of key:value pairs so {'password': '123', 'date_added': 12/12/2022} \n {'password': '456', 'date_added': 13/8/2023}. .keys() would = facebook, makers


'''Dictionaries are iterables:
Filter: takes iterable, returns filtered iterable where lambda is a func with no name that can be applied to iterable to judge True / False 
    e.g. list(filter(lambda param: param["password"] == "123", my_iterable))
Map: similar but returns same number as original e.g. list(map(lambda item: item > 1, [0, 1, 2])) = False, False, True 
lambda use in password manager with sorted func: sorted(self.dictionary.items(), key = lambda item: item[1]['added_on'], reverse = bool(reverse_arg))
    where sorted() sorts iterable based on func given with optional reverse param: key = lambda item: item[1]['added_on'] 
    -- means the key for 'sorting' is item[1]["added_on"] (item[1] = value in the items() tuple; "added_on" = key in value) for item in self.dictionary.items().'''

#What I'd do different in terms of approach: Review the whole problem, write down assumptions and requirements so when adding "added_on" don't have to restructure whole code.

'''Reflection from chapter 3 feedback:
- Use audio to explain code! This will also help with pair programming (Navigator).
- Clearer naming of variables: for dictionaries/lists/ and temp variables e.g. item for item in..../ password for password in....
- Instead of: (using .get())
     def get_for_service(self, service_name):
            if service_name in self.dictionary:
                return self.dictionary[service_name]['password']
                #return self.dictionary.get(service_name)
            else:
                return None
  - Use pytest to control workflow!
