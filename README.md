🧠 Django CV Builder

A full-featured Django web application that allows users to build, edit, and download professional CVs/resumes with ease.
This project helps individuals quickly generate optimized resumes using customizable templates, smart field validation, and automatic formatting — all within a secure and responsive web interface.

🚀 Features

✅ User-Friendly Resume Builder — Step-by-step interface for adding personal details, education, experience, and skills.
✅ Multiple Resume Templates — Choose from pre-designed templates optimized for clarity and applicant tracking systems (ATS).
✅ AI-Assisted Suggestions (optional) — Smart hints or pre-filled content ideas for roles, skills, and summaries.
✅ Export to PDF/Docx — Generate downloadable CVs in professional formats using Django templating and libraries like xhtml2pdf or wkhtmltopdf.
✅ Multi-Resume Support — Users can create and manage multiple versions of their resumes.
✅ Secure Authentication System — Django’s built-in authentication for user registration, login, and data privacy.
✅ Responsive Design — Fully mobile-friendly for creating or editing CVs on the go.
✅ Auto-Save Drafts — Resume data is automatically saved to prevent accidental loss.
✅ Spell Checker & Grammar Enhancer (optional) — Improve text quality using integrated proofing tools.
✅ Dashboard Analytics — Track versions, downloads, and edit history.

🛠️ Tech Stack
Component	Technology
Framework	Django (Python 3.10+)
Frontend	HTML5, CSS3, Bootstrap 5, JavaScript
Database	SQLite (default) / PostgreSQL (optional)
Authentication	Django Auth System
PDF Generation	xhtml2pdf / wkhtmltopdf
Environment	Virtualenv / venv
Deployment	Gunicorn + Nginx / Render / Heroku
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/Django-Cv-Builder.git
cd Django-Cv-Builder

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate it

Windows:

venv\Scripts\activate


macOS/Linux:

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create a superuser
python manage.py createsuperuser

7️⃣ Run the development server
python manage.py runserver


Open your browser and visit http://127.0.0.1:8000/
 🎉

📁 Folder Structure
Django-Cv-Builder/
│
├── cvbuilder/              # Main Django app
│   ├── templates/           # HTML templates (resume templates, forms, dashboard)
│   ├── static/              # CSS, JS, images
│   ├── models.py            # Resume, Education, Experience models
│   ├── views.py             # Main business logic
│   ├── forms.py             # Form definitions
│   ├── urls.py              # Application URLs
│   └── ...
│
├── cvbuilder_project/       # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md

🧩 How It Works

User signs up or logs in.

Fills out resume details (personal info, education, experience, etc.).

Preview updates dynamically as user enters data.

Choose a professional template.

Export to PDF or download the resume.

Optionally, edit or duplicate for another job role.

🎨 Resume Templates

You can easily create or modify templates inside:

/templates/resumes/


Each template extends a base layout for consistency.
Example: modern.html, classic.html, minimalist.html.

📦 Example .env Configuration
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1, localhost
DATABASE_URL=sqlite:///db.sqlite3

🧪 Testing

Run Django’s built-in test suite:

python manage.py test

🌍 Deployment (Optional)

To deploy on Render, Heroku, or VPS:

Set DEBUG=False

Collect static files:

python manage.py collectstatic


Configure database in settings.py or via environment variables.

Use Gunicorn:

gunicorn cvbuilder_project.wsgi:application

🧠 Future Improvements

✅ AI-based auto-summary and skill suggestions.

✅ Resume sharing via public URLs.

✅ Template marketplace.

✅ Dark mode interface.

✅ Integration with LinkedIn/Indeed APIs for profile import.

🤝 Contributing

Contributions are welcome!
If you’d like to improve the project:

Fork the repo.

Create a new branch (feature/awesome-feature).

Commit changes and push to your fork.

Submit a Pull Request.

🪪 License

This project is licensed under the MIT License — feel free to use, modify, and share responsibly.
See the LICENSE file for details.

👨‍💻 Author

Elvis Njaramba
💼 Full-Stack Web Developer (Python/Django | HTML | CSS | JS | React)
📧 [your.email@example.com
]
🌐 [yourportfolio.com]
📱 Passionate about building elegant and efficient web solutions.
