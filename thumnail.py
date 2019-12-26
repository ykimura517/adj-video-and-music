import subprocess
import sys
import cv2


thumImg = sys.argv[1]
#youtubeMovie = sys.argv[2]
print("movie part 4 thumnail was creating..")
cmd = "ffmpeg -loop 1 -i "+thumImg+" -vcodec libx264 -pix_fmt yuv420p -t 2 -r 30 thumnail.mp4 -y"
subprocess.call(cmd.split())
print("done")
# cmd2 = 'ffmpeg -i '+youtubeMovie+' -i thumnail.mp4 -filter_complex concat=n=2:v=0:a=1 4niconico.mp4 -y'

# cmd2 = 'ffmpeg -safe 0 -f concat -i index.txt -c:v copy -c:a copy -c:s copy -map 0:v -map 0:a -map 0:s? 4niconico.mp4'
#
# subprocess.call(cmd2.split())
# print("niconico movie was created!")

# 複数動画を連結させる関数
def m_combine(movie_info, path_out, scale_factor):
    i = 0                                                       # 動画数カウント用指標iを用意
    # 動画数分ループを回す
    for j in movie_info:                                        # 動画情報（[path, T/F]）をjに格納
        path = j[0]                                             # 動画ファイルへのパス
        color_flag = j[1]                                       # カラーかどうかをフラグ
        # 動画読み込みの設定
        movie = cv2.VideoCapture(path)

        # 動画ファイル保存用の設定
        fps = int(movie.get(cv2.CAP_PROP_FPS))                  # 元動画のFPSを取得
        fps_new = int(fps * scale_factor)                       # 動画保存時のFPSはスケールファクターをかける
        w = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))            # 動画の横幅を取得
        h = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))           # 動画の縦幅を取得
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')     # 動画保存時のfourcc設定（mp4用）

        # 最初だけvideoを定義（連結させるため）
        if i == 0:
            video = cv2.VideoWriter(path_out, fourcc, fps_new, (w, h), color_flag)  # 動画の仕様
        else:
            pass
        i = i + 1                                               # iを増分（動画連結数カウント）

        # ファイルからフレームを1枚ずつ取得して動画処理後に保存する
        while True:
            ret, frame = movie.read()                           # フレームを取得
            video.write(frame)                                  # 動画を保存する
            # フレームが取得できない場合はループを抜ける
            if not ret:
                break
    # 動画数分のループが終了した最後に、撮影用オブジェクトとウィンドウの解放
    movie.release()
    return

# ここからメイン実行文
movie1 = ["glo3-content.mp4", True]     # 元動画のパス1, カラーはTrue
movie2 = ['ad-final.mp4', True]    # 元動画のパス2, 白黒はFalse
path_out = 'youtubeMovie.mp4'        # 保存する動画のパス
scale_factor = 1                  # FPSにかけるスケールファクター

movie_info = [movie1, movie2]     # 動画情報を配列にまとめる
print("concatenating ad-final with thumnail..")
# 複数動画を連結させる関数を実行
#m_combine(movie_info, path_out, scale_factor)
print("done!!")
