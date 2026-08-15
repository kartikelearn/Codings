#include <stdio.h>

int main()
{
    int a, b, n;

    char *arr[] = {
        "one","two","three","four","five",
        "six","seven","eight","nine"
    };

    scanf("%d %d", &a, &b);
    scanf("%d",&n);

    for(a; a<= b; a++)
    {
        if(n >= 1 && n <= 9)
        {
            printf("%s\n", arr[n-1]);
            break;
        }
        
        if(n>9&&n%2==0)
                printf("even\n");
                break;
        if(n>9&&n%2!=0)
                printf("odd\n");
                break;
        
    }

    return 0;
}