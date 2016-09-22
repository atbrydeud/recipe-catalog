This file and the associated jars after the pcc-mock bundle of the bgpcep project is built successfully.

See more at :: https://wiki.opendaylight.org/view/BGP_LS_PCEP:Testing_components#PCEP
             https://github.com/opendaylight/bgpcep/tree/stable/beryllium/pcep/pcc-mock

Input arguments for "pcc-mock" ::

   --local-address <Address:Port> (optional, default 127.0.0.1) – first PCC IP address. If more PCCs are required, the IP address will be incremented. Port number can be optionally specified.

   --remote-address <Address1:Port1,Address2:Port2,Address3:Port3,...> (optional, default 127.0.0.1:4189) - the list of Ip address for the PCE servers. Port number can be optionally specified, otherwise default port number 4189 is used.

   --pcc <N> (optional, default 1) – number of Mock PCC instances

   --lsp <N> (optional, default 1) – number of tunnels (LSPs) reported per PCC, might be zero.

   --pcerr (optional flag) – if the flag is present, response with PCErr, otherwise PCUpd

   --log-level <LEVEL> (optional, default INFO) - set logging level for pcc-mock

   -d, --deadtimer <0..255> (optional, default 120) - DeadTimer value in seconds

   -ka, --keepalive <0.255> (optional, deafult 30) - KeepAlive timer value in seconds

   --password <password> (optional) - if password is present, it is used in TCP MD5 signature, otherwise plain TCP is used.

   --reconnect <seconds> (optional) - if the argument is present, the value in seconds, is used as a delay before each new reconnect (initial connect or connection re-establishment) attempt. The number of reconnect attempts is unlimited. If the argument is omitted, pcc-mock is not trying to reconnect.

   --redelegation-timeout <seconds> (optional, default 0) - The timeout starts when LSP delegation is returned or PCE fails, stops when LSP is re-delegated to PCE. When timeout expires, LSP delegation is revoked and held by PCC.

   --state-timeout <seconds> (optional, default -1 (disabled)) - The timeout starts when LSP delegation is returned or PCE fails, stops when LSP is re-delegated to PCE. When timeout expires, PCE-initiated LSP is removed.

   --state-sync-avoidance <disconnect_after_x_seconds> <reconnect_after_x_seconds> <dbVersion> uses synchronization avoidance procedure.

         disconnect_after_x_seconds: seconds that will pass until disconnections is forced. If set to smaller number than 1, disconnection wont be performed. 

         reconnect_after_x_seconds: seconds that will pass between disconnection and new connection attempt. Only happens if disconnection has been performed.

         dbVersion: dbVersion used in new Open and must be always equal or bigger than lsp. If equal than lsp skip synchronization will be performed, 
           if not full synchronization will be performed taking in account new starting dbVersion desired.

   --incremental-sync-procedure <disconnect_after_x_seconds> <reconnect_after_x_seconds> <dbVersion> uses incremental synchronization procedure.

         dbVersion: dbVersion used in new Open and must be always bigger than lsp. Incremental synchronization will be performed taking in account new starting dbVersion desired.

   --triggered-initial-sync uses trigger synchronization procedure. Can be combined combined with state-sync-avoidance/incremental-sync-procedure.

   --triggered-re-sync uses trigger re-synchronization procedure.