# import os
import re
import string

# print(os.getcwd())
print(list(string.punctuation))

with open('./ColumnarResume Format1/roadmap.md', 'r') as roadmapfile:
    lines = roadmapfile.readlines()

    # regex_pattern = r'[*][*][A-Za-z0-9 ]*[*][*]'
    regex_pattern = r'[*][*][^*]*[*][*]'
    skills_list = []
    for line in lines:
        # print(line)
        current_skills = [x.replace('*', '') for x in re.findall(regex_pattern, line)]
        # print(current_skills)
        current_skills_new = []
        for x in current_skills:
            # print("###", x)
            for punc in list(string.punctuation):
                x = x.replace(punc, '#').replace(' and ','#').replace(' or ','#')
            # print('---', x)
            current_skills_new.extend([y.strip().lower() for y in x.split('#')])
        # print(current_skills_new)
        skills_list.extend(current_skills_new)
        # print(skills_list)
        # print('#######')

print(set(skills_list))


# x = 'hello#how,are you'
# print(re.split(r'#|,', x))