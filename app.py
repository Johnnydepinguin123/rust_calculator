from flask import Flask, request, jsonify, render_template, url_for

app = Flask(__name__, static_url_path='/static')

# Define recycling values for components (60% mode)
RECYCLING_VALUES_60 = {
    "road.sign": {"scrap": 6, "hqm": 2, "metal": 0},
    "metal.pipe": {"scrap": 6, "hqm": 2, "metal": 0},
    "metal.blade": {"scrap": 2, "hqm": 0, "metal": 18},
    "metal.spring": {"scrap": 12, "hqm": 2, "metal": 0},
    "smg.body": {"scrap": 18, "hqm": 2, "metal": 0},
    "sar.body": {"scrap": 18, "hqm": 2, "metal": 90},
    "rifle.body": {"scrap": 30, "hqm": 2, "metal": 0},
    "sheet.metal": {"scrap": 9, "hqm": 2, "metal": 120},
    "tech.trash": {"scrap": 24, "hqm": 2, "metal": 0},
    "gears": {"scrap": 12, "hqm": 0, "metal": 15},
    "tarp": {"scrap": 0, "hqm": 0, "metal": 0, "cloth": 60},
    "sewing.kit": {"scrap": 0, "hqm": 0, "metal": 0, "cloth": 48},
    "rope": {"scrap": 0, "hqm": 0, "metal": 0, "cloth": 18}
}

# Define recycling values for components (40% mode)
RECYCLING_VALUES_40 = {
    "road.sign": {"scrap": 4, "hqm": 1, "metal": 0},
    "metal.pipe": {"scrap": 4, "hqm": 1, "metal": 0},
    "metal.blade": {"scrap": 1, "hqm": 0, "metal": 12},
    "metal.spring": {"scrap": 8, "hqm": 1, "metal": 0},
    "smg.body": {"scrap": 12, "hqm": 1, "metal": 0},
    "sar.body": {"scrap": 12, "hqm": 1, "metal": 60},
    "rifle.body": {"scrap": 20, "hqm": 1, "metal": 0},
    "sheet.metal": {"scrap": 6, "hqm": 1, "metal": 80},
    "tech.trash": {"scrap": 16, "hqm": 1, "metal": 0},
    "gears": {"scrap": 8, "hqm": 0, "metal": 10},
    "tarp": {"scrap": 0, "hqm": 0, "metal": 0, "cloth": 40},
    "sewing.kit": {"scrap": 0, "hqm": 0, "metal": 0, "cloth": 32},
    "rope": {"scrap": 0, "hqm": 0, "metal": 0, "cloth": 12}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json
        mode = data.get('mode', '60')  # Default to 60% mode
        
        # Select the appropriate recycling values based on mode
        recycling_values = RECYCLING_VALUES_40 if mode == '40' else RECYCLING_VALUES_60
        
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
            'gears': int(data.get('gears', 0)),
            'tarp': int(data.get('tarp', 0)),
            'sewing.kit': int(data.get('sewing_kit', 0)),
            'rope': int(data.get('rope', 0))
        }
        
        # Calculate totals
        total_scrap = sum(components[item] * recycling_values[item]["scrap"] for item in components)
        total_hqm = sum(components[item] * recycling_values[item]["hqm"] for item in components)
        total_metal = sum(components[item] * recycling_values[item]["metal"] for item in components)
        total_cloth = sum(components[item] * recycling_values[item].get("cloth", 0) for item in components)
        
        return jsonify({
            'scrap': total_scrap,
            'hqm': total_hqm,
            'metal': total_metal,
            'cloth': total_cloth
        })
        
    except (ValueError, KeyError) as e:
        return jsonify({'error': 'Invalid input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True) 