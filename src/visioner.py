#!/bin/python

import random

subjects = ['Your momma ', "Murcia's prime minister ", "A drunk seagull "
, "The King of Burgerking ", "Floridaman ", "Willy Wonka ", "A fish with pretty shoes "
, "The tiny humanoid in a flask ", "A computer-generated penguin ", "Frank's roommate "
, "Your worst nightmare ", "Aragorn, son of Arathorn and heir of Isildur, ", "Bubo, the very creepy clown, "
, "An ostrich ", "Great Cthulhu ", "The cyborg mime ", "The Flying Spaguetti Monster "
, "Adam Sandler ", "Rita La Cantaora ", "A canadian wearing leggins ", "A sentient toothbrush "
, "Donald Trump ", "The tiny manticore ", "The disembodied head of Danny de Vito ", "This microscopic dinosaur "
,"The inventor of comic sans ", "The number 3 ", "Humbert, the amish rapper, ", "Sonic the Hedgehog ", "Mariano Rajoy "
,"The little mermaid ", "This ugly mug ", "Billy the Kid ", "Al Capone ", "Carmen de Mairena ", "Alf "
, "The last transformation of Son Goku ", "That palm tree ", "Slimer ", "Doraemon ", "Julio Iglesias ", "Batman "
, "Robocop ", "Sarah Connor ", "Jabba the Hutt ", "The last person on Earth ", "Conan the Bacterion "
, "A mayonaisse golem ", "Peter Pan ", "Captain Obvious ", "A horseshoe crab ", "Tim, the magician, "
, "Dora the Explorer ", "Your neighbour ", "That floating eyeball ", "The ant in your arm ", "Tacocat ", "Moctezuma "
, "Jhonny Bravo ", "The fake pope ", "Francisco Pizarro ", "Gilgamesh ", "Quentin Tarantino ", "Lina Morgan "]

verbtypelist = ["is ", "is not ", "may be ", "was ", "must be ", "cannot be ", "should be ", "could be ", "wants to be ", "will be ", "has been ", "for sure is "]

attributes = ["a good partner in crime ", "fascinating in its own way ", "a worthy opponent at UNO "
, "a total asshole ", "a huge fan of The Big Bang Theory ", "the best friend you could imagine "
,"a midget riding another midget ", "a kind-hearted deity", "a portuguese ninja baker ", "married to a ginger "
, "the living proof of the absurdity of existence ", "Hodor ", "a pokemon ", "a type of kangaroo "
, "an alligator wrestler ", "kinda scary ", "delicious with honey mustard sauce ", "a valid ingredient for paella"
,"Peppa Pig's nemesis", "pregnant, but don't tell anyone", "a fungus in the Pezizomycotina clade "
,"a rotten avocado ", "looking for you ", "an action figure", "a collective hallucination", "a Horcrux ", "a sock puppet"
, "your reviewer ", "in great pain ", "a big fan of the bat-nipples ", "actually mexican, that's why is offended by your comments "
, "racist ", "destined to rule over Winterfell ", "a secret lover of Pep Guardiola ", "a problem only you can deal with "
, "in the new reboot of Ghostbusters ", "a succesful surgeon ", "your father ", "in your bed with you", "stir-fried", "super sexy"
,"the meaning of life ", "a traitor ", "dressed up as Lady Gaga ", "on fire ", "bathing in soy sauce ", "a bit disappointed"
, "a doctor and a pirate ", "a goat ", "sad that we all have to die eventually ", "a philosophy major "]

verbtype = verbtypelist[random.randrange(0,len(verbtypelist))]
	
print subjects[random.randrange(0,len(subjects))] + verbtype + attributes[random.randrange(0,len(attributes))]
