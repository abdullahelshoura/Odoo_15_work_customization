# Odoo_15_work_customization
Odoo_15_Work_customization

**res_partner_inherit** :
[Purchase >> Order >> Vendor ................ Or........ Sales >> Order >> Customer 
- if i choose company >> create and display 4 char field and must be mandatory with address and tax id >> الرقم التسجيل - الملف الضريبي - طبيعة التعامل - كود المأمورية المختص 
- if i choose individual >> create and display  2 char field and must be mandatory >> (الرقم القومي - ويجب ان يكون 14 رقم وان لا يتكرر ) + طيبعة التعامل

create 2 check box >> customer and vendor 
when i check on vendor create and display  new tab >> named (بيانات المورد ) .. and contain the following char field اسم بنك المورد - عنوان بنك المورد - رقم الحساب - Ibn Number - Swift Number 


 when i check on customer create and display new tab >> named (بيانات العميل ) .. and contain the following field اسم بنك المورد - عنوان بنك المورد - رقم الحساب - Ibn Number - Swift Number ]


**sale_order_inherit** :
add new screen called Maintenance list its inherit sale order view creating different sequence and different in functionality while invoicng as it doesn`t need to make delivery step to create invoice 
and add some new fields in sale order lines 



 **stock_inherit** :
 [
 model=stock.picking >> Inventory >> Configuration >> Operation type >> Receipt >> اذن استلام
Add New Field 
1) Internal Type
2) Work Order
(and in tree can search or group by or filter by them)

in table 
3) quantity on hand >> كمية المنتج في اليد المتاحة في المخزن الذي يتم الاستلام فيه  
4) internal reference  >> come from product.product
5) Note Line >> char field 
  


  model=stock.picking >> Inventory >> Configuration >> Operation type >> Receipt  >> اذن فحص واضافة
1) Add 3 New Field 
- Sales Order >> chose from sales Order Or Maintenance Order 
- Internal Type >> chose from transfer 
- Work Order >> char field 
in table 
New Tab >> named >> Sales Order >> and display product and qty in sales Order لو تم اختيار رقم امر بيع او صيانة في الفيلد الخاص باومر البيع
in table line >> New 3 Field >> 
- Qty on Hand >> الكمية المتاحة من المنتج في المخزن الذي يتم الاستلام فيه  
- internal Reference  .. يأتي من المنتج 
 -Internal Note >> char field


  model=stock.picking >> Inventory >> Configuration >> Operation type >> internal transfer  >>   التحويلات الداخلية واذون التسليم لاوامر الصيانة >>  التحويلات الداخلية واذون التسليم لاوامر الصيانة >> 

1- add new Field >> Contact >> chose from customer 
2- Sales Order >>  يتم اختيار من اوامر البيع او الصيانة الخاصة بالعميل الذي تم اختياره في رقم 1
3- Internal Type >>  يتم اختيار من حركات المخازن الخاصة برقم امر البيع اوا لصيانة الذي تم اختياره في رقم 2 والمحولة الي مخزن الذي تتم منه العملية.. ويتم تسجيل المنتجات المسجلة به تلقائيا في الجدول تحت 
 
]


 **disassemble_stock_screen** :
 [
 create new screen in stock.picking model named Dissasemble it makes the opposite of the operation that done in manufacturing module (mrp)
 it takes a product and separate it to multiple products passing with stock moves cyles
 
