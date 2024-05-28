from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'host.docker.internal'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'sensory_debug')
    )
    return conn

@app.route('/senzory', methods=['GET'])
def get_senzory():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = """
    SELECT s.id_sen, s.nazev, s.typ, s.misto, s.frekvence, st.barva as stav, 
           (SELECT COUNT(*) FROM zaznamy z WHERE z.id_sen = s.id_sen) as count_records
    FROM senzory s
    JOIN stav st ON s.id_stav = st.id_stav
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    
    sensors = []
    for row in rows:
        sensors.append({
            "id": row["id_sen"],
            "nazev": row["nazev"],
            "typ": row["typ"],
            "misto": row["misto"],
            "frekvence": row.get("frekvence"),
            "stav": row["stav"],
            "count_records": row["count_records"]
        })
    
    cursor.close()
    conn.close()
    
    return jsonify(sensors)


@app.route('/pocetzaminutu', methods=['GET'])
def get_zaminutu():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    current_time = datetime.datetime.now()
    one_minute_ago = current_time - datetime.timedelta(minutes=1)
    
    query = """
    SELECT COUNT(*) as count
    FROM zaznamy
    WHERE cas >= %s AND cas <= %s
    """
    
    cursor.execute(query, (one_minute_ago, current_time))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return jsonify(result)

@app.route('/pocetsenzoru', methods=['GET'])
def get_sensors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    query = "SELECT COUNT(*) as count FROM senzory"
    
    cursor.execute(query)
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
