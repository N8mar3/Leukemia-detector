from _data_process import CellsDataBuilder
from _utilites import UtilityWorker
from _main_worker import Predictor
from _Unet_architecture import UNet


class Worker:
    def __init__(self, data_path, model_name, device, warning_m):
        self.data_path = data_path
        self.model_name = model_name
        self.device = device
        self.warning = warning_m

    def forward(self):
        data, loader = CellsDataBuilder(data_path=self.data_path).forward()

        model = UNet(in_channels=3,     out_channels=2,
                     n_blocks=4,        start_filters=18,
                     activation='relu', normalization='batch',
                     conv_mode='same',  dim=2).to(self.device)

        prediction = Predictor(loader=loader,
                               model=model,
                               model_name=self.model_name,
                               device=self.device,
                               input_data_clean=data).forward()

        UtilityWorker(input_data_clean=data,
                      prediction=prediction,
                      device=self.device,
                      warning_m=self.warning).forward()
