import os
from dotenv import load_dotenv
from web3 import Web3, Account


class W3Class():

    def __init__(self, rpc_url, private_key, contract_addr):
        self.contract_abi = [
        {
            "inputs": [
            {
                "internalType": "string",
                "name": "name_",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symbol_",
                "type": "string"
            },
            {
                "internalType": "uint8",
                "name": "decimals_",
                "type": "uint8"
            },
            {
                "internalType": "uint256",
                "name": "initialBalance_",
                "type": "uint256"
            },
            {
                "internalType": "bytes",
                "name": "signature_",
                "type": "bytes"
            },
            {
                "internalType": "address payable",
                "name": "feeReceiver_",
                "type": "address"
            }
            ],
            "stateMutability": "payable",
            "type": "constructor"
        },
        {
            "inputs": [],
            "name": "AccessControlBadConfirmation",
            "type": "error"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "internalType": "bytes32",
                "name": "neededRole",
                "type": "bytes32"
            }
            ],
            "name": "AccessControlUnauthorizedAccount",
            "type": "error"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "allowance",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "needed",
                "type": "uint256"
            }
            ],
            "name": "ERC20InsufficientAllowance",
            "type": "error"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "balance",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "needed",
                "type": "uint256"
            }
            ],
            "name": "ERC20InsufficientBalance",
            "type": "error"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "approver",
                "type": "address"
            }
            ],
            "name": "ERC20InvalidApprover",
            "type": "error"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "receiver",
                "type": "address"
            }
            ],
            "name": "ERC20InvalidReceiver",
            "type": "error"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
            ],
            "name": "ERC20InvalidSender",
            "type": "error"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            }
            ],
            "name": "ERC20InvalidSpender",
            "type": "error"
        },
        {
            "inputs": [],
            "name": "ERC20MintingFinished",
            "type": "error"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            }
            ],
            "name": "OwnableInvalidOwner",
            "type": "error"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
            ],
            "name": "OwnableUnauthorizedAccount",
            "type": "error"
        },
        {
            "anonymous": "False",
            "inputs": [
            {
                "indexed": "True",
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": "True",
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": "False",
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "Approval",
            "type": "event"
        },
        {
            "anonymous": "False",
            "inputs": [],
            "name": "MintFinished",
            "type": "event"
        },
        {
            "anonymous": "False",
            "inputs": [
            {
                "indexed": "True",
                "internalType": "address",
                "name": "previousOwner",
                "type": "address"
            },
            {
                "indexed": "True",
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
            ],
            "name": "OwnershipTransferred",
            "type": "event"
        },
        {
            "anonymous": "False",
            "inputs": [
            {
                "indexed": "True",
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "indexed": "True",
                "internalType": "bytes32",
                "name": "previousAdminRole",
                "type": "bytes32"
            },
            {
                "indexed": "True",
                "internalType": "bytes32",
                "name": "newAdminRole",
                "type": "bytes32"
            }
            ],
            "name": "RoleAdminChanged",
            "type": "event"
        },
        {
            "anonymous": "False",
            "inputs": [
            {
                "indexed": "True",
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "indexed": "True",
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "indexed": "True",
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
            ],
            "name": "RoleGranted",
            "type": "event"
        },
        {
            "anonymous": "False",
            "inputs": [
            {
                "indexed": "True",
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "indexed": "True",
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "indexed": "True",
                "internalType": "address",
                "name": "sender",
                "type": "address"
            }
            ],
            "name": "RoleRevoked",
            "type": "event"
        },
        {
            "anonymous": "False",
            "inputs": [
            {
                "indexed": "True",
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "indexed": "True",
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "indexed": "False",
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "Transfer",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "DEFAULT_ADMIN_ROLE",
            "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "MINTER_ROLE",
            "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            }
            ],
            "name": "allowance",
            "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "approve",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
            ],
            "name": "balanceOf",
            "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "burn",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "burnFrom",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "decimals",
            "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "finishMinting",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            }
            ],
            "name": "getRoleAdmin",
            "outputs": [
            {
                "internalType": "bytes32",
                "name": "",
                "type": "bytes32"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
            ],
            "name": "grantRole",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
            ],
            "name": "hasRole",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "mint",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "mintingFinished",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "name",
            "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "renounceOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "callerConfirmation",
                "type": "address"
            }
            ],
            "name": "renounceRole",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "bytes32",
                "name": "role",
                "type": "bytes32"
            },
            {
                "internalType": "address",
                "name": "account",
                "type": "address"
            }
            ],
            "name": "revokeRole",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "bytes4",
                "name": "interfaceId",
                "type": "bytes4"
            }
            ],
            "name": "supportsInterface",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "symbol",
            "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "totalSupply",
            "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "transfer",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "from",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "value",
                "type": "uint256"
            }
            ],
            "name": "transferFrom",
            "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                "type": "address"
            }
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
        ]

        self.contract_addr = contract_addr

        self.w3 = Web3(Web3.HTTPProvider(rpc_url))

        self.network_id = self.w3.net.version 
        print(f"Connected to network with ID: {self.network_id}")

        self.account=Account.from_key(private_key) 
        print(f"Loaded account: {self.account.address}")

        self.contract=self.w3.eth.contract(address=contract_addr, abi=self.contract_abi)
        # balance=contract.functions.balanceOf(account.address).call() 
        # print(f"Contract balance: {balance}")

    # 18 decimal places
    def mint_token(self, amount, decimal_places = 1e18):
        token_amount = amount * int(decimal_places)
        transaction=self.contract.functions.mint(self.account.address, int(token_amount)).build_transaction(
            { 'from': self.account.address,
            'nonce': self.w3.eth.get_transaction_count(self.account.address, 'pending'),
            'gas': 200000, 'gasPrice': self.w3.to_wei('40', 'gwei') 
            }
            ) 

        signed_txn=self.w3.eth.account.sign_transaction(transaction, self.account._private_key) 
        transaction_hash=self.w3.eth.send_raw_transaction(signed_txn.raw_transaction) 

        print(f"Transaction sent: {transaction_hash.hex()}")


# if __name__ == "__main__":
#     while True:
#         input("Press enter to mint a RHEO token or press ctrl-c to exit")
#         mint_token(account.address)

