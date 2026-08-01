impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        if height.len() < 3 {
            return 0
        }

        let mut left = 0usize;
        let mut right = height.len() -1 ;
        let mut l_max = 0;
        let mut r_max = 0;
        let mut water = 0i64;
        while left < right {
            if height[left] <= height[right] {
                l_max = l_max.max(height[left]);
                water += (l_max - height[left]) as i64;
                left += 1;
            } else {
                r_max = r_max.max(height[right]);
                water += (r_max - height[right]) as i64;
                right -= 1;
            }
        }
        return water as i32;
    }
}
