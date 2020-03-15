.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_3
	putstatic MCClass/a I
.var 1 is b I from Label0 to Label1
	iconst_2
	istore_1
	getstatic MCClass/a I
	iload_1
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	getstatic MCClass/a I
	iconst_3
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label8
	getstatic MCClass/a I
	invokestatic io/putInt(I)V
Label8:
	goto Label5
Label4:
	iload_1
	invokestatic io/putInt(I)V
Label5:
Label1:
	return
.limit stack 9
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
