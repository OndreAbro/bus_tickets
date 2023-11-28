class TransportZone:
    def __init__(self, zone_id, remark):
        self.__id = zone_id
        self.__remark = remark

    def get_id(self):
        return self.__id

    def get_remark(self):
        return self.__remark

    def set_remark(self, remark):
        self.__remark = remark
