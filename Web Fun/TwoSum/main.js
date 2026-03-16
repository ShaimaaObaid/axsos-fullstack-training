/*function twoSum(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target) {
                return [i, j];
            }
        }
    }
}*/
function twoSum(nums, target) {
    let map = {}; 
    
    for (let i = 0; i < nums.length; i++) {
        let complement = target - nums[i];
        
        if (map[complement] !== undefined) {
            return [map[complement], i]; 
        }
        
        map[nums[i]] = i; 
    }
}