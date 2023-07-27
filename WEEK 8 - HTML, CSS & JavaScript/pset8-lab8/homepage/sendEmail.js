const nodemailer = require("nodemailer");

// Create a transporter object using SMTP transport
const transporter = nodemailer.createTransport({
  service: "your-email-service", // e.g., Gmail, Outlook, etc.
  auth: {
    user: "your-email@example.com", // Your email address
    pass: "your-email-password", // Your email password
  },
});

// Function to send the email
const sendEmail = (name, email, message) => {
  const mailOptions = {
    from: "your-email@example.com", // Sender's email address
    to: "recipient@example.com", // Recipient's email address
    subject: "New contact form submission",
    text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`,
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.log("Error sending email:", error);
    } else {
      console.log("Email sent:", info.response);
    }
  });
};

module.exports = sendEmail;
