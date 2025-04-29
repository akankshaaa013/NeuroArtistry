<!DOCTYPE html>

<body>

<h1>🎨 NeuroArtistry</h1>
<p>Transform your photos into stunning artworks by blending the structure of one image (content) with the artistic flair of another (style) using <strong>Neural Style Transfer</strong>.</p>

<hr>

<h2>📌 Objective</h2>
<p>To create a user-friendly application that leverages deep learning and computer vision to perform neural style transfer — combining the content of one image with the style of another to generate artistic outputs.</p>

<h2>⚙️ Technologies Used</h2>
<ul>
    <li><strong>PyTorch</strong> - for building and running the style transfer model</li>
    <li><strong>Streamlit</strong> - for the interactive web UI</li>
    <li><strong>OpenCV / PIL</strong> - for image processing</li>
    <li><strong>VGG-19</strong> - pre-trained model used for feature extraction</li>
    <li><strong>LBFGS</strong> - optimization algorithm used to minimize the style and content losses</li>
</ul>

<h2>🚀 Features</h2>
<ul>
    <li>Upload or select content and style images</li>
    <li>Adjust parameters like optimization steps, style weight, and image size</li>
    <li>Real-time progress updates and output preview</li>
    <li>Caching mechanism to reuse previously generated results</li>
    <li>Examples gallery with before/after comparisons</li>
</ul>

<h2>🧠 How It Works</h2>
<ol>
    <li>The VGG-19 model extracts features from both content and style images.</li>
    <li>Content and style losses are calculated at specific layers.</li>
    <li>The generated image is iteratively optimized to minimize these losses.</li>
</ol>

<h2>💻 Local Installation</h2>

<h3>Step 1: Clone the Repository</h3>
<pre><code>git clone https://github.com/yourusername/NeuroArtistry.git
cd NeuroArtistry</code></pre>

<h3>Step 2: Create and Activate Virtual Environment</h3>
<pre><code>python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate</code></pre>

<h3>Step 3: Install Dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>Step 4: Run the Application</h3>
<pre><code>streamlit run app.py</code></pre>

<h2>📁 Project Structure</h2>
<pre>
NeuroArtistry/
├── app.py                 # Streamlit app interface
├── src/
│   └── model.py           # Neural style transfer model
├── Examples/              # Sample images for content, style, and output
├── cache/                 # Stores generated outputs
├── requirements.txt       # Python dependencies
└── README.html            # Project overview
</pre>

<h2>📸 Example Output</h2>
<p>Check the Examples section in the app to see various styles applied to real-world images!</p>

<h2>User Interface Design</h2>

![image](https://github.com/user-attachments/assets/14a091a6-f34e-4c6d-95f2-2064b5a1bcb5)

![image](https://github.com/user-attachments/assets/c0cae0d4-affb-4f94-90cc-dd40b9857dcf)

![image](https://github.com/user-attachments/assets/9766ece2-e04f-4727-a2e9-8aacaa9fe858)

<h3>Model Settings: </h3>

![image](https://github.com/user-attachments/assets/221194bc-cbbc-43e5-888c-c8c1ab6d3053)

<h3>Running the style transfer: </h3>

![image](https://github.com/user-attachments/assets/0717e076-b5f7-4a1f-9945-2d2909bceb59)

<h3>Status: </h3>

![image](https://github.com/user-attachments/assets/14a21cb9-cde6-4640-bced-784c5bf8306e)

<h3>Progress: </h3>

![image](https://github.com/user-attachments/assets/56b0af5c-c88f-4af6-88a2-47c4b960248d)

<h3>Generated Image: </h3>

![image](https://github.com/user-attachments/assets/74e17f30-1860-42fe-90d7-4ad48933594b)

<h3> Cached Image Generation Feature </h3>
<h4><i>(Image with same model parameters generated immediately due to cache memory use):</i></h4>

![image](https://github.com/user-attachments/assets/3f6ba4f8-7d11-4a57-aff2-87ea11decbe6)



<h2>🙌 Acknowledgments</h2>
<ul>
    <li>Based on the foundational work by <a href="https://arxiv.org/abs/1508.06576" target="_blank">Gatys et al.</a></li>
    <li>Streamlit and PyTorch communities</li>
</ul>

<h2>🧑‍💻 Authors</h2>
<p></i>Made with ❤️ by Akanksha & Paakhi</p>

</body>
</html>
