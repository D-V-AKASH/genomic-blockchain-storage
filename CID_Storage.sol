// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract GenomicDataAccess {
    mapping(address => string[]) private userCIDs;
    mapping(address => mapping(address => bool)) private accessPermissions;

    event CIDAdded(address indexed owner, string cid);
    event AccessGranted(address indexed owner, address indexed grantee);
    event AccessRevoked(address indexed owner, address indexed grantee);

    function addCID(string calldata cid) external {
        userCIDs[msg.sender].push(cid);
        emit CIDAdded(msg.sender, cid);
    }

    function grantAccess(address grantee) external {
        accessPermissions[msg.sender][grantee] = true;
        emit AccessGranted(msg.sender, grantee);
    }

    function revokeAccess(address grantee) external {
        accessPermissions[msg.sender][grantee] = false;
        emit AccessRevoked(msg.sender, grantee);
    }

    function hasAccess(address owner, address user) public view returns (bool) {
        if (owner == user) return true;
        return accessPermissions[owner][user];
    }

    function getCIDs(address owner) external view returns (string[] memory) {
        require(
            hasAccess(owner, msg.sender),
            "Access denied"
        );
        return userCIDs[owner];
    }
}
