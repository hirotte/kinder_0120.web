import streamlit as st
from PIL import Image
import random
import csv
import base64

st.set_page_config(
    page_title="Kinder (筋der)",
    page_icon="💪",
    layout="wide",

)



def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./img/kinnniku.png')

tab1, tab2, tab3, tab4 = st.tabs(["筋derとは", "マッチング", "プロフィール", "チャット"])

with tab1:
    st.title("筋derとは")
    st.header("Tinderのようなマッチングアプリを使う理由")
    st.markdown("#### 筋肉には、足の筋肉（Leg Muscles）、お尻の筋肉（Butt Muscles）、背中の筋肉（Back Muscle）、胸の筋肉（Chest Muscles）、など、数多くの部位があります。理想の筋肉を探している人も、似あう筋肉を探している人も、自分にぴったりの相手を見つけられるアプリを求めています。")
    st.markdown("#### 筋肉に何を求めているか、自分はどんな風になりたいのかハッキリしないこともありますが、筋derにはさまざまな筋肉との出会いを可能にするための数々の機能が備わっています。筋肉との出会いが、より簡単になりました。")
    st.markdown("#### 筋derが最高の無料アプリだと断言する前に、実際に筋derを使用して頂き、みなさん自身に判断してもらいたいと思っています。皆様の理想の筋肉を見つけられるように応援させていただきます。")



