from django.shortcuts import render, render_to_response
import time


class Article:
    def __init__(self, id, type, content):
        self.id = id
        self.type = type
        self.content = content

    def __repr__(self):
        return "{}, {}, {}".format(self.id, self.type, self.content)


class Work:
    def __init__(self, name, description):
        self.name = name
        self.describtion = description

    def __str__(self):
        return "{}, {}".format(self.name, self.describtion)

    def __repr__(self):
        return "{}, {}".format(self.name, self.describtion)


class Study:
    def __init__(self, name, date_start, date_end, describe):
        self.name = name
        self.date_start = date_start
        self.date_end = date_end
        self.describe = describe

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.date_start, self.date_end, self.describe)

    def __repr__(self):
        return "{}, {}, {}, {}".format(self.name, self.date_start, self.date_end, self.describe)


class Company:
    def __init__(self, name, description):
        self.name = name
        self.describtion = description

    def __str__(self):
        return "{}, {}".format(self.name, self.describtion)

    def __repr__(self):
        return "{}, {}".format(self.name, self.describtion)


art01 = Article("art01", "python", "python content")
art02 = Article("art02", "JavaScript", "javascript content")
art03 = Article("art03", "Games", "games content")

wr01 = Work("site1", "Developer")
wr02 = Work("site2", "Developer")
wr03 = Work("site3", "Developer")

cmp01 = Company("Correlata", "Developer")
cmp02 = Company("Beame", "Developer")
cmp03 = Company("Yediot Ahronot", "Developer")

st01 = Study("SevNTU", time.time(), time.time(), "The best University in the WORLD")
st02 = Study("SevNTU", time.time(), time.time(), "The best University in the WORLD")
st03 = Study("SevNTU", time.time(), time.time(), "The best University in the WORLD")

person_info = {
    "first_name": "Denis",
    "last_name": "Sorokin",
    "birthday": time.time(),
    "study": [st01, st02, st03],
    "companies": [cmp01, cmp02, cmp03],
    "works": [wr01, wr02, wr03],
    "skills": ["CSS", "HTML", "JSON", "MySQL", "Javascript", "FlexBox", "Python"],
    "knowledges": {
        "NodeJS": [art01, art02, art03],
        "Python": [art01, art02, art03],
        "JavaScript": [art01, art02, art03]
    }
}


def mainapp(request):
    return render_to_response("index.html")


def about(request):
    about = {"name": "Denis"}
    return render_to_response("about.html", {"person_info": person_info})


def works(request):
    return render_to_response("works.html", {"works": person_info["works"]})


def knowledge_area(request):
    return render_to_response("knowledge_area.html", {"knowledge": person_info["knowledges"]})
