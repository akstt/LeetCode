class StorageSmallError(Exception):

    def __str__(self):
        return "存储空间分配太小"

