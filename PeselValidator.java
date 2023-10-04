public class PeselValidator {

    public static void main(String args[]){
        int[] pesel = { 9,7,0,4,2,8,4,7,1,5,1 };

        int x1 = pesel[0];
        int x2 = pesel[1];
        int x3 = pesel[2];
        int x4 = pesel[3];
        int x5 = pesel[4];
        int x6 = pesel[5];
        int x7 = pesel[6];
        int x8 = pesel[7];
        int x9 = pesel[8];
        int x10 = pesel[9];
        int x11 = pesel[10];

        //1-3-7-9-1-3-7-9-1-3.

        int y1 = 1;
        int y2 = 3;
        int y3 = 7;
        int y4 = 9;
        int y5 = 1;
        int y6 = 3;
        int y7 = 7;
        int y8 = 9;
        int y9 = 1;
        int y10 = 3;

        int z1 = x1 * y1;
        int z2 = x2 * y2;
        int z3 = x3 * y3;
        int z4 = x4 * y4;
        int z5 = x5 * y5;
        int z6 = x6 * y6;
        int z7 = x7 * y7;
        int z8 = x8 * y8;
        int z9 = x9 * y9;
        int z10 = x10 * y10;

        int suma = 0;
        if(z1 >= 10){
            suma = suma + z1 % 10; //13 ->13/10 = 1, r 3
        } else {
            suma = suma + z1;
        }

        if(z2 >= 10){
            suma = suma + z2 % 10;
        } else {
            suma = suma + z2;
        }

        if(z3 >= 10){
            suma = suma + z3 % 10;
        } else {
            suma = suma + z3;
        }

        if(z3 >= 10){
            suma = suma + z3 % 10;
        } else {
            suma = suma + z3;
        }

        if(z4 >= 10){
            suma = suma + z4 % 10;
        } else {
            suma = suma + z4;
        }

        if(z5 >= 10){
            suma = suma + z5 % 10;
        } else {
            suma = suma + z5;
        }

        if(z6 >= 10){
            suma = suma + z6 % 10;
        } else {
            suma = suma + z6;
        }

        if(z7 >= 10){
            suma = suma + z7 % 10;
        } else {
            suma = suma + z7;
        }

        if(z8 >= 10){
            suma = suma + z8 % 10;
        } else {
            suma = suma + z8;
        }

        if(z9 >= 10){
            suma = suma + z9 % 10;
        } else {
            suma = suma + z9;
        }

        if(z10 >= 10){
            suma = suma + z10 % 10;
        } else {
            suma = suma + z10;
        }

        if(suma >= 10){
            suma = suma % 10;
        }

        int sumaKontrolna = 10 - suma;
        if(sumaKontrolna == x11){
            System.out.println("pesel poprawny");
        } else {
            System.out.println("pesel niepoprawny");
        }
    }
}
