0.8.7+

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7; // ✅ use 0.8.7 for Remix VM compatibility

contract StudentData {
    // 1️⃣ Structure
    struct Student {
        uint id;
        string name;
        uint marks;
    }

    // 2️⃣ Array of structures
    Student[] public students;

    // Add a new student
    function addStudent(uint _id, string memory _name, uint _marks) public {
        students.push(Student(_id, _name, _marks));
    }

    // Get student count
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // Get student details
    function getStudent(uint index) public view returns (uint, string memory, uint) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.id, s.name, s.marks);
    }

    // 3️⃣ Fallback — accepts Ether or wrong calls
    fallback() external payable { }

    // Receive Ether directly
    receive() external payable { }

    // To check balance (if Ether is sent)
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}


_id: 1 _name: "Atharva" _marks: 90
_id: 2 _name: "Riya" _marks: 95


