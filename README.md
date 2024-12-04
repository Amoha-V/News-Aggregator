# Amo's Alert: News Aggregator

## Overview

Amo's Alert is a dynamic web application that revolutionizes news consumption by providing an interactive and personalized news browsing experience powered by NewsAPI.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [API Integration](#api-integration)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

-  Browse top headlines from multiple categories
-  Advanced news search with keyword filtering
-  Filter news by different sources
-  Save and manage interesting articles
-  Responsive and interactive user interface
-  Innovative 3D CSS transformations

## Demo

[Live Application](https://news-aggregator-95eh.onrender.com)

## Technologies

### Languages
- Python
- JavaScript
- HTML
- CSS

### Frameworks & Libraries
- Flask
- Requests
- python-dotenv

### API
- [NewsAPI](https://newsapi.org/)

### Deployment
- Render

## Getting Started

### Prerequisites
- Python 3.7+
- pip
- NewsAPI Key

### Installation

1. Clone the repository
```bash
git clone https://github.com/your-username/news-aggregator.git
cd news-aggregator
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure NewsAPI Key
- Create a `.env` file
- Add your NewsAPI key: `NEWS_API_KEY=your_api_key_here`

5. Run the application
```bash
flask run
```

## Project Structure

```
news-aggregator/
│
├── app.py           # Main Flask application
├── .env             # Environment variables
├── requirements.txt # Project dependencies
├── templates/       # HTML templates
│   ├── index.html
│   └── saved_articles.html
└── static/          # Static assets
    ├── css/
    └── js/
```

## API Integration

The application uses NewsAPI to:
- Fetch top headlines
- Search news by keywords
- Filter news by categories and sources

## Deployment

Deployed on Render with:
- Gunicorn web server
- Continuous integration from GitHub
- Environment variable management

## Design Highlights

### 3D Transformations
- Pure CSS-driven 3D effects
- No external libraries used


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## License

Distributed under the MIT License. See [LICENSE](https://opensource.org/licenses/MIT) for more information.

