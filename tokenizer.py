class Tokenizer(object):
    def parse_string(self,tags):
        result = []

        if(len(tags) > 1 ):
            tags = tags.replace(" ","")
            result = tags.split(",")

        return result