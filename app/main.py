"""Main Flask application module for NutritionClue."""
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')


# Sample data for recipes
RECIPES = [
    {
        'id': 1,
        'name': 'Calcium-Rich Smoothie',
        'description': 'A delicious smoothie packed with calcium for bone health.',
        'ingredients': ['Greek yogurt', 'Spinach', 'Almond milk', 'Banana', 'Chia seeds', 'Honey'],
        'benefits': 'Supports bone density and provides essential nutrients for menopause.',
        'image': 'smoothie.jpg'
    },
    {
        'id': 2,
        'name': 'Omega-3 Salmon Bowl',
        'description': 'Grilled salmon with quinoa and vegetables.',
        'ingredients': ['Salmon fillet', 'Quinoa', 'Broccoli', 'Sweet potato', 'Olive oil', 'Lemon'],
        'benefits': 'Rich in omega-3 fatty acids to support heart health and reduce inflammation.',
        'image': 'salmon.jpg'
    },
    {
        'id': 3,
        'name': 'Phytoestrogen Tofu Stir-Fry',
        'description': 'A plant-based dish with natural phytoestrogens.',
        'ingredients': ['Firm tofu', 'Bell peppers', 'Edamame', 'Sesame oil', 'Soy sauce', 'Ginger'],
        'benefits': 'Contains natural phytoestrogens that may help balance hormones.',
        'image': 'tofu.jpg'
    },
    {
        'id': 4,
        'name': 'Iron-Boosting Spinach Salad',
        'description': 'Fresh salad loaded with iron-rich ingredients.',
        'ingredients': ['Fresh spinach', 'Chickpeas', 'Pumpkin seeds', 'Dried apricots', 'Feta cheese', 'Balsamic dressing'],
        'benefits': 'High in iron to combat fatigue and support energy levels.',
        'image': 'salad.jpg'
    },
    {
        'id': 5,
        'name': 'Bone-Strengthening Sardine Toast',
        'description': 'Simple yet nutritious sardines on whole grain toast.',
        'ingredients': ['Sardines in olive oil', 'Whole grain bread', 'Avocado', 'Cherry tomatoes', 'Lemon juice', 'Fresh herbs'],
        'benefits': 'Excellent source of calcium and vitamin D for bone health.',
        'image': 'sardine.jpg'
    }
]

# Sample cooking lessons
COOKING_LESSONS = [
    {
        'id': 1,
        'title': 'Menopause-Friendly Meal Prep Basics',
        'description': 'Learn the fundamentals of preparing nutritious meals that support hormonal balance.',
        'duration': '45 minutes',
        'level': 'Beginner',
        'topics': ['Ingredient selection', 'Meal planning', 'Storage tips', 'Portion control']
    },
    {
        'id': 2,
        'title': 'Cooking with Phytoestrogens',
        'description': 'Master the art of incorporating phytoestrogen-rich foods into your daily cooking.',
        'duration': '60 minutes',
        'level': 'Intermediate',
        'topics': ['Tofu preparation', 'Soy-based recipes', 'Flaxseed incorporation', 'Legume cooking']
    },
    {
        'id': 3,
        'title': 'Anti-Inflammatory Cooking Techniques',
        'description': 'Discover cooking methods that preserve nutrients and reduce inflammation.',
        'duration': '50 minutes',
        'level': 'Intermediate',
        'topics': ['Steaming vegetables', 'Healthy fats', 'Spice usage', 'Low-heat cooking']
    },
    {
        'id': 4,
        'title': 'Quick & Healthy Snacks for Energy',
        'description': 'Learn to prepare energy-boosting snacks to combat fatigue.',
        'duration': '30 minutes',
        'level': 'Beginner',
        'topics': ['Nut mixes', 'Fruit combinations', 'Yogurt parfaits', 'Smoothie bowls']
    }
]

# Sample physical activities
PHYSICAL_ACTIVITIES = [
    {
        'id': 1,
        'name': 'Gentle Yoga for Hormonal Balance',
        'description': 'Calming yoga sequences designed to support hormonal health.',
        'duration': '30-45 minutes',
        'intensity': 'Low',
        'benefits': ['Reduces stress', 'Improves flexibility', 'Supports sleep', 'Balances hormones']
    },
    {
        'id': 2,
        'name': 'Strength Training for Bone Health',
        'description': 'Weight-bearing exercises to maintain bone density.',
        'duration': '20-30 minutes',
        'intensity': 'Moderate',
        'benefits': ['Builds bone density', 'Increases metabolism', 'Improves posture', 'Builds muscle']
    },
    {
        'id': 3,
        'name': 'Walking Program',
        'description': 'Structured walking routines for cardiovascular health.',
        'duration': '30-60 minutes',
        'intensity': 'Low to Moderate',
        'benefits': ['Heart health', 'Weight management', 'Mood improvement', 'Joint-friendly']
    },
    {
        'id': 4,
        'name': 'Swimming & Water Aerobics',
        'description': 'Low-impact water exercises perfect for joint health.',
        'duration': '30-45 minutes',
        'intensity': 'Low to Moderate',
        'benefits': ['Low impact', 'Full body workout', 'Cooling effect', 'Stress relief']
    },
    {
        'id': 5,
        'name': 'Stretching & Flexibility Routine',
        'description': 'Daily stretching exercises to maintain flexibility.',
        'duration': '15-20 minutes',
        'intensity': 'Low',
        'benefits': ['Reduces stiffness', 'Improves mobility', 'Relaxation', 'Better circulation']
    }
]

