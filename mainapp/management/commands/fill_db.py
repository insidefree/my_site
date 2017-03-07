from django.core.management.base import BaseCommand
from mainapp.models import Work, Hobby, Study, Company, Article, Skill, About
from datetime import date


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        works = [
            {'company': 'YIT - Yedioth Information Technology',
             'position': 'Software Developer',
             'duties': 'Big prodject on DJango',
             'date_from': date(1990, 9, 1),
             'date_to': date(1990, 9, 1)},
            {'company': 'Beame.io',
             'position': 'Front End Software Developer',
             'duties': 'Java script',
             'date_from': date(1990, 9, 1),
             'date_to': date(1990, 9, 1)},
            {'company': 'Correalata Solutions Ltd.',
             'position': 'Software Developer',
             'duties': 'Developed chart using VisJS to represent current status of network',
             'date_from': date(1990, 9, 1),
             'date_to': date(1990, 9, 1)},
        ]
        companies = [
            {'name': 'YIT - Yedioth Information Technology',
             'description': 'Yedioth Information Technologies (YIT) is an independent company, established '
                            'for the purpose of serving as the Information Technologies (IT) body of Yedioth Acharonot '
                            'group. During our ten years of activity we have led Yedioth Acharonot to the technology '
                            'front in the press field, and in other paralleling fields. In a short period of time we '
                            'have transformed from a small company providing only support to a company developing '
                            'products and selling them in Israel and worldwide.',
             'country': 'Israel',
             'city': 'Rishon LeTsiyon',
             'site': 'http://www.yit.co.il',
             'logo': '/static/images/logos/YIT.png'},
            {'name': 'Beame.io',
             'description': 'Beame.io is the first cryptographic identity services provider'
                            'that doesn\'t hold a single key. We developed a new way to'
                            'verify user access privileges using a cryptographic identity '
                            'that works seamlessly with mobile and IoT devices.',
             'country': 'Israel',
             'city': 'Tel Aviv',
             'site': 'https://www.beame.io',
             'logo': '/static/images/logos/Beameio.png'},
            {'name': 'Correalata Solutions Ltd.',
             'description': 'Correlata provides a new business-centric IT management layer that transforms IT '
                            'operations and service metrics into business metrics,  helping companies gain the highest'
                            'level of visibility and control on ALL their IT Infrastructure environments to senior'
                            'management, ensuring companies use their Data Center infrastructure investments'
                            'coordinating to their design intentions and business objectives.',
             'country': 'Israel',
             'city': 'Yavne',
             'site': 'http://www.correlata.com',
             'logo': '/static/images/logos/Correlata.png'}
        ]
        hobbies = [
            {'name': 'tourism'},
            {'name': 'programming'},
            {'name': 'digging -)'},
        ]
        studies = [
            {'school_name': 'Tel-Ran',
             'course_name': 'Master of Computer Applications (MCA) Field Of Study Computer Programming',
             'date_from': date(1990, 9, 1),
             'date_to': date(1998, 6, 1)},
            {'school_name': 'Technion - Israel Institute of Technology',
             'course_name': 'Network design and security',
             'date_from': date(1998, 9, 1),
             'date_to': date(2001, 6, 1)},
            {'school_name': 'Sevastopol National Technical University',
             'course_name': 'Master\'s degree Field Of Study Automatics and Computer Technology department with a '
                            'diploma in Systems',
             'date_from': date(2001, 9, 1),
             'date_to': date(2006, 8, 1)},
        ]
        articles = [
            {'type': 'javascript', 'content': 'javascript article'},
            {'type': 'python', 'content': 'python article'}
        ]
        skills = [
            {'name': 'python', 'describe': 'completed big project'},
            {'name': 'javascript', 'describe': 'completed big project'}
        ]
        about = {
            'first_name': 'Denis',
            'last_name': 'Sorokin',
            'email': 'denys.sorokin@gmail.com',
            'phone': '+792-555-55-55',
            'story': 'Hi I am developer'
        }

        Company.objects.all().delete()
        for company in companies:
            company = Company(**company)
            company.save()

        Work.objects.all().delete()
        for work in works:
            company_name = work['company']
            company = Company.objects.get(name=company_name)
            work['company'] = company
            work = Work(**work)
            work.save()

        Hobby.objects.all().delete()
        for hobby in hobbies:
            hobby = Hobby(**hobby)
            hobby.save()

        Study.objects.all().delete()
        for study in studies:
            study = Study(**study)
            study.save()

        Skill.objects.all().delete()
        for skill in skills:
            skill = Skill(**skill)
            skill.save()

        Article.objects.all().delete()
        for article in articles:
            article = Article(**article)
            article.save()

        About.objects.all().delete()
        about = About(**about)
        about.save()
