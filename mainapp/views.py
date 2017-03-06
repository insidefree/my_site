from django.shortcuts import render, render_to_response
from .models import Article, Work, Study, Company, Skill, About
from datetime import date

# art01 = Article(1, "python", "python content")
# art02 = Article(2, "JavaScript", "javascript content")
# art03 = Article(3, "Games", "games content")
# art01.save()
# art02.save()
# art03.save()
# wr01 = Work(1, "site1", "Developer")
# wr02 = Work(2, "site2", "Developer")
# wr03 = Work(3, "site3", "Developer")
# wr01.save()
# wr02.save()
# wr03.save()
# cmp01 = Company(1, "Correlata", "Developer")
# cmp02 = Company(2, "Beame", "Developer")
# cmp03 = Company(3, "Yediot Ahronot", "Developer")
# cmp01.save()
# cmp02.save()
# cmp03.save()
# st01 = Study(1, "SevNTU", date(2011, 8, 13), date(2011, 8, 13), "The best University in the WORLD")
# st02 = Study(2, "SevNTU", date(2011, 8, 13), date(2011, 8, 13), "The best University in the WORLD")
# st03 = Study(3, "SevNTU", date(2011, 8, 13), date(2011, 8, 13), "The best University in the WORLD")
# st01.save()
# st02.save()
# st03.save()
#
# skill01 = Skill(1, "Python", "Describtion...python")
# skill02 = Skill(2, "Django", "Describtion...django")
# skill01.save()
# skill02.save()
#
# about = About_me(1, "my story")
# about.save()


def mainapp(request):
    about = About.objects.all()
    skills = Skill.objects.all()
    works = Work.objects.all()
    studies = Study.objects.all()
    return render_to_response("index.html", {"about": about, "skills": skills, "works": works, "studies": studies})


def about(request):
    skills = Skill.objects.all()
    companies = Company.objects.all()
    return render_to_response("about.html", {"skills": skills, "companies": companies})


def works(request):
    works = Work.objects.all()
    return render_to_response("works.html", {"works": works})


def knowledge_area(request):
    knowledges = Article.objects.all()
    return render_to_response("knowledge_area.html", {"knowledge": knowledges})
