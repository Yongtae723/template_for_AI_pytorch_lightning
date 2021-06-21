import transformers
import torch.nn as nn


class BERTBaseClassifier(object):
    def __init__(self):
        super(BERTBaseClassifier(object)).__init__()
        self.bert = transformers.BertModel.from_pretrained(...) #FIXME
        self.bert_drop = nn.Dropout(0.3)
        self.out = nn.Linear(768, 1)

    def forward(self, ids, mask, token_type_ids):
        _, o2 = self.bert(ids, attention_mask=mask, token_type_ids=token_type_ids)
        bo = self.bert_drop(o2)
        output = self.out(bo)
        return output