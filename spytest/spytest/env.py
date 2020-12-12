import os

defaults = {
    "SPYTEST_LOGS_TIME_FMT_ELAPSED": "0",
    "SPYTEST_LOGS_MODULE_ONLY_SUPPORT" : "0",
    "SPYTEST_NO_CONSOLE_LOG": "0",
    "SPYTEST_PROMPTS_FILENAME": None,
    "SPYTEST_TEXTFSM_INDEX_FILENAME": "index",
    "SPYTEST_UI_POSITIVE_CASES_ONLY": "0",
    "SPYTEST_REPEAT_MODULE_SUPPORT": "0",
    "SPYTEST_FILE_PREFIX": "results",
    "SPYTEST_RESULTS_PREFIX": None,
    "SPYTEST_RESULTS_PNG": "1",
    "SPYTEST_MODULE_CSV_FILENAME": "modules.csv",
    "SPYTEST_MODULE_INFO_CSV_FILENAME": "module_info.csv",
    "SPYTEST_FUNCTION_INFO_CSV_FILENAME": "function_info.csv",
    "SPYTEST_TCMAP_CSV_FILENAME": "tcmap.csv",
    "SPYTEST_TESTBED_IGNORE_CONSTRAINTS": "",
    "SPYTEST_FLEX_DUT": "1",
    "SPYTEST_FLEX_PORT": "0",
    "SPYTEST_MGMT_IFNAME": "eth0",
    "SPYTEST_TOPO_SEP": None,
    "SPYTEST_TESTBED_RANDOMIZE_DEVICES": "0",
    "SPYTEST_BUCKETS_DEADNODE_RECOVERY": "1",
    "SPYTEST_BATCH_DEFAULT_BUCKET": "1",
    "SPYTEST_TOPO_1": "D1T1:2",
    "SPYTEST_TOPO_2": "D1T1:4 D1D2:6 D2T1:2",
    "SPYTEST_TOPO_3": "D1 D2 D3",
    "SPYTEST_TOPO_4": "D1T1:2 D2T1:2 D3T1:2 D4T1:2 D1D2:4 D2D3:4 D3D4:4 D4D1:4",
    "SPYTEST_TOPO_5": "D1 D2 D3 D4 D5",
    "SPYTEST_TOPO_6": "D1D3:4 D1D4:4 D1D5:2 D1D6:4 D2D3:4 D2D4:4 D2D5:4 D2D6:4 D3T1:2 D4T1:2 D5T1:2 D6T1:2",
    "SPYTEST_TOPO_7": "D1 D2 D3 D4 D5 D6 D7",
    "SPYTEST_TOPO_8": "D1 D2 D3 D4 D5 D6 D7 D8",
    "SPYTEST_EMAIL_BODY_PREFIX": "",
    "SPYTEST_TECH_SUPPORT_ONERROR": "system,port_list,port_status",
    "SPYTEST_SAVE_CLI_TYPE": "1",
    "SPYTEST_SAVE_CLI_CMDS": "1",
    "SPYTEST_SHUTDOWN_FREE_PORTS": "0",
    "SPYTEST_ABORT_ON_VERSION_MISMATCH": "2",
    "SPYTEST_TOPOLOGY_STATUS_MAX_WAIT": "60",
    "SPYTEST_TOPOLOGY_STATUS_ONFAIL_ABORT": "module",
    "SPYTEST_LIVE_RESULTS": "1",
    "SPYTEST_DEBUG_FIND_PROMPT": "0",
    "SPYTEST_KDUMP_ENABLE": "1",
    "SPYTEST_LOG_DUTID_FMT": "LABEL",
    "SPYTEST_SWAP_PASSWORD": "0",
    "SPYTEST_SYSRQ_ENABLE": "0",
    "SPYTEST_SET_STATIC_IP": "1",
    "SPYTEST_ONREBOOT_RENEW_MGMT_IP": "0",
    "SPYTEST_DATE_SYNC": "1",
    "SPYTEST_BOOT_FROM_GRUB": "0",
    "SPYTEST_RECOVERY_MECHANISMS": "1",
    "SPYTEST_RESET_CONSOLES": "0",
    "SPYTEST_ONCONSOLE_HANG": "recover",
    "SPYTEST_CONNECT_DEVICES_RETRY": "10",
    "SPYTEST_OPENCONFIG_API": "GNMI",
    "SPYTEST_IFA_ENABLE": "0",
    "SPYTEST_ROUTING_CONFIG_MODE": None,
    "SPYTEST_CLEAR_MGMT_INTERFACE": "0",
    "SPYTEST_CLEAR_DEVICE_METADATA_HOSTNAME": "0",
    "SPYTEST_NTP_CONFIG_INIT": "0",
    "SPYTEST_GENERATE_CERTIFICATE": "0",
    "SPYTEST_HOOKS_PORT_ADMIN_STATE_UITYPE": "click",
    "SPYTEST_HOOKS_PORT_STATUS_UITYPE": "click",
    "SPYTEST_HOOKS_VERSION_UITYPE": "click",
    "SPYTEST_HOOKS_BREAKOUT_UITYPE": "klish",
    "SPYTEST_HOOKS_SPEED_UITYPE": "",
    "SPYTEST_IFNAME_MAP_UITYPE": "click",
    "SPYTEST_API_INSTRUMENT_SUPPORT": "0",
    "SPYTEST_REDIS_DB_CLI_TYPE": "1",
    "SPYTEST_TOPOLOGY_SHOW_ALIAS": "0",
    "SPYTEST_TOPOLOGY_STATUS_FAST": "1",
    "SPYTEST_BGP_API_UITYPE": "",
    "SPYTEST_BGP_CFG_API_UITYPE": "",
    "SPYTEST_BGP_SHOW_API_UITYPE": "",
}

