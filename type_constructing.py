# type checker
"""
//.5↓..10↓..15↓..20↓..25↓..30↓..35↓..40↓..45↓..50↓..55↓..60↓..65↓..70↓..75↓..80↓

    A pairing function that contains a dictionary of "secret keys" which get
hashed with type constructor declarations, create unique identifiers, within the
type checker, for declared types. This allows the type checker to reject forged
types not produced by it's associated type=type-constructor=constructor (ttcc).

"""

# type=type-constructor=constructor (ttcc)
"""
//.5↓..10↓..15↓..20↓..25↓..30↓..35↓..40↓..45↓..50↓..55↓..60↓..65↓..70↓..75↓..80↓

    Needs to allow generic invocations, so you can decide if you want getters,
setters, etc.

    Fields also need to be types constructed by ttcc.

"""


# specific type constructor `new_car`
def new_car(make,model,year,owner):
    exec("global product\n" +
         "def product(getSet_field):\n" +
         "\tglobal " + owner + "\n" +

         # Match getSet_field
         "\tmatch getSet_field:\n"+

         # Getter cases
         "\t\tcase 'make': return '" + make + "'\n" +
         "\t\tcase 'model': return '" + model + "'\n" +
         "\t\tcase 'year': return '" + year + "'\n" +

        # Setter cases
         "\t\tcase setMake if setMake[:setMake.find('=')].strip() == 'make':\n" +
         "\t\t\tnew_car(setMake[setMake.find('=')+1:].strip(),'" + model +
         "','" + year + "','" + owner + "')\n" +

         "\t\tcase setModel if setModel[:setModel.find('=')].strip() == 'model':\n" +
         "\t\t\tnew_car('" + make +
         "', setModel[setModel.find('=')+1:].strip(),'" + year + "','" +
         owner + "')\n" +
         
         "\t\tcase setYear if setYear[:setYear.find('=')].strip() == 'year':\n" +
         "\t\t\tnew_car('" + make + "','" + model +
         "', setYear[setYear.find('=')+1:].strip(),'" + owner + "')\n" +

        # Error/Default case
         "\t\tcase _:\n" +
         "\t\t\tprint('Error: `' + getSet_field +'` is not a field of', " +
         owner + ")\n" +
         "\t" + owner + " = product\n" +
         "\treturn\n" +
         owner + "= product"
    )


# a function constructor `new_fn` where condouts = [[condition, output], ...]
#def new_fn(condouts, this):































    
