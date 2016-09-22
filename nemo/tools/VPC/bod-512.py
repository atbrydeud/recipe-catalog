#!/usr/bin/python
#Filename:servicechain.py
import requests,json
import argparse, sys
from requests.auth import HTTPBasicAuth

USERNAME='admin'
PASSWORD='admin'

TRANSACTION_BEGIN="http://%s:8181/restconf/operations/nemo-intent:begin-transaction"
TRANSACTION_END="http://%s:8181/restconf/operations/nemo-intent:end-transaction"
REGISTER_USER="http://%s:8181/restconf/operations/nemo-intent:register-user"
STRUCTURE_UPDATE_USERS="http://%s:8181/restconf/operations/nemo-intent:structure-style-nemo-update"

def register_user(contHost):
    data={
            "input":{
                    "user-id":"14ce424a-3e50-4a2a-ad5c-b29845158c8b",
                    "user-name":"user2",
                    "user-password":"abc",
                    "user-role":"tenant"
                    }
        }
    post(REGISTER_USER % contHost, data)

def transaction_begin(contHost):
    data={
            "input":{
                    "user-id":"14ce424a-3e50-4a2a-ad5c-b29845158c8b"                    
                    }
        }
    post(TRANSACTION_BEGIN % contHost, data)

def transaction_end(contHost):
    data={
            "input":{
                    "user-id":"14ce424a-3e50-4a2a-ad5c-b29845158c8b"                
                    }
        }
    post(TRANSACTION_END % contHost, data)

