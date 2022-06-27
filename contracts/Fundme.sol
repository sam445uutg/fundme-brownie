pragma solidity ^0.6.0;
// link:
//https://github.com/smartcontractkit/chainlink/blob/eb8d050e82068881a012fdcf86b3d3fa66d47a38/contracts/src/v0.4/interfaces/AggregatorV3Interface.sol
//https://github.com/smartcontractkit/chainlink/blob/eb8d050e82068881a012fdcf86b3d3fa66d47a38/contracts/src/v0.4/vendor/SafeMathChainlink.sol
import "./SafeMathChainlink.sol";
import "./AggregatorV3Interface.sol";
contract Fundme{
    using SafeMathChainlink for uint256;
    address[]  public funder; // funded to contract
    // owner of contract
    AggregatorV3Interface public price_fed;
    address public owner;
    // constructor () public {
    //     //price_fed = AggregatorV3Interface(_priceFed);
    //     owner = msg.sender;
    // }
    constructor (address _priceFed) public {
        price_fed = AggregatorV3Interface(_priceFed);
        owner = msg.sender;
    }
    mapping (address=> uint256) public addresstouint256;
    function  fundme() public payable {
        uint256 min_usd = 5;
       require(min_usd <= convisionrate(msg.value));
        addresstouint256[msg.sender] += msg.value;
        funder.push(msg.sender);
      
    }
    //enterance fee
    
    // get version 
    function getversion() public view returns(uint256){
       // AggregatorV3Interface  = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return price_fed.version();
    }
    // get price
    function getprice() public view returns(uint256){
       // AggregatorV3Interface price_fed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
       ( ,int256 answer,,,)=price_fed.latestRoundData();
       return uint256(answer);
    }
    //consion of price
    function convisionrate(uint256 ether_amt) public view returns(uint256){
        uint256 price_per= getprice();
        uint256 eth_usd = (price_per*ether_amt)/100000000;
        return eth_usd;
    }
    // to check contract owner
    modifier onlyowner{
       // _;
        require(msg.sender == owner);
        _;
    }
    //withdraw transfer to owner account
    function withdraw() public onlyowner payable {
        msg.sender.transfer(address(this).balance);
        for (uint8 i=0; i<funder.length; i++ ){
            address funder_add =funder[i];
            addresstouint256[funder_add]=0;
        }
        funder =new address[](0);
    }

    function enetrance() public view returns(uint256){
        uint256 minusd = 5*10**18;
        uint256 price= getprice();
        uint256 perscion =100*10**18;
        return ((minusd*price)/perscion);
    }

}