import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import StringIO
from datetime import datetime
import geopandas as gpd
from shapely.geometry import Point
import seaborn as sns
from sklearn.neighbors import KernelDensity
import folium
from folium.plugins import HeatMap


class TornadoRiskAnalysis:
    def __init__(self, state='OH', city='Columbus', radius_miles=50):
        """
        Initialize the tornado risk analysis tool.

        Parameters:
        -----------
        state : str
            State abbreviation (e.g., 'OH' for Ohio)
        city : str
            City name (e.g., 'Columbus')
        radius_miles : float
            Radius in miles around the city to analyze
        """
        self.state = state
        self.city = city
        self.radius_miles = radius_miles
        self.data = None
        self.city_coords = None
        self.local_tornadoes = None

        # EF scale classification and corresponding wind speeds (mph)
        self.ef_scale = {
            0: "EF0 (65-85 mph)",
            1: "EF1 (86-110 mph)",
            2: "EF2 (111-135 mph)",
            3: "EF3 (136-165 mph)",
            4: "EF4 (166-200 mph)",
            5: "EF5 (>200 mph)"
        }

    def download_data(self):
        """Download NOAA tornado data."""
        print("Downloading NOAA tornado data...")
        url = "https://www.spc.noaa.gov/wcm/data/1950-2022_actual_tornadoes.csv"

        try:
            response = requests.get(url)
            response.raise_for_status()

            # Parse the CSV data
            self.data = pd.read_csv(StringIO(response.text))

            # Convert date information to datetime
            # Using pandas string methods instead of deprecated agg method
            date_str = self.data['yr'].astype(str) + '-' + self.data['mo'].astype(str) + '-' + self.data['dy'].astype(
                str)
            self.data['date'] = pd.to_datetime(date_str)

            # Convert F-scale to EF-scale (post-2007 classification)
            # For simplicity, we're treating F0-F5 as equivalent to EF0-EF5
            self.data['ef'] = self.data['mag']

            print(f"Downloaded data with {len(self.data)} tornado records.")
            return True
        except Exception as e:
            print(f"Error downloading data: {e}")
            return False

    def get_city_coordinates(self):
        """Get the latitude and longitude for the specified city."""
        try:
            # Use a geocoding service to get coordinates
            # For this example, hardcoding Columbus, OH coordinates
            if self.city.lower() == 'columbus' and self.state.lower() == 'oh':
                lat, lon = 39.9612, -82.9988
            else:
                # In a real implementation, you would use a geocoding service here
                print("Only Columbus, OH is supported in this example")
                lat, lon = 39.9612, -82.9988

            self.city_coords = (lat, lon)
            print(f"City coordinates: {self.city_coords}")
            return True
        except Exception as e:
            print(f"Error getting city coordinates: {e}")
            return False

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        """
        Calculate the great circle distance between two points
        on the earth specified in decimal degrees of latitude and longitude.
        """
        # Convert decimal degrees to radians
        # Use np.radians directly instead of map function for numpy 2.0 compatibility
        lat1_rad = np.radians(lat1)
        lon1_rad = np.radians(lon1)
        lat2_rad = np.radians(lat2)
        lon2_rad = np.radians(lon2)

        # Haversine formula
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad

        # Use numpy's functions directly
        a = np.sin(dlat / 2) ** 2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2) ** 2
        c = 2 * np.arcsin(np.sqrt(a))
        r = 3956  # Radius of earth in miles
        return c * r

    def filter_local_tornadoes(self):
        """Filter tornadoes within the specified radius of the city."""
        if self.data is None or self.city_coords is None:
            print("Data or city coordinates not available")
            return False

        city_lat, city_lon = self.city_coords

        # Calculate distance from the city to each tornado - vectorized approach for numpy 2.0+
        slat_array = np.array(self.data['slat'])
        slon_array = np.array(self.data['slon'])

        # Vectorized calculation
        # Convert to radians
        city_lat_rad = np.radians(city_lat)
        city_lon_rad = np.radians(city_lon)
        slat_rad = np.radians(slat_array)
        slon_rad = np.radians(slon_array)

        # Haversine formula components
        dlon = slon_rad - city_lon_rad
        dlat = slat_rad - city_lat_rad

        a = np.sin(dlat / 2) ** 2 + np.cos(city_lat_rad) * np.cos(slat_rad) * np.sin(dlon / 2) ** 2
        c = 2 * np.arcsin(np.sqrt(a))
        distances = c * 3956  # Earth radius in miles

        # Filter tornadoes within the radius
        mask = distances <= self.radius_miles
        self.local_tornadoes = self.data[mask].copy()

        # Create a geometry column for spatial analysis
        geometry = [Point(xy) for xy in zip(self.local_tornadoes['slon'], self.local_tornadoes['slat'])]
        self.local_tornadoes = gpd.GeoDataFrame(self.local_tornadoes, geometry=geometry)

        print(
            f"Found {len(self.local_tornadoes)} tornadoes within {self.radius_miles} miles of {self.city}, {self.state}")
        return True

    def analyze_ef_distribution(self):
        """Analyze the distribution of tornadoes by EF scale."""
        if self.local_tornadoes is None:
            print("Local tornado data not available")
            return None

        # Count tornadoes by EF scale
        ef_counts = self.local_tornadoes['ef'].value_counts().sort_index()

        # Ensure all EF scales are represented
        for ef in range(6):  # EF0 to EF5
            if ef not in ef_counts.index:
                ef_counts[ef] = 0

        ef_counts = ef_counts.sort_index()

        return ef_counts

    def analyze_monthly_distribution(self):
        """Analyze the monthly distribution of tornadoes."""
        if self.local_tornadoes is None:
            print("Local tornado data not available")
            return None

        monthly_counts = self.local_tornadoes['mo'].value_counts().sort_index()

        # Ensure all months are represented
        for month in range(1, 13):
            if month not in monthly_counts.index:
                monthly_counts[month] = 0

        monthly_counts = monthly_counts.sort_index()

        # Convert month numbers to names
        month_names = {
            1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
        }

        monthly_counts.index = [month_names[m] for m in monthly_counts.index]

        return monthly_counts

    def analyze_yearly_trend(self):
        """Analyze the yearly trend of tornadoes."""
        if self.local_tornadoes is None:
            print("Local tornado data not available")
            return None

        yearly_counts = self.local_tornadoes['yr'].value_counts().sort_index()

        # Fill in missing years
        year_range = range(int(min(yearly_counts.index)), int(max(yearly_counts.index)) + 1)
        for year in year_range:
            if year not in yearly_counts.index:
                yearly_counts[year] = 0

        yearly_counts = yearly_counts.sort_index()

        return yearly_counts

    def calculate_risk_score(self):
        """
        Calculate an overall tornado risk score for the area.
        Score ranges from 0-100, with higher values indicating higher risk.
        """
        if self.local_tornadoes is None or len(self.local_tornadoes) == 0:
            return 0

        # Get the total number of years in the dataset
        years_span = self.local_tornadoes['yr'].max() - self.local_tornadoes['yr'].min() + 1

        # Calculate the average number of tornadoes per year
        tornadoes_per_year = len(self.local_tornadoes) / years_span

        # Calculate a weighted score based on EF scale
        # Higher weight for stronger tornadoes
        ef_weights = np.array([1, 2, 4, 8, 16, 32])  # For EF0-EF5

        # Calculate weighted sum using numpy operations
        ef_counts = np.zeros(6)
        for ef in range(6):
            ef_counts[ef] = np.sum(self.local_tornadoes['ef'] == ef)

        weighted_sum = np.sum(ef_counts * ef_weights)

        # Normalize to a score out of 100
        norm_factor = 20  # Tuning parameter
        risk_score = min(100, (weighted_sum / years_span) * norm_factor)

        return risk_score

    def generate_risk_report(self):
        """Generate a comprehensive risk report."""
        risk_score = self.calculate_risk_score()
        ef_distribution = self.analyze_ef_distribution()
        monthly_distribution = self.analyze_monthly_distribution()
        yearly_trend = self.analyze_yearly_trend()

        # Risk level categorization
        risk_levels = [
            (0, 20, "Low"),
            (20, 40, "Moderate-Low"),
            (40, 60, "Moderate"),
            (60, 80, "Moderate-High"),
            (80, 100, "High")
        ]

        risk_level = next((level for min_val, max_val, level in risk_levels
                           if min_val <= risk_score < max_val), "High")

        report = {
            'city': self.city,
            'state': self.state,
            'radius_miles': self.radius_miles,
            'tornado_count': len(self.local_tornadoes),
            'risk_score': risk_score,
            'risk_level': risk_level,
            'ef_distribution': ef_distribution,
            'monthly_distribution': monthly_distribution,
            'yearly_trend': yearly_trend
        }

        return report

    def plot_ef_distribution(self):
        """Plot the distribution of tornadoes by EF scale."""
        ef_counts = self.analyze_ef_distribution()

        plt.figure(figsize=(10, 6))
        bars = plt.bar(ef_counts.index, ef_counts.values, color='skyblue')

        # Add labels to the bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
                     f'{int(height)}', ha='center', va='bottom')

        plt.title(f'Tornado Counts by EF Scale within {self.radius_miles} miles of {self.city}, {self.state}')
        plt.xlabel('EF Scale')
        plt.ylabel('Number of Tornadoes')
        plt.xticks(range(6), [self.ef_scale[i] for i in range(6)], rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

    def plot_monthly_distribution(self):
        """Plot the monthly distribution of tornadoes."""
        monthly_counts = self.analyze_monthly_distribution()

        plt.figure(figsize=(10, 6))
        bars = plt.bar(monthly_counts.index, monthly_counts.values, color='lightgreen')

        # Add labels to the bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
                     f'{int(height)}', ha='center', va='bottom')

        plt.title(f'Monthly Tornado Distribution within {self.radius_miles} miles of {self.city}, {self.state}')
        plt.xlabel('Month')
        plt.ylabel('Number of Tornadoes')
        plt.tight_layout()
        plt.show()

    def plot_yearly_trend(self):
        """Plot the yearly trend of tornadoes."""
        yearly_counts = self.analyze_yearly_trend()

        plt.figure(figsize=(12, 6))
        plt.plot(yearly_counts.index, yearly_counts.values, marker='o', linestyle='-', color='darkblue', alpha=0.7)

        # Add a 10-year moving average
        yearly_counts_df = pd.DataFrame(yearly_counts)
        yearly_counts_df.columns = ['count']
        yearly_counts_df['moving_avg'] = yearly_counts_df['count'].rolling(window=10, min_periods=1).mean()

        plt.plot(yearly_counts_df.index, yearly_counts_df['moving_avg'],
                 color='red', linestyle='--', linewidth=2, label='10-Year Moving Average')

        plt.title(f'Yearly Tornado Trend within {self.radius_miles} miles of {self.city}, {self.state}')
        plt.xlabel('Year')
        plt.ylabel('Number of Tornadoes')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def create_heatmap(self):
        """Create a heatmap of tornado occurrences."""
        if self.local_tornadoes is None or len(self.local_tornadoes) == 0:
            print("No local tornado data available for heatmap")
            return None

        # Create a map centered on the city
        city_map = folium.Map(location=self.city_coords, zoom_start=8)

        # Mark the city
        folium.Marker(
            self.city_coords,
            popup=f"{self.city}, {self.state}",
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(city_map)

        # Add a circle to show the analysis radius
        folium.Circle(
            self.city_coords,
            radius=self.radius_miles * 1609.34,  # convert miles to meters
            popup=f"{self.radius_miles} mile radius",
            color='green',
            fill=True,
            fill_opacity=0.1
        ).add_to(city_map)

        # Create heatmap data using numpy arrays
        heat_data = np.column_stack((
            self.local_tornadoes['slat'].values,
            self.local_tornadoes['slon'].values
        )).tolist()

        # Add heatmap layer
        HeatMap(heat_data).add_to(city_map)

        return city_map

    def run_analysis(self):
        """Run the complete tornado risk analysis."""
        print(f"Starting tornado risk analysis for {self.city}, {self.state}")

        # Download data
        if not self.download_data():
            return False

        # Get city coordinates
        if not self.get_city_coordinates():
            return False

        # Filter local tornadoes
        if not self.filter_local_tornadoes():
            return False

        # Generate risk report
        report = self.generate_risk_report()

        # Display results
        print("\n" + "=" * 50)
        print(f"TORNADO RISK ANALYSIS: {self.city}, {self.state}")
        print("=" * 50)
        print(f"Analysis radius: {self.radius_miles} miles")
        print(f"Total tornadoes in history: {report['tornado_count']}")
        print(f"Risk score (0-100): {report['risk_score']:.1f}")
        print(f"Risk level: {report['risk_level']}")
        print("=" * 50)

        # Display EF distribution
        print("\nEF Scale Distribution:")
        for ef, count in report['ef_distribution'].items():
            print(f"{self.ef_scale[ef]}: {count} tornadoes")

        # Generate plots
        self.plot_ef_distribution()
        self.plot_monthly_distribution()
        self.plot_yearly_trend()

        # Create heatmap
        heatmap = self.create_heatmap()

        return report


# Example usage
if __name__ == "__main__":
    # Initialize the analysis for Columbus, Ohio with a 50-mile radius
    analysis = TornadoRiskAnalysis(state='OH', city='Columbus', radius_miles=50)

    # Run the analysis
    report = analysis.run_analysis()