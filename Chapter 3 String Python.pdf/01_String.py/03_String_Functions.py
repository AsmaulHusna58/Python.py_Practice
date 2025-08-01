story = "Once upon a time there was a modest girl name Ankhy who is a CSE student in PSTU upon"
print(story[0:7])

# String Functions
print(len(story))
print(story.endswith("asdfghkl"))
print(story.endswith("PSTU"))
print(story.endswith("in"))
print(story.count("a"))
print(story.count("upon"))
print(story.capitalize())
print(story.find("upon")) # it find just first word. It never find second same word   
print(story.find("tie"))
print(story.find("Once"))
print(story.replace("Ankhy", "AsmaulHusnaAnkhy"))