public class NumberUtils
{
	
  
  public static int byte2ToJavaIShort(byte[] paramArrayOfByte)
  {
    return (paramArrayOfByte[0] << 0 & 0xFF) + (0xFF00 & paramArrayOfByte[1] << 8);
  }
  
  public static int byte2ToJavaInt(byte[] paramArrayOfByte)
  {
    return (paramArrayOfByte[1] << 0 & 0xFF) + (0xFF00 & paramArrayOfByte[0] << 8);
  }
  
  public static int byte2ToJavaShort(byte[] paramArrayOfByte)
  {
    return (paramArrayOfByte[1] << 0 & 0xFF) + (0xFF00 & paramArrayOfByte[0] << 8);
  }
  
  public static float byte4ToJavaFloat(byte[] paramArrayOfByte)
  {
    int i = 0;
    int j = 0;
    while (i < 4)
    {
      j |= (paramArrayOfByte[i] & 0xFF) << i * 8;
      i += 1;
    }
    return Assist.intBitsToFloat(j);
  }
  
  public static int byte4ToJavaIInt(byte[] paramArrayOfByte)
  {
    return (0xFF000000 & paramArrayOfByte[3] << 24) + (0xFF0000 & paramArrayOfByte[2] << 16) + (0xFF00 & paramArrayOfByte[1] << 8) + (paramArrayOfByte[0] & 0xFF);
  }
  
  public static int byte4ToJavaInt(byte[] paramArrayOfByte)
  {
    return (0xFF000000 & paramArrayOfByte[0] << 24) + (0xFF0000 & paramArrayOfByte[1] << 16) + (0xFF00 & paramArrayOfByte[2] << 8) + (paramArrayOfByte[3] & 0xFF);
  }
  
  public static double byte8ToJavaDouble(byte[] paramArrayOfByte)
  {
    long l = 0L;
    int i = 0;
    while (i < 8)
    {
      l |= (paramArrayOfByte[i] & 0xFF) << (7 - i) * 8;
      i += 1;
    }
    return Assist.longBitsToDouble(l);
  }
  
  public static double byte8ToJavaDoubleB(byte[] paramArrayOfByte)
  {
    long l = 0L;
    int i = 0;
    while (i < 8)
    {
      l |= (paramArrayOfByte[i] & 0xFF) << i * 8;
      i += 1;
    }
    return Assist.longBitsToDouble(l);
  }
  
  public static long byte8ToJavaILong(byte[] paramArrayOfByte)
  {
    long l = 0L;
    int i = 0;
    while (i < 8)
    {
      l |= (paramArrayOfByte[(7 - i)] & 0xFF) << (7 - i) * 8;
      i += 1;
    }
    return l;
  }
  
  public static long byte8ToJavaLong(byte[] paramArrayOfByte)
  {
    long l = 0L;
    int i = 0;
    while (i < 8)
    {
      l |= (paramArrayOfByte[i] & 0xFF) << (7 - i) * 8;
      i += 1;
    }
    return l;
  }
  
  public static byte[] doubleToBytes(double paramDouble, boolean paramBoolean)
  {
    return toBytes(Assist.doubleToLongBits(paramDouble), 8, paramBoolean);
  }
  
  public static byte[] floatToBytes(float paramFloat, boolean paramBoolean)
  {
    return toBytes(Assist.floatToIntBits(paramFloat), 4, paramBoolean);
  }
  
  public static byte[] toBytes(long paramLong, int paramInt, boolean paramBoolean)
  {
    int i = 0;
    int j = 0;
    byte[] arrayOfByte = new byte[paramInt];
    if (paramBoolean)
    {
      i = j;
      while (i < paramInt)
      {
        arrayOfByte[i] = ((byte)(int)(paramLong >> (paramInt - 1 - i) * 8 & 0xFF));
        i += 1;
      }
    }
    while (i < paramInt)
    {
      arrayOfByte[i] = ((byte)(int)(paramLong >> i * 8 & 0xFF));
      i += 1;
    }
    return arrayOfByte;
  }
  				   
  
}