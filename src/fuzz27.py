def BrokenMethod(strInput):
    if len(strInput) >= 1:
        return strInput[0] == 'F' and strInput[1] == 'U'

def FuzzerEntrypoint(Data):
    try:
        strData = Data.read().decode("utf-8")
        BrokenMethod(strData)
    except UnicodeDecodeError, e:
        return