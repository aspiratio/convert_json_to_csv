import csv
import json
import shutil

file = input("Input a file name")

# JSONファイルを読み込んで辞書型に変換
with open(file, "r") as f:
    json_dict = json.load(f)

# CSVファイルに書き込み
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(
        f,  # 読み込み対象のファイル
        fieldnames=json_dict[0].keys(),  # ヘッダー
        doublequote=True,  # 文字列内にquotechar（")が含まれるとき、同じquotechar（")でエスケープするか
        quoting=csv.QUOTE_ALL,  # 全てのフィールドをquotecharで囲む
    )
    writer.writeheader()  # ヘッダーに fieldnames に指定したkeyのリストを出力
    writer.writerows(json_dict)  # 辞書を渡してvalueを書き込む
