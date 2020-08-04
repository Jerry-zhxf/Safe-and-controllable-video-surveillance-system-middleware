# Safe-and-controllable-video-surveillance-system-middleware
设计摄像头与云存储之间的安全中间件，进行自主储存加密和直播流加密，保证视频音频不泄露。
1. 采用国密算法 SM2,SM3,SM4 和 ZUC 算法进行加解密
2. 中间件为树莓派（Raspberry Pi），加密过程均在上面完成；
3. 用户终端用 PyQt 与 DLL 实现；
4. 加入可信模块 TPM2.0 保证中间件的安全性；
