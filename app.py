from transformers import BartTokenizer, BartForConditionalGeneration

longTokenizer = BartTokenizer.from_pretrained('datien228/distilbart-cnn-12-6-ftn-multi_news')
longModel = BartForConditionalGeneration.from_pretrained('datien228/distilbart-cnn-12-6-ftn-multi_news')


def summarize(text, num_beams=5, length_penalty=2.0, max_length=50, min_length=15, no_repeat_ngram_size=3):
    
    text = text.replace('\n','')

    text_input_ids = longTokenizer.encode(text, return_tensors='pt', max_length=1024, truncation=True)
    summary_ids = longModel.generate(text_input_ids, num_beams=int(num_beams),
                                    length_penalty=float(length_penalty), 
                                    # max_length=int(max_length)+45,
                                    # min_length=int(min_length)+45, 
                                    no_repeat_ngram_size=int(no_repeat_ngram_size),
                                    top_k=50)

    long_summary_txt = longTokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True,
                                            clean_up_tokenization_spaces=False)

    return long_summary_txt