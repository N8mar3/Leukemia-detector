import torch


class Predictor:
    def __init__(self,
                 loader,
                 model,
                 model_name,
                 device,
                 input_data_clean):
        self.loader = loader
        self.model = model
        self.model_name = model_name
        self.device = device
        self.input_data_clean = input_data_clean

    def forward(self):
        prediction = self.predictor()
        decoded_data = self.data_decoder(prediction)

        return decoded_data

    def predictor(self):
        self.model.load_state_dict(torch.load(self.model_name))
        self.model.eval()
        prediction = []
        with torch.no_grad():
            for x in self.loader:
                x = x.to(self.device, dtype=torch.float)
                x = torch.movedim(x, -1, 1)
                prediction.append(torch.sigmoid(self.model(x)))

        return torch.cat(prediction, 0)

    @staticmethod
    def data_decoder(prediction):
        data, data_i_row = torch.movedim(prediction, 1, 0), []
        data = torch.where(data[0] > 0.7, 1, 0) + \
               torch.where(data[1] > 0.3, 2, 0)
        data = torch.where(data == 3, 1, data)
        data_chunked = torch.stack(torch.chunk(data, 4), 0)
        for i in range(data_chunked.shape[0]):
            data_i_row.append(torch.cat((data_chunked[i][0],
                                         data_chunked[i][1],
                                         data_chunked[i][2],
                                         data_chunked[i][3]), 0))

        return torch.cat(data_i_row, 1)
