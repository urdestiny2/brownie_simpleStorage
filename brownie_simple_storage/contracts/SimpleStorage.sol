//SPDX-License-Identifier: MIT;

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    uint256 public favNum; // if not specified then gets initialised with 1.

    function store(uint256 _favNum) public returns (uint256) {
        favNum = _favNum;
        return _favNum;
    }

    function show() public view returns (uint256) {
        // view functions only read state of the blockchain, hence they dont commit any transaction.
        return favNum;
    }

    /* function triple_favNum(uint _favNum) public pure{  //simply used to do some maths, doesn't store any value, doesnt reads anything of the chain.
        3*_favNum;
    }
    */

    struct people {
        uint256 amt;
        string name;
    }

    people[] public person;
    mapping(string => uint256) public nametofavNum;

    function addtoarray(uint256 _amt, string memory _name) public {
        person.push(people(_amt, _name));
        nametofavNum[_name] = _amt;
    }
}
