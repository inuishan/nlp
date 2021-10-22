# from transformers import AutoTokenizer, AutoModelForSequenceClassification
# from transformers import pipeline
#
# tokenizer = AutoTokenizer.from_pretrained("valhalla/distilbart-mnli-12-3")
# model = AutoModelForSequenceClassification.from_pretrained("valhalla/distilbart-mnli-12-3")
#
# classifier = pipeline("zero-shot-classification",
#                       model="valhalla/distilbart-mnli-12-3")
# candidate_labels = ['High Inflow of Letters', 'Person seen keeping activity watch', 'Person seen in non-business hours',
#                     'Unattended Vehicle in Parking', 'Package Without Name']
#
#
# def classify(text):
#     res = classifier(text, candidate_labels)
#     return res['labels']
#
#
# if __name__ == "__main__":
#     classify('Man who was armed with a knife at an hospital in Dallas, Texas, has been shot dead by police; no officers injured; special unit investigating the case')
