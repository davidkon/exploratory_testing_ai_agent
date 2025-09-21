import pandas as pd

class RequirementsIngestionModule:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.requirements = None
        self.coverage_status = None
        self.load_requirements()

    def load_requirements(self):
        # Load the CSV file into a DataFrame
        self.requirements = pd.read_csv(self.csv_path)
        # Initialize coverage status dictionary: requirement ID -> covered or not
        # Assumes a column 'RequirementID' exists in CSV
        self.coverage_status = {req_id: False for req_id in self.requirements['RequirementID']}

    def mark_covered(self, requirement_id):
        if requirement_id in self.coverage_status:
            self.coverage_status[requirement_id] = True

    def get_coverage_report(self):
        total = len(self.coverage_status)
        covered = sum(self.coverage_status.values())
        uncovered = total - covered
        return {
            'total_requirements': total,
            'covered_requirements': covered,
            'uncovered_requirements': uncovered
        }

    def get_uncovered_requirements(self):
        # Return list of uncovered requirement IDs
        return [req_id for req_id, covered in self.coverage_status.items() if not covered]

    def get_requirement_details(self, requirement_id):
        # Return full details of a requirement by ID
        entry = self.requirements[self.requirements['RequirementID'] == requirement_id]
        if not entry.empty:
            return entry.iloc[0].to_dict()
        return None
