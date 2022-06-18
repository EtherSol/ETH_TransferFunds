// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract transaction {
    
    AggregatorV3Interface internal ethUsdPriceFeed;

    address payable public minter;
    uint256 public usdFee; 
    mapping (address => uint) public balances;

    event Deposit(address sender, uint amount, uint balance);
    event Transfer(address caller, uint amount, string message);
    // event Transfer(address to, uint amount, string message)/*uint balance*/;

    constructor(address _priceFeedAddress) payable{
        minter = payable(msg.sender);
        usdFee = 12.0444 * (10**18);
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    function mint(address payable _receiver, uint _amount) public payable returns (uint256){
        require(msg.sender == minter);
        _amount = msg.value;
        require(msg.value == _amount, "msg.value does not equal to _amount");
        return _amount;
    }

    // function deposit(address payable sender,uint256 amount) public payable {
    //     emit Deposit(sender = msg.sender,amount = msg.value,address(this).balance);
    // }

    modifier onlyOwner() {
        require(msg.sender == minter,"Not Owner");
        _;
    }

    function contract_balance() public view returns (uint) {
        return address(this).balance;
        //return balances[minter]; Shows the balance of Wei
    }

    fallback () external payable {
        emit Transfer(msg.sender,msg.value,"Fallback was called");
    }

    receive () external payable onlyOwner {
        emit Transfer(msg.sender, msg.value, "Receive");
    }

    function transfer_eth(address payable _to,uint256 _amount,string memory _message) public payable onlyOwner {
        emit Transfer(_to, msg.value, _message);
    }

    function getPrice() public view returns (uint256) {
        (, int256 price, , , ) = ethUsdPriceFeed.latestRoundData();
        uint256 adjustedPrice = uint256(price) * 10**10;
        //Sending 0.01 ETH, or $11 Equivalent
        // 'x' / $ 1,163 = 0.01 Eth
        // x = $ 11
        uint256 minimum_eth = (usdFee * 10**18) / adjustedPrice;
        return minimum_eth;
    }
}