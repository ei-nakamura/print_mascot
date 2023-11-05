import tarminalcolor
import time
import printdataarray

# 出力データ設定
pd = printdataarray.PrintDataArray
# ミライトワ(モノクロ)
#data_array = pd.DATA_ARRAY_MIRAITOWA
# ソメイティ(フルカラー)
data_array = pd.DATA_ARRAY_SOMEITY

# メイン処理
tc = tarminalcolor.TerminalColor
for i, v in enumerate(data_array):
    print_str = ""
    for j, c in enumerate(v):
        if c == 0:
            # 白
            print_str += tc.WHITE
            print_str += "■"            
        elif c == 2:
            # 黒
            print_str += tc.BLACK
            print_str += "□"
        elif c == 5:
            # ピンク
            print_str += tc.MAGENTA
            print_str += "■" 
        elif c == 9:
            # 青
            print_str += tc.BLUE
            print_str += "■" 
        elif c == 14:
            # 赤
            print_str += tc.RED
            print_str += "■" 

    print_str += tc._END

    # そのままprintすると全体が一瞬で表示されてしまって面白くないため、1行ずつsleepしてゆっくり出力されるようにする
    time.sleep(0.18)
    print(print_str)