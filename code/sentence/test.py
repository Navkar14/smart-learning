# from pprint import pprint
# #
# print en.is_number(12)
# print en.is_number("twelve")
# #
# print en.verb.past_participle("consist")
#
# farm = ["goose", "goose", "chicken", "chicken", "chicken","duck","duck","duck"]
# print en.list.conjunction(farm)
#
# print en.list.conjunction((1,2,3,4,5), generalize=True)
# print en.list.conjunction(en, generalize=True)
#
# pprint( en.sentence.chunk("Navkar performed well.") )
# pprint( en.sentence.chunk("A white shirt always looks sharp.") )
# #
# import markovify
# with open("/Users/navkar14/Desktop/Smart Learning/test.rtf") as f:
#     text = f.read()
#
# # Build the model.
# text_model = markovify.NewlineText(text)
#
# # Print five randomly-generated sentences
# for i in range(5):
#     print(text_model.make_sentence())
#
# # Print three randomly-generated sentences of no more than 280 characters
# for i in range(3):
#     print(text_model.make_short_sentence(280))