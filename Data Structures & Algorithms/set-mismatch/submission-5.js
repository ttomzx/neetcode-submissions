class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    findErrorNums(nums) {
        const freq = {};
        const res = []

        for (let x of nums) {
            if (freq[x]) {
                freq[x]++;
            } else {
                freq[x] = 1;
            }
        }

        for (let key in freq) {
            if (freq[key] === 2) {
                res.push(key);
                break;
            }
        }

        for (let i = 1; i <= nums.length + 1; i++) {
            if (!freq[i]) {
                res.push(i);
                break;
            }
        }

        return res
    }
}
