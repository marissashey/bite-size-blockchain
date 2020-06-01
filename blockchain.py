def test_code():
    """Test creating chain of 20 blocks."""
    blockchain = [make_genesis_block()]
    prev_block = blockchain[0]
    for _ in range(0, 20):
        block = next_block(prev_block, data='some data here')
        blockchain.append(block)
        prev_block = block
        print('{} added to blockchain'.format(block))
        print('Hash: {}\n'.format(block.hash))