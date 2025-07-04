import pandas as pd

class Portfolio:
    def __init__(self, file_path="app/resource/my_portfolio.csv"):
        self.data = pd.read_csv(file_path)

    def get_all_links(self):
        return self.data

    def match_links(self, skills, portfolio_df):
        matched = []
        for skill in skills:
            matches = portfolio_df[portfolio_df["Techstack"].str.contains(skill, case=False, na=False)]
            matched.extend(matches["Links"].tolist())
        return matched[:3]  # return top 3
