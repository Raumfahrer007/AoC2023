#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(void) {

    FILE *txtFile = fopen("day07Input.txt", "r");

    const int maxLen = 256;
    char line[256];
    long sum = 0;

    long long *hands[1000][2];
    //int *bets[1000];
    for (int i = 0; i < 1000; i++){
        hands[i][0] = 0;
        hands[i][1] = 0;
    }

    int z = 0;
    while (fgets(line, maxLen, txtFile)) {
        char *hand = strtok(line, " ");
        int *betStr = strtok(NULL, " ");

        int bet = atoi(betStr);

        int cardCount[] = {0,0,0,0,0,0,0,0,0,0,0,0,0};
        long long handValue = 0;
        long long k = 100000000;

        for (int i = 0; i < strlen(hand); i++) {
            int cardScore;
            if (hand[i] == '2') { 
                cardCount[0] += 1;
                cardScore = 0;
            }
            else if (hand[i] == '3') { 
                cardCount[1] += 1;
                cardScore = 1;
            }
            else if (hand[i] == '4') { 
                cardCount[2] += 1;
                cardScore = 2;
            }
            else if (hand[i] == '5') { 
                cardCount[3] += 1;
                cardScore = 3;
            }
            else if (hand[i] == '6') { 
                cardCount[4] += 1;
                cardScore = 4;
            }
            else if (hand[i] == '7') { 
                cardCount[5] += 1;
                cardScore = 5;
            }
            else if (hand[i] == '8') { 
                cardCount[6] += 1;
                cardScore = 6;
            }
            else if (hand[i] == '9') { 
                cardCount[7] += 1;
                cardScore = 7;
            }
            else if (hand[i] == 'T') { 
                cardCount[8] += 1;
                cardScore = 8;
            }
            else if (hand[i] == 'J') { 
                cardCount[9] += 1;
                cardScore = 9;
            }
            else if (hand[i] == 'Q') { 
                cardCount[10] += 1;
                cardScore = 10;
            }
            else if (hand[i] == 'K') { 
                cardCount[11] += 1;
                cardScore = 11;
            }
            else if (hand[i] == 'A') { 
                cardCount[12] += 1;
                cardScore = 12;
            }

            handValue += (cardScore * k);
            k = k / 100;
        }
        
        k = 1;
        int handType = 0;
        for (int i = 1; i <= 5; i++) {
            for (int j = 0; j < sizeof(cardCount); j++){
                if (cardCount[j] == i){
                    handType += (cardCount[j] * k);
                    k *= 10;
                }
            }
        }

        switch(handType) {
            case 5:
                handValue += 60000000000;
                break;
            case 41:
                handValue += 50000000000;
                break;
            case 32:
                handValue += 40000000000;
                break;
            case 311:
                handValue += 30000000000;
                break;
            case 221:
                handValue += 20000000000;
                break;
            case 211:
                handValue += 10000000000;
                break;
            case 11111:
                handValue += 0;
                break;
        }

        hands[z][0] += handValue;
        hands[z][1] += bet;
        z++;
        printf("Hand: %lli\n", handValue);
        printf("Bet: %d\n", hands[z][1]);
        
    }
    
    int temp[2];
    /*for (int i = 0; i < sizeof(hands) - 1; i++){
        for (int j = 0; j < sizeof(hands)-i-1; j++){
            if (hands[i][0] > hands[i+1][0]){
                //printf("BEFORE: %d\n", hands[i][0]);
                temp[0] = hands[i][0];
                temp[1] = hands[i][1];
                hands[i][0] = hands[i+1][0];
                hands[i][1] = hands[i+1][1];
                hands[i+1][0] = temp[0];
                hands[i+1][1] = temp[1];
                //printf("After: %d\n", hands[i+1][0]);
            }
        }
    }*/

    /*for (int i = 0; i < sizeof(hands); i++){
        printf("Hand: %lli\n", hands[i][0]);
        printf("Bet: %d\n", hands[i][1]);
    }*/
    return 0;
}