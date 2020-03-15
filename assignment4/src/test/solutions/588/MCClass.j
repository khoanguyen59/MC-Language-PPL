.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static i I

.method public static f()I
Label0:
	sipush 200
	ireturn
Label1:
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is main I from Label0 to Label1
	invokestatic MCClass/f()I
	invokestatic MCClass/f()I
	iload_1
	invokestatic io/putIntLn(I)V
.var 2 is i I from Label0 to Label1
.var 3 is main I from Label0 to Label1
.var 4 is f I from Label0 to Label1
	bipush 100
	istore_1
	bipush 100
	putstatic MCClass/f ()I
	bipush 100
	putstatic MCClass/i I
	getstatic MCClass/i I
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
	getstatic MCClass/f ()I
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 9
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