# Sample community discussions
DISCUSSIONS = [
    {
        'id': 1,
        'title': 'Managing Hot Flashes Through Diet',
        'author': 'Sarah M.',
        'date': '2024-01-15',
        'content': 'I found that reducing caffeine and eating more soy-based foods helped with my hot flashes. What has worked for you?',
        'replies': 12
    },
    {
        'id': 2,
        'title': 'Best Supplements for Pre-Menopause',
        'author': 'Jennifer K.',
        'date': '2024-01-14',
        'content': 'My doctor recommended vitamin D and calcium. Would love to hear about other supplements that have helped.',
        'replies': 8
    },
    {
        'id': 3,
        'title': 'Exercise Routines That Actually Work',
        'author': 'Maria L.',
        'date': '2024-01-13',
        'content': 'Started doing yoga and light strength training. The difference in my energy levels is amazing!',
        'replies': 15
    },
    {
        'id': 4,
        'title': 'Meal Planning Tips for Busy Women',
        'author': 'Linda R.',
        'date': '2024-01-12',
        'content': 'Batch cooking on Sundays has been a game changer. Share your meal prep strategies!',
        'replies': 20
    }
]

# Sample menu items for catering
MENU_ITEMS = [
    {
        'id': 1,
        'name': 'Hormone Balance Bowl',
        'description': 'Quinoa, grilled tofu, steamed vegetables, and tahini dressing.',
        'price': 14.99,
        'category': 'Main Course',
        'tags': ['Phytoestrogens', 'High Protein', 'Vegan']
    },
    {
        'id': 2,
        'name': 'Bone Builder Plate',
        'description': 'Grilled salmon, kale salad, sweet potato, and calcium-rich dressing.',
        'price': 18.99,
        'category': 'Main Course',
        'tags': ['Omega-3', 'Calcium-Rich', 'High Protein']
    },
    {
        'id': 3,
        'name': 'Energy Boost Smoothie',
        'description': 'Greek yogurt, mixed berries, spinach, and chia seeds.',
        'price': 7.99,
        'category': 'Beverages',
        'tags': ['Antioxidants', 'Protein', 'Fiber']
    },
    {
        'id': 4,
        'name': 'Anti-Inflammatory Soup',
        'description': 'Turmeric-ginger soup with lentils and vegetables.',
        'price': 9.99,
        'category': 'Soups',
        'tags': ['Anti-inflammatory', 'Fiber', 'Warming']
    },
    {
        'id': 5,
        'name': 'Calcium Power Parfait',
        'description': 'Layers of Greek yogurt, granola, and fresh fruits.',
        'price': 8.99,
        'category': 'Breakfast',
        'tags': ['Calcium-Rich', 'Probiotics', 'Energy']
    }
]


@app.route('/')
def home():
    """Home page that welcomes users and displays service options."""
    return render_template('home.html')


@app.route('/catering', methods=['GET', 'POST'])
def catering():
    """Catering service page for ordering cooked foods."""
    if request.method == 'POST':
        # Process the catering order form
        name = request.form.get('name')
        email = request.form.get('email')
        dietary_needs = request.form.get('dietary_needs')
        health_goals = request.form.get('health_goals')
        selected_items = request.form.getlist('menu_items')
        
        # In a real app, this would save to a database
        flash('Your order has been received! We will contact you shortly to confirm your catering order.', 'success')
        return redirect(url_for('catering'))
    
    return render_template('catering.html', menu_items=MENU_ITEMS)


@app.route('/cooking-lessons', methods=['GET', 'POST'])
def cooking_lessons():
    """Cooking lessons page."""
    if request.method == 'POST':
        # Process the cooking lesson enrollment form
        name = request.form.get('name')
        email = request.form.get('email')
        experience_level = request.form.get('experience_level')
        health_concerns = request.form.get('health_concerns')
        preferred_lessons = request.form.getlist('lessons')
        
        # In a real app, this would save to a database
        flash('Thank you for enrolling! You will receive lesson details via email.', 'success')
        return redirect(url_for('cooking_lessons'))
    
    return render_template('cooking_lessons.html', lessons=COOKING_LESSONS)


@app.route('/recipes')
def recipes():
    """Recipes page with ingredients listing."""
    return render_template('recipes.html', recipes=RECIPES)


@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    """Individual recipe detail page."""
    recipe = next((r for r in RECIPES if r['id'] == recipe_id), None)
    if recipe is None:
        flash('Recipe not found.', 'error')
        return redirect(url_for('recipes'))
    return render_template('recipe_detail.html', recipe=recipe)


@app.route('/community', methods=['GET', 'POST'])
def community():
    """Community discussion page."""
    if request.method == 'POST':
        # Process new discussion post
        title = request.form.get('title')
        content = request.form.get('content')
        
        # In a real app, this would save to a database
        flash('Your discussion has been posted!', 'success')
        return redirect(url_for('community'))
    
    return render_template('community.html', discussions=DISCUSSIONS)


@app.route('/physical-activity')
def physical_activity():
    """Physical activity recommendations page."""
    return render_template('physical_activity.html', activities=PHYSICAL_ACTIVITIES)


@app.route('/about')
def about():
    """About page with information about the application."""
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
