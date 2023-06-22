import smtplib
import sqlite3
import logging

from flask import Flask, render_template, request

# Configurating application
app = Flask(__name__)

# Configurating SQLite database
conn = sqlite3.connect("letters.db")
cursor = conn.cursor()

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Defining routes
@app.route("/", methods=["GET", "POST"])
def layout()-> str:
    """Render the home page.

    Handles GET and POST requests to the / route.
    GET request: Renders the layout.html template.
    POST request: Handles newsletter form submission. 
    Adds all the added information to a database "letters", 
    as it is created for demostration purposes only.

    Returns:
        str: Rendered HTML content.
    """

    # Creating form for newsletter
    if request.method == "GET":
        return render_template("layout.html")
    name = request.form.get("name")
    email = request.form.get("email")

    # Adding data from form to data base
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)", 
        (name, email)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return render_template("layout.html")


@app.route("/contact", methods=["GET", "POST"])
def contact() -> str:
    """Render the contact page.

    Handles GET and POST requests to the /contact route.
    GET request: Renders the contact.html template.
    POST request: Handles form submission.

    Returns:
        str: Rendered HTML content.
    """
    return render_template("contact.html")

@app.route("/italy")
def italy() -> str:
    """Render the content page "Italy" .

    Returns:
        str: Rendered HTML content.
    """
    return render_template("italy.html")

@app.route("/form")
def form()-> str:
    """Render the payment form page.

    The payment form allows users to choose a package to purchase
    and fill out their details. Note that this form is for
    demonstration purposes only and does not process actual payments.

    Returns:
        str: Rendered HTML content of the payment form.
    """
    return render_template("form.html")

@app.route("/send-email", methods=["POST"])
def send_email() -> str:
    """Handle the contact form submission and send an email.

    This function is responsible for handling the form submission of the
    contact form. It validates the form data, including the name, email,
    and message fields. If any required field is missing, it returns an
    error message prompting the user to fill out all fields.

    If all form data is provided, the function constructs an email message
    containing the user's name, email, and message. It then uses a configured
    SMTP server to send the email to the specified recipient email address.

    Note:
        This function assumes the availability of a properly configured
        SMTP server for sending emails.

    Returns:
        str: A success message if the email was sent successfully,
             or an error message if there was a problem sending the email.

    Raises:
        smtplib.SMTPException: If an error occurs during the email sending process.
    """
    # Function implementation

    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Validating the form data
    if not name or not email or not message:
        return "Please fill out all fields."

    # Setting the recipient email address
    to = "Theworldonaplate2023@outlook.com" # pylint: disable=unused-variable

    # Setting the email subject
    subject = "New contact"

    # Setting the email message
    email_message = "Subject: " + subject + "\n"
    email_message = "Name: " + name + "\n\n"
    email_message += "Email: " + email + "\n\n"
    email_message += "Message:\n" + message + "\n"

    # Sending the email
    try:
        smtp_server = "smtp.office365.com"
        port = 587
        sender_email = "Theworldonaplate2023@outlook.com"
        password = "Rivnecity1970?"
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, to, email_message)
        server.quit()

        return "Thank you for your message!"
    # Error Handling and Logging
    except smtplib.SMTPException as exception: # pylint: disable=unused-variable
        error_message = "An error occurred while sending the email. Please try again later."
        logging.exception(error_message)
        return error_message

@app.route("/packages")
def packages() -> str:
    """Render the content page "Italy" .

    Returns:
        str: Rendered HTML content.
    """
    return render_template("packages.html")
