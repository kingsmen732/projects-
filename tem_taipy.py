from taipy.gui import Gui
import taipy.gui.builder as tgb
import numpy as np
import pandas as pd

# create data with Dates
data = pd.DataFrame(
    {
        "Date": pd.date_range("2020-01-01", periods=5, freq="ME", tz="Europe/Paris").tz_convert("UTC"),
        "Value": np.random.rand(5),
    }
)

with tgb.Page() as page:
    tgb.chart("{data}", x="Date", y="Value", height="800px")
    tgb.table("{data}")

print(data)

Gui(page).run(use_reloader=True, port=5003, title="Date issue")