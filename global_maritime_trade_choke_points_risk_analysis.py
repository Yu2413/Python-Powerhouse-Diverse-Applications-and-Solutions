import folium
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt


class GeopoliticalTradeChokepoints:
    def __init__(self):
        self.choke_points = {
            'Strait of Hormuz': {
                'coordinates': [27.0844, 56.2654],
                'region': 'Middle East',
                'strategic_importance': 'Oil Transport',
                'daily_oil_volume': 20.4,  # million barrels
                'geopolitical_tension': 'High',
                'countries_involved': ['Iran', 'Oman', 'UAE']
            },
            'Strait of Malacca': {
                'coordinates': [3.4, 98.8],
                'region': 'Southeast Asia',
                'strategic_importance': 'Asian Trade Route',
                'daily_trade_volume': 25.0,  # trillion USD
                'geopolitical_tension': 'Moderate',
                'countries_involved': ['Malaysia', 'Indonesia', 'Singapore']
            },
            'Suez Canal': {
                'coordinates': [30.5852, 32.5499],
                'region': 'Middle East/Africa',
                'strategic_importance': 'Europe-Asia Maritime Route',
                'daily_trade_volume': 15.7,  # trillion USD
                'geopolitical_tension': 'High',
                'countries_involved': ['Egypt']
            },
            'Panama Canal': {
                'coordinates': [9.0, -79.5],
                'region': 'Central America',
                'strategic_importance': 'North-South Trade',
                'daily_trade_volume': 12.5,  # trillion USD
                'geopolitical_tension': 'Low',
                'countries_involved': ['Panama']
            },
            'Bab el-Mandeb Strait': {
                'coordinates': [12.5, 43.3],
                'region': 'Middle East/Africa',
                'strategic_importance': 'Red Sea Access',
                'daily_oil_volume': 6.2,  # million barrels
                'geopolitical_tension': 'Very High',
                'countries_involved': ['Yemen', 'Djibouti', 'Eritrea']
            },
            'Strait of Gibraltar': {
                'coordinates': [36.0, -5.5],
                'region': 'Europe/Africa',
                'strategic_importance': 'Mediterranean Access',
                'daily_trade_volume': 8.5,  # trillion USD
                'geopolitical_tension': 'Low',
                'countries_involved': ['Spain', 'Morocco']
            }
        }

    def create_geopolitical_risk_map(self):
        # Create world map
        world_map = folium.Map(location=[20, 0], zoom_start=2)

        # Color mapping for tension levels
        tension_colors = {
            'Very High': 'red',
            'High': 'orange',
            'Moderate': 'yellow',
            'Low': 'green'
        }

        # Add markers for choke points
        for name, details in self.choke_points.items():
            folium.CircleMarker(
                location=details['coordinates'],
                radius=10,
                popup=f"""
                <b>{name}</b><br>
                Region: {details['region']}<br>
                Strategic Importance: {details['strategic_importance']}<br>
                Geopolitical Tension: {details['geopolitical_tension']}
                """,
                color=tension_colors.get(details['geopolitical_tension'], 'blue'),
                fill=True,
                fill_opacity=0.7
            ).add_to(world_map)

        world_map.save('geopolitical_choke_points.html')

    def analyze_trade_disruption_risk(self):
        # Calculate composite risk score
        risk_scores = {}

        for name, details in self.choke_points.items():
            # Develop risk scoring algorithm
            tension_score = {
                'Very High': 10,
                'High': 7,
                'Moderate': 4,
                'Low': 1
            }

            trade_volume = details.get('daily_trade_volume', 0)
            oil_volume = details.get('daily_oil_volume', 0)

            risk_score = (
                    tension_score.get(details['geopolitical_tension'], 0) *
                    (trade_volume + oil_volume) / 10
            )

            risk_scores[name] = {
                'risk_score': risk_score,
                'tension_level': details['geopolitical_tension']
            }

        # Sort and display risk analysis
        sorted_risks = sorted(risk_scores.items(), key=lambda x: x[1]['risk_score'], reverse=True)

        print("Trade Disruption Risk Analysis:")
        for location, risk_data in sorted_risks:
            print(f"{location}: Risk Score {risk_data['risk_score']:.2f} - {risk_data['tension_level']} Tension")

    def generate_trade_impact_report(self):
        # Simulate potential global economic impact of trade disruptions
        total_global_trade = 32.0  # trillion USD

        disruption_scenarios = {
            'Strait of Hormuz': 0.4,  # 40% disruption potential
            'Suez Canal': 0.3,  # 30% disruption potential
            'Strait of Malacca': 0.2  # 20% disruption potential
        }

        economic_impact = {}
        for point, disruption_rate in disruption_scenarios.items():
            point_details = self.choke_points[point]
            estimated_impact = point_details.get('daily_trade_volume', 0) * disruption_rate

            economic_impact[point] = {
                'disruption_rate': disruption_rate * 100,
                'estimated_economic_loss': estimated_impact
            }

        print("\nGlobal Trade Disruption Economic Impact:")
        for location, impact in economic_impact.items():
            print(f"{location}:")
            print(f"  Disruption Rate: {impact['disruption_rate']}%")
            print(f"  Estimated Economic Loss: ${impact['estimated_economic_loss']} trillion")


def main():
    trade_analysis = GeopoliticalTradeChokepoints()

    # Generate interactive map
    trade_analysis.create_geopolitical_risk_map()

    # Analyze trade disruption risks
    trade_analysis.analyze_trade_disruption_risk()

    # Generate economic impact report
    trade_analysis.generate_trade_impact_report()


if __name__ == "__main__":
    main()