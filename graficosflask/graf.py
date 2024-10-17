# Importing required functions 
import os
import numpy as np 
import matplotlib.pyplot as plt 
from flask import Flask, render_template 


# Flask constructor 
app = Flask(__name__) 

# Generate a scatter plot and returns the figure 
def get_plot(): 
	data = { 
		'a': np.arange(50), 
		'c': np.random.randint(0, 50, 50), 
		'd': np.random.randn(50) 
	} 
	data['b'] = data['a'] + 10 * np.random.randn(50) 
	data['d'] = np.abs(data['d']) * 100

	plt.scatter('a', 'b', c='c', s='d', data=data) 
	plt.xlabel('X label') 
	plt.ylabel('Y label') 
	return plt 

# Root URL 
@app.get('/') 
def single_converter(): 
	# Get the matplotlib plot 
	plot = get_plot() 

	# Save the figure in the static directory 
	plot.savefig(os.path.join('static', 'images', 'plot.png')) 

	return render_template('doc1.html') 

# Main Driver Function 
if __name__ == '__main__': 
	# Run the application on the local development server 
	app.run(debug=True) 
