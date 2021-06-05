import torch
from vedo import Picture, show
from _canny_edge_maker import canny


class UtilityWorker:
    def __init__(self,
                 input_data_clean,
                 prediction,
                 device,
                 warning_m):
        self.prediction = prediction
        self.device = device
        self.input_data_clean = input_data_clean
        self.red = torch.tensor([255, 0, 0]).cpu()
        self.green = torch.tensor([0, 255, 0]).cpu()
        self.checker = torch.tensor([1, 1, 1]).cpu()
        self.threshold = 0.038
        self.warning = warning_m

    def forward(self):
        resume = self.cell_amount_finder()
        prediction_1, prediction_2 = self.prediction_splitter()
        canny_1 = self.canny_edge_maker(prediction_1)
        canny_2 = self.canny_edge_maker(prediction_2)
        final_data = self.canny_edge_applier(canny_1, canny_2)
        self.show_save(self.input_data_clean, resume, self.prediction, final_data)

    def cell_amount_finder(self):
        amount_finder = self.prediction.unique(return_counts=True)[1]
        good_c, bad_c = amount_finder[2], amount_finder[1]

        return bad_c / good_c

    def prediction_splitter(self):
        prediction_1 = torch.where(self.prediction == 1, 1, 0)
        prediction_2 = torch.where(self.prediction == 2, 1, 0)

        return prediction_1, prediction_2

    def canny_edge_maker(self, some_data):
        data = torch.unsqueeze(some_data, 0)
        data = data.expand(3, 1920, 2560).to(torch.float).cpu()
        image = canny(data)
        image = torch.squeeze(image, 0)
        image = torch.movedim(image, 0, -1) / torch.max(image).item()
        image = torch.where(image > self.threshold, 1, 0)

        return image.expand(1920, 2560, 3)

    def canny_edge_applier(self, canny_1, canny_2):
        data = self.input_data_clean.to(torch.int64)
        canny_applier = torch.where(canny_1 == self.checker,
                                    self.red, data)

        return torch.where(canny_2 == self.checker,
                           self.green, canny_applier)

    def show_save(self, victim, resume,
                  prediction_filled,
                  prediction_combined):
        data_clean = victim.to(torch.uint8).cpu().detach().numpy()
        data_mask = torch.unsqueeze(prediction_filled, -1)\
                         .expand(1920, 2560, 3)\
                         .to(device='cpu', dtype=torch.int64)
        data_mask = torch.where(data_mask == self.checker, self.red,
                                data_mask*self.green).detach().numpy()
        diagnosis = 'You are healthy\n' if resume < self.warning else 'Warning\n'
        combi = prediction_combined.to(torch.uint8).detach().numpy()
        p1 = Picture(data_clean)
        p2 = Picture(data_mask).z(1200)
        p3 = Picture(combi).z(2400)
        show((p1, 'Input sample'),
             (p2, '\nPrediction masks'),
             (p3, '\n\nPrediction edge&mask\n\nDiagnose\n'+diagnosis+str(round(resume.item(), 3))),
             __doc__, axes=7, viewup="y", bg='black').close()
