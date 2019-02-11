import java.nio.ByteBuffer;
import java.security.InvalidKeyException;

//Avery Higgins, Sam Martins

public class PA2 {

public static void main(String [] args) throws InvalidKeyException{



    File savedText = new File("savedText.txt");

    PrintWriter printWriter = new PrintWriter(savedText);

    byte[] inKey = new byte[16];

    

    String cipherTextString = "8F9C9C3EC872D10E8C955CFE5D0672716A9A7C285876B94A6BD3133193E67DB7C2D0278FAC5499898389EC1A5F8C9B247530D564DECEC99B829D7CC45EAB3EFFEE9B2639AF76033641E86E67A5F80564";
    
    byte[] cipherText = cipherTextString.getBytes();

    int numOfCiphertextBlocks = cipherText.length / 16 - 1; // Each AES block has 16 bytes and we need to exclude the IV
	byte[] cleartextBlocks = new byte[numOfCiphertextBlocks * 16];

    int lowerBound = 32;
    int upperBound = 127;

    byte[] currentDecryptionBlock = new byte[16];
    
    boolean legit = false;

    int value = 0x0000000000000;

    int max = 0xFFFFFFFF;

    while((value & 0xfffffff) < (max & 0xfffffff)){

        System.out.printf("%x\n", value);

        inKey = ByteBuffer.allocate(16).putInt(value).array();

        Object decryptRoundKeys = Rijndael_Algorithm.makeKey (Rijndael_Algorithm.DECRYPT_MODE, inKey);

        for (int i=0; i < numOfCiphertextBlocks - 1; i++) {
            if(i > 1){
                printWriter.println("Key: " + inKey);
                printWriter.println(new String (cleartextBlocks));
            }

            for (int j=0; j < 16; j++) currentDecryptionBlock [j] = cipherText[(i+1)*16 + j]; // Note that the first block is the IV

            byte[] thisDecryptedBlock = Rijndael_Algorithm.blockDecrypt2 (currentDecryptionBlock, 0, decryptRoundKeys);
        
            for (int j=0; j < 16; j++){
                //System.out.println(i*16 + j);

                cleartextBlocks[i*16+j] =  (byte) (thisDecryptedBlock[j] ^ cipherText[i*16 + j]);
                if(cleartextBlocks[i*16+j] < lowerBound || cleartextBlocks[i*16+j] > upperBound){
                    i = numOfCiphertextBlocks + 1;
                    //value += 1;
                    j = 17;
                }
                else {
                    //System.out.print(cleartextBlocks[i*16+j]);

                }
            }

            
        }

        value += 1; 
        //egit = true;

    }


}
}