/**
 * BinarySearch.java
 * Author: RhettYoungberg
 * Borrowed from Dream In Code: http://www.dreamincode.net/forums/topic/196941-whats-wrong-with-my-code/
 */


import java.util.Arrays;

public class BinarySearch
{
   public static final int NOT_FOUND = -1;
   public static int binarySearch(Integer[] a, int x)
   {
       int low=0;
       int high = a.length - 1;
       int mid;
       while (low <= high)
       {
           mid = (low + high) / 2;
           if (a[mid].compareTo(x)<0)
           low = mid + 1;
           else if (a[mid].compareTo (x) > 0)
           high = mid -1;
           else
           return mid;
        }
        return NOT_FOUND;
    }
  
    public static void main(String[] args) {
      int SIZE =  7;
        double [] a = {-3,10,5,24,45.3,10.5};
        Arrays.sort(a);
       System.out.println(a);
       }
}

