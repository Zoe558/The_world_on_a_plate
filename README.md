# THE WORLD ON A PLATE
#### Video Demo:  <https://youtu.be/IW8Mf-DMWGg>

#### Table of Contents
##### [Introduction](#Introduction)
##### [Description](#Description)
##### [Technologies](#Technologies)


### Introduction

##### CS50

This was my final project to conclude the CS50 Introduction to Computer Science course.

##### Explaining the project

My final project is a web application that will allow users to get the information about world's cuisines and also purchase a package, that will include meal plan for different amount of days for a specific country.

##### Inspiration

The idea is originally mine and I wanted to create a web application that will connect both of my passions, that are travelling and cooking. On the finished website, I would like to see all the countries of the world presented so that people from Asia can not only have a meal plan presented to them, but also travel to Africa or Europe from their kitchen.
### Description

***Homepage (layout.html):***
 Maine page will give an information for users about what company offers, as well as interactive map and a photogallery of countries that people can order a meal plan from. This page will also provide an oportunity to sign up for a newsletter from a company, that will save contact information in a database and present team members with a possibility of contacting them.

***Country description (italy.html):***
  This file is an example of a specific country that users are interested in. From the maine page they can access to it by presing on a country on the intarective map or follow the link from a photogallery. On this page people can order the package they like, depending on amount of days or weeks and other services they are looking for. After pressing "order now", they will be sent to a payform.

***Example of a package (packages.html):***
  I have created this file as an example of how a meal plan dor a day will look like.

***Contact information (contact.html):***
  On this page users will have all the contact information about the company as well as access to a form that they can use to send a message. I have programmed it so company email account ("outlook.com"), will recieve this message.

***Payform (form.html):***
  This file is created so that users can purchase a plan directly from a website. They have couple of ways of accessing it: they can choose the plan they are interested in on the page of a specific country or they can press a link after a meal plan example that i have created.


### Technologies

* Python

I have created an app.py file to make a base for my application and also connect all the programming languages that I will be using. It was also needed to create routes, work with my data base and check my forms. Also with a help of Python I programmed the application to send an email to a "company" email address, to recieve a message from a contact form.

      @app.route('/send-email', methods=['POST'])
      def send_email():
          name = request.form['name']
          email = request.form['email']
          message = request.form['message']

          # Validate the form data
          if not name or not email or not message:
            return 'Please fill out all fields.'

          # Seting the recipient email address
          to = "*****@outlook.com"

          # Seting the email subject
          subject = "New contact"

          # Seting the email message
          email_message = "Name: " + name + "\n\n"
          email_message += "Email: " + email + "\n\n"
          email_message += "Message:\n" + message + "\n"

          # Sending the email
          try:
            smtp_server = "smtp.office365.com"
            port = 587
            sender_email = "*****@outlook.com"
            password = "******"
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, to, email_message)
            server.quit()

            return "Thank you for your message!"
            return render_template("layout.html")
           except Exception as e:
            print(e)
            return "There was a problem sending your message."


* HTML

I have created a layout.html file that shows the main homepage and all the needed extends.

* CSS

With CSS I've designed all my pages to my liking and also tried to make it user-friendly and connected.

* SQL

For my newsletter part, I wanted to have contact information of my users to be saved to a data base, so I have created a database letters.db and updating it with a help of Python.

      @app.route("/", methods=["GET", "POST"])
      def layout():

          # Receive newsletter
          if request.method == "GET":
              return render_template("layout.html")
          else:
              name = request.form.get("name")
              mail = request.form.get("mail")

          db.execute("INSERT INTO users ( name, email) VALUES (:name, :email)", name=name, email=mail)
          return render_template("layout.html")

* Jinja

Jinja helped me to connect all my HTML files.

* JavaScript

To make my application more interactive, I have created a couple of features in JavaScript that help users move around the web comfortably and make their experience easier, allowing them to focus on the main purpose of an application, that is to purchase a package. One of the feautures was a calculator for my payform:

    // Getting the elements from the form
    const countrySelect = document.querySelector('#country-select');
    const packageSelect = document.querySelector('#package-select');
    const totalValue = document.querySelector('#total-value');

    // Defining the prices for the different packages
    const packagePrices = {
      'Basic': 10,
      'Deluxe': 50,
      'Super Deluxe': 70
    };

    // Defining the taxes for the different countries
    const countryTaxes = {
      'Afghanistan': 0.05,
      'Åland Islands': 0.1,
      'Albania': 0.2,
      'Algeria': 0.15,
      'American Samoa': 0.1,
      'Andorra': 0.2,
      'Angola': 0.15,
      'Anguilla': 0.1,
      'Antarctica': 0.05,
      'Antigua and Barbuda': 0.1,
      'Argentina': 0.2,
      'Armenia': 0.2,
      'Aruba': 0.1,
      'Australia': 0.1,
      'Austria': 0.2,
      'Azerbaijan': 0.2,
      'Bahamas': 0.1,
      'Bahrain': 0.15,
      'Bangladesh': 0.2,
      'Barbados': 0.1,
      'Belarus': 0.2
      };

    // Calculating the total value based on the selected country and package
    function calculateTotal() {
         const selectedPackage = packageSelect.value;
         const packagePrice = packagePrices[selectedPackage];
         const selectedCountry = countrySelect.value;
         const countryTax = countryTaxes[selectedCountry];
         const totalPrice = packagePrice + (packagePrice * countryTax);
         totalValue.innerHTML = `Total: $${totalPrice.toFixed(2)}`;
    }
     // Adding an event listener to the package and country selects to recalculate the total when the user selects a different option
     packageSelect.addEventListener('change', calculateTotal);
     countrySelect.addEventListener('change', calculateTotal);


