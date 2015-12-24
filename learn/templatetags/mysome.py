from django import template 
register = template.Library() 
def key(d,key_name): 
        value = 0
        try: 
                value = d[key_name][:-1]
        except KeyError: 
                value = 0
        return value 
register.filter('key',key)