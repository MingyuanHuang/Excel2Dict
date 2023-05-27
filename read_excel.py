import pandas as pd

class ReadExcel:
    _excel_path = ""
    dict_data = {}
    keys = []

    def __init__(self, file_path):
        # 初始化时，就读取并创建好各个成员
        self._excel_path = file_path
        self.dict_data  = self.read_excel_to_dict(file_path)
        self.keys = list(self.dict_data.keys())
    

    def __repr__(self) -> str:
        # 获取dict内容
        dict_str = ""
        for key, value in self.dict_data.items():
            dict_str += f"\n    {key}: {value}"
        # 打印
        return f"{self.__class__.__name__}{{\n  READ_PATH: {repr(self._excel_path)},\n  KEYS: {repr(self.keys)},\n  READ_DICT: {{{dict_str}\n  }}\n}}"


    def read_excel_to_dict(self, file_path = _excel_path):
        # 读取Excel表格数据
        df = pd.read_excel(file_path)
        
        # 将列名和值存储到字典中
        data_dict = {}
        for column in df.columns:
            data_dict[column] = df[column].values.tolist()
        
        return data_dict

# # 使用方法
# if __name__ == "__main__":
#     # 指定Excel文件路径
#     test_edict = ReadExcel("./test.xlsx")
#     print(test_edict)
#     print(test_edict.dict_data)
