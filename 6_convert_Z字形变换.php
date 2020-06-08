//Z字变换
class Solution {

    /**
     * @param String $s
     * @param Integer $numRows
     * @return String
     */
    function convert($s, $numRows) {
        $len=strlen($s);
        if($numRows<=1) return $s;
        $str='';
        for ($row=0;$row<$numRows;$row+=1){
            for($num=$row;$num<$len;$num+=(2*$numRows-2)){
                $str=$str.$s[$num];
                if($row==0 || $row==$numRows-1){}else{
                    if($num+2*$numRows-2*$row-2<$len){
                        $str=$str.$s[$num+2*$numRows-2*$row-2];
                    }
                }
            }
        }
        return $str;
    }
}
//20ms，80.18%
//14.9MB,71.43%
