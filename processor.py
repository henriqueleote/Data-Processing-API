class EnergyProcessor:
    def calculate_reduced_demand(self, asset_data):
        """
        Calculates the reduced energy demand for an asset, considering electricity output.

        Args:
            asset_data (dict): A dictionary containing asset data, including energy demand and output.

        Returns:
            dict: A dictionary containing the reduced energy demand, total demand, and output reduction percentage.
        """

        reduced_demand = {}
        total_demand = 0

        for energy_type, demand_group in asset_data["energy_demand"].items():   # Iterates through the "energy_demand" data
            output = asset_data["energy_output"]

            demand = demand_group["value"]
            system = demand_group["system"]

            if output < 0:  # Check for negative output (unlikely but good practice)
                print(f"Warning: Negative energy output detected for asset {asset_data['name']}")
                output = 0

            if output > 0 and system == "electricity":  # Reduce demand only from electricity output
                reduction = min(output, demand)
                demand -= reduction
                output -= reduction
                total_demand += demand
            else:
                total_demand += demand

            reduced_demand[energy_type] = demand

        energy_output_reduction = (asset_data["energy_output"] / total_demand) * 100
        return {    # Return values to be displayed
            "energy_demand": reduced_demand,
            "total_energy_demand": total_demand,
            "energy_output_reduction": f"{energy_output_reduction:.2f}"
        }
