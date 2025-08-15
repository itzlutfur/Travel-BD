import random
from django.core.management.base import BaseCommand
from hire_guide.models import Guide


class Command(BaseCommand):
    help = 'Creates demo guides for testing'

    def handle(self, *args, **options):
        # Sample data
        demo_guides = [
            {
                'name': 'Abdul Rahman Khan',
                'bio': 'Experienced guide with deep knowledge of historical sites across Bangladesh. Passionate about sharing the rich heritage and culture of our beautiful country.',
                'short_bio': 'Expert historical guide with 8+ years experience. Specializes in Mughal architecture and ancient archaeological sites.',
                'location': 'Old Dhaka',
                'district': 'Dhaka',
                'division': 'Dhaka',
                'specialization': 'historical',
                'experience_level': 'experienced',
                'phone': '+8801712345678',
                'email': 'abdul.rahman@email.com',
                'daily_rate': 2500.00,
                'languages': 'Bengali, English, Hindi',
                'rating': 4.8,
                'total_tours': 156,
                'featured': True,
            },
            {
                'name': 'Fatima Begum',
                'bio': 'Adventure enthusiast and mountain trekking expert. Has explored every hill tract in Bangladesh and loves taking tourists on thrilling adventures.',
                'short_bio': 'Adventure guide specializing in hill tracts and trekking. Safety-certified with wilderness first aid training.',
                'location': 'Bandarban',
                'district': 'Bandarban',
                'division': 'Chittagong',
                'specialization': 'adventure',
                'experience_level': 'expert',
                'phone': '+8801887654321',
                'email': 'fatima.adventure@email.com',
                'daily_rate': 3000.00,
                'languages': 'Bengali, English, Chakma',
                'rating': 4.9,
                'total_tours': 203,
                'featured': True,
            },
            {
                'name': 'Mohammad Karim',
                'bio': 'Beach and coastal area specialist. Born and raised in Cox\'s Bazar, knows every hidden spot along the coastline.',
                'short_bio': 'Local Cox\'s Bazar guide with extensive knowledge of beaches, seafood, and coastal activities.',
                'location': 'Cox\'s Bazar',
                'district': 'Cox\'s Bazar',
                'division': 'Chittagong',
                'specialization': 'beach',
                'experience_level': 'experienced',
                'phone': '+8801912345678',
                'email': 'karim.beach@email.com',
                'daily_rate': 2200.00,
                'languages': 'Bengali, English',
                'rating': 4.6,
                'total_tours': 189,
                'featured': False,
            },
            {
                'name': 'Rashida Islam',
                'bio': 'Cultural heritage expert with deep knowledge of traditional Bengali culture, festivals, and customs. Perfect for cultural immersion tours.',
                'short_bio': 'Cultural guide specializing in Bengali traditions, folk music, and village life experiences.',
                'location': 'Shantahar',
                'district': 'Bogura',
                'division': 'Rajshahi',
                'specialization': 'cultural',
                'experience_level': 'intermediate',
                'phone': '+8801534567890',
                'email': 'rashida.culture@email.com',
                'daily_rate': 1800.00,
                'languages': 'Bengali, English',
                'rating': 4.5,
                'total_tours': 87,
                'featured': False,
            },
            {
                'name': 'Imam Hossain',
                'bio': 'Religious sites and pilgrimage expert. Knowledgeable about Islamic heritage sites, mosques, and religious practices in Bangladesh.',
                'short_bio': 'Specialized guide for religious tours and pilgrimage sites across Bangladesh.',
                'location': 'Sylhet',
                'district': 'Sylhet',
                'division': 'Sylhet',
                'specialization': 'religious',
                'experience_level': 'experienced',
                'phone': '+8801645678901',
                'email': 'imam.religious@email.com',
                'daily_rate': 2000.00,
                'languages': 'Bengali, English, Arabic',
                'rating': 4.7,
                'total_tours': 134,
                'featured': True,
            },
            {
                'name': 'Nasir Ahmed',
                'bio': 'Mountain and hill district specialist. Expert in Chittagong Hill Tracts with knowledge of tribal culture and mountain climbing.',
                'short_bio': 'Hill tracts expert with tribal culture knowledge and mountain climbing experience.',
                'location': 'Rangamati',
                'district': 'Rangamati',
                'division': 'Chittagong',
                'specialization': 'mountain',
                'experience_level': 'expert',
                'phone': '+8801756789012',
                'email': 'nasir.mountain@email.com',
                'daily_rate': 2800.00,
                'languages': 'Bengali, English, Marma',
                'rating': 4.8,
                'total_tours': 176,
                'featured': False,
            },
            {
                'name': 'Salma Khatun',
                'bio': 'Young and energetic guide with a passion for showing the modern and traditional sides of Dhaka. Great for city tours and food walks.',
                'short_bio': 'Dhaka city specialist offering food tours, street art walks, and modern city experiences.',
                'location': 'Dhanmondi',
                'district': 'Dhaka',
                'division': 'Dhaka',
                'specialization': 'cultural',
                'experience_level': 'intermediate',
                'phone': '+8801867890123',
                'email': 'salma.dhaka@email.com',
                'daily_rate': 2100.00,
                'languages': 'Bengali, English, Hindi',
                'rating': 4.4,
                'total_tours': 92,
                'featured': False,
            },
            {
                'name': 'Rafiq Uddin',
                'bio': 'Sundarbans specialist with extensive knowledge of mangrove forests, wildlife, and boat navigation through the world\'s largest delta.',
                'short_bio': 'Sundarbans expert guide specializing in wildlife tours and mangrove forest exploration.',
                'location': 'Khulna',
                'district': 'Khulna',
                'division': 'Khulna',
                'specialization': 'adventure',
                'experience_level': 'expert',
                'phone': '+8801978901234',
                'email': 'rafiq.sundarbans@email.com',
                'daily_rate': 3200.00,
                'languages': 'Bengali, English',
                'rating': 4.9,
                'total_tours': 234,
                'featured': True,
            }
        ]

        created_count = 0
        
        for guide_data in demo_guides:
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
            self.style.SUCCESS(f'\nCreated {created_count} new demo guides!')
        )