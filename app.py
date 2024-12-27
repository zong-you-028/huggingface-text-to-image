import streamlit as st
from PIL import Image
from flux import FLUXModel  # Assuming FLUX.1-dev provides this

# Initialize the FLUX model (load only once)
@st.cache_resource
def load_model():
    return FLUXModel.from_pretrained("flux-1-dev")

model = load_model()

# Streamlit GUI
st.title("Text-to-Image Generator with FLUX.1-dev")
st.subheader("Enter a prompt to generate stunning images!")

# Text input
prompt = st.text_input("Enter your prompt", "")

# Generate image when button is clicked
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image... Please wait."):
            try:
                image = model.generate_image(prompt)  # Generate image
                st.image(image, caption="Generated Image", use_column_width=True)
            except Exception as e:
                st.error(f"Error generating image: {e}")
    else:
        st.warning("Please enter a prompt!")

# Footer
st.write("Powered by FLUX.1-dev and Streamlit")
