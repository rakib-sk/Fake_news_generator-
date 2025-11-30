# Fake News Generator

A simple, fun, and responsive web app built with **Flask** that generates random funny news headlines based on a person's name. Perfect for pranks, jokes, or just for fun!

---

## 🚀 Features

- Generates random funny headlines dynamically using **Python & Flask**.
- Responsive design with fixed bottom input form.
- Easy to add more funny headlines in a **JSON file** (`news_data.json`).
- Lightweight and easy to deploy.
- Future-ready for AI-generated extended news based on the headline.

---

## 📂 Project Structure
```Fake_news
Fake_news
   > templates
      > index.html
   > news_data.json
   > app.py
```

---

## 🛠 Installation & Setup

### 1. Install Python

Make sure you have Python 3 installed:

```bash
python --version
```
- If not, download it from ***Python.org.***

## 2. Create Virtual Environment (Recommended)
```Bash
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows
```

## 3. Install Flask
```Bash
pip install Flask
```

## 4. . Project Files
- app.py – main Flask application.
- news_data.json – contains all funny actions and places:


### Example structure:
```json
{
  "actions": [
    "একটি গুরুত্বপূর্ণ সিদ্ধান্ত নিয়েছে",
    "ভাইরাল হয়ে গেছে",
    "চমকে দেওয়ার মতো কাজ করেছে"
  ],
  "places": [
    "স্কুলে",
    "বাজারে",
    "রাস্তায়"
  ]
}
```

- templates/index.html – HTML template with responsive design.


## 5. Run the Flask App
```bash
python app.py
```

- Open your browser at http://127.0.0.1:5000/.
- Enter a person's name in the input field.
- Press Generate to see a funny headline appear instantly.

## 🎨 How It Works
- Flask reads the news_data.json file to get lists of actions and places.
- When a user submits a name via the form, a random action and place are chosen.
- The headline is generated as:


``` <person_name> <random_action> <random_place>```

- The HTML template displays the headline in a clean, responsive design.

## 📈 Next Features (Planned)
- AI-powered news generation: Generate funny news paragraphs automatically based on the headline.
- Shareable headlines: Copy/share the generated headline on social media.
- Dynamic JSON editor: Add/remove actions and places via admin panel.
- Multiple languages support: More fun worldwide!

## 💡 Tips
- Add more funny actions and places to news_data.json to make the headlines more creative.
- Always keep UTF-8 encoding for proper rendering of Bengali or any other language characters.
- Use virtual environment for clean dependency management.

## ⚡ License
- This project is open-source and free to use under the MIT License.
