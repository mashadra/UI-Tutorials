import view.SaveInputView as v
import model.SaveInputModel as m

class SaveInputController:

    def __init__(self) -> None:       
        self.model = m.SaveInputModel(self)
        self.view = v.SaveInputView(self)