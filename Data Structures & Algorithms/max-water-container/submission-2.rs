impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut left = 0usize;
        let mut right = heights.len() - 1;
        let mut max_area: i64 = 0;

        while left < right {
            let h = heights[left].min(heights[right]);
            let width = (right as i64) - (left as i64);
            let current_area = (h as i64) * width;
            max_area = max_area.max(current_area);

            if heights[left] < heights[right] {
                left += 1;
            } else {
                right -= 1;
            }
        }

        max_area as i32
    }
}
