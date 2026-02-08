指紋資料集簡介 (Sokoto Coverntry Fingerprint Dataset)

來自 600 個非洲人的 6,000 個指紋
經過三種 STRANGE toolbox 轉換 (obliteration, central rotation, z-cut) 得到 49,270(合成後)+6,000(原本的)=55,270張指紋照片
49,270 = 17,931(easy parameter settings) + 17,067(medium para. settings) + 14,272(hard para. settings)
每一張照片格式 : 1*96*103 (gray * width * height)
SOCOFing  │----- Real
 	   │-----Altered --- │---Altered-Easy
		                 │---Altered-Medium
		                 │---Altered-Hard 
e.g.
001_M_Left_little_finger_obl.bmp
001 : 代表第幾個人 (001-600)
M : 代表性別 (M-male, F-female)
Left : 左手或右手 (Left, Right)
little : 手指名稱 (little, ring, middle, index, thumb)
obl : 合成類別 (Obl-obliteration, CR-central rotation, Zcut)
bmp : 照片格式 (全部都是 .bmp)