dev_defaults = {
    "SPYTEST_TOPOLOGY_SIMULATE_FAIL": "0",
    "SPYTEST_REST_TEST_URL": None,
    "SPYTEST_BATCH_BACKUP_NODES": None,
    "SPYTEST_BATCH_RERUN_NODES": None,
    "SPYTEST_BATCH_MODULE_TOPO_PREF": None,
    "SPYTEST_BATCH_MATCHING_BUCKET_ORDER": "larger,largest",
    "SPYTEST_BATCH_RERUN": None,
    "SPYTEST_TESTBED_FILE": "testbed.yaml",
    "SPYTEST_FILE_MODE": "0",
    "SPYTEST_SCHEDULING": None,
    "SPYTEST_BATCH_RUN": None,
    "PYTEST_XDIST_WORKER": None,
    "SPYTEST_BUCKETS_DEADNODE_SIMULATE": "0",
    "SPYTEST_USER_ROOT": None,
    "SPYTEST_CMDLINE_ARGS": "",
    "SPYTEST_SUITE_ARGS": "",
    "SPYTEST_TEXTFSM_DUMP_INDENT_JSON": None,
    "SPYTEST_TESTBED_EXCLUDE_DEVICES": None,
    "SPYTEST_TESTBED_INCLUDE_DEVICES": None,
    "SPYTEST_LOGS_PATH": None,
    "SPYTEST_LOGS_LEVEL": "info",
    "SPYTEST_APPLY_BASE_CONFIG_AFTER_MODULE": "0",
    "SPYTEST_COMMUNITY_BUILD_FEATURES": "0",
    "SPYTEST_ONFAIL_TGEN_STATS": "0",
    "SPYTEST_SYSTEM_READY_AFTER_PORT_SETTINGS": "0",
    "SPYTEST_APPLY_CONFIG_BEFORE_BREAKOUT": None,
    "SPYTEST_TCLIST_FILE": None,
    "SPYTEST_MODULE_REPORT_SORTER": "CDT",
    "SPYTEST_ASAN_OPTIONS": "",
    "SPYTEST_RECOVER_INITIAL_SYSTEM_NOT_READY": "0",
    "SPYTEST_LIVE_TRACE_OUTPUT": "0",
    "SPYTEST_USE_SAMPLE_DATA": None,
    "SPYTEST_DRYRUN_CMD_DELAY": "0",
    "SPYTEST_FASTER_CLI_OVERRIDE": None,
    "SPYTEST_FASTER_CLI_LAST_PROMPT": "1",
    "SPYTEST_NEW_FIND_PROMPT": "0",
    "SPYTEST_DETECT_CONCURRENT_ACCESS": "0",
    "SPYTEST_SPLIT_COMMAND_LIST": "0",
    "SPYTEST_CHECK_SKIP_ERROR": "0",
    "SPYTEST_HELPER_CONFIG_DB_RELOAD": "yes",
    "SPYTEST_CHECK_HELPER_SIGNATURE": "0",
    "SPYTEST_CLICK_HELPER_ARGS": "",
}

def _get_logs_path():
    user_root = os.getenv("SPYTEST_USER_ROOT", os.getcwd())
    logs_path = os.getenv("SPYTEST_LOGS_PATH", user_root)
    if not os.path.isabs(logs_path):
        logs_path = os.path.join(user_root, logs_path)
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)
    return logs_path

def get(name, default=None):
    cur_def = defaults.get(name, default)
    if cur_def is None and default is not None:
        cur_def = default
    retval = os.getenv(name, cur_def)
    return retval

def get_default_all():
    return sorted(defaults.items())
