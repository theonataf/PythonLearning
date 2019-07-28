import json


class MenuManager():
    def __init__(self):
        with open('menu.json', 'r') as f:
            self.menu = json.load(f)

    def add_item(self, name, price):
        self.menu['items'].append({
            'name': name,
            'price': price
        })

    def remove_item(self, name):
        found = False
        for item in self.menu['items']:
            if item['name'] == name:
                self.menu['items'].remove(item)
                found = True
                break
        if found == False:
            print('we did not find what you were looking for')

    def save_to_file(self):
        with open('menu.json', 'w') as f:
            f.write(json.dumps(self.menu, indent=4))



