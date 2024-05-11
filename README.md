
# Zodiac Compatibility Emailer

A web-based Zodiac Compatibility Emailer that allows users to find out their zodiac compatibility and receive it via email.


## Features

- **Email Zodiac Compatibility Reports:** Users can enter their email and zodiac sign to receive their zodiac compatibility reports directly in their inbox.
- **Interactive Web Interface:** A user-friendly Flask-based GUI where users can input their details and submit the form to get results.
- **Dynamic Zodiac Sign Dropdown:** Dynamically generated dropdown for zodiac signs ensures a user-friendly experience.
- **Robust Error Handling:** Clear and informative error messages guide the user through correcting inputs.
- **Mobile Responsive Design:** Ensures that the web application is usable on both desktop and mobile devices.



## Tech Stack

**Python:** Core programming language.
- **Flask:** Web framework used to build the server-side application.
- **HTML/CSS:** For structuring and styling the web interface.
- **JavaScript (minimal if used):** For enhancing frontend interactivity.


## Prerequisites

Before running this project, you need to have Python and Flask installed on your system.
## Installation

Clone the repository:

```bash
 git clone https://github.com/SeanMarkWD/Zodiac-Compat-Mailer.git
  cd Zodiac-Compatibility-Emailer
```
    
pip install -r requirements.txt

The application uses the Twin Flame Horoscope API to fetch zodiac compatibility data. You will need to obtain an API key to use the API:

### Sign up for an API key:

- Visit [Twin Flame's Developer Site](https://www.twinflamedev.com/api) to sign up for an API key. They offer a **7-day free trial** on monthly subscriptions, which you can use to test the application.

### Set up your API key:

- Once you have your API key, you need to set it in your environment variables. Create a `.env` file in the root of your project and add the following:

  ```env
  TWIN_FLAME_API=your_api_key_here
  FLASK_SECRET_KEY=your_secret_key_here
  SENDER_EMAIL=your_email_here
  SENDER_PASSWORD=your_email_password_here

Replace your_api_key_here with your actual Twin Flame API key.
