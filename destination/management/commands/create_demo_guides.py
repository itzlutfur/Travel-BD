import random
from django.core.management.base import BaseCommand
from hire_guide.models import Guide


class Command(BaseCommand):
    help = 'Creates additional demo guides for pagination testing'

    def handle(self, *args, **options):
        # Additional demo guides
        additional_guides = [
            {
                'name': 'Aminul Islam',
                'bio': 'Beach specialist with expertise in water sports and coastal tourism.',
                'short_bio': 'Cox\'s Bazar native specializing in beach activities and seafood tours.',
                'location': 'Inani Beach',
                'district': 'Cox\'s Bazar',
                'division': 'Chittagong',
                'specialization': 'beach',
                'experience_level': 'intermediate',
                'phone': '+8801712111111',
                'email': 'aminul.beach@email.com',
                'daily_rate': 2000.00,
                'languages': 'Bengali, English',
                'rating': 4.3,
                'total_tours': 78,
                'featured': False,
            },
            {
                'name': 'Ruma Chakma',
                'bio': 'Tribal culture expert from Chittagong Hill Tracts with deep knowledge of indigenous communities.',
                'short_bio': 'Hill tracts guide specializing in tribal culture and traditional crafts.',
                'location': 'Khagrachari',
                'district': 'Khagrachari',
                'division': 'Chittagong',
                'specialization': 'cultural',
                'experience_level': 'experienced',
                'phone': '+8801812222222',
                'email': 'ruma.tribal@email.com',
                'daily_rate': 2300.00,
                'languages': 'Bengali, English, Chakma',
                'rating': 4.7,
                'total_tours': 145,
                'featured': True,
            },
            {
                'name': 'Shahidul Alam',
                'bio': 'Historical monuments and archaeology specialist focusing on ancient Bengal civilization.',
                'short_bio': 'Archaeology expert with specialization in ancient Bengal and Mughal period.',
                'location': 'Mahasthangarh',
                'district': 'Bogra',
                'division': 'Rajshahi',
                'specialization': 'historical',
                'experience_level': 'expert',
                'phone': '+8801913333333',
                'email': 'shahid.history@email.com',
                'daily_rate': 2700.00,
                'languages': 'Bengali, English, Urdu',
                'rating': 4.8,
                'total_tours': 198,
                'featured': False,
            },
            {
                'name': 'Nasreen Sultana',
                'bio': 'Adventure sports and rock climbing instructor with wilderness survival skills.',
                'short_bio': 'Certified adventure guide with rock climbing and wilderness survival expertise.',
                'location': 'Srimangal',
                'district': 'Moulvibazar',
                'division': 'Sylhet',
                'specialization': 'adventure',
                'experience_level': 'experienced',
                'phone': '+8801814444444',
                'email': 'nasreen.adventure@email.com',
                'daily_rate': 2600.00,
                'languages': 'Bengali, English',
                'rating': 4.6,
                'total_tours': 112,
                'featured': True,
            },
            {
                'name': 'Jamal Uddin',
                'bio': 'River cruise and boat tour specialist covering major rivers of Bangladesh.',
                'short_bio': 'River tourism expert offering boat tours on Padma, Meghna, and Jamuna.',
                'location': 'Manikganj',
                'district': 'Manikganj',
                'division': 'Dhaka',
                'specialization': 'adventure',
                'experience_level': 'intermediate',
                'phone': '+8801715555555',
                'email': 'jamal.river@email.com',
                'daily_rate': 1900.00,
                'languages': 'Bengali, English',
                'rating': 4.4,
                'total_tours': 89,
                'featured': False,
            },
            {
                'name': 'Sultana Begum',
                'bio': 'Rural tourism and village life specialist offering authentic Bengali countryside experiences.',
                'short_bio': 'Village tourism expert showcasing traditional Bengali rural life and customs.',
                'location': 'Kushtia',
                'district': 'Kushtia',
                'division': 'Khulna',
                'specialization': 'cultural',
                'experience_level': 'experienced',
                'phone': '+8801816666666',
                'email': 'sultana.village@email.com',
                'daily_rate': 1700.00,
                'languages': 'Bengali, English',
                'rating': 4.5,
                'total_tours': 167,
                'featured': False,
            },
            {
                'name': 'Rakib Hassan',
                'bio': 'Wildlife photography and bird watching guide specializing in migratory birds.',
                'short_bio': 'Wildlife photographer and bird watching expert covering wetlands and forests.',
                'location': 'Tanguar Haor',
                'district': 'Sunamganj',
                'division': 'Sylhet',
                'specialization': 'adventure',
                'experience_level': 'expert',
                'phone': '+8801917777777',
                'email': 'rakib.wildlife@email.com',
                'daily_rate': 3100.00,
                'languages': 'Bengali, English',
                'rating': 4.9,
                'total_tours': 267,
                'featured': True,
            },
            {
                'name': 'Marium Khatun',
                'bio': 'Food tourism and culinary heritage specialist offering authentic Bengali cooking experiences.',
                'short_bio': 'Culinary guide offering food tours and traditional Bengali cooking classes.',
                'location': 'Chittagong',
                'district': 'Chittagong',
                'division': 'Chittagong',
                'specialization': 'cultural',
                'experience_level': 'intermediate',
                'phone': '+8801818888888',
                'email': 'marium.food@email.com',
                'daily_rate': 2100.00,
                'languages': 'Bengali, English',
                'rating': 4.6,
                'total_tours': 94,
                'featured': False,
            },
        ]

        created_count = 0
        
        for guide_data in additional_guides:
            guide, created = Guide.objects.get_or_create(
                name=guide_data['name'],
                defaults=guide_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created guide: {guide.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Guide already exists: {guide.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(f'\nCreated {created_count} additional demo guides!')
        )