const express = require("express");
const sendEmail = require("./sendEmail");

const app = express();
const port = 3000;

app.use(express.json());

app.post("/sendEmail", (req, res) => {
  const { name, email, message } = req.body;

  sendEmail(name, email, message);

  res.json({ message: "Email sent" });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
