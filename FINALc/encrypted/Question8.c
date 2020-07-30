//
//  Question8.c
//  Final
//
//  Created by Minh Nguyen on 7/29/20.
//  Copyright © 2020 Minh Nguyen. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <dirent.h>

int main(int argc, const char * argv[]) {
    char *directory = "../decrypted";
    char *path = ".";
    char *programName = "Question8.c";
    char *exeFile = "Question8";
    int encryptOrDecrypt = 1; // 0 for encrypt, 1 for decrypt
    
    printf("\nReading this directory...\n");
    struct dirent *dp;
    DIR *dir = opendir(path);

    while ((dp = readdir(dir)) != NULL) {
        if (strcmp(dp->d_name, ".") == 0 || strcmp(dp->d_name, "..") == 0 || strcmp(dp->d_name, programName) == 0 || strcmp(dp->d_name, exeFile) == 0)
            continue;
        
        char pathFile[100];
        sprintf(pathFile, "%s/%s", path, dp->d_name);
        if (encryptOrDecrypt == 0) {
            printf("Encrypting %s\n", pathFile);
        } else {
            printf("Decrypting %s\n", pathFile);
        }
        FILE *input;
        input = fopen(pathFile, "rb");
        
        sprintf(pathFile, "%s/%s", directory, dp->d_name);
        FILE *output;
        output = fopen(pathFile, "wb");
        
        char *buffer;
        long filelen;
        int i;

        fseek(input, 0, SEEK_END);
        filelen = ftell(input);
        rewind(input);
        buffer = (char *)malloc((filelen + 1) * sizeof(char));
        
        int key = 150;
        int shift = key % 26;
        int num = key % 10;
        if (encryptOrDecrypt == 1) {
            shift = 26 - shift;
            num = 10 - num;
        }
        for(i = 0; i < filelen; i++) {
            fread(buffer + i, 1, 1, input);
            char *p = &*(buffer + i);
            if (*p >= 'A' && *p <= 'Z') {
                *p = (char)((int)(*p + shift - 'A') % 26 + 'A');
                key = key - 1 > 0 ? ( key - 1 ) % 256 : 255;
            } else if (*p >= 'a' && *p <= 'z') {
                *p = (char)((int)(*p + shift - 'a') % 26 + 'a');
                key = key - 1 > 0 ? ( key - 1 ) % 256 : 255;
            } else if (*p >= '0' && *p <= '9') {
                *p = (char)((int)(*p + num - '0') % 10 + '0');
                key = key - 1 > 0 ? ( key - 1 ) % 256 : 255;
            }
        }
        
        printf("Copy to %s\n", pathFile);
        fwrite(buffer, filelen, 1, output);
        
        fclose(input);
        fclose(output);
    }
    
    closedir(dir);
    return 0;
}

