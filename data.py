#imports
import json
import logging

class DataAccessObject:
    def __init__(self, data_file):

        """
        Initializes the DataAccessObject to load and structure data from a JSON file.

        Args:
            data_file (str): The path to the JSON file containing asset data.
        """

        try:    # try catch to failsafe errors
            with open(data_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            logging.error(f"Data file '{data_file}' not found") # Log error
            raise
        except json.JSONDecodeError:
            logging.error(f"Failed to parse JSON data from '{data_file}'")  # Log error
            raise

    def get_asset_data(self, asset_id):

        """
        Retrieves data for a specific asset from the loaded JSON data.

        Args:
            asset_id (int): The ID of the asset to retrieve data for.

        Returns:
            dict: A dictionary containing the data for the requested asset.
        """

        asset_info = self.data["asset"][asset_id - 1]
        energy_demand = self.get_asset_energy_demand(asset_id)
        energy_output = self.get_asset_energy_output(asset_id)
        return {
            "name": asset_info["name"],
            "energy_demand": energy_demand,
            "energy_output": energy_output
        }

    def get_asset_energy_demand(self, asset_id):

        """
        Retrieves energy demand data for a specific asset from the loaded JSON data.

        Args:
            asset_id (int): The ID of the asset to retrieve data for.

        Returns:
            dict: A dictionary containing energy demand data for the requested asset,
                      in the format {energy_type: {system, value}}.
                      If no data is found for the asset, returns an empty dictionary.
        """

        demand = {}
        for item in self.data["asset_energy_demand"]: # Iterates through the "asset_energy_demand" data
            if item["asset"] == asset_id: # If it finds a matching object
                energy_type_id = item["energy_type"]
                energy_type_name = self.data["energy_type"][energy_type_id - 1]["name"]  # -1 because of object positioning
                system_id = self.get_energy_system_id(item["asset"], energy_type_id)    # get id
                if (system_id != -1):   #if id is -1, means that doesn't exist, thus no need to fetch next data
                    system_name = self.data["energy_system"][system_id - 1]["name"]
                    demand[energy_type_name] = {
                        'system': system_name,
                        'value': item["energy_demand"]
                    }

        return demand

    def get_asset_energy_output(self, asset_id):

        """
        Retrieves the energy output value for a specific asset from the loaded JSON data.

        Args:
            asset_id (int): The ID of the asset to retrieve the energy output for.

        Returns:
            int: The energy output value for the asset, or None if not found.
        """

        for item in self.data["asset_energy_output"]: # Iterates through the "asset_energy_output" data
            if item["asset"] == asset_id: # If it finds a matching object
                return item["energy_output"] # Returns the object

    def get_energy_system_id(self, asset_id, energy_type_id):

        """
        Retrieves the ID of the energy system associated with a given asset and energy type.

        Args:
            asset_id (int): The ID of the asset.
            energy_type_id (int): The ID of the energy type.

        Returns:
            int: The ID of the corresponding energy system, or -1 if not found.
        """

        returnItem = -1 # Initialize the return value to -1 (not found)

        for item in self.data["asset_energy_system"]: # Iterates through the "asset_energy_system" data
            if item["asset"] == asset_id and item["energy_type"] == energy_type_id: # If it finds a matching object
                returnItem = item["energy_system"] # Returns the object
        return returnItem
