import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Subway Sweepers - Smart Urban Cleaners",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main Title and Header
st.title("Subway Sweepers")
st.header("Smart Urban Cleaners Powered by Solar Energy")
st.subheader("Redefining Urban Waste Management")

# Product Description
st.write("""
Subway Sweepers is a solar-powered robot designed to efficiently detect, collect, and dispose of urban waste. 
Using a Raspberry Pi running a YOLO-based object detection system and an Arduino-driven control mechanism, 
this robot autonomously cleans city streets, subway platforms, and public spaces with minimal environmental impact.
""")

# Display an image (replace the URL with your actual project image)
st.image("https://via.placeholder.com/800x400.png?text=Subway+Sweepers", 
         caption="Subway Sweepers in Action", 
         use_container_width=True)

# Features Section
st.markdown("## Features")
st.markdown("""
- **Solar-Powered Operation:** Runs entirely on renewable energy for sustainable urban cleaning.
- **Real-Time Object Detection:** Utilizes a Raspberry Pi with YOLO-based computer vision to identify trash.
- **Autonomous Navigation:** An Arduino processes sensor inputs to navigate and collect waste efficiently.
- **Versatile Deployment:** Ideal for city roads, subway stations, and various public environments.
""")

# How It Works Section
st.markdown("## How It Works")
st.write("""
Subway Sweepers integrates hardware and software to provide a complete cleaning solution:
- A Raspberry Pi, paired with a webcam and LCD monitor, processes live video using YOLO for trash detection.
- An Arduino converts sensor data into precise navigation commands, guiding the robot to collect trash.
- Solar panels supply sustainable power, while a mechanical scooping mechanism collects and deposits waste at designated locations.
""")

# Demo Video Section
st.markdown("## Watch the Demo")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Replace with your actual demo video link

# Sidebar for Navigation and Contact Information
st.sidebar.title("Navigation")
st.sidebar.markdown("""
- [Home](#)
- [Features](#features)
- [Demo](#watch-the-demo)
- [Contact](#get-in-touch)
""")
st.sidebar.markdown("## Contact Us")
st.sidebar.write("""
For more information or collaboration opportunities, please contact us:
- **Email:** info@subwaysweepers.com
- **Phone:** (123) 456-7890
""")

# Testimonials Section
st.markdown("## Testimonials")
st.write("""
> "Subway Sweepers is a breakthrough in urban waste management. Its autonomous operation and sustainable design offer a practical solution to keeping our cities clean."  
> *— Urban Planning Expert*
""")

# Contact Form
st.markdown("## Get In Touch")
contact_form = """
<form action="https://formsubmit.co/your-email@example.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 8px; margin-bottom: 10px;">
    <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 8px; margin-bottom: 10px;">
    <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 8px; margin-bottom: 10px;"></textarea>
    <button type="submit" style="padding: 10px 20px;">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Footer
st.write("Thank you for visiting Subway Sweepers! Stay tuned for more updates.")




