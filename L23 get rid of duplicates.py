sudent_data = {
    "id1" : {"name" : ["sara"],
             "class" : ["V"],
             "subject_interogtion" : ["english, math, science"]
             },

    "id2" : {"name" : ["david"],
             "class" : ["V"],
             "subject_interogtion" : ["english, math, science"]
             },

    "id3" : {"name" : ["sara"],
             "class" : ["V"],
             "subject_interogtion" : ["english, math, science"]
             },

    "id4" : {"name" : ["surya"],
             "class" : ["V"],
             "subject_interogtion" : ["english, math, science"]
             },
}

result = {} #empty dictionary

for key,value in sudent_data.items():
    if value not in result.values():
        result[key] = value

print(result)