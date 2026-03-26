import pandas as pd
import dash_mantine_components as dmc


def to_dmc_table(table):
    df = pd.DataFrame(table.data[1:], columns=table.data[0])
    df = df.astype(str)
    return dmc.Table(
        data={"head": df.columns.tolist(), "body": df.values.tolist()},
        striped=True,
        highlightOnHover=True,
        withTableBorder=True,
        withColumnBorders=True,
    )
