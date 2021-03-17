import java.util.*;
import java.io.*;
public class Compress
{
	
	public static byte createByte(byte i, byte j)
	{
		byte firstNibble = (byte)(i<<4);
		byte secondNibble = j;
		byte finalByte = (byte)(firstNibble | secondNibble);
		
		return finalByte;
	
	}
	public static byte[] extractByte(byte finalByte)
	{
		byte firstNibble, secondNibble;
		byte key[]=new byte[2];
		firstNibble = (byte)((finalByte>>4)&15);
		secondNibble = (byte)(finalByte & 15);
		key[0]=firstNibble;
		key[1]=secondNibble;
		return key;
		
	}

	public static long compress() throws Exception
	{
		int even=0;
		Scanner input=new Scanner(new File("TATEnc.txt"));
		input.useDelimiter(" +"); //delimitor is one or more spaces
		ArrayList<Byte> byteStream = new ArrayList();	
		byte byteFilled = (byte)0b00000000;
		byte[] currentByte={(byte)0b11101110, (byte)0b11101110};
		final long startTime = System.currentTimeMillis();
		while(input.hasNext())
		{
  			String s = input.next();
			if(s.length()>1)
			{
				if(s.charAt(0)=='0'&&s.charAt(1)=='0')
				{
					StringBuilder sb = new StringBuilder(s);
					sb.deleteCharAt(0);
					s = sb.toString();
				}
			}
			if(s.length()%2==0)
			{
				even = (even+1)%2;
				if(even==0)
				{
					byte k = createByte(currentByte[0], currentByte[1]);
					byteStream.add(k);
				}
			}
			System.out.println(s);
			System.out.println(even);
			for (int i = 0; i < s.length(); i++)  
        		{
				if(i%2==0)
				{
					currentByte[0]=(byte)Character.getNumericValue(s.charAt(i));
					if((i+1)<s.length())
					{
						currentByte[1]=(byte)Character.getNumericValue(s.charAt(i+1));
					}
					System.out.println(currentByte[0]+"  "+currentByte[1]);
					System.out.println(" ");
					System.out.println(" ");
					byte k = createByte(currentByte[0], currentByte[1]);
					byteStream.add(k);
				}
			} 

		}
		FileOutputStream fos = new FileOutputStream(new File("Compress"));
		for(byte b:byteStream)
		{
			fos.write((byte)b);
			//System.out.println((char)b);	
		}
		final long endTime = System.currentTimeMillis();
		System.out.println("Sized of Compressed XML without backend: "+byteStream.size());	
                return  (endTime - startTime);

	}
	public static void main(String[] args) throws Exception
	{
		compress();
	}

}
