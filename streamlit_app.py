import streamlit as st
import openai

# Retrieve your OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set the page configuration
st.set_page_config(
    page_title="Ahoy! - Revolutionary Product",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main Title and Header
st.title("Ahoy!")
st.header("Welcome to the Future of Innovation")
st.subheader("Introducing Our Revolutionary Product")

# Product Description
st.write("""
Our product is designed to transform the way you experience technology.
From cutting-edge features to user-friendly design, we provide a unique experience 
that stands out in today's competitive market.
""")

# Display an image (replace the URL with your product image)
st.image(
    "https://via.placeholder.com/800x400.png?text=Our+Innovative+Product", 
    caption="Our Revolutionary Product", 
    use_container_width=True  # Updated parameter
)

# Features Section
st.markdown("## Features")
st.markdown("""
- **Innovative Design:** Sleek and modern, integrating seamlessly into your lifestyle.
- **High Performance:** Powered by the latest technology for an unmatched experience.
- **User-Centric Interface:** Intuitive and easy-to-use, perfect for everyone.
- **Eco-Friendly:** Engineered with sustainability in mind.
""")

# How It Works Section
st.markdown("## How It Works")
st.write("""
Our product utilizes state-of-the-art algorithms and robust architecture to deliver 
a smooth, efficient experience. Whether at home, work, or on the go, our technology 
adapts to your needs.
""")

# Demo Video Section
st.markdown("## Watch the Demo")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Replace with your video link

# Generative AI Integration Section
st.markdown("## AI-Powered Ideas")
st.write("Need some creative inspiration for your product? Use our AI assistant to generate innovative ideas or taglines!")

# Get user prompt for generative AI
ai_prompt = st.text_input("Enter your prompt for AI:", placeholder="E.g., Suggest a creative tagline for our product...")

if ai_prompt:
    st.write("Generating response...")
    try:
        # Updated to use ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": ai_prompt},
            ],
            max_tokens=150,
            temperature=0.7
        )
        generated_text = response.choices[0].message["content"].strip()
        st.subheader("AI Generated Response:")
        st.write(generated_text)
    except Exception as e:
        st.error(f"Error generating response: {e}")

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
Have any questions or want to learn more? Reach out to us at:
- **Email:** info@ourproduct.com
- **Phone:** (123) 456-7890
""")

# Testimonials Section
st.markdown("## Testimonials")
st.write("""
> "This product has completely transformed the way I work and live. Truly revolutionary!"  
> *— A Satisfied Customer*
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
st.write("Thank you for visiting our website! Stay tuned for more updates.")

