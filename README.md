# Topic to MP3/Video Generator

A Flask application for generating videos, images, and captions from text prompts, optimized for Vercel deployment.

## One-Click Deployment

The easiest way to deploy this application is with Vercel's one-click deployment:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fyour-username%2Ftopic-to-mp3)

## Manual Deployment Steps

### 1. Fork or Clone this Repository

```bash
git clone https://github.com/your-username/topic-to-mp3.git
cd topic-to-mp3
```

### 2. Install Vercel CLI (Optional)

```bash
npm install -g vercel
```

### 3. Deploy to Vercel

#### Option A: Using Vercel CLI

```bash
vercel login
vercel
```

Follow the prompts to deploy your application.

#### Option B: Using Vercel Dashboard

1. Go to [Vercel](https://vercel.com/new)
2. Import your GitHub repository
3. Configure the project:
   - Framework Preset: Flask
   - Root Directory: ./
   - Build Command: Leave empty
   - Output Directory: Leave empty
4. Click "Deploy"

## Project Structure

```
├── app.py                # Main Flask application
├── index.py              # Entry point for Vercel
├── wsgi.py               # WSGI entry point
├── routes/               # Route modules
│   ├── api.py            # API routes
│   └── pages.py          # Page routes
├── utils/                # Utility modules
│   ├── config.py         # Configuration
│   ├── video_processor.py # Video processing
│   ├── image_generator.py # Image generation
│   └── caption_generator.py # Caption generation
├── static/               # Static files
│   ├── styles.css        # CSS styles
│   ├── scripts.js        # Client-side JavaScript
│   └── ...               # Other static files
├── templates/            # HTML templates
│   ├── home.html         # Home page
│   └── ...               # Other templates
├── vercel.json           # Vercel configuration
└── requirements.txt      # Python dependencies
```

## Local Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## API Endpoints

### Generate Video

```
POST /api/generate-video
Content-Type: application/json

{
  "topic": "Your video topic"
}
```

### Generate Image

```
POST /api/generate-image
Content-Type: application/json

{
  "prompt": "Your image prompt"
}
```

### Generate Captions

```
POST /api/generate-captions
Content-Type: application/json

{
  "filename": "video_filename.mp4"
}
```

## Customization

- Edit HTML templates in the `templates` directory to change the UI
- Modify API endpoints in the `routes/api.py` file to change functionality
- Update styles in `static/styles.css` to customize the appearance 