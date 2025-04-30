from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__, static_url_path='/static')

# Define recycling values for components
RECYCLING_VALUES = {
    "road.sign": {"scrap": 6, "hqm": 2, "metal": 0},
    "metal.pipe": {"scrap": 6, "hqm": 2, "metal": 0},
    "metal.blade": {"scrap": 2, "hqm": 0, "metal": 18},
    "metal.spring": {"scrap": 12, "hqm": 2, "metal": 0},
    "smg.body": {"scrap": 18, "hqm": 2, "metal": 0},
    "sar.body": {"scrap": 18, "hqm": 2, "metal": 90},
    "rifle.body": {"scrap": 30, "hqm": 2, "metal": 0},
    "sheet.metal": {"scrap": 9, "hqm": 2, "metal": 120},
    "tech.trash": {"scrap": 24, "hqm": 2, "metal": 0},
    "gears": {"scrap": 12, "hqm": 0, "metal": 15}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        
        # Get numbers from input
        components = {
            'road.sign': int(data.get('signs', 0)),
            'metal.pipe': int(data.get('pipes', 0)),
            'metal.blade': int(data.get('blades', 0)),
            'metal.spring': int(data.get('springs', 0)),
            'smg.body': int(data.get('smg', 0)),
            'sar.body': int(data.get('sar', 0)),
            'rifle.body': int(data.get('rifle', 0)),
            'sheet.metal': int(data.get('sheet', 0)),
            'tech.trash': int(data.get('tech', 0)),
            'gears': int(data.get('gears', 0))
        }
        
        # Calculate totals
        total_scrap = sum(components[item] * RECYCLING_VALUES[item]["scrap"] for item in components)
        total_hqm = sum(components[item] * RECYCLING_VALUES[item]["hqm"] for item in components)
        total_metal = sum(components[item] * RECYCLING_VALUES[item]["metal"] for item in components)
        
        return jsonify({
            'scrap': total_scrap,
            'hqm': total_hqm,
            'metal': total_metal
        })
        
    except (ValueError, KeyError) as e:
        return jsonify({'error': 'Invalid input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True) 