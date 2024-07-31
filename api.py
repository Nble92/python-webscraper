from flask import Flask, request, jsonify  # Corrected E231
import db

app = Flask(__name__)


@app.route('/')  # Corrected E303 and W293
def home():
    return 'Hello'

@app.route('/store', methods=['GET'])  # Corrected E302
def get():
    try:
        query = "SELECT * FROM closures"
        db.cursor.execute(query)
        results = db.cursor.fetchall()  # Fetch the results

        # Convert the results to a list of dicts (or similar, depending on your data structure)
        closures = []
        for row in results:
            closures.append({
                'Organization': row[1],
                'Status': row[2],
                # Add other columns as needed
            })

        return jsonify(closures)  # Return the data in JSON format

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Return an error message in case of an exception

@app.route('/store', methods=['POST'])  # Corrected E302
def store():
    data = request.json.get('data')
    if data and 'URL' in data:
        url = data['URL']
        district_name = data['DistrictName']
        district_status = data['Status']

        db.get_db_connection()
        try:
            query = "INSERT INTO SchoolClosures (URL, Dis trictName, Status) VALUES (%s, %s, %s);"  # Corrected E231
            db.cursor.execute(query, (url, district_name, district_status))  # Corrected E225

            # Commit the transaction  # Corrected E117
            db.conn.commit()

            return jsonify({'message': district_name + ' added successfully'}), 201  # Corrected E225

        except Exception as e:
            # Rollback in case of any error  # Corrected indentation E111
            db.conn.rollback()
            return jsonify({'error': str(e)}), 500

        finally:
            db.close_connection()

    else:
        return jsonify({'error': 'Invalid data provided'}), 400


if __name__ == '__main__':
    app.run(debug=True)  # Corrected E305 and W292


# Ensure there's a newline here at the end of the file
