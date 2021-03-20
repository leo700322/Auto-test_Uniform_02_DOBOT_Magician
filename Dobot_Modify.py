import DobotDllType as dType

#Load Dll
api = dType.load()

#Connect Dobot (修改"COM8"為裝置管理員中的USB COM port number)
state = dType.ConnectDobot(api, "COM8", 115200)[0]

#Connect status
CON_STR = { 
    dType.DobotConnect.DobotConnect_NoError:  "DobotConnect_NoError",
    dType.DobotConnect.DobotConnect_NotFound: "DobotConnect_NotFound",
    dType.DobotConnect.DobotConnect_Occupied: "DobotConnect_Occupied"}
print("Connect status:",CON_STR[state])

# 將DobotStudio的Blockly功能編成的"通用代碼"貼入通用代碼區內。
# ========== 通用代碼區 Start ========== 
current_pose = dType.GetPose(api)
dType.SetPTPCmdEx(api, 2, 231.1,  23,  126, current_pose[3], 1)
for count in range(1):
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 272.7,  23.8,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.SetWAITCmdEx(api, 1, 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 272.7,  23.8,  50, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 191,  16.5,  98.3, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 145.3,  9.2,  (-23.3), current_pose[3], 1)
  dType.SetWAITCmdEx(api, 3, 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 191,  16.5,  98.3, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 272.7,  23.8,  50, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 272.7,  23.8,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.SetWAITCmdEx(api, 1, 1)
  dType.SetPTPCmdEx(api, 0, 273.4,  129.1,  20, 0, 1)
  dType.SetEndEffectorSuctionCupEx(api, 1, 1)
  dType.SetWAITCmdEx(api, 1, 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 273.4,  129.1,  50, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 191,  16.5,  98.3, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 145.3,  9.2,  (-23.3), current_pose[3], 1)
  dType.SetWAITCmdEx(api, 3, 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 191,  16.5,  98.3, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 273.4,  129.1,  50, current_pose[3], 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 273.4,  129.1,  20, current_pose[3], 1)
  dType.SetEndEffectorSuctionCupEx(api, 0, 1)
  dType.SetWAITCmdEx(api, 1, 1)
  current_pose = dType.GetPose(api)
  dType.SetPTPCmdEx(api, 2, 231.1,  23,  126, current_pose[3], 1)
# ========== 通用代碼區 End ========== 

#Disconnect Dobot
dType.DisconnectDobot(api)
print('Mission complate. Disconnect!')
