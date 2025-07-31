class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        String prefix = strs[0]; // Start with the first string

        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(prefix)) {
                // Shorten prefix until it matches
                prefix = prefix.substring(0, prefix.length() - 1);
                if (prefix.isEmpty()) return "";
            }
        }

        return prefix;
    }
}
