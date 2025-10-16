# 🧠 Django CV Builder

A full-featured Django web application that allows users to build, edit, and download professional CVs/resumes with ease.
This project helps individuals quickly generate optimized resumes using customizable templates, smart field validation, and automatic formatting — all within a secure and responsive web interface.

# 🚀 Features
1. User-Friendly Resume Builder — Step-by-step interface for adding personal details, education, experience, and skills.
2. Multiple Resume Templates — Choose from pre-designed templates optimized for clarity and applicant tracking systems (ATS).
3. Export to PDF/Docx — Generate downloadable CVs in professional formats using Django templating and libraries like xhtml2pdf or wkhtmltopdf.
4. Multi-Resume Support — Users can create and manage multiple versions of their resumes.
5. Secure Authentication System — Django’s built-in authentication for user registration, login, and data privacy.
6. Responsive Design — Fully mobile-friendly for creating or editing CVs on the go.
7. Auto-Save Drafts — Resume data is automatically saved to prevent accidental loss.
8. Dashboard Analytics — Track versions, downloads, and edit history.

# 🛠️ Tech Stack
Framework	Django (Python 3.10+)
Frontend	HTML5, CSS3, Bootstrap 5, JavaScript
Database	SQLite (default) 
Authentication	Django Auth System
PDF Generation	xhtml2pdf / wkhtmltopdf
Environment	Virtualenv / venv

# ⚙️ Installation & Setup
1. Clone the repository
> git clone https://github.com/<your-username>/Django-Cv-Builder.git
> cd Django-Cv-Builder

2. Create a virtual environment
> python -m venv venv

3. Activate it

Windows:

> venv\Scripts\activate


macOS/Linux:

> source venv/bin/activate

4. Install dependencies
> pip install -r requirements.txt

5. Run migrations
> python manage.py makemigrations
> python manage.py migrate

6. Create a superuser
> python manage.py createsuperuser

7. Run the development server
> python manage.py runserver


Open your browser and visit http://127.0.0.1:8000/

# 🧩 How It Works

User signs up or logs in.

Fills out resume details (personal info, education, experience, etc.).

Preview updates dynamically as user enters data.

Choose a professional template.

Export to PDF or download the resume.

# 🎨 Resume Templates

You can easily create or modify templates inside:

/templates/resumes/


Each template extends a base layout for consistency.
Example: modern.html, classic.html, minimalist.html.

# 📦 Example .env Configuration
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost
DATABASE_URL=sqlite:///db.sqlite3

# 👨‍💻 Author

Elvis Njaramba
💼 Full-Stack Web Developer (Python/Django | HTML | CSS | JS | React)