with tab2:
    # 初期の筋肉リスト
    # 50種類の筋肉を含むリスト
    muscle_list = [
    "胸", "背中", "腕", "脚", "肩",
    "腹直筋", "広背筋", "上腕二頭筋", "大腿四頭筋", "三角筋",
    "腹斜筋", "菱形筋", "上腕三頭筋", "ハムストリング", "腹横筋",
    "僧帽筋", "腹斜筋", "前腕屈筋", "腓腹筋", "広腰筋",
    "大円筋", "中部背筋", "腕橈骨伸筋", "ヒラメ筋", "内腹斜筋",
    "腹横筋", "脊柱起立筋", "短頭二頭筋", "大腿二頭筋", "三頭筋",
    "腹直筋", "大菱形筋", "上腕二頭筋", "大腓腹筋", "広腰筋",
    "僧帽筋", "腹斜筋", "前腕屈筋", "腓腹筋", "大腰筋",
    "大円筋", "中部背筋", "腕橈骨伸筋", "ヒラメ筋", "内腹斜筋",
    "腹横筋", "脊柱起立筋", "短頭二頭筋", "大腿二頭筋", "三頭筋"
]

 
    # グッドリストとバッドリストの初期化
    good_list = []
    # グッドリストの読み込み
    try:
        with open('good_list.csv', 'r') as file:
            reader = csv.reader(file)
            good_list = next(reader, [])  # 既存のデータがあれば読み込む
    except FileNotFoundError:
        pass
    bad_list = []
    # バッドリストの読み込み
    bad_list = []
    try:
        with open('bad_list.csv', 'r') as file:
            reader = csv.reader(file)
            bad_list = next(reader, [])  # 既存のデータがあれば読み込む
    except FileNotFoundError:
        pass
 
    if st.button("次の筋肉とマッチング"):
        # ランダムな筋肉を選択
        selected_muscle = random.choice(muscle_list)
 
        # 選択された筋肉を表示
        st.write(f"次は {selected_muscle} です！")
 
        # 丸かバツのボタン
        user_decision = st.radio("評価:", ("👍", "👎"))
        
 
        # ユーザーの判断に応じて処理
        if user_decision == "👍":
            good_list.append(selected_muscle)
            st.success(f"{selected_muscle} をグッドリストに追加しました！")

        # 選択された筋肉をリストから削除
            muscle_list.remove(selected_muscle)
 
        elif user_decision == "👎":
            bad_list.append(selected_muscle)
            st.warning(f"{selected_muscle} はバッドリストに追加しました！")
            st.write("バッドリスト", good_list)

        # データをCSVファイルに保存
        with open('good_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([good_list])
            
        with open('bad_list.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([bad_list])

def save_user_profile(profile):
    with open('user_profile.txt', 'w') as file:
        file.write(f"名前: {profile['名前']}\n")
        file.write(f"年齢: {profile['年齢']}\n")
        file.write(f"性別: {profile['性別']}\n")
        file.write(f"好きな部位: {profile['好きな部位']}\n")
        file.write(f"身長: {profile['身長']}\n")
        file.write(f"体重: {profile['体重']}\n")
        file.write(f"体脂肪率: {profile['体脂肪率']}\n")
        file.write(f"除脂肪体重: {profile['除脂肪体重']}\n")
        file.write(f"筋肉量: {profile['筋肉量']}\n")
        file.write(f"理想体重: {profile['理想体重']}\n")
        file.write(f"理想体脂肪率: {profile['理想体脂肪率']}\n")
        file.write(f"理想筋肉量: {profile['理想筋肉量']}\n")

# ユーザープロフィール情報を読み込むための関数
def load_user_profile():
    user_profile = {}
    try:
        with open('user_profile.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(': ', 1)
                if len(parts) == 2:
                    key, value = parts
                    user_profile[key] = value
    except FileNotFoundError:
        pass
    return user_profile
with tab3:
    st.header('プロフィール')

    # ユーザープロフィール情報を読み込む
    user_profile = load_user_profile()

    col1, col2, col3, col4 = st.columns((3, 2, 2, 5))
    with col1:
        user_profile['名前'] = st.text_input("名前", user_profile.get('名前', ''))
        
    with col2:
        user_profile['年齢'] = st.text_input("年齢", user_profile.get('年齢', ''))
        
    with col3:
        user_profile['性別'] = st.radio("性別", ("男", "女"), key="gender", index=0 if user_profile.get('性別') == '男' else 1)
        
    with col4:
        user_profile['好きな部位'] = st.text_input("好きな部位", user_profile.get('好きな部位', ''))
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        user_profile['身長'] = st.text_input("身長", user_profile.get('身長', ''))
        
    with col2:
        user_profile['体重'] = st.text_input("体重", user_profile.get('体重', ''))
        
    with col3:
        user_profile['体脂肪率'] = st.text_input("体脂肪率", user_profile.get('体脂肪率', ''))
        
    with col4:
        user_profile['除脂肪体重'] = st.text_input("除脂肪体重", user_profile.get('除脂肪体重', ''))

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        user_profile['筋肉量'] = st.text_input("筋肉量", user_profile.get('筋肉量', ''))
        
    with col2:
        user_profile['理想体重'] = st.text_input("理想体重", user_profile.get('理想体重', ''))
        
    with col3:
        user_profile['理想体脂肪率'] = st.text_input("理想体脂肪率", user_profile.get('理想体脂肪率', ''))
        
    with col4:
        user_profile['理想筋肉量'] = st.text_input("理想筋肉量", user_profile.get('理想筋肉量', ''))

    # ユーザープロフィール情報を保存
    save_user_profile(user_profile)


    st.markdown("#### これからもご利用ください♡")
with tab4:

    # 筋トレメニューリストの作成
    workout_menus = [
    "ベンチプレス",
    "デッドリフト",
    "スクワット",
    "プルアップ",
    "ショルダープレス",
    "クランチ",
    "レッグプレス",
    "バーベルカール",
    "ディップス",
    "ディクラインベンチプレス",
    "バーベルロウ",
    "ミリタリープレス",
    "レッグカール",
    "レッグエクステンション",
    "ラットプルダウン",
    "ハンマーカール",
    "フレンチプレス",
    "バイセップスカール",
    "デッドリフト",
    "ハックスクワット",
    "ラットプルダウン",
    "ベントオーバーロウ",
    "アーノルドプレス",
    "レッグカール",
    "トライセップスエクステンション",
    "アブドミナルクランチ",
    "カーフレイズ",
    "ウォークアウト"
     "ワイドグリッププルアップ",
    "ベントオーバーバーベルロウ",
    "インクラインベンチプレス",
    "ダンベルフライ",
    "バーベルシュラッグ",
    "ワンアームダンベルロウ",
    "フロントスクワット",
    "レッグプレスマシン",
    "ハンドスタンドプッシュアップ",
    "ウィンドシールドワイパー",
    "スタッガードスタンスデッドリフト",
    "ワンレッグカール",
    "プッシュプレス",
    "バーベルウェイトランジ",
    "アップライトロウ",
    "スラムボールトス",
    "ヒップスラスト",
    "ツイストクランチ",
    "バーベルクロール",
    "サイドプランク",
    "クロスハンマーカール",
    "ダンベルランジ",
    "プッシュアップ",
    "インクラインダンベルプレス",
    "ディクラインプレスマシン",
    "サイドレイズ",
    "キックバック",
    "シットアップ",
    "チンニング",
    "ウォーキングランジ",
    "ダンベルパルフェ",
    "フロントレイズ",
    "ハーフジャック",
    "スクワットジャンプ",
    "ディープランジ",
    "ダンベルスナッチ",
    "バーベルキューブロウ",
    "リバースフライ",
    "トライセプトライセップスエクステンション",
    "クロスクランチ",
    "ハンドリングリップデッドリフト",
    "ツイストダンベルクランチ",
    "ジャンプスクワット",
    "リバースクランチ",
    "トウヒールスタンディング",
    "アングルクランチ",
    "ベンチディップ",
    "ワンレッグバーベルスクワット",
    "ウォーキングプッシュアップ",
    "ダンベルカーフレイズ",
    "ワンレッグプレス",
    "ハンギングニーキック",
    "スレッドミルスプリント",
    "ディープスクワット",
    "ツイストハンマーカール",
    "ダンベルデッドリフト",
    "クロスプッシュアップ",
    "スタッガードスタンスプッシュプレス",
    "ハンギングトゥルースウィング",
    "バーベルサイドベンド",
    "ウィークリーフリッパーズ",
    "アームレスハンガーサイドプランク",
    "サイドハンギングアングルレッグプレス",
    "キャベツフロート",
    "クロスアンダーハンドキック",
    "エキスパンドレッグデッドリフト",
    "ツイストダンベルサイドクランチ",
    "クロスフロントトゥデッドリフト",
    "ディープキャベツクランチ",
    "キャベツクランチ",
    "ハンギングトゥデッドリフト",
    "アームレスサイドプランク",
    "クロスアンダーハンドハンギングニーキック",
    "アームレスハンギングキック",
    "アームレスクロスフロントトゥデッドリフト",
    "アームレススワンキック",
    "バーベルアップライトロウ",
    "アームレスサイドハンギングアングルレッグプレス",
    "アームレスサイドハンギングキック",
    "ツイストフロントスクワット",
    "クロスハンギングニーキック",
    "ツイストレッグカール",
    "クロスバーベルウェイトランジ",
    "クロスハンギングレッグプレス",
    ]
    # 各筋肉に対応するCSVファイルの初期化
    for muscle in good_list:
        try:
            with open(f'{muscle}_chat_data.csv', 'r') as file:
                pass
        except FileNotFoundError:
            with open(f'{muscle}_chat_data.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["ユーザー", "メッセージ"])

    # 選択された筋肉に対応するCSVファイルの読み込み
    selected_muscle = st.sidebar.selectbox("筋肉さんを選択", good_list)
    chat_data = []
    try:
        with open(f'{selected_muscle}_chat_data.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            chat_data = list(reader)
    except FileNotFoundError:
        pass

    # チャット画面
    st.header(f"{selected_muscle}さんとチャット")

    # チャットメッセージの入力
    user_message = st.text_input("メッセージを送る:")

    # 送信ボタン
    if st.button("送信"):
        st.success(f"メッセージを送信しました: {user_message}")

        # チャットデータに追加
        chat_data.append(["あなた", user_message])

        # 特定のキーワードに対するシステムの応答
        if "今日は何しようか" in user_message:
            workout_menu = f"{random.choice(workout_menus)} , はどう？"
            st.info(workout_menu)

            # システムからのメッセージを追加
            chat_data.append([{selected_muscle}, workout_menu])

        # データをCSVファイルに保存
        with open(f'{selected_muscle}_chat_data.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(chat_data)

        # チャットデータを表示
        st.header("チャット欄")
        for chat in chat_data:
            st.write(f"{chat[0]}: {chat[1]}")