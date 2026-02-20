from flask import Flask, render_template_string

app = Flask(__name__)

# -------------------- BASE TEMPLATE --------------------

base_template = """
<!DOCTYPE html>
<html>
<head>
    <title>BG Tech - Training Solutions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background-color: #f4f6f8;
        }
        header {
            background-color: #0a1f44;
            color: white;
            padding: 20px;
            text-align: center;
        }
        nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }
        nav a:hover {
            text-decoration: underline;
        }
        .container {
            padding: 40px;
            min-height: 70vh;
        }
        footer {
            background-color: #0a1f44;
            color: white;
            text-align: center;
            padding: 15px;
        }
        ul {
            line-height: 1.8;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            background: #0a1f44;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .button:hover {
            background: #163a7a;
        }
    </style>
</head>
<body>

<header>
    <h1>BG Tech</h1>
    <p>Professional IT Training Solutions</p>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/courses">Courses</a>
        <a href="/contact">Contact</a>
    </nav>
</header>

<div class="container">
    {{ content }}
</div>

<footer>
    <p>© 2026 BG Tech | Empowering Tech Professionals</p>
</footer>

</body>
</html>
"""

# -------------------- ROUTES --------------------

@app.route("/")
def home():
    content = """
    <h2>Welcome to BG Tech</h2>
    <p>Your trusted partner for professional IT and technology training.</p>
    <p>We specialize in:</p>
    <ul>
        <li>Cloud Computing</li>
        <li>Cybersecurity</li>
        <li>DevOps & Automation</li>
        <li>Networking & Infrastructure</li>
    </ul>
    <a class="button" href="/courses">Explore Courses</a>
    """
    return render_template_string(base_template, content=content)

@app.route("/about")
def about():
    content = """
    <h2>About BG Tech</h2>
    <p>BG Tech is a professional training company delivering industry-focused IT education.</p>
    <p>Our mission is to equip professionals with practical, real-world skills that drive career growth.</p>
    <p>We provide instructor-led training, corporate programs, and customized workshops.</p>
    """
    return render_template_string(base_template, content=content)

@app.route("/courses")
def courses():
    content = """
    <h2>Our Courses</h2>
    <ul>
        <li><strong>Cloud Computing</strong> – AWS & Azure fundamentals to advanced architecture</li>
        <li><strong>Cybersecurity</strong> – Network security, SOC, ethical hacking basics</li>
        <li><strong>DevOps</strong> – CI/CD pipelines, Docker, Kubernetes</li>
        <li><strong>Networking</strong> – Enterprise networking & infrastructure</li>
    </ul>
    """
    return render_template_string(base_template, content=content)

@app.route("/contact")
def contact():
    content = """
    <h2>Contact Us</h2>
    <p>Email: info@bgtech.com</p>
    <p>Phone: +48 123 456 789</p>
    <p>Location: Europe</p>
    """
    return render_template_string(base_template, content=content)

# -------------------- RUN APP --------------------

if __name__ == "__main__":
    app.run(debug=True)