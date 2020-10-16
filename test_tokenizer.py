from tokenizer import Tokenizer

def test_split_empty_string_result_empty_array():
    #arrange
    stringToSplit = ""

    expResult = []
    result = None
    cut = Tokenizer()

    #act
    result = cut.parse_string(stringToSplit)

    #assert
    assert result == expResult

def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","

    expResult = []
    result = None
    cut = Tokenizer()

    #act
    result = cut.parse_string(stringToSplit)

    #assert
    assert result == expResult

def test_split_one_string_result_array_of_one():
    # arrange
    stringToSplit = "java"

    expResult = ["java"]
    result = None
    cut = Tokenizer()

    #act
    result = cut.parse_string(stringToSplit)

    #assert
    assert result == expResult

def test_split_two_strings_result_array_of_two():
    # arrange
    stringToSplit = "java, python"

    expResult = ["java", "python"]
    result = None
    cut = Tokenizer()

    #act
    result = cut.parse_string(stringToSplit)

    #assert
    assert result == expResult

def test_split_one_string_comma_result_array_of_one():
    # arrange
    stringToSplit = ",java"

    expResult = ["java"]
    result = None
    cut = Tokenizer()

    #act
    result = cut.parse_string(stringToSplit)

    #assert
    assert result == expResult