def add_server1_host(contHost):
    data={
            "input":{                
                  "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
                  "objects":{
                        "node":[
                                {
                                    "node-name": "server1",
                                    "node-type": "host",
                                    "node-id":"7b796915-adf4-4356-b5ca-de005ac410c1"
                                }
                            ]
                        }
                    }
        }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_server2_host(contHost):
    data={
            "input":{
                  "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
                  "objects":{
                        "node":[
                                {
                                    "node-name": "server2",
                                    "node-type": "host",
                                    "node-id":"22282cca-9a13-4d0c-a67e-a933ebb0b0ae"
                                }
                            ]
                        }
                    }
        }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_vm1_host(contHost):
    data={
            "input":{
                  "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
                  "objects":{
                        "node":[
                                {
                                    "node-name": "vm1",
                                    "node-type": "host",
                                    "node-id":"1eaf9a67-a171-42a8-9282-71cf702f61dd"
                                }
                            ]
                        }
                    }
        }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_vm2_host(contHost):
    data={
            "input":{
                  "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
                  "objects":{
                        "node":[
                                {
                                    "node-name": "vm2",
                                    "node-type": "host",
                                    "node-id":"6c787caa-156a-49ed-8546-547bdccf283c"
                                }
                            ]
                        }
                    }
        }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_enterpise_node(contHost):
    data={
          "input":{
              "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
              "objects":{
              "node":[
                      {
                            "node-name": "enterprise",
                            "node-type": "ext-group",
                            "property": [
                                          {
                                            "property-name": "location",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "openflow:4:2"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "ac-info-network",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "layer3"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "ac-info-protocol",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "static"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "ip-prefix",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "192.168.13.0/24"
                                                            }
                                                        ]
                                                    }
                                          }
                                        ],
                            "node-id": "94a6fb90-b425-4ffd-9515-c0684aa4c37f"
                          }
                    ]
              }
          }
        }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_internet_node(contHost):
    data={
          "input":{
              "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
              "objects":{
              "node":[
                      {
                            "node-name": "internet",
                            "node-type": "ext-group",
                            "property": [
                                          {
                                            "property-name": "location",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "openflow:3:4"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "ac-info-network",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "layer3"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "ac-info-protocol",
                                            "property-values": {
                                                        "string-value": [
                                                            {
                                                                "order": "0",
                                                                "value": "static"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "ip-prefix",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              #wait for external network ip
                                                              "value": "172.168.1.0/24"
                                                            }
                                                        ]
                                                    }
                                          }
                                        ],
                            "node-id": "d463232f-363f-491c-a6f5-097ed0a794d3"
                          }
                    ]
              }
          }
        }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_dmz_node(contHost):
    data={
          "input":{
              "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
              "objects":{
              "node":[
                      {
                            "node-name": "dmz",
                            "node-type": "l2-group",
                            "sub-node": [
                                          {
                                            "node-id":"7b796915-adf4-4356-b5ca-de005ac410c1",
                                            "order":"0"
                                          }
                                ],
                            "property": [
                                          {
                                            "property-name": "location",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "openflow:3"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "ip-prefix",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "192.168.11.0/24"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "gateway-ip",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "192.168.11.1"
                                                            }
                                                        ]
                                                    }
                                          }
                                        ],
                            "node-id": "b46cfa7f-93a3-43f4-ac20-09307c75feca"
                          }
                    ]
              }
          }
        }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_interior_node(contHost):
    data={
          "input":{
              "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
              "objects":{
              "node":[
                      {
                            "node-name": "interior",
                            "node-type": "l2-group",
                            "sub-node": [
                                          {
                                            "node-id":"22282cca-9a13-4d0c-a67e-a933ebb0b0ae",
                                            "order":"0"
                                          },
                                          {
                                            "node-id":"1eaf9a67-a171-42a8-9282-71cf702f61dd",
                                            "order":"0"
                                          },
                                          {
                                            "node-id":"6c787caa-156a-49ed-8546-547bdccf283c",
                                            "order":"0"
                                          }
                                ],
                            "property": [
                                          {
                                            "property-name": "location",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "openflow:3"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "ip-prefix",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "192.168.12.0/24"
                                                            }
                                                        ]
                                                    }
                                          },
                                          {
                                            "property-name": "gateway-ip",
                                            "property-values": {
                                                      "string-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "192.168.12.1"
                                                            }
                                                        ]
                                                    }
                                          }
                                        ],
                            "node-id": "175425f7-c9c9-474a-962c-70cb6c180d4d"
                          }
                    ]
              }
          }
        }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_enterprise_interior_connection(contHost):
    data={
         "input": {
              "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
              "objects":{
                  "connection": [
                          {
                            "connection-name": "c1",
                            "connection-id": "30da6667-608e-4d2f-bb50-79e5cabcc523",
                            "end-node": [
                              {
                                "order": "0",
                                "node-id": "94a6fb90-b425-4ffd-9515-c0684aa4c37f"
                              },
                              {
                                "order": "0",
                                "node-id": "175425f7-c9c9-474a-962c-70cb6c180d4d"
                              }
                            ],
                            "connection-type": "p2p",
                            "property": [
                                {
                                    "property-name": "bandwidth",
                                    "property-values": {
                                                      "int-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "512"
                                                            }
                                                        ]
                                                    }
                                }
                            ]
                        }
                    ]
                }
          }
    }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_interior_dmz_connection(contHost):
    data={
         "input": {
              "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
              "objects":{
                  "connection": [
                          {
                            "connection-name": "c2",
                            "connection-id": "b49e3960-c08d-4fff-b9fc-08b65ebcde2c",
                            "end-node": [
                              {
                                "order": "0",
                                "node-id": "175425f7-c9c9-474a-962c-70cb6c180d4d"
                              },
                              {
                                "order": "0",
                                "node-id": "b46cfa7f-93a3-43f4-ac20-09307c75feca"
                              }
                            ],
                            "connection-type": "p2p"
                        }
                    ]
                }
          }
    }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def add_dmz_internet_connection(contHost):
    data={
         "input": {
              "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
              "objects":{
                  "connection": [
                          {
                            "connection-name": "c3",
                            "connection-id": "e0d56fee-7235-4748-a2a1-eb5e3733d866",
                            "end-node": [
                              {
                                "order": "0",
                                "node-id": "b46cfa7f-93a3-43f4-ac20-09307c75feca"
                              },
                              {
                                "order": "0",
                                "node-id": "d463232f-363f-491c-a6f5-097ed0a794d3"
                              }
                            ],
                            "connection-type": "p2p"
                        }
                    ]
                }
          }
    }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def update_enterprise_interior_connection(contHost):
    data={
         "input": {
              "user-id": "14ce424a-3e50-4a2a-ad5c-b29845158c8b",
              "objects":{
                  "connection": [
                          {
                            "connection-name": "c1",
                            "connection-id": "30da6667-608e-4d2f-bb50-79e5cabcc523",
                            "end-node": [
                              {
                                "order": "0",
                                "node-id": "94a6fb90-b425-4ffd-9515-c0684aa4c37f"
                              },
                              {
                                "order": "0",
                                "node-id": "175425f7-c9c9-474a-962c-70cb6c180d4d"
                              }
                            ],
                            "connection-type": "p2p",
                            "property": [
                                {
                                    "property-name": "bandwidth",
                                    "property-values": {
                                                      "int-value": [
                                                            {
                                                              "order": "0",
                                                              "value": "512"
                                                            }
                                                        ]
                                                    }
                                }
                            ]
                        }
                    ]
                }
          }
    }
    post(STRUCTURE_UPDATE_USERS % contHost, data)

