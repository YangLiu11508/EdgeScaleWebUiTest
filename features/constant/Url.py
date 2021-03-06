class Url:

    global BASE_URL
    global LOGIN
    global DEVICE
    global DEVICE_CREATE
    global APP_CREATE
    global APP
    global SOLUTION
    global SOLUTION_CREATE
    global REGISTER
    global MODEL
    global TASK
    global USER
    global VENDOR

    # 正式版
    BASE_URL = "https://console.edgescale.org"
    # 开发版
    # BASE_URL = "https://dashboard-dev.edgescale.org"
    LOGIN = "/login"
    DEVICE = "/device"
    DEVICE_CREATE = "/device/create"
    APP_CREATE = "/software/app/create"
    APP = "/software/app"
    SOLUTION = "/software/solution"
    SOLUTION_CREATE = "/software/solution/create"
    REGISTER = "/apply"
    MODEL = "/model"
    TASK = "/task"
    USER = "/manage/user"
    VENDOR = "/manage/vendor"
