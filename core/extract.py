import json
import pandas as pd

from airflow.decorators import task


class Extractor:

    def load(self):
        """
        Loads data from the given file paths and returns a pandas DataFrame.

        Returns:
            p
        """
        output = []
        for f_path in self.get_file_paths():
            with open(f_path, 'r') as f:
                # Reading from json file
                json_data = json.load(f)
                output.extend(json.loads(json_data))
        return pd.DataFrame(output)
        
    def get_file_paths(self):
        """
        Returns a list of file paths.

        This method retrieves a list of file paths from a specific source or directory.
        
        Returns:
            list: A list of file paths.        
        """
        return ["sample.json"]

    
@task
def extract_task():
    e = Extractor()   
    load_task = PythonOperator(task_id="load",python_callable=e.load)
    return load_task
    

    
