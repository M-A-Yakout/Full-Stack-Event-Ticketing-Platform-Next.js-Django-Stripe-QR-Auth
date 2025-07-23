# 🎫 Event Ticketing Platform

[![Next.js](https://img.shields.io/badge/Next.js-15.4.3-black?style=flat&logo=next.js)](https://nextjs.org/)
[![Django](https://img.shields.io/badge/Django-5.2.4-green?style=flat&logo=django)](https://www.djangoproject.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0.0-blue?style=flat&logo=typescript)](https://www.typescriptlang.org/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.3.3-06B6D4?style=flat&logo=tailwind-css)](https://tailwindcss.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python)](https://www.python.org/)

A full-stack event ticketing platform built with Next.js and Django, featuring QR code-based ticket validation, secure payments, and real-time event management.

## ✨ Features

- 🎪 Browse and search events
- 🔐 User authentication and authorization
- 💳 Secure payment processing with Stripe
- 🎟️ QR code-based ticket generation and validation
- 📱 Responsive design for all devices
- 🌐 RESTful API architecture

## 🚀 Tech Stack

### Frontend
- Next.js 15.4.3
- TypeScript
- TailwindCSS
- Radix UI Components
- Axios for API requests
- Framer Motion for animations

### Backend
- Django 5.2.4
- Django REST Framework
- SimpleJWT for authentication
- SQLite database
- QR Code generation
- Pillow for image processing

## 🛠️ Installation

### Prerequisites
- Node.js (v18 or higher)
- Python 3.11 or higher
- npm or yarn

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Start the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

## 🌐 Environment Setup

### Backend (.env)
```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### Frontend (.env.local)
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_STRIPE_PUBLIC_KEY=your_stripe_public_key
```

## 📱 Features Showcase

### Event Listing
- Grid-based event display
- Event details with images
- Price and location information
- Smooth loading animations

### User Management
- User registration and login
- JWT-based authentication
- Profile management
- Ticket history

### Ticket Management
- QR code generation for tickets
- Ticket validation system
- Check-in functionality
- Ticket transfer capability

## 🔒 API Security

- JWT authentication
- CORS configuration
- Permission-based access control
- Secure payment processing

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - Initial work - [Mohamed M.](https://github.com/M-A-Yakout)

## 🙏 Acknowledgments

- Next.js team for the amazing framework
- Django community for the robust backend framework
- All contributors who helped with the project
# Full-Stack-Event-Ticketing-Platform-Next.js-Django-Stripe-QR-Auth
