import java.nio.ByteBuffer;
import java.security.InvalidKeyException;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.FileOutputStream;
import java.util.Arrays;
import java.math.BigInteger;

//Avery Higgins, Sam Martins

public class PA2 {

public static void main(String [] args) throws InvalidKeyException, FileNotFoundException{




    File savedText = new File("savedText.txt");

    PrintWriter printWriter = new PrintWriter(new FileOutputStream(savedText, true));

  //  byte[] inKey = new byte[16];

    //inKey[15] = (byte) 0x03;
    //for(int i = 14; i > 4; i--){
    //    inKey[i] = (byte) 0x00;
  //

    byte [] inKey = {(byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00,
        (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x00,
        (byte) 0x00, (byte) 0x00, (byte) 0x00, (byte) 0x03};


    String cipherTextString = "8F9C9C3EC872D10E8C955CFE5D0672716A9A7C285876B94A6BD3133193E67DB7C2D0278FAC5499898389EC1A5F8C9B247530D564DECEC99B829D7CC45EAB3EFFEE9B2639AF76033641E86E67A5F80564";

    byte [] cipherText = new byte[cipherTextString.length() / 2];
    for(int i = 0; i < cipherText.length; i++){
        cipherText[i] = (byte) Integer.parseInt(cipherTextString.substring(i*2, i *2 + 2), 16);

    }
    //byte[] cipherText = cipherTextString.getBytes();
  //  System.out.println(AESExample.convertToString(cipherText));


    int numOfCiphertextBlocks = cipherText.length / 16 - 1; // Each AES block has 16 bytes and we need to exclude the IV
	  byte[] cleartextBlocks = new byte[numOfCiphertextBlocks * 16];

    byte[] receivedIV = new byte[16];
    for (int i = 0; i < 16; i++){
      receivedIV[i] = cipherText[i];
    }

    int lowerBound = 31;
    int upperBound = 128;

    byte[] currentDecryptionBlock = new byte[16];

    //long value = 0x0000000000000;
    BigInteger value = new BigInteger(args[0], 16);
    //long max = 0xFFFFFFFF;
    BigInteger max = new BigInteger(args[1],16);
    BigInteger one = new BigInteger("1");
    long start = System.currentTimeMillis();

  //  while((value & 0xfffffff) < (max & 0xfffffff))
    while(value.compareTo(max) < 0){

        byte [] hexnums = value.toByteArray();
        //byte [] hexnums = ByteBuffer.allocate(4).putInt(value).array();
        int index = 3;
        for(int x = hexnums.length; x > 0; x--){
            inKey[index] = hexnums[x - 1];
            index--;
            //inKey[x] = (byte) inKey[x];
        }

        inKey[4] = (byte) 0x60;

        Object decryptRoundKeys = Rijndael_Algorithm.makeKey (Rijndael_Algorithm.DECRYPT_MODE, inKey);

        for (int i=0; i < numOfCiphertextBlocks; i++) {
            if(i > 1){
                System.out.println("Succes!!");
                printWriter.append("\nKey: " + new String(inKey));
                printWriter.append("\n" + new String (cleartextBlocks));
            }

            for (int j=0; j < 16; j++) currentDecryptionBlock [j] = cipherText[(i+1)*16 + j]; // Note that the first block is the IV

            byte[] thisDecryptedBlock = Rijndael_Algorithm.blockDecrypt2 (currentDecryptionBlock, 0, decryptRoundKeys);

            for (int j=0; j < 16; j++){
                //System.out.println(i*16 + j);

                cleartextBlocks[i*16+j] =  (byte) (thisDecryptedBlock[j] ^ cipherText[i*16 + j]);
                if((cleartextBlocks[i*16+j] & 0xff) < lowerBound || (cleartextBlocks[i*16+j] & 0xff) > upperBound){
                    i = numOfCiphertextBlocks + 1;
                    //value += 1;
                    j = 17;
                }
              //  else {
                    //System.out.print(cleartextBlocks[i*16+j]);

              //  }
            }




        }

        inKey[4] = (byte) 0xe0;
        decryptRoundKeys  = Rijndael_Algorithm.makeKey (Rijndael_Algorithm.DECRYPT_MODE, inKey);

        for (int i=0; i < numOfCiphertextBlocks; i++) {
            if(i > 1){
                System.out.println("Succes!!");
                printWriter.append("\nKey: " + inKey);
                printWriter.append(new String (cleartextBlocks));
            }

            for (int j=0; j < 16; j++) currentDecryptionBlock [j] = cipherText[(i+1)*16 + j]; // Note that the first block is the IV

            byte[] thisDecryptedBlock = Rijndael_Algorithm.blockDecrypt2 (currentDecryptionBlock, 0, decryptRoundKeys);

            for (int j=0; j < 16; j++){
                //System.out.println(i*16 + j);

                cleartextBlocks[i*16+j] =  (byte) (thisDecryptedBlock[j] ^ cipherText[i*16 + j]);
                if((cleartextBlocks[i*16+j] & 0xff) < lowerBound || (cleartextBlocks[i*16+j] & 0xff) > upperBound){
                    i = numOfCiphertextBlocks + 1;
                    //value += 1;
                    j = 17;
                }
            //    else {
                    //System.out.print(cleartextBlocks[i*16+j]);

              //  }
            }




        }



        value = value.add(one);
        //egit = true;

    }

    long finish = System.currentTimeMillis();
    long tdelta = finish - start;

    double elapsed = tdelta / 100.0;

    printWriter.append("\n" + elapsed);
    printWriter.close();

}
}
