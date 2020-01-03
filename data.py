def getFns(folder_path):
    file_names = []
    onlyfiles = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for i in onlyfiles:
        file_names.append(i)
    return file_names, folder_path

def importText(file_name, encoding="utf8"):
    array = []
    with open(file_name, "r", encoding=encoding) as infile:
        for line in infile:
            array.append(line.strip())
    return array

def writeText(name, array, encoding="utf8"):
    file = open(name, "w", encoding=encoding)
    for i in range(len(array)):
        file.write(str(array[i]) + "\n")
    file.close()
