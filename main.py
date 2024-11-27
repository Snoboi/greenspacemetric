from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)

# Define the output directory for server-side saving
OUTPUT_DIR = os.path.join('assets', 'footprints_output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to save categorized footprints
@app.route('/save-footprints', methods=['POST'])
def save_footprints():
    data = request.json
    category = data.get('category')
    geojson = data.get('geojson')

    if not category or not geojson:
        return jsonify({'error': 'Invalid data'}), 400

    file_path = os.path.join(OUTPUT_DIR, f'{category}.geojson')
    with open(file_path, 'w') as file:
        json.dump(geojson, file)

    return jsonify({'message': f'Footprints for {category} saved successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
