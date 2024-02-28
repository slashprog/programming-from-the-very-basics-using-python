#include <stdio.h>
#include <gmp.h>
#include <stdlib.h>

#include <readline/readline.h>
#include <readline/history.h>

int main()
{
    char *input;
    char *result;

    mpz_t n;
    mpz_t r;

    int i;

    mpz_init(n);
    mpz_init(r);

    input = readline("Enter a number: ");
    mpz_set_str(n, input, 0);

    for (i=1; i<=10; i++) {
        mpz_mul_si(r, n, i);
        result = mpz_get_str(NULL, 10, r);
        printf("%s x %d = %s\n", input, i, result);
    }
    free(input);
    free(result);

    return 0;

}
