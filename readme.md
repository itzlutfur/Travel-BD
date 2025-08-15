# Travel BD - Django Web Application

A comprehensive travel platform for exploring Bangladesh, connecting travelers with local guides and discovering amazing destinations across the country.

## 🌟 Features

### Core Functionality

- **Destination Discovery**: Browse and explore top destinations across Bangladesh
- **Guide Hiring**: Connect with experienced local guides
- **Tour Booking**: Book complete tour packages
- **User Authentication**: Secure registration and login system
- **Responsive Design**: Mobile-first responsive web design

### User Features

- Browse featured destinations and guides
- Detailed destination and guide profiles
- Advanced search and filtering
- Booking management system
- User reviews and ratings
- Secure payment integration

### Admin Features

- Content management system
- Booking management
- User management
- Analytics dashboard
- Guide verification system

## 🚀 Technology Stack

### Backend

- **Framework**: Django 4.x
- **Database**: PostgreSQL/SQLite
- **Authentication**: Django Auth
- **Admin Interface**: Django Admin

### Frontend

- **CSS Framework**: Tailwind CSS
- **JavaScript**: Vanilla JS with modern ES6+
- **Icons**: Heroicons
- **Responsive Design**: Mobile-first approach

### Development Tools

- **Version Control**: Git
- **Package Management**: pip
- **Environment**: Python Virtual Environment

## 📁 Project Structure

```
Travel_BD Django/
├── core/                   # Core application (Homepage, etc.)
├── destination/            # Destination management
├── hire_guide/            # Guide hiring system
├── tour_booking/          # Tour booking system
├── accounts/              # User authentication
├── static/                # Static files (CSS, JS, Images)
├── templates/             # HTML templates
├── media/                 # User uploaded files
├── travel_bd/             # Main project settings
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── README.md             # Project documentation
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- Git
- Virtual Environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/travel-bd-django.git
cd travel-bd-django
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration

Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Step 5: Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Step 6: Collect Static Files

```bash
python manage.py collectstatic
```

### Step 7: Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the application.

## 🗄️ Database Models

### Core Models

- **User**: Extended Django user model
- **Destination**: Travel destinations
- **Guide**: Local tour guides
- **Booking**: Tour bookings
- **Review**: User reviews and ratings

### Key Relationships

- User → Bookings (One-to-Many)
- Guide → Bookings (One-to-Many)
- Destination → Bookings (One-to-Many)
- User → Reviews (One-to-Many)

## 🎨 Design System

### Color Palette

- **Primary Blue**: `#2563eb`
- **Primary Green**: `#16a34a`
- **Secondary**: `#64748b`
- **Accent**: `#fbbf24`

### Typography

- **Headings**: Font weights 600-800
- **Body**: Font weight 400-500
- **Responsive**: Base 16px, scaling with breakpoints

### Components

- Cards with rounded corners and shadows
- Gradient buttons with hover effects
- Glass-morphism elements
- Smooth transitions and animations

## 📱 Responsive Breakpoints

```css
/* Tailwind CSS Breakpoints */
sm: 640px    /* Small devices */
md: 768px    /* Tablets */
lg: 1024px   /* Laptops */
xl: 1280px   /* Desktops */
2xl: 1536px  /* Large screens */
```

## 🔐 Authentication System

### User Types

- **Travelers**: Regular users who book tours
- **Guides**: Service providers
- **Admins**: System administrators

### Features

- Registration with email verification
- Secure login/logout
- Password reset functionality
- Profile management
- Role-based permissions

## 📊 Admin Panel

Access the admin panel at `/admin/` with superuser credentials.

### Manageable Content

- Users and profiles
- Destinations and categories
- Guides and specializations
- Bookings and payments
- Reviews and ratings
- Site settings

## 🧪 Testing

### Run Tests

```bash
python manage.py test
```

### Test Coverage

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

## 🚀 Deployment

### Production Settings

1. Set `DEBUG=False`
2. Configure production database
3. Set up static file serving
4. Configure email backend
5. Set secure headers

### Deployment Platforms

- **Heroku**: Easy deployment with Procfile
- **DigitalOcean**: VPS deployment
- **AWS**: Scalable cloud deployment
- **Railway**: Modern deployment platform

### Environment Variables

```env
DEBUG=False
SECRET_KEY=production-secret-key
DATABASE_URL=postgresql://user:pass@host:port/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## 🤝 Contributing

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Submit a pull request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions/classes
- Keep functions small and focused

### Commit Messages

```
feat: add new destination search feature
fix: resolve booking date validation issue
docs: update API documentation
style: format code with black
test: add unit tests for guide model
```

## 📝 API Documentation

### Endpoints

- `GET /api/destinations/` - List destinations
- `GET /api/guides/` - List guides
- `POST /api/bookings/` - Create booking
- `GET /api/user/profile/` - User profile

### Authentication

API uses Django REST Framework token authentication.

## 🐛 Troubleshooting

### Common Issues

**Database Errors**

```bash
python manage.py migrate --run-syncdb
```

**Static Files Not Loading**

```bash
python manage.py collectstatic --clear
```

**Permission Errors**

```bash
# Check file permissions
ls -la
chmod +x manage.py
```

### Logs

Check Django logs in the console or configure logging in settings.py.

## 📞 Support

### Getting Help

- Check the [Wiki](https://github.com/yourusername/travel-bd-django/wiki)
- Open an [Issue](https://github.com/yourusername/travel-bd-django/issues)
- Join our [Discord](https://discord.gg/travel-bd)

### Contact

- **Email**: support@travel-bd.com
- **Website**: https://travel-bd.com
- **Documentation**: https://docs.travel-bd.com

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Django community for the amazing framework
- Tailwind CSS for the utility-first CSS framework
- Heroicons for the beautiful icon set
- Contributors and beta testers

## 🔮 Future Enhancements

- [ ] Mobile app development
- [ ] Real-time chat system
- [ ] Advanced analytics dashboard
- [ ] Multi-language support
- [ ] Payment gateway integration
- [ ] Social media integration
- [ ] PWA implementation
- [ ] AI-powered recommendations

---

**Made with ❤️ for Bangladesh Tourism**

_Last updated: August 2025_
