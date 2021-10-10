from django.core.files.storage import Storage
from django.conf import settings

class FastDFSStorage(Storage):
    """自定义文件存储类"""

    # def __init__(self, option=None):
    #     """文件存储类的初始化"""
    #     if not option:
    #         option = settings.CUSTOM_STORAGE_OPTIONS
    #         pass

    def _open(self, name, mode='rb'):
        """打开文件时会被调用的：文档告诉我必须重写"""
        # 因为当前不是去打开某个文件，所以这个方法目前无用，但是又必须重写，所以pass
        pass

    def _save(self, name, content):
        """保存文件时会被调用的：文档告诉我必须重写"""
        # 因为当前不是去保存某个文件，所以这个方法目前无用，但是又必须重写，所以pass
        pass

    def url(self, name):
        """返回文件的全路径，文件的全路径（http://192.168.103.158:8888/group1/M00/00/00/wKhnnlxw_gmAcoWmAAEXU5wmjPs35.jpeg）"""
        return "http://192.168.159.2:8888/" + name