//
//  Question2.c
//  Final
//
//  Created by Minh Nguyen on 7/29/20.
//  Copyright © 2020 Minh Nguyen. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int main(int argc, const char * argv[]) {
    // insert code here...
    
    if (argc != 2) {
        printf("Please provide 1 input for this program:\n");
        printf("   1. A name of output file.\n");
        printf("Please run the program again.\n");
    }
    
    printf("Creating a 'FINALc' folder\n");
    system("mkdir FINALc");

    printf("\nPart 1:\nCreating a subdirectory of FINALc called 'copies'\n");
    system("mkdir FINALc/copies");

    printf("Creating a subdirectory of FINALc called 'encrypted'\n");
    system("mkdir FINALc/encrypted");

    printf("Creating a subdirectory of FINALc called 'decrypted'\n");
    system("mkdir FINALc/decrypted");

    printf("Creating a copy of Question2.c and places the copy into FINALc\n");
    system("cp Question2.c FINALc/");

    printf("\n*********************\n");
    printf("Part 2:\nSaving the outputs to the file\n");
    char command[100] = " > FINALc/";
    strcat(command, argv[1]);
    system(command);
    
    return 0;
}

