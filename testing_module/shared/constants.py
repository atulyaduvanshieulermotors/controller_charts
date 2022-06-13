RANDOM_DIAGNOSIS_COMMAND = b"TESTING_COMMAND\t"

STARK_DIAGNOSIS_START_COMMAND = b"DIAG_STARK_START\t"

STARK_DIAGNOSIS_STOP_COMMAND = b"DIAG_STARK_STOP\t"

STARK_DIAGNOSIS_MODE_STRING = "DIAG_STARK_START"

BMS_DIAGNOSIS_START_COMMAND = b"DIAG_BMS_START\t"

BMS_DIAGNOSIS_STOP_COMMAND = b"DIAG_BMS_STOP\t"

BMS_DIAGNOSIS_MODE_STRING = "DIAG_BMS_START"

CONTROLLER_DIAGNOSIS_START_COMMAND = b"DIAG_CONTROLLER_START\t"

CONTROLLER_DIAGNOSIS_STOP_COMMAND = b"DIAG_CONTROLLER_STOP\t"

CONTROLLER_DIAGNOSIS_MODE_STRING = "DIAG_CONTROLLER_START"

DEFAULT_EXPECTED_OUTPUT = "43794"

SERIAL_BAUDRATE = 115200

CAN_BUSTYPE = "socketcan"

CAN_CHANNEL = "can0"

CAN_BITRATE = 250000

CAN_INPUT_ID = 0x7A1

CAN_POWER_UP_COMMAND = "sudo ip link set can0 up type can bitrate 250000"

SUCCESS = "Success"

FAILURE = "Error"

CAN_DATA_LOGGING_TIME = 15  # 15sec

CHECK_BUFFER_DATA_COUNTER = 3

SERIAL_DATA_LOG_FILENAME = "stark_serial_log.txt"

INPUT_MSG = [0xAB, 0x12, 00, 00, 00, 00, 00, 00]

DIAGNOSIS_COUNTER = 6

ERROR_COUNTER_LIMIT = 3

NO_SERIAL_DATA = "No Serial Data"

NO_SERIAL_DATA_COUNTER_LIMIT = 2

TIMEOUT_RETURN_VALUE = "TIMEOUT"

TIMEOUT_TIME = 150  # 150 sec

SERIAL_MSG = '81,99,0.00,0.00,-0.60,95.55,100.00,82.40,3,18.00,18.00,17.00,18.00,17.00,18.00,165.10,19.20,4115.60,4116.10,4116.20,4116.20,4116.00,4115.80,4115.60,4115.90,4115.40,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,4123.10,4123.10,4123.20,4123.00,4123.00,4123.20,4123.10,4123.20,0.00,4123.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1,25,25,0,0,306.50,2,0,0,0,306,0,0,0,0,19,19,217,7,82,82,0,2354663,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,100098,1,14,37,0,1,16.42,-273.15,-273.15,1,0,1,2,0,4125.20,0,0,2,5,50,0,0.00,83.10,0.00,84.00,0.00,0.00,0,4095,68.00,250.00,v3.0,v0.5.4,1,81'

BMS_IDS_LIST = ['110','111','112','113','114','115','116','117','118','11c','12a']

CONTROLLER_IDS_LIST = ['705','706','708','710','715','716','717','724','725','726','258','259','1806e5f4','7a0']

CONTROLLER_FAULT_STATUS_ROUNDABOUT = 0

CONTROLLER_FAULT_STATUS_MULTIPLIER = 1

UNIT_TEST_STRINGS_FOR_BMS_VALIDATION = [
    "DIAG_BMS_START,0,0,-4294967298,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,4294967298,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,61,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,85,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3098,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4202,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,202,0,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-2,0,0,0,0,0",
    "DIAG_BMS_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,202,0,0,0,0,0",
]

UNIT_TEST_STRINGS_FOR_CONTROLLER_VALIDATION = [
    "DIAG_CONTROLLER_START,-52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,-52,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,202,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,-62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-502,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,502,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,252,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,252,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,252,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
]

UNIT_TEST_STRINGS_FOR_BMS_TESTING = [
    "DIAG_BMS_START,0,0,-4294967296,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,DIAG_BMS_START,0,0,-4294967296,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "",
    "DIAG_BMS_START,0,0,-4294967296,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
]

UNIT_TEST_STRINGS_FOR_CONTROLLER_TESTING = [
    "DIAG_CONTROLLER_START,-52,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,202,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,-52,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,202,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,-62,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,62,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,-502,0,0,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,502,0,0,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,-102,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,102,0,0,0,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,-1,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,252,0,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,-1,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,252,0,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,-1,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,252,100,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,8,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,102,100,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,102,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,100,3,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
    "DIAG_CONTROLLER_START,0,0,0,0,0.00,0,0,0,0,0,0,0,0,0,0,0,0.00,0.00,0,0,0,0.00,0.00,0,0,0,0,0,0,0,0,0,100,100,102,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
]
