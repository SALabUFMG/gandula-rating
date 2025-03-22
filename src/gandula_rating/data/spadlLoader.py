from typing import Any, Dict, Optional, Union
import pandas as pd
import numpy as np
from socceraction.spadl.kloppy import convert_to_actions
from kloppy.domain.models.event import EventDataset
from kloppy import statsbomb
import gandula

def get_spadl_actions(
    gandula_df: Optional[pd.DataFrame] = None,
    game_id: Optional[Union[str, int]] = None,
) -> pd.DataFrame:

    #    dataset = gandula.to_kloppy(gandula_df)

    dataset = statsbomb.load_open_data(event_types=["pass", "shot"])
    
    # Convert Kloppy dataset to SPADL actions
    actions = convert_to_actions(dataset, game_id=game_id)  
    
    return actions


def save_spadl_actions(
    actions: pd.DataFrame,
    file_path: str = "data/interim/spadlActions.pkl"
):
    """
    Save SPADL actions to a pickle file.

    Parameters:
        actions (pd.DataFrame): The SPADL actions to save.
        file_path (str): The path to save the SPADL actions.
    """

    actions.to_pickle(file_path)
