
# Django Quiz Application

This is a Django-based web application that allows users to take quizzes. The app supports multiple-choice questions, tracks answers, shows whether answers are correct or incorrect, and calculates the final score at the end of the quiz.

## Features

- **Start a New Quiz**: Users can start a new quiz session and answer questions one by one.
- **Multiple-Choice Questions**: Each question has multiple answers, where users can select the correct answer.
- **Real-Time Feedback**: After answering each question, users are shown whether their answer is correct or incorrect.
- **Progressive Quiz Flow**: The quiz progresses smoothly with the option to move to the next question after submitting an answer.
- **Final Score**: Once the quiz is completed, users can see their score with a breakdown of correct and incorrect answers.
- **Prevent Navigation**: Users are warned if they attempt to leave the page mid-quiz.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, HTMX
- **Database**: SQLite (for development, can be switched to PostgreSQL in production)
- **Version Control**: Git & GitHub

## Installation

### Prerequisites

1. Python 3.6 or higher
2. Django 4.x
3. Git

### Steps to Run the Project Locally

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/quiz-app.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd quiz-app
   ```

3. **Create a Virtual Environment** (Optional but recommended):

   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**:

   - On Windows:

     ```bash
     venv\Scriptsctivate
     ```

   - On Mac/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

7. **Create a Superuser** (Optional, for admin access):

   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

9. **Access the Application**:

   Open a web browser and go to `http://127.0.0.1:8000/` to start using the quiz app.

## Usage

### How to Take a Quiz:

1. **Start a Quiz**: Navigate to the home page and click on "Start a quiz" to begin.
2. **Answer Questions**: Select an answer for each multiple-choice question and click "Submit your answer."
3. **View Feedback**: After each question, you'll see whether your answer was correct or incorrect.
4. **Finish the Quiz**: Once all questions are answered, the final score will be displayed along with a breakdown of correct and incorrect answers.

### How to Create a New Quiz:

1. **Login to Admin Panel**: Go to `http://127.0.0.1:8000/admin/` and login with the superuser credentials.
2. **Add a Quiz**: In the admin panel, create a new quiz by adding a `Quiz` instance.
3. **Add Questions and Answers**: After creating a quiz, add questions and their corresponding multiple-choice answers. Mark the correct answer for each question.

## File Structure

```
quiz-app/
│
├── core/                 # Main project directory
│   ├── settings.py               # Django project settings
│   ├── urls.py                   # URL routing
│   ├── wsgi.py                   # WSGI config for production
│   └── asgi.py                   # ASGI config
│
├── sim/                          # Quiz app directory
│   ├── migrations/               # Database migrations
│   ├── models.py                 # Database models (Quiz, Question, Answer)
│   ├── views.py                  # View functions handling the quiz logic
│   ├── urls.py                   # URL routing for quiz-related views
│   ├── start.html                # Display the starting page of the quizz app
│   ├── templates/                # HTML templates for quiz app
│   │   ├── question.html         # Display questions and options
│   │   ├── answer.html           # Display answer feedback
│   │   └── finish.html           # Display final score
│
├── db.sqlite3                    #The database file
├── quiz_data.yaml                # Yaml file which contains all the          
                                     questions and their answers
├── manage.py                     # Django management script
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## Common Issues and Troubleshooting

- **Database Errors**: Ensure that you have run `python manage.py migrate` to apply the migrations and set up the database.
- **Missing Dependencies**: If you encounter `ModuleNotFoundError`, make sure you have installed all dependencies listed in `requirements.txt`.

## Deployment

### Deploying on Heroku

1. **Install Heroku CLI**: Download and install the Heroku CLI from [here](https://devcenter.heroku.com/articles/heroku-cli).
2. **Login to Heroku**:

   ```bash
   heroku login
   ```

3. **Create a Heroku Application**:

   ```bash
   heroku create
   ```

4. **Add Heroku Remote**:

   ```bash
   git remote add heroku https://git.heroku.com/your-app-name.git
   ```

5. **Deploy to Heroku**:

   ```bash
   git push heroku main
   ```

6. **Migrate Database on Heroku**:

   ```bash
   heroku run python manage.py migrate
   ```

7. **Open the App**:

   ```bash
   heroku open
   ```

### Deploying on Vercel/Netlify

1. **Push your code to GitHub**.
2. **Connect your repository to Vercel/Netlify** (both support automatic Django deployments).
3. **Add necessary environment variables** (e.g., `SECRET_KEY`, `ALLOWED_HOSTS`, database credentials).
4. **Deploy and access your live application**.

## Contributing

1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
