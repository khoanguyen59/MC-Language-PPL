.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static double()I
.var 0 is a I from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	iload_0
	iconst_2
	imul
	istore_1
	iload_1
	ireturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	iconst_4
	invokestatic MCClass/double()I
	iconst_4
	invokestatic MCClass/double()I
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 5
.limit locals 2
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
