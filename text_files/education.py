education = {
    "Portuguese": [
        {"title": "MBA Data Science & Analytics", "institution": "Universidade de São Paulo", "period": "2022-2024", "description": ""},
        {"title": "Mestrado", "institution": "Universidade Federal do Paraná", "period": "2019-2021", "description": ""},
        {"title": "Bacharelado", "institution": "Universidade Federal do Paraná", "period": "2015-2018", "description": ""}
    ],
    "English": [
        {"title": "MBA Data Science & Analytics", "institution": "Universidade de São Paulo", "period": "2022-2024", "description": ""},
        {"title": "Master of Science", "institution": "Universidade Federal do Paraná", "period": "2019-2021", "description": ""},
        {"title": "Bachelor of Science", "institution": "Universidade Federal do Paraná", "period": "2015-2018", "description": ""}
    ]
}

def display_education(language):
    ret_info_all = []
    for course in education[language]:
        ret_info = [
            f"## {course['title']}",
            f"**{course['institution']}** -- **{course['period']}**",
            course['description']
        ]
        ret_info_all.append('\n'.join(ret_info))

    return '\n'.join(ret_info_all)