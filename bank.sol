0.8.7+

1 Ether deposit

Click getBalance()
Output: 1000000000000000000  (1 Ether in Wei)

Withdraw Ether
Enter 1000000000000000000 in withdraw()


// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract BankAccount {
    // Mapping to store balance of each user
    mapping(address => uint) private balances;

    // Deposit money (Ether) into the account
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    // Withdraw money from the account
    function withdraw(uint amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    // Show current balance
    function getBalance() public view returns (uint) {
        return balances[msg.sender];
    }

    // Optional: allow direct Ether transfers (not required for basic version)
    receive() external payable {}
}
