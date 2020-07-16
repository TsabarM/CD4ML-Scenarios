from cd4ml.problems.houses.config.problem_params import problem_params
from cd4ml.problems.houses.config.ml_model_params import model_parameters
from cd4ml.problems.houses.readers.stream_data import stream_data
from cd4ml.problems.houses.readers.zip_lookup import get_zip_lookup
from cd4ml.splitter import splitter
from cd4ml.problem import Problem


def get_params():
    return {'problem_name': 'houses',
            'problem_params': problem_params,
            'model_params': model_parameters}


class HousesProblem(Problem):
    def __init__(self):
        super(HousesProblem, self).__init__()
        self.pipeline_params = get_params()
        self.problem_name = self.pipeline_params['problem_name']

        self._stream_data = stream_data
        self.training_filter, self.validation_filter = splitter(self.pipeline_params)
        if self.pipeline_params['problem_params']['feature_set_name'] == 'feature_set_1':
            from cd4ml.problems.houses.features.feature_set_1 import FeatureSet1 as FeatureSet
            self.feature_set = FeatureSet({})
        else:
            self.feature_set = None

    def prepare_feature_data(self):
        zip_lookup = get_zip_lookup()
        if self.feature_set is not None:
            self.feature_set.zip_lookup = zip_lookup
