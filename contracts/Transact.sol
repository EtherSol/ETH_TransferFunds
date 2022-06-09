pragma solidity >=0.4.0 <0.9.0;

contract Transact {
    mapping (address => uint) public balances;

    error InsufficientBalance(uint requested, uint available);
    event Sent(address from, address to, uint amount);

    function giveMoney(address account, uint amount) public{
        balances[account] += amount;
    }

    function send(address receiver, uint amount) public {
        if (amount > balances[msg.sender])
            revert InsufficientBalance({
                requested: amount,
                available: balances[msg.sender]
            });

            balances[msg.sender] -= amount;
            balances[receiver] += amount;
            emit Sent(msg.sender, receiver, amount);
    }
}