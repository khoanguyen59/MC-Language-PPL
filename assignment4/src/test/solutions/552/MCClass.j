.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_1
	iconst_0
	istore_2
	iload_1
	iload_1
	iconst_3
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	istore_2
	iload_2
	iload_2
	iload_1
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	iload_2
	invokestatic io/putInt(I)V
Label6:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	iload_1
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label7
	iload_2
	invokestatic io/putInt(I)V
	goto Label6
Label7:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_3
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label3
	iconst_0
	istore_2
	iload_2
	iload_2
	iload_1
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label15
	iload_2
	invokestatic io/putInt(I)V
Label14:
	iload_2
	iconst_1
	iadd
	istore_2
	iload_2
	iload_1
	if_icmpge Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label15
	iload_2
	invokestatic io/putInt(I)V
	goto Label14
Label15:
	goto Label2
Label3:
Label1:
	return
.limit stack 30
.limit locals 3
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
