from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from destination.models import Destination


class Command(BaseCommand):
    help = 'Add sample destinations to the database'

    def generate_unique_slug(self, name):
        """Generate a unique slug for the destination"""
        base_slug = slugify(name)
        slug = base_slug
        counter = 1
        
        while Destination.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        
        return slug

    def handle(self, *args, **options):
        # Get or create a user for created_by field
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@travelbd.com', 'is_staff': True, 'is_superuser': True}
        )

        destinations_data = [
            {
                'name': "Cox's Bazar",
                'description': """Cox's Bazar is the longest natural sea beach in the world, stretching over 120 kilometers. 
                Located in the southeastern part of Bangladesh, it's famous for its golden sandy beach, clear blue waters, 
                and stunning sunsets. The area offers various activities including surfing, paragliding, and water sports. 
                The nearby Himchari National Park and Inani Beach add to the natural beauty of this coastal paradise.""",
                'short_description': "World's longest natural sea beach with golden sand and crystal clear waters.",
                'location': "Cox's Bazar Sadar",
                'district': "Cox's Bazar",
                'division': 'Chittagong',
                'category': 'beach',
                'best_time_to_visit': 'November to March',
                'entry_fee': 0.00,
                'duration': '2-3 days',
                'difficulty_level': 'easy',
                'latitude': 21.4272,
                'longitude': 92.0058,
                'featured': True,
            },
            {
                'name': 'Sundarbans',
                'description': """The Sundarbans is the largest mangrove forest in the world and a UNESCO World Heritage Site. 
                This unique ecosystem is home to the Royal Bengal Tiger, spotted deer, crocodiles, and over 270 bird species. 
                The forest spans across Bangladesh and India, with intricate networks of rivers, creeks, and islands. 
                Visitors can explore by boat, experiencing the wild beauty and biodiversity of this natural wonder.""",
                'short_description': "World's largest mangrove forest and home to the Royal Bengal Tiger.",
                'location': 'Khulna Region',
                'district': 'Khulna',
                'division': 'Khulna',
                'category': 'nature',
                'best_time_to_visit': 'October to March',
                'entry_fee': 500.00,
                'duration': '2-4 days',
                'difficulty_level': 'moderate',
                'latitude': 22.4876,
                'longitude': 89.5319,
                'featured': True,
            },
            {
                'name': 'Srimangal',
                'description': """Known as the tea capital of Bangladesh, Srimangal is famous for its sprawling tea gardens, 
                lush green hills, and diverse wildlife. The area is home to Lawachara National Park, where visitors can 
                spot various species of birds and primates. The seven-color tea, a local specialty, is a must-try. 
                The serene environment and cool climate make it perfect for nature lovers and photography enthusiasts.""",
                'short_description': "Tea capital of Bangladesh with lush tea gardens and wildlife sanctuaries.",
                'location': 'Srimangal Upazila',
                'district': 'Moulvibazar',
                'division': 'Sylhet',
                'category': 'nature',
                'best_time_to_visit': 'October to April',
                'entry_fee': 50.00,
                'duration': '1-2 days',
                'difficulty_level': 'easy',
                'latitude': 24.3065,
                'longitude': 91.7296,
                'featured': True,
            },
            {
                'name': 'Rangamati',
                'description': """Rangamati, known as the 'Lake City of Bangladesh', is built around Kaptai Lake, 
                the largest artificial lake in the country. This hill district offers breathtaking scenery with 
                hills, forests, and lake views. Visitors can enjoy boat rides, visit tribal villages, explore 
                hanging bridges, and experience the unique culture of indigenous communities. The area is perfect 
                for eco-tourism and cultural exploration.""",
                'short_description': "Scenic hill district known as the 'Lake City' with Kaptai Lake and tribal culture.",
                'location': 'Rangamati Sadar',
                'district': 'Rangamati',
                'division': 'Chittagong',
                'category': 'nature',
                'best_time_to_visit': 'October to March',
                'entry_fee': 100.00,
                'duration': '2-3 days',
                'difficulty_level': 'easy',
                'latitude': 22.6533,
                'longitude': 92.1761,
                'featured': False,
            },
            {
                'name': 'Sajek Valley',
                'description': """Sajek Valley is one of the most beautiful hill stations in Bangladesh, offering 
                panoramic views of mountains, clouds, and valleys. Located in the Rangamati district, it's famous 
                for its cloud-kissed peaks and stunning sunrise/sunset views. The area is inhabited by various 
                indigenous communities, adding cultural richness to the natural beauty. Adventure seekers can 
                enjoy trekking, camping, and photography.""",
                'short_description': "Spectacular hill station with cloud-kissed peaks and panoramic mountain views.",
                'location': 'Sajek Union',
                'district': 'Rangamati',
                'division': 'Chittagong',
                'category': 'mountain',
                'best_time_to_visit': 'October to April',
                'entry_fee': 0.00,
                'duration': '1-2 days',
                'difficulty_level': 'moderate',
                'latitude': 23.3833,
                'longitude': 92.2833,
                'featured': True,
            },
            {
                'name': 'Paharpur',
                'description': """Paharpur is home to the ruins of the ancient Buddhist monastery Somapura Mahavihara, 
                a UNESCO World Heritage Site. Dating back to the 8th century, it was once the largest Buddhist monastery 
                south of the Himalayas. The site features impressive brick structures, intricate terracotta plaques, 
                and sculptures that showcase the rich Buddhist heritage of the region. It's a must-visit for history 
                and archaeology enthusiasts.""",
                'short_description': "UNESCO World Heritage Site featuring ancient Buddhist monastery ruins.",
                'location': 'Paharpur Village',
                'district': 'Naogaon',
                'division': 'Rajshahi',
                'category': 'archaeological',
                'best_time_to_visit': 'October to March',
                'entry_fee': 30.00,
                'duration': '3-4 hours',
                'difficulty_level': 'easy',
                'latitude': 25.0300,
                'longitude': 88.9769,
                'featured': False,
            },
            {
                'name': 'Sixty Dome Mosque',
                'description': """The Sixty Dome Mosque (Shait Gumbad Mosque) in Bagerhat is a UNESCO World Heritage Site 
                and one of the finest examples of Islamic architecture in Bangladesh. Built in the 15th century by 
                Khan Jahan Ali, this magnificent mosque features 60 domes, 7 longitudinal aisles, and 11 transverse 
                aisles. The mosque is made of burnt brick and represents the early Islamic architectural style in Bengal.""",
                'short_description': "UNESCO World Heritage mosque showcasing magnificent Islamic architecture.",
                'location': 'Bagerhat Sadar',
                'district': 'Bagerhat',
                'division': 'Khulna',
                'category': 'historical',
                'best_time_to_visit': 'October to March',
                'entry_fee': 20.00,
                'duration': '2-3 hours',
                'difficulty_level': 'easy',
                'latitude': 22.6742,
                'longitude': 89.7875,
                'featured': False,
            },
            {
                'name': 'Kuakata',
                'description': """Kuakata is a unique beach destination where you can witness both sunrise and sunset 
                from the same location. Known as the 'Daughter of the Sea', this 18-kilometer-long beach offers 
                panoramic views of the Bay of Bengal. The area is also culturally significant to the Rakhine community. 
                Visitors can enjoy beach activities, visit the Buddhist temple, and explore the nearby mangrove forests.""",
                'short_description': "Unique beach where you can see both sunrise and sunset from the same spot.",
                'location': 'Kuakata Upazila',
                'district': 'Patuakhali',
                'division': 'Barisal',
                'category': 'beach',
                'best_time_to_visit': 'October to March',
                'entry_fee': 0.00,
                'duration': '1-2 days',
                'difficulty_level': 'easy',
                'latitude': 21.8167,
                'longitude': 90.1167,
                'featured': True,
            },
            {
                'name': 'Ratargul Swamp Forest',
                'description': """Ratargul is the only swamp forest in Bangladesh, located in Sylhet. This unique 
                freshwater swamp forest is home to various species of trees, birds, and wildlife. During monsoon, 
                the forest remains submerged, creating a mystical atmosphere. Visitors can explore by boat during 
                the wet season or walk through during the dry season. It's a paradise for nature photographers 
                and bird watchers.""",
                'short_description': "Bangladesh's only swamp forest offering unique boat tours through submerged trees.",
                'location': 'Gowainghat Upazila',
                'district': 'Sylhet',
                'division': 'Sylhet',
                'category': 'forest',
                'best_time_to_visit': 'June to October (for boat tours)',
                'entry_fee': 50.00,
                'duration': '3-4 hours',
                'difficulty_level': 'easy',
                'latitude': 25.0083,
                'longitude': 91.8833,
                'featured': False,
            },
            {
                'name': 'Bandarban',
                'description': """Bandarban is the most mountainous district in Bangladesh, offering spectacular 
                hill landscapes, tribal culture, and adventure activities. Home to the highest peaks in the country 
                including Keokradong and Tahjindong, it's a paradise for trekkers and adventure enthusiasts. 
                The area features Buddhist temples, tribal villages, waterfalls, and diverse flora and fauna. 
                Visitors can experience unique tribal cultures and enjoy activities like hiking and camping.""",
                'short_description': "Mountainous district with highest peaks, tribal culture, and adventure activities.",
                'location': 'Bandarban Sadar',
                'district': 'Bandarban',
                'division': 'Chittagong',
                'category': 'mountain',
                'best_time_to_visit': 'October to April',
                'entry_fee': 0.00,
                'duration': '2-4 days',
                'difficulty_level': 'hard',
                'latitude': 22.1953,
                'longitude': 92.2183,
                'featured': True,
            },
        ]

        for dest_data in destinations_data:
            # Generate unique slug
            dest_data['slug'] = self.generate_unique_slug(dest_data['name'])
            
            # Try to create destination
            try:
                destination, created = Destination.objects.get_or_create(
                    name=dest_data['name'],
                    defaults={**dest_data, 'created_by': user}
                )
                
                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Successfully created destination: {destination.name} (slug: {destination.slug})')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Destination already exists: {destination.name}')
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error creating destination {dest_data["name"]}: {str(e)}')
                )

        self.stdout.write(
            self.style.SUCCESS('Successfully completed adding sample destinations!')
        )