.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo()I
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is c Ljava/lang/String; from Label0 to Label1
Label0:
	aload_2
	invokestatic io/putString(Ljava/lang/String;)V
	iload_0
	i2f
	fload_1
	fadd
	ireturn
Label1:
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ldc 1.5
	ldc "Tong: "
	invokestatic MCClass/foo()I
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 4
.limit locals 1
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
