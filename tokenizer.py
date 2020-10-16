class Tokenizer(object):
    def parse_string(self,tags):
        result = []

        if(len(tags) > 1 ):
            tags = tags.replace(" ","")
            tags = tags.split(",")
            result= []
            for element in tags:
                if element != "," and element != "":
                    result.append(element)

        return result