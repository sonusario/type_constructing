x = {'x':(lambda: eval("x['x']()"))}
#x['x']()

y = (lambda n: (exec('''
def fact(n):
    def factIter(n, acc):
        if n == 0: return acc
        return factIter(n - 1, n * acc)
    return factIter(n - 1, n)
'''),

    eval('fact(n)'))[1]
 
)(5)

Car = {
    'fields': ['make','model','year','serial'],
    'new': (lambda make,model,year: {
        'make': make,
        'model': model,
        'year': year,
        'serial': 0
    })
}

def struct(struct_name, struct_fields):
    
