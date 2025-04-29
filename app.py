import streamlit as st
import hashlib
import os
from src.model import run_style_transfer
from streamlit_image_select import image_select
from PIL import Image

st.markdown(
    """
    <style>
        .title {
            font-size: 28px;
            font-weight: bold;
            color: #2E86C1;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 24px;
            font-weight: bold;
            color: #1B4F72;
            margin-top: 20px;
        }
        .content {
            font-size: 20px;
            line-height: 1.6;
            color: #333333;
            margin-bottom: 20px;
        }
        .highlight {
            font-weight: bold;
            color: #D35400;
        }
        .note {
            font-size: 18px;
            font-style: italic;
            color: #7D3C98;
            margin-top: 20px;
        }
        ul {
            margin-top: 10px;
            padding-left: 20px;
        }
        li {
            margin-bottom: 8px;
        }
    </style>

    <div class="title">🎨Transform Your Images with Neural Style Transfer!✨</div>  

    <div class="content">
        Turn your photos into stunning pieces of art using the power of deep learning!  
        Our <span class="highlight">Neural Style Transfer</span> model blends the structure of one image with the artistic style of another,  
        giving you <span class="highlight">a completely unique, AI-generated masterpiece</span>.  
    </div>

    <div class="subtitle">🚀How It Works:</div>
    <ul class="content">
        <li><strong>Upload your images:</strong> Choose a <span class="highlight">content image</span> (your subject)  
            and a <span class="highlight">style image</span> (the artistic effect you want to apply).</li>
        <li><strong>Fine-tune the transformation:</strong></li>
        <ul>
            <li>🛠 <strong>Optimization Steps:</strong> More steps refine the details, but take longer.</li>
            <li>🎭 <strong>Style Weight:</strong> Control how much of the style is applied.</li>
            <li>📏 <strong>Max Image Size:</strong> Higher resolution gives better details but requires more computation.</li>
        </ul>
        <li><strong>Click ‘Run Style Transfer’</strong> to create your custom artwork!</li>
    </ul>

    <div class="note">⚡Note: A GPU significantly speeds up processing. Running on a CPU may take longer, but it still works! ⚡</div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
    <style>
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #f7f9fc;
            padding: 10px;
            border-right: 2px solid #d9d9d9;
        }

        /* Sidebar Headers */
        .sidebar-title {
            font-size: 20px !important;
            font-weight: bold !important;
            color: #333333 !important;
            padding-bottom: 5px;
        }

        /* File Upload Box */
        [data-testid="stFileUploaderDropzone"] {
            border: 2px dashed #4CAF50 !important;
            border-radius: 10px !important;
            background-color: #e8f5e9 !important;
        }

        /* Uploaded Image Preview */
        img {
            border-radius: 10px !important;
            border: 2px solid #4CAF50 !important;
            margin-bottom: 10px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for Content Image
st.sidebar.subheader("📷 Select Content Image", help="Upload or Choose a Content Image")
uploaded_content = st.sidebar.file_uploader(
    "Upload a Content Image", type=["jpg", "jpeg", "png", "webp"], key="content1"
)

with st.sidebar:
    if uploaded_content:
        with open("uploaded_content.jpg", "wb") as f:
            f.write(uploaded_content.getbuffer())
        content_img = "uploaded_content.jpg"
        st.sidebar.image(content_img, caption="✅ Content Image", use_container_width=True)
    else:
        content_img = image_select(
            label="or Choose a Content Image",
            images=[
                "Examples/Content/staring.jpg",
                "Examples/Content/boy.jpg",
                "Examples/Content/sea.jpg",
                "Examples/Content/bears.jpg",
                "Examples/Content/flower.jpg"
            ],
            captions=["Staring", "Boy", "Sea", "Bears", "Flower"],
            key="content2",
            use_container_width=False
        )

# Sidebar for Style Image
st.sidebar.subheader("🎨 Select Style Image", help="Upload or Choose a Style Image")
uploaded_style = st.sidebar.file_uploader(
    "Upload a Style Image", type=["jpg", "jpeg", "png", "webp"], key="style1"
)

with st.sidebar:
    if uploaded_style:
        with open("uploaded_style.jpg", "wb") as f:
            f.write(uploaded_style.getbuffer())
        style_img = "uploaded_style.jpg"
        st.sidebar.image(style_img, caption="✅ Style Image", use_container_width=True)
    else:
        style_img = image_select(
            label="or Choose a Style Image",
            images=[
                "Examples/Style/monet.jpeg",
                "Examples/Style/starrynight.jpg",
                "Examples/Style/kandinsky.jpeg",
                "Examples/Style/artic.jpg",
                "Examples/Style/hokusai.jpeg"
            ],
            captions=["Monet", "Starry Night", "Kandinsky", "Arctic", "Hokusai"],
            key="style2",
            use_container_width=False
        )

############################################################################################

# Custom CSS for Sliders
st.markdown("""
    <style>
        /* Slider Labels */
        .stSlider label {
            font-size: 16px !important;
            font-weight: bold !important;
            color: #333333 !important;
            margin-bottom: 5px !important;
        }

        /* Slider Styling */
        div[data-testid="stSlider"] {
            padding: 8px !important;
            border-radius: 9px !important;
            background-color: #f7f9fc !important;
            border: 1px solid #00897b !important;
            transition: 0.3s ease-in-out;
        }

        /* Slider Hover Effect */
        div[data-testid="stSlider"]:hover {
            box-shadow: 0px 0px 10px rgba(76, 175, 80, 0.7) !important;
            border-color: #3e4a3d !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Sliders with Enhanced Styling
st.sidebar.subheader("⚙️Model Parameters", help="Adjust these parameters to fine-tune the style transfer")

steps = st.sidebar.slider(
    "📊Optimization Steps", min_value=300, max_value=900, value=300, step=100,
    help="Defines the number of optimization steps. Higher values improve quality but take more time."
)

style_weight = st.sidebar.slider(
    "🎨Style Weight", min_value=1e6, max_value=1e7, value=1e6, step=1e6,
    help="Controls the importance of the style. A higher value means the final image retains more of the style."
)

max_size = st.sidebar.slider(
    "📏Max Image Size", min_value=128, max_value=2160, value=512, step=64,
    help="Sets the resolution of the generated image. Higher values improve detail but require more memory."
)

# Ensure cache directory exists
if not os.path.exists("cache"):
    os.makedirs("cache")

# Initialize session state for output image
if "output_image" not in st.session_state:
    st.session_state.output_image = None

def update_progress(progress):
    """Update progress bar during NST."""
    st.session_state.progress_bar.progress(progress)

@st.cache_data
def get_cached_image(content_path, style_path, steps, style_weight, max_size):
    """
    Retrieve cached image from disk if it exists. Otherwise, return None.
    """
    key = f"{content_path}_{style_path}_{steps}_{style_weight}_{max_size}"
    key_hash = hashlib.md5(key.encode()).hexdigest()
    output_path = f"cache/{key_hash}.jpg"

    if os.path.exists(output_path):
        # Read the image bytes and return it
        with open(output_path, "rb") as f:
            return f.read()
    
    return None  # Cache miss, need to run NST

# Run NST when the button is clicked
if st.button("Run Style Transfer"):

    if content_img and style_img:
        # Reset session state for output image
        st.session_state.output_image = None

        # Create a progress bar in session state
        st.session_state.progress_bar = st.progress(0)

        # Retrieve cached image content if exists
        cached_image = get_cached_image(content_img, style_img, steps, style_weight, max_size)

        if cached_image:
            st.session_state.output_image = cached_image  # Load cached image
        else:
            # Generate output image path
            key_hash = hashlib.md5(f"{content_img}_{style_img}_{steps}_{style_weight}_{max_size}".encode()).hexdigest()
            output_path = f"cache/{key_hash}.jpg"

            # Run NST
            run_style_transfer(
                content_img, style_img, output_path, max_size, 
                num_steps=steps, style_weight=style_weight, 
                progress_callback=update_progress
            )

            # Read the generated image and store it in session state
            with open(output_path, "rb") as f:
                st.session_state.output_image = f.read()

    else:
        st.error("Please upload both a content and style image before running the model.")

# Display the output image if it exists
if st.session_state.output_image:
    st.image(st.session_state.output_image, caption="Output Image", use_container_width=True)

# Function to open and resize images to 250x250
def load_and_resize(image_path):
    img = Image.open(image_path)
    img = img.resize((265, 250))  # Resize to uniform size
    return img

# Apply CSS for styling
st.markdown("""
    <style>
        .stImage > img {
            border-radius: 10px; /* Rounded corners */
            border: 2px solid #4CAF50; /* Green border */
            object-fit: cover; /* Ensures proper fit */
            width: 100% !important; /* Ensures same width */
            height: auto !important; /* Maintains aspect ratio */
        }
    </style>
""", unsafe_allow_html=True)

example_container = st.container()
with example_container:
    st.subheader("✨Output Examples")

    example1 = st.columns(3, gap="small")
    with example1[0]:
        st.image(load_and_resize("Examples/Content/bears.jpg"), caption="🖼Content Image", use_container_width=True)
    with example1[1]:
        st.image(load_and_resize("Examples/Style/sea.jpg"), caption="🎨Style Image", use_container_width=True)
    with example1[2]:
        st.image(load_and_resize("Examples/Output/bear_sea.png"), caption="✨Generated Image", use_container_width=True)

    example2 = st.columns(3, gap="small")
    with example2[0]:
        st.image(load_and_resize("Examples/Content/staring.jpg"), caption="🖼Content Image", use_container_width=True)
    with example2[1]:
        st.image(load_and_resize("Examples/Style/starrynight.jpg"), caption="🎨Style Image", use_container_width=True)
    with example2[2]:
        st.image(load_and_resize("Examples/Output/staring__starry_night.png"), caption="✨Generated Image", use_container_width=True)

    example3 = st.columns(3, gap="small")
    with example3[0]:
        st.image(load_and_resize("Examples/Content/fishing.jpg"), caption="🖼Content Image", use_container_width=True)
    with example3[1]:
        st.image(load_and_resize("Examples/Style/unsplash.jpg"), caption="🎨Style Image", use_container_width=True)
    with example3[2]:
        st.image(load_and_resize("Examples/Output/fishing_unsplash.png"), caption="✨Generated Image", use_container_width=True)

    example4 = st.columns(3, gap="small")
    with example4[0]:
        st.image(load_and_resize("Examples/Content/goose.jpg"), caption="🖼Content Image", use_container_width=True)
    with example4[1]:
        st.image(load_and_resize("Examples/Style/artic2.jpg"), caption="🎨Style Image", use_container_width=True)
    with example4[2]:
        st.image(load_and_resize("Examples/Output/goose_artic.png"), caption="✨Generated Image", use_container_width=True)

    example5 = st.columns(3, gap="small")
    with example5[0]:
        st.image(load_and_resize("Examples/Content/squirrel.jpg"), caption="🖼Content Image", use_container_width=True)
    with example5[1]:
        st.image(load_and_resize("Examples/Style/holy_women.jpg"), caption="🎨Style Image", use_container_width=True)
    with example5[2]:
        st.image(load_and_resize("Examples/Output/squirrel__holy_women.png"), caption="✨Generated Image", use_container_width=True)

###########################################################################################################

# Display the footer
st.markdown(
    """
    <style>
        .footer {
            font-size: 14px;
            font-style: italic;
            color: #7D3C98;
            text-align: center;
            margin-top: 20px;
        }
    </style>

    <div class="footer">
        Made with ❤️ by Akanksha & Paakhi 
    </div>
    """,
    unsafe_allow_html=True
)