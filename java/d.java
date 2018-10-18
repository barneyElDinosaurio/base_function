import com.google.devtools.build.android.desugar.runtime.ThrowableExtension;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import NumberUtils;

public final class d
{
  public int a;
  int b;
  int c;
  public int d;
  public int e;
  int f;
  int g;
  int h;
  int i;
  int j;
  public int k;
  public int l;
  byte[] m;
  
  public boolean d()
  {
    try
    {
      ByteArrayOutputStream localByteArrayOutputStream = new ByteArrayOutputStream();
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.a, 1, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.b, 1, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.c, 1, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.d, 4, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.e, 1, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.f, 4, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.g, 1, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.h, 4, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.i, 4, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.j, 1, true));
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.k, 4, true));
      this.m = localByteArrayOutputStream.toByteArray();
      this.l = a();
      localByteArrayOutputStream.write(NumberUtils.toBytes(this.l, 2, true));
      this.m = localByteArrayOutputStream.toByteArray();
	  System.out.println('mmmmmm');
	  System.out.println(this.m);
      return true;
    }
    catch (IOException localIOException)
    {
      this.m = null;
    }
    return false;
  }
  
  public final int a()
  {
    int i1 = 0;
    int n = 25;
    for (;;)
    {
      if (n > 1) {
        try
        {
          int i2 = this.m[n];
          i1 += (i2 + 256) % 256;
          n -= 1;
        }
        catch (Throwable localThrowable)
        {
          ThrowableExtension.printStackTrace(localThrowable);
        }
      }
    }
    return i1;
  }
  
  public final void a(byte[] paramArrayOfByte)
  {
    if (d()) {
      System.arraycopy(this.m, 0, paramArrayOfByte, 0, this.m.length);
    }
  }
  
  public final boolean a(byte[] paramArrayOfByte, int paramInt)
  {
    boolean bool2 = false;
    try
    {
      this.m = new byte[paramArrayOfByte.length - paramInt];
      System.arraycopy(paramArrayOfByte, paramInt, this.m, 0, this.m.length);
      paramArrayOfByte = new ByteArrayInputStream(paramArrayOfByte);
      paramArrayOfByte.skip(paramInt);
      this.a = paramArrayOfByte.read();
      this.b = paramArrayOfByte.read();
      this.c = paramArrayOfByte.read();
      byte[] arrayOfByte = new byte[4];
      paramArrayOfByte.read(arrayOfByte);
      this.d = NumberUtils.byte4ToJavaInt(arrayOfByte);
      this.e = paramArrayOfByte.read();
      paramArrayOfByte.read(arrayOfByte);
      this.f = NumberUtils.byte4ToJavaInt(arrayOfByte);
      this.g = paramArrayOfByte.read();
      paramArrayOfByte.read(arrayOfByte);
      this.h = NumberUtils.byte4ToJavaInt(arrayOfByte);
      paramArrayOfByte.read(arrayOfByte);
      this.i = NumberUtils.byte4ToJavaInt(arrayOfByte);
      this.j = paramArrayOfByte.read();
      paramArrayOfByte.read(arrayOfByte);
      this.k = NumberUtils.byte4ToJavaInt(arrayOfByte);
      arrayOfByte = new byte[2];
      paramArrayOfByte.read(arrayOfByte);
      this.l = NumberUtils.byte2ToJavaInt(arrayOfByte);
      boolean bool1 = bool2;
      if (this.a == 119)
      {
        paramInt = this.c;
        bool1 = bool2;
        if ((paramInt & 0x3) != 3) {
          bool1 = true;
        }
      }
      return bool1;
    }
    catch (IOException paramArrayOfByte)
    {
      ThrowableExtension.printStackTrace(paramArrayOfByte);
    }
    return false;
  }
  
  public final boolean b()
  {
    return this.j == 10;
  }
  
  public final void c()
  {
    this.c = ((this.c & 0xCF) + 48);
  }
}