import sys
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


# =========================
# Kaggle 下载工具
# =========================
def download_kaggle_dataset(dataset, target_dir="./data"):
    os.makedirs(target_dir, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    print(f"🔹 Downloading Kaggle dataset: {dataset}")
    api.dataset_download_files(
        dataset,
        path=target_dir,
        unzip=False,
        quiet=False,
    )

    zip_name = dataset.split("/")[-1] + ".zip"
    zip_path = os.path.join(target_dir, zip_name)

    if os.path.exists(zip_path):
        print("🔹 Extracting...")
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(target_dir)
        print("✅ Done")


# =========================
# 占位：非 Kaggle 数据集
# =========================
def download_bach_cello():
    import os
    import requests

    urls = [
        "http://www.jsbach.net/midi/cs1-1pre.mid",
        "http://www.jsbach.net/midi/cs1-2all.mid",
        "http://www.jsbach.net/midi/cs1-3cou.mid",
        "http://www.jsbach.net/midi/cs1-4sar.mid",
        "http://www.jsbach.net/midi/cs1-5men.mid",
        "http://www.jsbach.net/midi/cs1-6gig.mid",
        "http://www.jsbach.net/midi/cs2-1pre.mid",
        "http://www.jsbach.net/midi/cs2-2all.mid",
        "http://www.jsbach.net/midi/cs2-3cou.mid",
        "http://www.jsbach.net/midi/cs2-4sar.mid",
        "http://www.jsbach.net/midi/cs2-5men.mid",
        "http://www.jsbach.net/midi/cs2-6gig.mid",
        "http://www.jsbach.net/midi/cs3-1pre.mid",
        "http://www.jsbach.net/midi/cs3-2all.mid",
        "http://www.jsbach.net/midi/cs3-3cou.mid",
        "http://www.jsbach.net/midi/cs3-4sar.mid",
        "http://www.jsbach.net/midi/cs3-5bou.mid",
        "http://www.jsbach.net/midi/cs3-6gig.mid",
        "http://www.jsbach.net/midi/cs4-1pre.mid",
        "http://www.jsbach.net/midi/cs4-2all.mid",
        "http://www.jsbach.net/midi/cs4-3cou.mid",
        "http://www.jsbach.net/midi/cs4-4sar.mid",
        "http://www.jsbach.net/midi/cs4-5bou.mid",
        "http://www.jsbach.net/midi/cs4-6gig.mid",
        "http://www.jsbach.net/midi/cs5-1pre.mid",
        "http://www.jsbach.net/midi/cs5-2all.mid",
        "http://www.jsbach.net/midi/cs5-3cou.mid",
        "http://www.jsbach.net/midi/cs5-4sar.mid",
        "http://www.jsbach.net/midi/cs5-5gav.mid",
        "http://www.jsbach.net/midi/cs5-6gig.mid",
        "http://www.jsbach.net/midi/cs6-1pre.mid",
        "http://www.jsbach.net/midi/cs6-2all.mid",
        "http://www.jsbach.net/midi/cs6-3cou.mid",
        "http://www.jsbach.net/midi/cs6-4sar.mid",
        "http://www.jsbach.net/midi/cs6-5gav.mid",
        "http://www.jsbach.net/midi/cs6-6gig.mid",
    ]

    save_dir = "./data/bach-cello"
    os.makedirs(save_dir, exist_ok=True)

    for url in urls:
        fname = url.split("/")[-1]
        path = os.path.join(save_dir, fname)
        print(f"Downloading {fname}...")
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)

    print("🚀 All files downloaded!")


def download_bach_chorales():
    import os
    import urllib.request

    # 目标路径
    save_dir = "./data/bach-chorales"
    os.makedirs(save_dir, exist_ok=True)

    url = "https://github.com/czhuang/JSB-Chorales-dataset/raw/master/Jsb16thSeparated.npz"
    save_path = os.path.join(save_dir, "Jsb16thSeparated.npz")

    print("Downloading...")
    urllib.request.urlretrieve(url, save_path)
    print("🚀 Done!")



# =========================
# 主逻辑（等价 if / elif）
# =========================
def main():
    if len(sys.argv) < 2:
        print(
            "❌ Missing dataset name\n"
            "Choose from: faces, bricks, recipes, flowers, wines, cellosuites, chorales"
        )
        return

    dataset = sys.argv[1]

    if dataset == "faces":
        download_kaggle_dataset("jessicali9530/celeba-dataset")

    elif dataset == "bricks":
        download_kaggle_dataset("joosthazelzet/lego-brick-images")

    elif dataset == "recipes":
        download_kaggle_dataset("hugodarwood/epirecipes")

    elif dataset == "flowers":
        download_kaggle_dataset("nunenuh/pytorch-challange-flower-dataset")

    elif dataset == "wines":
        download_kaggle_dataset("zynicide/wine-reviews")

    elif dataset == "cellosuites":
        download_bach_cello()

    elif dataset == "chorales":
        download_bach_chorales()

    else:
        print(
            "❌ Invalid dataset name\n"
            "Choose from: faces, bricks, recipes, flowers, wines, cellosuites, chorales"
        )


if __name__ == "__main__":
    main()