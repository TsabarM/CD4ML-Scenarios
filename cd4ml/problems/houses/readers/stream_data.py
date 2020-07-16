from csv import DictReader
from cd4ml.filenames import file_names
from cd4ml.problems.houses.config.raw_schema import raw_schema


def stream_raw(pipeline_params):
    """
    :param pipeline_params: pipeline_params data structure
    :return: stream to raw rows of house sales data
    """
    assert pipeline_params['problem_name'] == 'houses'
    filename = file_names['raw_house_data']
    return (dict(row) for row in DictReader(open(filename, 'r')))


def stream_data(pipeline_params):
    """
    :param pipeline_params: pipeline_params data structure
    :return: stream to processed rows of house sales data
    """
    schema = raw_schema
    return (process_row(row, schema) for row in stream_raw(pipeline_params))


def float_or_zero(x):
    """
    :param x: any value
    :return: converted to float if possible, otherwise 0.0
    """
    try:
        return float(x)

    except ValueError:
        return 0.0


def process_row(row, schema):
    """
    Process a raw row of house data and give it the right schema
    :param row: raw row
    :param schema: raw_schema_dict
    :return: processed row
    """

    catergorical_fields = list(schema['categorical'])
    numeric_fields = schema['numerical']

    # Make sure there are no overlaps
    overlap = set(catergorical_fields).intersection(numeric_fields)
    assert len(overlap) == 0

    row_out = {k: row[k] for k in catergorical_fields}

    for field in numeric_fields:
        row_out[field] = float_or_zero(row[field])

    return row_out
