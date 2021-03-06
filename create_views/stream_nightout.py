# [Team 2]
# Posung Chen / poc2 / 773278
# Xiao liang / liangx4 / 754282
# Jiawei Zhang / jiaweiz6 / 815546
# Jia Wang / jiaw8 / 815814
# Fan Hong / hongf / 795265

import couchdb,sys
from couchdb.design import ViewDefinition

couch = couchdb.Server('http://admin:admin@localhost:15984/')
print couch
db = couch[sys.argv[1]]
print db

#2.brunch
#view = ViewDefinition('category', 'brunch',
#'''function(doc) {
#constraint_1 = (doc.metadata.place.name == 'Melbourne' || 
#doc.metadata.place.name == 'Sydney')

#regex=/(#| |^)brunch( |$|s|es)/i
#constraint_2 = doc.metadata.text.match(regex)
#var hour = new Date(doc.metadata.created_at).getHours();
#constraint_3 = (hour >=9) && (hour <=15)

#if(constraint_1 && constraint_2 && constraint_3) 
#emit([doc.metadata.place.name,'brunch',doc._id,doc.metadata.coordinates.coordinates,doc.metadata.created_at], 1); 
#}''')
#view.sync(db)

#3.nightout
view = ViewDefinition('category', 'nightout', 
'''function(doc) {
constraint_1 = (doc.metadata.place.name == 'Melbourne' || 
doc.metadata.place.name == 'Sydney')

regex=/(#| |^)(bar|clubbing|beer|cocktail|wine|sake|champagne|vodka|tequilla|cheers)( |$|s|es)|\uD83C\uDF7A|\uD83C\uDF78|\uD83C\uDF77|\uD83C\uDF76|\uD83C\uDF79|\uD83C\uDF7B|\uD83C\uDF7E/i
constraint_2 = doc.metadata.text.match(regex)

var hour = new Date(doc.metadata.created_at).getHours();
var date = new Date(doc.metadata.created_at).toString();
constraint_3 = (hour >=18) || (hour <=6)

if(constraint_1 && constraint_2 && constraint_3)  
emit([doc.metadata.place.name,'nightout',doc._id,doc.metadata.coordinates.coordinates,date,doc.metadata.text,doc.sentiment], 1);
}''')
view.sync(db)

print 'complete!'
