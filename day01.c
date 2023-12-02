#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {

    FILE *txtFile = fopen("day01Input.txt", "r");
    FILE *outputFile = fopen("output.txt", "rw");

    const int maxLen = 256;
    char line[256];

    while (fgets(line, maxLen, txtFile) != NULL) {
        char *text = strtok(line, "\n");
        int len = strlen(text);
        printf("%d", len);

        printf("%*s", text);
        for (int i = 0; i < len; i++) {
            if (text[i] > 47 && text[i] < 58) {
                fprintf(outputFile, "%d", text[i] - '0');
            }
        }
        fprintf(outputFile, "\n");
    }

    fclose(txtFile);

    int sum = 0;
    int endsum = 0;

    while (fgets(line, maxLen, outputFile)) {
        char *text = strtok(line, "\n");
        int len = strlen(text);

        if (len == 2) {
            sum += (text[0] - '0') + (text[0] - '0');
        }
        else if (len > 2) {
            sum += (text[0] - '0') + (text[len-1] - '0');
        }
    }

    printf("%d\n", sum);

    fclose(outputFile);
}