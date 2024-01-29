class Imogi_converter:
    def __init__(self):
        pass
    def converter(self, face):
        imo_dic={":)":"😀",
                 ":/":"🫤",
                 ":}$":"🤑"}
        word=face.split(" ")
        var=""
        for w in word:
            var+=imo_dic.get(w,w)
        print(var)



