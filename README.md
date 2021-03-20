# Introduction

Dobot Magician是一個易於一般使用者操作的機械手臂產品，藉由USB來連線控制，並透過軟體"DobotStudio"來設定、執行工作及任務.

## How to control the device

1. 將Dobot Magician要用的產品配件組裝完成後，以USB線連接Dobot Magician至電腦上並開啟電源。
2. 安裝應用程式DobotStudio至電腦上。
3. 開啟應用程式DobotStudio後，選擇 Blockly 圖形化編程工具在畫面中找出符合需求的功能，並將這些功能拼湊成一系列的程序拼圖並設定座標及功能及時間參數。
4. 在裝置管理員中找出 "Silicon Labs CP210x USB to UART Bridge" 項目，並選擇正確的 "COM(port number)" 再點擊"連接"icon。
5. 點擊左上角"連接"按鈕，再點選"開始"按鈕。
6. 觀察機械手臂的動作是否符合預期。

## How to code for Dobot Magician

1. 於DobotStudio確認所有動作皆符合需求後，複製右下角"通用代碼"的所有內容。
2. 修改Dobot_Modify.py檔案內的"COM8"為裝置管理員中的USB COM port number，設定如下圖所示：

   ```Python
   #Connect Dobot
   state = dType.ConnectDobot(api, "COM8", 115200)[0]
   ```

3. 貼上通用代碼至Dobot_Modify.py檔案內的"通用代碼"區域內，如下圖所示：

   ```Python
   # 將DobotStudio的Blockly功能編成的"通用代碼"貼入通用代碼區內。
   # ========== 通用代碼區 Start ==========
   ...
   # ========== 通用代碼區 End ==========
   ```

4. 複製檔案DobotDll.dll及DobotDllType.py至Dobot_Modify.py檔案的相同目錄下，即可使用Dobot_Modify.py操作Dobot Magician。

5. 若機器手臂無法使用，請確認電源按鈕是否啟動，DobotStudio軟體是否已經關閉或斷開 COM port 連線。
