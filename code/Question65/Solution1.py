'''
这题尽量用java做
python由于存储类型会比较麻烦
参考
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/
'''
'''
java版
class Solution {
    public int add(int a, int b) {
        while(b!=0){
            int c = (a&b)<<1;
            a = a^b;
            b = c;
        }
        return a;
    }
}
'''
'''
一个整数取负数 全部取反加1 想想一个32位的数由2变成-2的过程
若补码 aa 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。 a ^ x 运算将 1 至 32 位按位取反；
~ 运算是将整个数字取反；因此， ~(a ^ x) 是将 32 位以上的位取反，1 至 32 位不变。
'''
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)