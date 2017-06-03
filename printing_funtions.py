#python3 printing_funtions.py


#import print_models

#print_models(unprinted_designs, completed_models)
#print_models(unprinted_designs[:], completed_models)
#show_completed_models(completed_models)

#print(unprinted_designs)


#from print_models import print_models

#print_models(unprinted_designs, completed_models)


#from print_models import print_models as pm


#import print_models as pm

from print_models import * #Only one that seems to work.

unprinted_designs = ['iphone case', 'android case', 'dodecahedron', 'test']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#This list overrides list in module.