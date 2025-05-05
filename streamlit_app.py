import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Subway Sweepers - Smart Urban Cleaners",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            color: #2c3e50;
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 0;
        }
        .section-header {
            font-size: 28px;
            margin-top: 40px;
            color: #34495e;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 5px;
        }
        .subheader {
            font-size: 20px;
            color: #7f8c8d;
            margin-top: -10px;
        }
        .feature-box {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        .testimonial {
            font-style: italic;
            background-color: #ecf0f1;
            padding: 15px;
            border-left: 5px solid #2ecc71;
            margin-top: 20px;
            border-radius: 8px;
        }
        form {
            margin-top: 20px;
        }
        button {
            background-color: #2ecc71;
            border: none;
            color: white;
            border-radius: 6px;
        }
        button:hover {
            background-color: #27ae60;
        }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("<h1 class='main-title'>Subway Sweepers</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Smart Urban Cleaners Powered by Solar Energy</p>", unsafe_allow_html=True)
st.write("### Redefining Urban Waste Management")

# Product Description
st.markdown("#### What is Subway Sweepers?")
st.write("""
Subway Sweepers is a **solar-powered autonomous cleaning robot** that revolutionizes public sanitation in urban areas. 
Using AI-powered object detection and efficient hardware integration, it keeps subways, sidewalks, and public spaces clean with minimal human intervention.
""")

# Features Section
st.markdown("<h2 class='section-header'>Features</h2>", unsafe_allow_html=True)

cols = st.columns(2)
with cols[0]:
    st.markdown("""<div class='feature-box'>✅ **Solar-Powered Operation**  
    Runs entirely on renewable energy for sustainable urban cleaning.</div>""", unsafe_allow_html=True)
    st.markdown("""<div class='feature-box'>🧠 **Real-Time Object Detection**  
    Uses YOLO + Raspberry Pi to identify and classify urban trash.</div>""", unsafe_allow_html=True)

with cols[1]:
    st.markdown("""<div class='feature-box'>🧭 **Autonomous Navigation**  
    Arduino interprets sensors to smartly navigate and collect waste.</div>""", unsafe_allow_html=True)
    st.markdown("""<div class='feature-box'>🌆 **Versatile Deployment**  
    Works on subway platforms, sidewalks, parks, and urban streets.</div>""", unsafe_allow_html=True)

# How It Works Section
st.markdown("<h2 class='section-header'>How It Works</h2>", unsafe_allow_html=True)
st.write("""
- **Trash Detection**: A webcam sends video feed to a Raspberry Pi running a YOLO-based model.
- **Smart Control**: An Arduino receives sensor data and controls motors and steering.
- **Power Supply**: High-efficiency solar panels power the system, stored in a compact battery unit.
- **Waste Handling**: A mechanical arm scoops and stores detected trash in an onboard container.
""")

# Testimonials Section
st.markdown("<h2 class='section-header'>Testimonials</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='testimonial'>
“Subway Sweepers is a breakthrough in urban waste management. Its autonomous operation and sustainable design offer a practical solution to keeping our cities clean.”  
<br><br>— <strong>Urban Planning Expert</strong>
</div>
""", unsafe_allow_html=True)

# Contact Form Section
st.markdown("<h2 class='section-header'>Get In Touch</h2>", unsafe_allow_html=True)
st.write("Interested in collaboration or want to learn more? Reach out below:")

contact_form = """
<form action="https://formsubmit.co/your-email@example.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 6px; border: 1px solid #ccc;">
    <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 6px; border: 1px solid #ccc;">
    <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 6px; border: 1px solid #ccc;"></textarea>
    <button type="submit" style="padding: 10px 20px;">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("### Quick Links")
st.sidebar.markdown("""
- [Home](#)
- [Features](#features)
- [How It Works](#how-it-works)
- [Get In Touch](#get-in-touch)
""")
st.sidebar.markdown("### Contact")
st.sidebar.write("""
📧 info@subwaysweepers.com  
📞 (123) 456-7890
""")

# Footer
st.markdown("---")
st.write("© 2025 Subway Sweepers. Built with 🛠️ Streamlit.")






