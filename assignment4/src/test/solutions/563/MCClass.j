.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
	iload_1
	iload_1
	iconst_4
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	goto Label2
	iload_1
	invokestatic io/putInt(I)V
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_4
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	goto Label2
	iload_1
	invokestatic io/putInt(I)V
	goto Label2
Label3:
Label1:
	return
.limit stack 10
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
