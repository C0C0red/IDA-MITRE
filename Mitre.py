


from marshal import loads

bytecode = loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00M\x00\x00\x00@\x00\x00\x00s\xe4\x00\x00\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02d\x00d\x01l\x03Z\x03d\x00d\x01l\x04Z\x04d\x02d\x02d\x02d\x02d\x02d\x03d\x03d\x04d\x03d\x05d\x05d\x05d\x05d\x05d\x05d\x05d\x05d\x05d\x05d\x06d\x06d\x06d\x07d\x08d\x08d\td\td\nd\nd\x0bd\x0cd\x05d\x05d\rd\rd\rd\rd\x0ed\x0fd\x10d\x10d\x10d\x10d\x10d\x10d\x10d\x10d\x10d\x11d\x11d\x11d\x11d\x11d\x11d\x12d\x13d\x13d\td\td\td\td\td\td\x08d\x08d\x08d\x14d\x15d\x16d\x0bd\x0bd\x17d\x18d\x18d\x08d\x19d\x1a\x9cLZ\x05G\x00d\x1bd\x1c\x84\x00d\x1ce\x00j\x06\x83\x03Z\x07d\x1dd\x1e\x84\x00Z\x08d\x01S\x00)\x1f\xe9\x00\x00\x00\x00N)\x02Z\x05T1059z\x16Command-Line Interface)\x02Z\x05T1106z\x15Execution through API)\x02Z\x05T1215z\x1dKernel Modules and Extensions)\x02\xda\x05T1055z\x11Process Injection)\x02Z\x05T1003z Credential Dumping: LSASS Memory)\x02z\tT1003.002z(Credential Dumping: Credentials in Files)\x02Z\x05T1134z\x19Access Token Manipulation)\x02Z\x05T1112z\x0fModify Registry)\x02Z\x05T1050z\x0bNew Service)\x02Z\x05T1179Z\x07Hooking)\x02z\tT1546.002z\x19Event Triggered Execution)\x02Z\x05T1622z\x10Debugger Evasion)\x02Z\x05T1018z"Discovery: Remote System Discovery)\x02z\tT1070.004\xfa\x19Indicator Removal on Host)\x02z\tT1071.001z)Application Layer Protocol: Web Protocols)\x02Z\x05T1083z\x1cFile and Directory Discovery)\x02Z\x05T1031z\x0eScheduled Task)\x02z\tT1021.002z\x18SMB/Windows Admin Shares)\x02r\x02\x00\x00\x00z\x13Process Termination)\x02Z\x05T1070r\x03\x00\x00\x00)\x02Z\x05T1071z+Application Layer Protocol: Custom Protocol)\x02z\tT1056.001z\x19Input Capture: Keylogging)\x02Z\x05T1056z\rInput Capture)\x02Z\x05T1069z\x1bPermission Groups Discovery)LZ\x0eCreateProcessAZ\x0eCreateProcessWZ\rShellExecuteAZ\rShellExecuteWZ\x07WinExecZ\x0cLoadLibraryAZ\x0cLoadLibraryWZ\x0cNtLoadDriverZ\x13RtlCreateUserThreadZ\x0eVirtualAllocExZ\x12WriteProcessMemoryZ\x12CreateRemoteThreadZ\x10NtCreateThreadExZ\x12NtMapViewOfSectionZ\x12ZwMapViewOfSectionZ\x0cQueueUserAPCZ\x10NtQueueApcThreadZ\x10GetThreadContextZ\x10SetThreadContextZ\x16LsaRetrievePrivateDataZ\x19LsaEnumerateLogonSessionsZ\x19LsaQueryInformationPolicyZ\x12CryptUnprotectDataZ\x10OpenProcessTokenZ\x10DuplicateTokenExZ\x0eRegSetValueExAZ\x0eRegSetValueExWZ\x0eCreateServiceAZ\x0eCreateServiceWZ\x10SetWindowsHookExZ\x0eRegisterHotKeyZ\x14CreateProcessAsUserAZ\x14CreateProcessAsUserWZ\x1aCheckRemoteDebuggerPresentZ\x11IsDebuggerPresentZ\x16NtSetInformationThreadZ\x16ZwSetInformationThreadZ\x19NtQueryInformationProcessZ\x07NtCloseZ\rInternetOpenAZ\rInternetOpenWZ\x10InternetConnectAZ\x10InternetConnectWZ\x10HttpOpenRequestAZ\x10HttpOpenRequestWZ\nWSASocketAZ\nWSASocketW\xda\x07connectZ\x0eFindFirstFileAZ\x0eFindFirstFileWZ\rFindNextFileAZ\rFindNextFileWZ\x12GetFileAttributesAZ\x12GetFileAttributesWZ\x11NetScheduleJobAddZ\x13WNetAddConnection2AZ\x13WNetAddConnection2WZ\rRegOpenKeyExAZ\rRegOpenKeyExWZ\rRegDeleteKeyAZ\rRegDeleteKeyWZ\x10RegQueryValueExAZ\x10RegQueryValueExWZ\x15AdjustTokenPrivilegesZ\x15LookupPrivilegeValueAZ\x15LookupPrivilegeValueWZ\x10TerminateProcessZ\x14NtUnmapViewOfSectionZ\rSuspendThreadZ\x11SetWindowsHookExAZ\x11SetWindowsHookExWZ\x10GetAsyncKeyStateZ\x13GetForegroundWindowZ\x0cGetCursorPosZ\x12RtlAdjustPrivilegeZ\x10NtRaiseHardErrorc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00sB\x00\x00\x00e\x00Z\x01d\x00Z\x02e\x03j\x04Z\x05d\x01Z\x06d\x02Z\x07d\x03Z\x08d\x04Z\td\x05d\x06\x84\x00Z\nd\x07d\x08\x84\x00Z\x0bd\td\n\x84\x00Z\x0cd\x0bd\x0c\x84\x00Z\rd\rS\x00)\x0e\xda\x10MitreAttckPluginz\x1bMITRE ATT&CK Plugin with UI\xda\x00z\x0cMITRE ATT&CKz\x0cCtrl-Shift-Mc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00C\x00\x00\x00s\x0e\x00\x00\x00t\x00d\x01\x83\x01\x01\x00t\x01j\x02S\x00)\x02Nz$[*] MITRE ATT&CK Plugin initialized.)\x03\xda\x05print\xda\x06idaapiZ\tPLUGIN_OK\xa9\x01\xda\x04self\xa9\x00r\x0b\x00\x00\x00\xfa\x08<string>\xda\x04initz\x00\x00\x00s\x04\x00\x00\x00\x00\x01\x08\x01z\x15MitreAttckPlugin.initc\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00C\x00\x00\x00s\x0c\x00\x00\x00|\x00\xa0\x00\xa1\x00\x01\x00d\x00S\x00\xa9\x01N)\x01\xda\x0bshow_dialog)\x02r\n\x00\x00\x00\xda\x03argr\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\x03run~\x00\x00\x00s\x02\x00\x00\x00\x00\x01z\x14MitreAttckPlugin.runc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00C\x00\x00\x00s\x0c\x00\x00\x00t\x00d\x01\x83\x01\x01\x00d\x00S\x00)\x02Nz#[*] MITRE ATT&CK Plugin terminated.)\x01r\x07\x00\x00\x00r\t\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\x04term\x81\x00\x00\x00s\x02\x00\x00\x00\x00\x01z\x15MitreAttckPlugin.termc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00C\x00\x00\x00s4\x00\x00\x00G\x00d\x01d\x02\x84\x00d\x02t\x00j\x01\x83\x03}\x01|\x01\x83\x00}\x02|\x02\xa0\x02\xa1\x00\x01\x00|\x02\xa0\x03\xa1\x00\x01\x00|\x02\xa0\x04\xa1\x00\x01\x00d\x00S\x00)\x03Nc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00sJ\x00\x00\x00e\x00Z\x01d\x00Z\x02\x87\x00f\x01d\x01d\x02\x84\x08Z\x03d\x03d\x04\x84\x00Z\x04d\x0ed\x06d\x07\x84\x01Z\x05d\x0fd\x08d\t\x84\x01Z\x06d\x10d\nd\x0b\x84\x01Z\x07d\x0cd\r\x84\x00Z\x08\x87\x00\x04\x00Z\tS\x00)\x11z3MitreAttckPlugin.show_dialog.<locals>.MitreScanFormc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\t\x00\x00\x00\x13\x00\x00\x00sJ\x00\x00\x00g\x00|\x00_\x00t\x01\x83\x00\xa0\x02d\x01t\x03j\x04\xa0\x05|\x00j\x06\xa1\x01t\x03j\x04\xa0\x05|\x00j\x07\xa1\x01t\x03j\x04\xa0\x05|\x00j\x08\xa1\x01t\x03j\x04\xa0\t|\x00j\n\xa1\x01d\x02\x9c\x04\xa1\x02\x01\x00d\x00S\x00)\x03Nz\xc1MITRE ATT&CK\n                   BY Muteb\n\n                    {FormChangeCb}\n                    <Start Scan:{iStartScan}><Results:{iShowResults}><LinkedIn:{iVisitProfile}>\n                    )\x04Z\niStartScanZ\x0ciShowResultsZ\riVisitProfile\xda\x0cFormChangeCb)\x0b\xda\x07results\xda\x05super\xda\x08__init__\xda\x0bida_kernwin\xda\x04FormZ\x0bButtonInput\xda\ron_start_scan\xda\x0fon_show_results\xda\x10on_visit_profiler\x13\x00\x00\x00\xda\x0cOnFormChanger\t\x00\x00\x00\xa9\x01\xda\t__class__r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x16\x00\x00\x00\x86\x00\x00\x00s\x12\x00\x00\x00\x00\x01\x06\x01\x06\x01\x02\x07\x0c\x01\x0c\x01\x0c\x01\x0c\xfc\x04\xf9z<MitreAttckPlugin.show_dialog.<locals>.MitreScanForm.__init__c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00S\x00\x00\x00s\x04\x00\x00\x00d\x01S\x00)\x02N\xe9\x01\x00\x00\x00r\x0b\x00\x00\x00)\x02r\n\x00\x00\x00Z\x03fidr\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x1c\x00\x00\x00\x97\x00\x00\x00s\x02\x00\x00\x00\x00\x01z@MitreAttckPlugin.show_dialog.<locals>.MitreScanForm.OnFormChanger\x01\x00\x00\x00c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00S\x00\x00\x00sV\x00\x00\x00t\x00d\x01\x83\x01\x01\x00|\x00\xa0\x01\xa1\x00|\x00_\x02|\x00j\x02s$t\x03\xa0\x04d\x02\xa1\x01\x01\x00n\x18t\x03\xa0\x05d\x03t\x06|\x00j\x02\x83\x01\x9b\x00d\x04\x9d\x03\xa1\x01\x01\x00t\x00d\x05t\x06|\x00j\x02\x83\x01\x9b\x00d\x06\x9d\x03\x83\x01\x01\x00d\x00S\x00)\x07Nz0[*] Starting scan for MITRE ATT&CK techniques...z0No MITRE ATT&CK techniques found in this binary.z\x16Scan completed. Found z\x19 MITRE ATT&CK techniques.z\x1a[+] Scan completed. Found z\x0c techniques.)\x07r\x07\x00\x00\x00\xda\x19scan_for_mitre_techniquesr\x14\x00\x00\x00r\x17\x00\x00\x00\xda\x07warning\xda\x04info\xda\x03len\xa9\x02r\n\x00\x00\x00\xda\x04coder\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x19\x00\x00\x00\x9a\x00\x00\x00s\x0c\x00\x00\x00\x00\x01\x08\x01\n\x01\x06\x01\x0c\x02\x18\x01zAMitreAttckPlugin.show_dialog.<locals>.MitreScanForm.on_start_scanc\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00s^\x00\x00\x00|\x00j\x00s\x12t\x01\xa0\x02d\x01\xa1\x01\x01\x00nHt\x03d\x02t\x04|\x00j\x00\x83\x01\x9b\x00d\x03\x9d\x03\x83\x01\x01\x00G\x00d\x04d\x05\x84\x00d\x05t\x01j\x05\x83\x03}\x02d\x06d\x07\x84\x00|\x00j\x00D\x00\x83\x01}\x03|\x02|\x03\x83\x01}\x04|\x04\xa0\x06\xa1\x00\x01\x00d\x00S\x00)\x08Nz\x1aPlease run the scan first.z\x0f[+] Displaying z\x18 results in the chooser.c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s,\x00\x00\x00e\x00Z\x01d\x00Z\x02d\x01d\x02\x84\x00Z\x03d\x03d\x04\x84\x00Z\x04d\x05d\x06\x84\x00Z\x05d\x07d\x08\x84\x00Z\x06d\tS\x00)\nz[MitreAttckPlugin.show_dialog.<locals>.MitreScanForm.on_show_results.<locals>.ResultsChooserc\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\t\x00\x00\x00S\x00\x00\x00sD\x00\x00\x00t\x00j\x01\xa0\x02|\x00d\x01d\x02t\x00j\x01j\x03d\x03B\x00g\x02d\x04t\x00j\x01j\x04d\x05B\x00g\x02d\x06t\x00j\x01j\x04d\x07B\x00g\x02g\x03\xa1\x03\x01\x00|\x01|\x00_\x05d\x00S\x00)\x08Nz\x14MITRE ATT&CK Resultsu\x0b\x00\x00\x00Address \xe2\x86\x93\xe9\n\x00\x00\x00u\x07\x00\x00\x00API \xe2\x86\x93\xe9\x14\x00\x00\x00u\x10\x00\x00\x00MITRE ATT&CK \xe2\x86\x93\xe9(\x00\x00\x00)\x06r\x17\x00\x00\x00\xda\x06Chooser\x16\x00\x00\x00Z\tCHCOL_HEXZ\x0bCHCOL_PLAIN\xda\x05items)\x02r\n\x00\x00\x00r*\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x16\x00\x00\x00\xa9\x00\x00\x00s\x12\x00\x00\x00\x00\x01\x06\x01\x02\x01\x02\x01\x0e\x01\x0e\x01\x0e\xfe\x02\xfd\x04\x07zdMitreAttckPlugin.show_dialog.<locals>.MitreScanForm.on_show_results.<locals>.ResultsChooser.__init__c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00S\x00\x00\x00s\n\x00\x00\x00|\x00j\x00|\x01\x19\x00S\x00r\x0e\x00\x00\x00)\x01r*\x00\x00\x00)\x02r\n\x00\x00\x00\xda\x01nr\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\tOnGetLine\xb3\x00\x00\x00s\x02\x00\x00\x00\x00\x01zeMitreAttckPlugin.show_dialog.<locals>.MitreScanForm.on_show_results.<locals>.ResultsChooser.OnGetLinec\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00S\x00\x00\x00s\n\x00\x00\x00t\x00|\x00j\x01\x83\x01S\x00r\x0e\x00\x00\x00)\x02r#\x00\x00\x00r*\x00\x00\x00r\t\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\tOnGetSize\xb6\x00\x00\x00s\x02\x00\x00\x00\x00\x01zeMitreAttckPlugin.show_dialog.<locals>.MitreScanForm.on_show_results.<locals>.ResultsChooser.OnGetSizec\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00s"\x00\x00\x00t\x00|\x00j\x01|\x01\x19\x00d\x01\x19\x00d\x02\x83\x02}\x02t\x02\xa0\x03|\x02\xa1\x01\x01\x00d\x00S\x00)\x03Nr\x01\x00\x00\x00\xe9\x10\x00\x00\x00)\x04\xda\x03intr*\x00\x00\x00r\x17\x00\x00\x00Z\x06jumpto)\x03r\n\x00\x00\x00r+\x00\x00\x00\xda\x02ear\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\x0cOnSelectLine\xb9\x00\x00\x00s\x04\x00\x00\x00\x00\x02\x14\x01zhMitreAttckPlugin.show_dialog.<locals>.MitreScanForm.on_show_results.<locals>.ResultsChooser.OnSelectLineN)\x07\xda\x08__name__\xda\n__module__\xda\x0c__qualname__r\x16\x00\x00\x00r,\x00\x00\x00r-\x00\x00\x00r1\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\x0eResultsChooser\xa8\x00\x00\x00s\x08\x00\x00\x00\x08\x01\x08\n\x08\x03\x08\x03r5\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00S\x00\x00\x00s \x00\x00\x00g\x00|\x00]\x18\\\x03}\x01}\x02}\x03t\x00|\x01\x83\x01|\x02|\x03g\x03\x91\x02q\x04S\x00r\x0b\x00\x00\x00)\x01\xda\x03hex)\x04\xda\x02.0\xda\x04addr\xda\tfunc_nameZ\x0fmitre_techniquer\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\n<listcomp>\xbf\x00\x00\x00\xf3\x00\x00\x00\x00zWMitreAttckPlugin.show_dialog.<locals>.MitreScanForm.on_show_results.<locals>.<listcomp>)\x07r\x14\x00\x00\x00r\x17\x00\x00\x00r!\x00\x00\x00r\x07\x00\x00\x00r#\x00\x00\x00r)\x00\x00\x00Z\x04Show)\x05r\n\x00\x00\x00r%\x00\x00\x00r5\x00\x00\x00Z\x0cresults_listZ\x07chooserr\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x1a\x00\x00\x00\xa3\x00\x00\x00s\x0e\x00\x00\x00\x00\x01\x06\x01\x0c\x02\x16\x01\x12\x17\x10\x01\x08\x01zCMitreAttckPlugin.show_dialog.<locals>.MitreScanForm.on_show_resultsc\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00S\x00\x00\x00s\x0e\x00\x00\x00t\x00\xa0\x01d\x01\xa1\x01\x01\x00d\x00S\x00)\x02NzQhttps://sa.linkedin.com/in/muteb-bayomi-90ba96241?trk=public_post_feed-actor-name)\x02\xda\nwebbrowser\xda\x04openr$\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x1b\x00\x00\x00\xc3\x00\x00\x00s\x02\x00\x00\x00\x00\x02zDMitreAttckPlugin.show_dialog.<locals>.MitreScanForm.on_visit_profilec\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\t\x00\x00\x00\x13\x00\x00\x00sB\x01\x00\x00g\x00\x89\x00t\x00\xa0\x01\xa1\x00D\x00]\xe0}\x01t\x02\xa0\x03|\x01\xa1\x01}\x02t\x04d\x01|\x02\x9b\x00\x9d\x02\x83\x01\x01\x00t\x00\xa0\x05|\x01t\x02\xa0\x06|\x01t\x02j\x07\xa1\x02\xa1\x02D\x00]\xac}\x03t\x02\xa0\x08t\x02\xa0\t|\x03\xa1\x01\xa1\x01r>t\x02\xa0\n|\x03\xa1\x01}\x04t\x02\xa0\x0b|\x03d\x02\xa1\x02}\x05t\x04d\x03t\x0c|\x03\x83\x01\x9b\x00d\x04|\x04\x9b\x00d\x05|\x05\x9b\x00\x9d\x06\x83\x01\x01\x00|\x05t\rv\x00r>t\r|\x05\x19\x00\\\x02}\x06}\x07|\x07\x9b\x00d\x06|\x06\x9b\x00d\x07\x9d\x04}\x08t\x04d\x08t\x0c|\x03\x83\x01\x9b\x00d\x04|\x08\x9b\x00\x9d\x04\x83\x01\x01\x00t\x02\xa0\x0e|\x03|\x08d\x02\xa1\x03\x01\x00\x88\x00\xa0\x0f|\x03|\x02|\x06\x9b\x00d\x04|\x07\x9b\x00\x9d\x03f\x03\xa1\x01\x01\x00q>q\x0ct\x04d\t\x83\x01\x01\x00t\x10t\x11\xa0\x12\xa1\x00\x83\x01D\x00](}\tt\x11\xa0\x13|\t\xa1\x01}\n\x87\x00f\x01d\nd\x0b\x84\x08}\x0bt\x11\xa0\x14|\t|\x0b\xa1\x02\x01\x00\x90\x01q\x02t\x04d\x0ct\x15\x88\x00\x83\x01\x9b\x00\x9d\x02\x83\x01\x01\x00\x88\x00S\x00)\rNz\x17[*] Scanning function: r\x01\x00\x00\x00z\x0fInstruction at \xfa\x02: \xfa\x01 \xfa\x02 (\xfa\x01)z\x1d[+] Found MITRE technique at z [*] Checking import functions...c\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x07\x00\x00\x00\x13\x00\x00\x00sL\x00\x00\x00|\x01rH|\x01t\x00v\x00rHt\x00|\x01\x19\x00\\\x02}\x03}\x04t\x01d\x01|\x01\x9b\x00d\x02|\x04\x9b\x00d\x03\x9d\x05\x83\x01\x01\x00\x88\x00\xa0\x02|\x00|\x01|\x03\x9b\x00d\x04|\x04\x9b\x00\x9d\x03f\x03\xa1\x01\x01\x00d\x05S\x00)\x06Nz&[+] Found MITRE technique in imports: r@\x00\x00\x00rA\x00\x00\x00r>\x00\x00\x00T)\x03\xda\x14mitre_attack_mappingr\x07\x00\x00\x00\xda\x06append)\x05r0\x00\x00\x00\xda\x04nameZ\x07ordinal\xda\tattack_id\xda\x0battack_desc\xa9\x01r\x14\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\x06imp_cb\xe1\x00\x00\x00s\n\x00\x00\x00\x00\x01\x0c\x01\x0c\x01\x16\x01\x1a\x01z]MitreAttckPlugin.show_dialog.<locals>.MitreScanForm.scan_for_mitre_techniques.<locals>.imp_cbz/[+] Finished scanning. Total techniques found: )\x16\xda\x08idautilsZ\tFunctions\xda\x03idcZ\rget_func_namer\x07\x00\x00\x00Z\x05HeadsZ\rget_func_attrZ\x0cFUNCATTR_ENDZ\x07is_codeZ\x0eget_full_flagsZ\x0fprint_insn_mnemZ\rprint_operandr6\x00\x00\x00rB\x00\x00\x00Z\x07set_cmtrC\x00\x00\x00\xda\x05ranger\x08\x00\x00\x00Z\x15get_import_module_qtyZ\x16get_import_module_nameZ\x11enum_import_namesr#\x00\x00\x00)\x0cr\n\x00\x00\x00Z\x0bfunction_eaZ\rfunction_name\xda\x04headZ\x08mnemonic\xda\x07operandrE\x00\x00\x00rF\x00\x00\x00\xda\x07comment\xda\x01i\xda\x0bimport_namerH\x00\x00\x00r\x0b\x00\x00\x00rG\x00\x00\x00r\x0c\x00\x00\x00r \x00\x00\x00\xc7\x00\x00\x00s,\x00\x00\x00\x00\x01\x04\x02\x0c\x01\n\x01\x0e\x02\x1a\x01\x10\x01\n\x01\x0c\x03\x1e\x02\x08\x01\x0c\x01\x10\x01\x18\x01\x0e\x01\x1e\x03\x08\x01\x10\x01\n\x01\x0c\x06\x10\x02\x12\x01zMMitreAttckPlugin.show_dialog.<locals>.MitreScanForm.scan_for_mitre_techniques)\x01r\x01\x00\x00\x00)\x01r\x01\x00\x00\x00)\x01r\x01\x00\x00\x00)\nr2\x00\x00\x00r3\x00\x00\x00r4\x00\x00\x00r\x16\x00\x00\x00r\x1c\x00\x00\x00r\x19\x00\x00\x00r\x1a\x00\x00\x00r\x1b\x00\x00\x00r \x00\x00\x00\xda\r__classcell__r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x1d\x00\x00\x00r\x0c\x00\x00\x00\xda\rMitreScanForm\x85\x00\x00\x00s\x0c\x00\x00\x00\x08\x01\x0c\x11\x08\x03\n\t\n \n\x04rR\x00\x00\x00)\x05r\x17\x00\x00\x00r\x18\x00\x00\x00Z\x07CompileZ\x07ExecuteZ\x04Free)\x03r\n\x00\x00\x00rR\x00\x00\x00\xda\x04formr\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x0f\x00\x00\x00\x84\x00\x00\x00s\n\x00\x00\x00\x00\x01\x12g\x06\x01\x08\x01\x08\x01z\x1cMitreAttckPlugin.show_dialogN)\x0er2\x00\x00\x00r3\x00\x00\x00r4\x00\x00\x00r\x08\x00\x00\x00Z\nPLUGIN_UNL\xda\x05flagsrN\x00\x00\x00\xda\x04helpZ\x0bwanted_nameZ\rwanted_hotkeyr\r\x00\x00\x00r\x11\x00\x00\x00r\x12\x00\x00\x00r\x0f\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\x05\x00\x00\x00s\x00\x00\x00s\x12\x00\x00\x00\x08\x01\x06\x01\x04\x01\x04\x01\x04\x01\x04\x02\x08\x04\x08\x03\x08\x03r\x05\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00C\x00\x00\x00s\x06\x00\x00\x00t\x00\x83\x00S\x00r\x0e\x00\x00\x00)\x01r\x05\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\x0cPLUGIN_ENTRY\xf1\x00\x00\x00s\x02\x00\x00\x00\x00\x01rV\x00\x00\x00)\tr\x08\x00\x00\x00rI\x00\x00\x00rJ\x00\x00\x00r\x17\x00\x00\x00r<\x00\x00\x00rB\x00\x00\x00Z\x08plugin_tr\x05\x00\x00\x00rV\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xda\x08<module>\x01\x00\x00\x00s\xa6\x00\x00\x00\x08\x01\x08\x01\x08\x01\x08\x01\x08\x05\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x03\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x03\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x03\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x03\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x03\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x03\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x03\x02\x01\x02\x01\x02\x03\x02\x01\x02\x01\x02\x01\x02\x01\x02\x01\x02\x03\x02\x01\x02\x01\x02\x03\x02\x03\x02\x01\x02\x03\x02\x01\x02\x01\x02\x01\x02\x01\x02\x03\x02\x01\x02\x99\x06k\x12~')

exec(bytecode)

