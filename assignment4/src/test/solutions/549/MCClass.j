.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
	iconst_3
	invokestatic io/putInt(I)V
	ldc "negative"
	invokestatic io/putString(Ljava/lang/String;)V
Label4:
	iload_1
	iconst_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	ldc "negative"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label4
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
Label2:
	iload_1
	iconst_3
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label3
	iconst_3
	invokestatic io/putInt(I)V
	ldc "negative"
	invokestatic io/putString(Ljava/lang/String;)V
Label10:
	iload_1
	iconst_0
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label11
	ldc "negative"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label10
Label11:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label1:
	return
.limit stack 13
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
