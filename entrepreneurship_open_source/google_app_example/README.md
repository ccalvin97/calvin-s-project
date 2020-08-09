## Cola detector - CNN image classification

### 如何部署 web app:

Step0: 參考 [fastai官網步驟](https://course.fast.ai/deployment_google_app_engine.html) 直到 git clone 跳到 Step1

Step1: ``$ git clone https://github.com/benwufc/google-app-engine.git`` to your google cloud shell

Step2: 如何客製化成為你的辨識器

* 修改 ``app/server.py`` 中三個變數: **export_file_url**, **export_file_name**, **classes** 
* **export_file_url:** 上傳你訓練好的"export.pkl" 到 google drive 或是 dropbox，將檔案設定成公開連結，接著將連結轉成下載連結
  * Google Drive: https://www.wonderplugin.com/online-tools/google-drive-direct-link-generator
  * Dropbox: https://syncwithtech.blogspot.com/p/direct-download-link-generator.html

Step3: 調整 web app 的 GUI：

* 修改 ``app/view/index.html`` ：
  * 標題：``<div class='title'>Cola Detector</div>``
  *  插入圖片 (可有可無)： ``<img src="link.jpg" width="150" height="100">``
  * 按鈕上的文字： ``<button class='choose-file-button' type='button' onclick='showPicker()'>Select Coke or Pepsi Image</button>``
  * 修改好你的GUI 可以到 https://www.ifreesite.com/runcode.htm 測試網頁的樣式。

Step4: ``$ gcloud app deploy app.yaml`` ，等待十分鐘左右就可以成功完成部署，之後就可以到 http://YOUR_PROJECT_ID.appspot.com 試試你的 web app!

* ``app.yaml`` 細節可以參考[google官方連結]( https://cloud.google.com/appengine/docs/flexible/custom-runtimes/configuring-your-app-with-app-yaml?authuser=2)，我在這邊只改了必要參數讓部署可以成功，不會出現 timeout error

### error 解決辦法

*_pickle.UnpicklingError: invalid load key, ‘<’.* ：代表你在 ``app/server.py`` 中變數**export_file_url** 提供的不是正確連結，可以使用 ``$ wget 下載連結`` 試試看，是否能成功下載檔案 "export.pkl"







### Reference

* 參考架構: https://github.com/jinudaniel/cars-classifier-web-app
* Debug 參考論壇: https://forums.fast.ai/t/solved-error-when-trying-to-deploy-model-on-google-app-engine-and-locally/39937/3