def post(url, data):
    headers = {'Content-type': 'application/yang.data+json',
               'Accept': 'application/yang.data+json'}
    print "POST %s" % url
    print json.dumps(data, indent=4, sort_keys=True)
    r = requests.post(url, data=json.dumps(data), headers=headers, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    print r.text
    r.raise_for_status()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--controller', default='127.0.0.1', help='controller IP')
    args=parser.parse_args()

    # CREATE User;
    register_user(args.controller)

    # IMPORT Node server1 Type host;
    transaction_begin(args.controller)
    add_server1_host(args.controller)
    #transaction_end(args.controller)

    # IMPORT Node server2 Type host;
    #transaction_begin(args.controller)
    add_server2_host(args.controller)
    #transaction_end(args.controller)

    # IMPORT Node vm1 Type host;
    #transaction_begin(args.controller)
    add_vm1_host(args.controller)
    #transaction_end(args.controller)

    # IMPORT Node vm2 Type host;
    #transaction_begin(args.controller)
    add_vm2_host(args.controller)
    #transaction_end(args.controller)

    # IMPORT Node enterprise Type ext-group Property location:openflow:4:2, ip-prefix:192.18.13.0/24;
    #transaction_begin(args.controller)
    add_enterpise_node(args.controller)
    #transaction_end(args.controller)

    # CREATE Node interior Type l2-group Contain server1,vm1,vm2;
    #transaction_begin(args.controller)
    add_interior_node(args.controller)
    #transaction_end(args.controller)

    # CREATE Node dmz Type l2-group Contain server2;
    #transaction_begin(args.controller)
    add_dmz_node(args.controller)
    #transaction_end(args.controller)

    # IMPORT Node internet Type ext-group Property location:openflow:3:4, ip-prefix:172.168.1.0/24;
    #transaction_begin(args.controller)
    add_internet_node(args.controller)
    #transaction_end(args.controller)

    # CREATE Connection c1 Endnodes enterprise,interior Property bandwidth:128(kbps);
    #transaction_begin(args.controller)
    add_enterprise_interior_connection(args.controller)
    #transaction_end(args.controller)

    # CREATE Connection c2 Endnodes interior,dmz;
    #transaction_begin(args.controller)
    add_interior_dmz_connection(args.controller)
    #transaction_end(args.controller)

    # CREATE Connection c3 Endnodes dmz,internet;
    #transaction_begin(args.controller)
    add_dmz_internet_connection(args.controller)
    transaction_end(args.controller)

    # UPDATE Connection c1 Endnodes enterprise,interior Property bandwidth:512(kbps);
    #transaction_begin(args.controller)
    #update_enterprise_interior_connection(args.controller)
    #transaction_end(args.controller)