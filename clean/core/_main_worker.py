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

    def predictor(self,
                  switch: bool = True):
        self.model.load_state_dict(torch.load(self.model_name))
        self.model.eval()
        with torch.no_grad():
            for x in self.loader:
                x = x.to(self.device, dtype=torch.float)
                x = torch.movedim(x, -1, 1)
                prediction = torch.sigmoid(self.model(x))
                if switch:
                    m_tensor, switch = prediction, False
                else:
                    m_tensor = torch.cat((m_tensor, prediction), 0)

        return m_tensor

    @staticmethod
    def data_decoder(prediction):
        data, data_i_row = torch.movedim(prediction, 1, 0), []
        data = torch.where(data[0] > 0.7, 1, 0) + \
               torch.where(data[1] > 0.3, 2, 0)
        data = torch.where(data == 3, 1, data)
        data_chunked = torch.stack(torch.chunk(data, 4), 0)
        data_chunked_t = data_chunked
        for i in range(data_chunked.shape[0]):
            data_i_row.append(torch.cat((data_chunked_t[i][0],
                                         data_chunked_t[i][1],
                                         data_chunked_t[i][2],
                                         data_chunked_t[i][3]), 0))

        return torch.cat(data_i_row, 1)
