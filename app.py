#imports
from flask import Flask, jsonify, render_template
from data import DataAccessObject
from processor import EnergyProcessor
import logging

logging.basicConfig(level=logging.INFO)  # Change to DEBUG for more detailed logs

# Initialize the Flask/FastAPI application
app = Flask(__name__)

# Create a DataAccessObject instance to access data from json_database.json
dao = DataAccessObject("json_database.json")

# Create an EnergyProcessor instance to calculate energy demand
processor = EnergyProcessor()

# example route - http://127.0.0.1:5000/asset/3
@app.route("/asset/<int:asset_id>", methods=["GET"])
def get_asset_energy_data(asset_id):
    """
    Retrieve processed energy data for a specific asset based on its ID via REST GET call /asset/{asset_id}.

    Args:
        asset_id (int): The ID of the asset to retrieve data for.

    Returns:
        dict: A dictionary containing the processed energy data in the specified format.
              In case of errors, returns an error response with status code 400.
    """

    try:    # try catch to failsafe errors
        asset_data = dao.get_asset_data(asset_id)
        processed_data = processor.calculate_reduced_demand(asset_data)
        processed_data["name"] = asset_data["name"]
        #return jsonify(processed_data) # return as json
        return render_template("index.html", processed_data=processed_data) #return as HTML

    except (KeyError, ValueError) as e:
        logging.error(f"Error processing asset {asset_id}: {e}")    # Log error
        return jsonify({"error": "Invalid asset ID or data format"}), 400

# Ensure main block for direct execution, if applicable
if __name__ == "__main__":
    app.run(debug=True) # Start the application in debug mode
