#include <stdio.h>
#include <stdlib.h>

int main()
{
    char type;
    int hourEntry, minuteEntry, hourExit, minuteExit, entry, exit, totalParkingTime; 
    float totalRounded, totalChargeFee; 
    printf("||    ***PARKING CHARGES***     ||\n");
    printf("Car-C : Bus-b : Truck-t : Scooter-s : Cycle-c : Motorcycle-m\n\n");
    printf("Enter type of vehicle:"); 
    scanf("%c", &type);
    printf("Enter an integer between 0 and 24 showing the hour the vehicle entered the lot: ", hourEntry); 
    scanf("%d", &hourEntry);
    printf("Enter an integer between 0 and 60 showing the minute the vehicle entered the lot: ", minuteEntry); 
    scanf("%d", &minuteEntry);
    printf("Enter an integer between 0 and 24 showing the hour the vehicle exited the lot: ", hourExit); 
    scanf("%d", &hourExit);
    printf("Enter an integer between 0 and 60 showing the minute the vehicle exited the lot: ", minuteExit);
    scanf("%d", &minuteExit);

    entry = hourEntry + minuteEntry;
    exit = hourExit + minuteExit;
    totalParkingTime = exit - entry;

    switch(type)
    {
        case 'C':
            if(totalParkingTime <= 3)
                totalChargeFee = 10 *3* totalParkingTime;
            else if(totalParkingTime > 3){
                totalChargeFee = 10 * 3 + 20 * (totalParkingTime - 3);
             }
              break;

        case 't':
            if(totalParkingTime <= 3)
                totalChargeFee = 20*3 * totalParkingTime;
            else if(totalParkingTime > 3){
                totalChargeFee = 20 * 3 + 30 * (totalParkingTime - 3);
    }
    break;

        case 'b':
             if(totalParkingTime <= 3)
                totalChargeFee = 20 *3* totalParkingTime;
            else if(totalParkingTime > 3){
                totalChargeFee = 20 * 3 + 30 * (totalParkingTime - 3);
    }break;
        case 's':
            if(totalParkingTime <= 3)
                totalChargeFee = 5*3* totalParkingTime;
            else if(totalParkingTime > 3){
                totalChargeFee = 5 * 3 + 10 * (totalParkingTime - 3);
    }
    break;
        case 'c':
            if(totalParkingTime <= 3)
                totalChargeFee = 5*3* totalParkingTime;
            else if(totalParkingTime > 3){
                totalChargeFee = 5 * 3 + 10 * (totalParkingTime - 3);
    }
    break;
         case 'm':
           if(totalParkingTime <= 3)
                totalChargeFee = 5*3* totalParkingTime;
            else if(totalParkingTime > 3){
                totalChargeFee = 5 * 3 + 10 * (totalParkingTime - 3);
            }
            break;
    }



    printf("Entry time:%d\n",+entry );
    printf("Exit time: %d\n",+exit);
    printf("***Total Parking time***: %d hrs\n", +totalParkingTime);
    printf("***Type of vechile ****: %c\n",+type);
    printf("***Total Parking Fare***: %f\n",+totalChargeFee);

    return 0;
}