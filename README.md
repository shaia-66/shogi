できること  
> 将棋DB2から棋譜を探し、棋譜を取得するよ。  

使い方  
> a. https://shogidb2.com/latest の検索窓から取得したい戦型を入力。  
      ---> 戦型リストを作成し、そこに全ての戦型を格納させ、順次取得させる。  
> b. 全ての戦型を検索し、結果をファイルに格納させる。  
> c. 開いたURLで「棋戦」「棋戦詳細」「先手」「後手」「戦型」情報を取得する。  
> d. 次に、「進む矢印キー」で「投了」を取得するまでクリックをし続ける。  
> e. 投了を取得したら、初手から、終局までの棋譜をファイルにまとめる。(拡張子はまだ不明)  
      ---> 同じファイルに、「棋戦」「棋戦詳細」「先手」「後手」「戦型」情報を書き込む。  
> f. 1ファイル＝1局にし、ファイル名を"日付_AAAA/BB/CC_戦型_角換わり_先手_藤井猛_後手_渡辺明"  
> g. 戦型ごとにフォルダの作成。ファイル名の戦型を取得し、フォルダにMoveさせる。  
> h. 全ての処理が終了したら、ファイルを保存し、Slackに投げる。  
      ---> もしくは、処理終了の合図を投げて、ファイル確認は自宅PCで行う。  

環境  
> python3, heroku, selenium,