impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        let n = nums.len();
        let mut result = Vec::new();

        for i in 0..n-2 {
            // skip duplicate
            if i > 0 && nums[i] == nums[i-1] {
                continue;
            }
            //exit early
            if nums[i] + nums[i+1] + nums[i+2] > 0 {
                break;
            }

            //Early continuation: if the largest possible sum with nums[i] is < 0, skip this i
            if nums[i] + nums[n - 2] + nums[n - 1] < 0 {
                continue;
            }
            let mut left = i + 1;
            let mut right = n -1;
            while left < right {
                let total = nums[i] + nums[left] + nums[right];
                match total.cmp(&0) {
                    std::cmp::Ordering::Equal => {
                        result.push(vec![nums[i], nums[left], nums[right]]);
                        left+=1;
                        right-=1;
                        while left < right && nums[left] == nums[left - 1] {
                            left+=1;
                        }
                        while left < right && nums[right] == nums[right+1] {
                            right-=1;
                        }
                    }
                    std::cmp::Ordering::Greater => {
                        right-=1;
                    }
                    std::cmp::Ordering::Less => {
                        left+=1;
                    }
                }
            }
        }
        result
    }
}
