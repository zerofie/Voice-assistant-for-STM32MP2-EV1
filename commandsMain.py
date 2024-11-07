#commands.py
common_intents = {
    "start": "launch",
    "launch": "launch",
    "initialize": "launch",
    "begin": "launch",
    "open": "launch",
    "kill": "kill",
    "stop": "kill",
    "end": "kill",
    "close": "kill",
    "suspend": "kill",
    "exit": "kill"

}
commands = {
    "terminal": {
        "command": "terminal",
        "aliases": ["shell", "bash", "genome terminal"],
        "intents": common_intents,
        "full_commands": {
            "launch": {
                "command": "launch terminal",
                "action": "weston-terminal"
            },
            "kill": {
                "command": "kill terminal",
                "action": "weston-terminal"
            }
        }
    },
     "3d cube":{
        "command":"3d cube",
        "aliases":["3D-Cube", "3dcube","cube","3d","gpu","three D","three-d","3d cube"],
        "intents":common_intents,
        "full_commands":{
            "launch":{
                "command":"launch 3d-cube",
                "action":"/usr/local/demo/application/3d-cube/bin/launch_cube_3D.sh >& /dev/null"
            },
            "kill":{
                "command":"kill 3d-cube",
                "action":"weston-st-egl-cube-tex"
            }
        }
    },
    "camera":{
        "command":"camera",
        "aliases":["camera","cam","ai camera","lens"],
        "intents":common_intents,
        "full_commands":{
            "launch":{
                "command":"launch camera",
                "action":"/usr/local/demo/application/camera/bin/launch_camera.sh >& /dev/null"
            },
            "kill":{
                "command":"kill camera",
                "action":"touch-event-gtk-player"
            }
        }
    },
    "pose estimation":{
        "command":"pose estimation",
        "aliases":["pose camera","post","post detection","pose ai","pose detection","pose detect","pose detect ai ","pose","estimation"],
        "intents":common_intents,
        "full_commands":{
            "launch":{
                "command":"launch pose estimation",
                "action":"/usr/local/x-linux-ai/pose-estimation/launch_python_pose_estimation.sh >& /dev/null"
            },
            "kill":{
                "command":"kill pose estimation",
                "action":"stai_mpu_pose_estimation.py"
            }
        }
    },
    "reboot":{
        "command":"reboot",
        "aliases":["restart","reopen"],
        "intents":"launch",
        "full_commands":{
            "launch":{
                "command":"launch reboot",
                "action":"reboot"
            },
            "kill":{
                "command":"",
                "action":"reboot"
            }
        }
    }
}