import pandas as pd
class Loader:
    @staticmethod
    def store(data_frame: pd.DataFrame, output_path: str):
        """
        Stores a DataFrame to the specified output path.

        Args:
            data_frame (pandas.DataFrame): The DataFrame to be stored.
            output_path (str): The path where the DataFrame will be saved.

        Returns:
            None
        """        
        data_frame.to_csv(output_path + "/output.csv", index=False)