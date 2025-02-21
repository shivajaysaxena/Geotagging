import os
import streamlit as st
from embedding_module import embed_text
from extraction_module import extract_data
from PIL import Image

static_dir = 'F:\\Geotagging_final\\static\\'
os.makedirs(static_dir, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

def main():
    st.title("Image Data Processing App")
    
    # Create tabs for different functionalities
    tab1, tab2 = st.tabs(["Embed Data", "Extract Data"])
    
    # Embed Data Tab
    with tab1:
        st.header("Embed Data into Image")
        uploaded_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'], key="embed_uploader")
        data_to_embed = st.text_area("Enter data to embed")
        
        if st.button("Embed Data"):
            if uploaded_file is not None and data_to_embed:
                if allowed_file(uploaded_file.name):
                    output_path = os.path.join(static_dir, 'embedded_image.png')
                    embed_text(uploaded_file, data_to_embed, output_path)
                    
                    # Display result
                    st.success("Data embedded successfully!")
                    
                    # Show embedded image
                    embedded_image = Image.open(output_path)
                    st.image(embedded_image, caption="Embedded Image")
                    
                    # Download button
                    with open(output_path, "rb") as file:
                        st.download_button(
                            label="Download Embedded Image",
                            data=file,
                            file_name="embedded_image.png",
                            mime="image/png"
                        )
                else:
                    st.error("Please upload a valid image file")
            else:
                st.warning("Please upload an image and enter data to embed")

    # Extract Data Tab
    with tab2:
        st.header("Extract Data from Image")
        extract_file = st.file_uploader("Choose an image file", type=['jpg', 'jpeg', 'png'], key="extract_uploader")
        
        if st.button("Extract Data"):
            if extract_file is not None:
                if allowed_file(extract_file.name):
                    extracted_data = extract_data(extract_file)
                    st.success("Data extracted successfully!")
                    st.text_area("Extracted Data", extracted_data, height=150)
                else:
                    st.error("Please upload a valid image file")
            else:
                st.warning("Please upload an image to extract data from")

if __name__ == '__main__':
    main()










