from flask import Flask, render_template,request,redirect
from dotenv import load_dotenv
import pymysql
import os
load_dotenv()

app = Flask(__name__)


connection = pymysql.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    port = int(os.getenv("DB_PORT")),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME"),
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def home():

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM resources")

    resources = cursor.fetchall()

    cursor.close()

    return render_template("index.html", resources=resources)


@app.route('/add-resource', methods=['GET', 'POST'])
def add_resource():

    if request.method == 'POST':

        resource_name = request.form['resource_name']
        resource_type = request.form['resource_type']
        region = request.form['region']
        status = request.form['status']
        owner = request.form['owner']

        cursor = connection.cursor()

        sql = """
        INSERT INTO resources
        (resource_name, resource_type, region, status, owner)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            resource_name,
            resource_type,
            region,
            status,
            owner
        ))

        connection.commit()

        cursor.close()

        return redirect('/')

    return render_template("add_resource.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug = True)
 
      

