import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Subway Sweepers - Smart Urban Cleaners",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
pages = {
    "Home": "home",
    "Inspiration": "inspiration",
    "What It Does": "what_it_does",
    "How We Built It": "how_we_built_it",
    "Challenges": "challenges",
    "Accomplishments": "accomplishments",
    "What We Learned": "what_we_learned",
    "What's Next": "whats_next"
}

selection = st.sidebar.radio("Navigation", list(pages.keys()))

# Define each page as a function
def home_page():
    st.markdown("# Subway Sweepers")
    st.markdown("### Powering Urban Cleanliness with Smart, Solar-Powered Robotics")
    st.image("https://via.placeholder.com/800x400.png?text=Subway+Sweepers", 
             caption="Subway Sweepers in Action", 
             use_container_width=True)
    st.write("Welcome to Subway Sweepers, a project dedicated to transforming urban waste management with cutting-edge robotics and sustainable energy.")

def inspiration_page():
    st.markdown("## Inspiration")
    st.write("""
    Subway Sweepers was born from a clear need: improving how urban environments handle waste. 
    Inefficient cleaning methods in public spaces lead to persistent litter problems. 
    Our solution is a self-contained robot that detects, collects, and properly disposes of trash.
    By using a Raspberry Pi with YOLO-based object detection and an Arduino for precise control, 
    Subway Sweepers offers a practical and sustainable approach to keeping public areas cleaner.
    """)

def what_it_does_page():
    st.markdown("## What It Does")
    st.write("""
    Subway Sweepers is a solar-powered robot designed for urban waste management. It uses a 
    Raspberry Pi running a YOLO-based object detection system to identify trash in real time. 
    Upon detection, the robot uses a scooping mechanism and distance sensors to collect trash 
    and deposit it in the proper disposal location. This system is optimized for environments 
    such as city roads, subways, and other public spaces.
    """)

def how_we_built_it_page():
    st.markdown("## How We Built It")
    st.write("""
    Our project combines both hardware and software innovations:
    - **Computer Vision:** A Raspberry Pi is paired with a webcam and LCD monitor. Using YOLO and OpenCV, the system identifies a wide range of objects.
    - **Control System:** An Arduino processes sensor data and converts it into navigation commands, allowing the robot to move autonomously.
    - **Sustainable Power:** Solar panels power the system through a USB-A to USB-C connection.
    - **Mechanical Design:** Rotary motors and a repurposed can plow work together to enable effective trash collection.
    """)
    st.image("https://via.placeholder.com/800x400.png?text=Hardware+Components", 
             caption="Hardware Components Overview", 
             use_container_width=True)

def challenges_page():
    st.markdown("## Challenges")
    st.write("""
    Throughout the development of Subway Sweepers, we encountered several challenges:
    - Establishing a reliable connection between the Raspberry Pi and the LCD display.
    - Overcoming mechanical difficulties in assembling the rotary motor and plow mechanism.
    - Integrating various hardware components to function seamlessly together.
    These challenges drove us to innovate and refine our approach, ultimately resulting in a more robust system.
    """)

def accomplishments_page():
    st.markdown("## Accomplishments")
    st.write("""
    Our key accomplishments include:
    - Successfully integrating a YOLO-based object detection system on a Raspberry Pi for real-time trash detection.
    - Developing an Arduino-driven control system that processes sensor data for precise navigation.
    - Building a robust, solar-powered robot capable of autonomous cleaning in urban settings.
    - Creating an engaging and informative web interface with Streamlit to showcase our project.
    """)

def what_we_learned_page():
    st.markdown("## What We Learned")
    st.write("""
    This project provided us with valuable technical insights:
    - Practical experience deploying machine learning models on resource-constrained hardware.
    - Techniques for integrating YOLO object detection with Raspberry Pi and interfacing sensor data via Arduino.
    - Strategies for optimizing energy management using renewable power sources.
    - The importance of modular design and iterative improvements when developing complex systems.
    """)

def whats_next_page():
    st.markdown("## What's Next")
    st.write("""
    Moving forward, we plan to:
    - Incorporate advanced sensors to gather quantitative data on waste levels, graffiti, and infrastructure conditions.
    - Upgrade the hardware with higher-torque motors and refined mechanical components for increased durability.
    - Develop a fleet management system for scalable deployment and real-time monitoring.
    - Expand our web interface to include an interactive dashboard for tracking environmental data.
    """)

# Render selected page
if pages[selection] == "home":
    home_page()
elif pages[selection] == "inspiration":
    inspiration_page()
elif pages[selection] == "what_it_does":
    what_it_does_page()
elif pages[selection] == "how_we_built_it":
    how_we_built_it_page()
elif pages[selection] == "challenges":
    challenges_page()
elif pages[selection] == "accomplishments":
    accomplishments_page()
elif pages[selection] == "what_we_learned":
    what_we_learned_page()
elif pages[selection] == "whats_next":
    whats_next_page()

# Footer for all pages
st.write("---")
st.write("© 2025 Subway Sweepers. All rights reserved.")



