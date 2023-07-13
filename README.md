# V2VBlockchain

## This implements a basic blockchain of V2V communication
#### It defines a Block class that represents a block in the blockchain. Each block contains an index, timestamp, previous hash, a list of messages, a nonce, and a hash. 

#### It defines a Blockchain class that represents the entire blockchain. It maintains a chain of blocks and a list of vehicles participating in the V2V communication. The blockchain has a specified difficulty level for mining blocks.

#### The create_genesis_block method creates the first block in the chain (genesis block).
#### The add_member method adds a new member to the blockchain.
#### The add_block method adds a new block to the chain, mining it with the specified difficulty level.
#### The is_chain_valid method checks if the blockchain is valid by verifying the hashes and previous hashes of all blocks.
