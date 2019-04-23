from flask import Flask, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__, static_folder='images')

html_template = '''
<html>
    <body>
        <h1>Antimicrobial Resistance (AMR) Data for Klebsiella pneumoniae</h1>
        <h3>Please choose a country</h3>
        <form method='POST' action='/show' >
            <select name='selected_country'>
            {countries}
            </select>
            <input type='submit' />
        </form>
        {show}
    </body>
</html>
'''

df = pd.read_csv('data/klebsiella.csv')

c = df['Country'].unique()
new_c = []
for el in c:
    new_el = '<option value="{0}">{0}</option>'.format(el)
    new_c.append(new_el)

new_c_str = '\n'.join(new_c)

@app.route('/images/<country>')
def create_plot(country):
    plt.figure(figsize=(10, 4))
    df2 = df[(df['Country']==country)]
    antibiotics = df2['Antibiotic'].unique().tolist()
    legend_entries = []

    for antibiotic in antibiotics:
        df_filt = df2[df2['Antibiotic']==antibiotic]
        if df_filt.shape[0] >= 5:
            plt.plot( 'Year', 'PercResistant', data=df_filt)
            legend_entries.append(antibiotic)
    plt.legend(legend_entries, bbox_to_anchor=(1.05, 1.0))
    plt.ylim(-5,105)
    plt.ylabel('Percentage')
    plt.xlabel('Year')
    plt.title('K. pneumoniae AMR in {}'.format(country))
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img)
    img.seek(0)

    return send_file(img, mimetype='image/png')

@app.route('/')
def index_page():
    response = html_template.format(countries=new_c_str, show='')
    return response

@app.route('/show', methods=['POST'])
def show_resistance():
    result = request.form['selected_country']
    figure = '<img src="images/{}" />'.format(result)
    response = html_template.format(countries=new_c_str, show=figure)
    return response

if __name__ == '__main__':
    app.run(debug=True)
