import sabrina
import maria_string
import celia_name
import emily
import gur_string

#imports for the story:
import celia_story1 # paragraph 1 act 1

def team_introduction():
    return "This is Team Trashmasters. We are " + sabrina.sabrina_name() + ", " + maria_string.marias_name() + ", " + celia_name.name() + ", " + gur_string.gur_name() + ", and " + emily.emily() + "." 

print(team_introduction())

#story:
print("Act 1: The beginning of the night")
#paragraph 1: celia
print(celia_story1.text())