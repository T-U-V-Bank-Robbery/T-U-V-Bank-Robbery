// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HeistToken is ERC20, Ownable {

    constructor(uint256 initialSupply) ERC20("HeistToken", "HEIST") {
        _mint(msg.sender, initialSupply);
    }

    // Function to burn tokens
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    // Function to distribute rewards
    function reward(address recipient, uint256 amount) external onlyOwner {
        require(balanceOf(owner()) >= amount, "Insufficient tokens");
        _transfer(owner(), recipient, amount);
    }
}
