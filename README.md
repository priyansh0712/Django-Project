# Django Tweet Application 🐦

A simple yet elegant Twitter-like web application built with Django that demonstrates fundamental Django concepts and modern web development practices. This project showcases user authentication, CRUD operations, file uploads, and responsive design.

![Django](https://img.shields.io/badge/Django-5.2.6-green?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![HTML](https://img.shields.io/badge/HTML-CSS-orange?style=flat-square&logo=html5)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.8-purple?style=flat-square&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

## 🌟 Features

- **Tweet Management**: Create, read, update, and delete tweets
- **Photo Upload**: Attach images to your tweets
- **User Authentication**: Secure user login and registration system
- **Responsive Design**: Beautiful, mobile-friendly interface with Bootstrap
- **Modern UI**: Gradient backgrounds and smooth animations
- **CRUD Operations**: Full Create, Read, Update, Delete functionality
- **SQLite Database**: Lightweight database for development

## 🚀 Technologies Used

- **Backend**: Django 5.2.6
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.8
- **Database**: SQLite3
- **Python**: 3.x
- **File Handling**: Django's file upload system

## 📁 Project Structure

```
Django-Project/
├── Project/
│   ├── manage.py                 # Django management script
│   ├── Project/
│   │   ├── __init__.py
│   │   ├── settings.py          # Django settings
│   │   ├── urls.py              # Main URL configuration
│   │   ├── wsgi.py              # WSGI configuration
│   │   └── asgi.py              # ASGI configuration
│   ├── tweet/
│   │   ├── __init__.py
│   │   ├── apps.py              # App configuration
│   │   ├── models.py            # Tweet model
│   │   ├── views.py             # View functions
│   │   ├── forms.py             # Django forms
│   │   ├── urls.py              # App URL patterns
│   │   └── templates/
│   │       ├── tweet_list.html  # Tweet display template
│   │       └── tweet_delete.html # Delete confirmation
│   └── templates/
│       └── layout.html          # Base template
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.x installed on your system
- pip (Python package installer)
- Git

### Step-by-step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/priyansh0712/Django-Project.git
   cd Django-Project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   pip install Pillow  # For image handling
   ```

4. **Navigate to the project directory**
   ```bash
   cd Project
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Open your browser and go to `http://127.0.0.1:8000/`

## 🎯 Usage

### Main Features

1. **View Tweets**: Browse all tweets on the homepage
2. **Create Tweet**: Click "Post Tweet" to create a new tweet with text and optional photo
3. **Edit Tweet**: Modify your existing tweets
4. **Delete Tweet**: Remove tweets with confirmation dialog

### URL Patterns

- `/` - Display all tweets (homepage)
- `/create/` - Create a new tweet
- `/<int:tweet_id>/edit/` - Edit a specific tweet
- `/<int:tweet_id>/delete/` - Delete a specific tweet

## 🎨 UI Features

- **Modern Design**: Gradient backgrounds and smooth transitions
- **Responsive Layout**: Works perfectly on desktop and mobile devices
- **Bootstrap Integration**: Clean and professional styling
- **Interactive Elements**: Hover effects and animations
- **User-Friendly Navigation**: Intuitive interface design

## 🔧 Configuration

### Settings

The main settings are configured in `Project/settings.py`:

- **Debug Mode**: Currently set to `True` for development
- **Database**: SQLite3 (default)
- **Static Files**: Configured for CSS, JS, and images
- **Media Files**: Set up for user uploads

### Security Note

⚠️ **Important**: The `SECRET_KEY` in settings.py should be changed for production use!

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

## 🐛 Known Issues

- Secret key should be moved to environment variables for production
- Media files configuration may need adjustment for deployment
- User authentication flow can be enhanced

## 🔮 Future Enhancements

- [ ] User profiles and avatars
- [ ] Like and comment functionality
- [ ] Real-time updates
- [ ] Follow/unfollow users
- [ ] Tweet search functionality
- [ ] Email notifications
- [ ] API endpoints for mobile app

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Priyansh** - [@priyansh0712](https://github.com/priyansh0712)

## 🙏 Acknowledgments

- Django documentation and community
- Bootstrap for the responsive design framework
- The Django tutorial that inspired this project

## 📞 Support

If you have any questions or run into issues, please:

1. Check the [Issues](https://github.com/priyansh0712/Django-Project/issues) page
2. Create a new issue if your problem isn't already listed
3. Reach out via GitHub discussions

---

⭐ **Star this repository if you found it helpful!**

*Last updated: September 2025*
