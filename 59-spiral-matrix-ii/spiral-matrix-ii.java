class Solution {
    public int[][] generateMatrix(int n) {
int [][]matrix = new int[n][n];
if(n==0){
    return matrix;
}
    int rawBegin = 0;
    int rawEnd = n-1;//2
    int columnBegin = 0;
    int columnEnd = n-1;//2
    int num =1;
while(rawBegin <= rawEnd && columnBegin <= columnEnd){
    for(int i=columnBegin; i<=columnEnd; i++){
      matrix[rawBegin][i]=num++;
    }
    rawBegin++;//1

    for(int i=rawBegin; i<=rawEnd; i++){
      matrix[i][columnEnd]=num++;
    }

    columnEnd--;//1

   
    for(int i=columnEnd; i>=columnBegin; i--){
         if(rawBegin<=rawEnd)
      matrix[rawEnd][i]=num++;
    }
    rawEnd--;


  
    for(int i=rawEnd ; i>=rawBegin;i--){
         if(columnBegin <= columnEnd)
      matrix[i][columnBegin]=num++;
    }
    
    columnBegin++;
    
    }
     return matrix;
}}