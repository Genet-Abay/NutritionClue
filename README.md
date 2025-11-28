# NutritionClue

A web application for nutrition recommendations specifically designed for women in pre-menopause or menopause.

## Features

- **Home Page**: Welcomes users and presents service options (ordering cooked foods, menus with recipes, cooking tutorials)
- **Catering Service**: Order nutritionally balanced meals with a personalized form based on dietary needs and health goals
- **Cooking Lessons**: Expert-led tutorials with enrollment form based on user's experience and health concerns
- **Recipes**: Browse recipes with complete ingredient lists and health benefits
- **Community Discussion**: Connect with other women, share experiences, and support each other
- **Physical Activity**: Exercise recommendations tailored for women during menopause

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Genet-Abay/NutritionClue.git
   cd NutritionClue
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   cd app
   python main.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
NutritionClue/
├── app/
│   ├── __init__.py
│   └── main.py          # Main Flask application
├── templates/           # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── catering.html
│   ├── cooking_lessons.html
│   ├── recipes.html
│   ├── recipe_detail.html
│   ├── community.html
│   ├── physical_activity.html
│   └── about.html
├── static/
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   └── js/
│       └── main.js      # JavaScript functionality
├── requirements.txt
└── README.md
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design

## License

This project is open source and available under the MIT License.