# Sharma Tent House Management System

# 1. Three-Sentence Specification

The program I am building will help Sharma Tent House manage bookings, customers, rental items, payments, deliveries, returns, and damaged items using one computer system instead of handwritten records.  

The main users of this system will be Rakesh ji and Ankit because both of them manage bookings and inventory, but Rakesh ji may focus more on payments and customer handling while Ankit may focus more on delivery and item management.  

 project will be considered complete if the system can correctly store bookings, prevent basic overbooking mistakes, track item movement, and keep all business records saved properly.


# 2. The Information Your Program Must Remember

After carefully reading the full story, I understood that Sharma Tent House does not only rent chairs and tables. The business actually manages :- customers, event schedules, booking overlap, delivery timing, damaged items, deposits, missing items, and payment tracking together. Because of this, I divided the information into different groups instead of storing everything in one place.

## A. Customer Information

This section stores all customer-related details 

1. customer_id :- string , Required 
2. customer_name :- string , Required 
3. phone_number :- string , Required 
4. address :- string , Optional 
5. customer_notes :- string , Optional 
6. total_previous_bookings :- integer ,   Optional 

### Why I included these fields:
- Phone number is important because many customers may have similar names during wedding season.
- Customer notes are useful because Rakesh ji sometimes trusts old customers and allows balance payment after the event.ike he give discount to his father's friend as mentioned in story
- Previous booking count can help identify regular customers.

### Example:
Agarwal family from Talwandi may already have booked items many times before, so the system should remember their history.

---

## B. Item Information

This section stores all rental items available in the tent house.

1. item_id - string , Required 
2. item_name - string , Required 
3. category - string , Required  
4. tracking_type - string , Required  
5. total_quantity - integer , Required  
6. rental_price_per_day - float , Required  
7. damage_charge - float , Optional  
8. late_fee_per_day - float , Required  
9. item_condition - string , Required

I separated category and tracking_type because both solve different problems in the system.  

Category tells what kind of item it is from a business perspective, like seating, lighting, decoration, cooking equipment, or sound systems.  

Tracking type tells how the system should manage booking rules and availability for that item.  

For example:
- Plastic chairs may use bulk_quantity tracking because only total quantity matters.
- LED walls or VIP sofa sets may use unique_item tracking because the same exact unit cannot be booked for two functions on the same date.
- Gas burners or coolers may use limited_count tracking because only a few units exist and overlapping bookings must be checked carefully.

I first thought of storing available_quantity directly inside the item information, but after thinking more carefully, I realized availability changes depending on booking dates and overlapping bookings.  

For example, Sharma Tent House may have 500 total chairs, but only 200 may be free on a particular wedding date because other bookings may already reserve the remaining stock for overlapping days.  

Because of this, I think availability should be calculated dynamically by checking active bookings for the requested dates instead of storing a fixed available_quantity value permanently inside the item record.
---

## C. Booking Information

This section stores complete event booking details.


1. booking_id - string , Required 
2. customer_id  - string , Required 
3. event_name - string , Required 
4. event_location - string , Required 
5. event_date - date , Required  
6. item_dispatch_date - date , Required  
7. expected_return_date - date , Required
8. booking_status - string , Required 
9. deposit_amount - float , Required 
10. total_amount - float , Required 
11. amount_paid - float , Required 
12. remaining_balance - float , Required  
13. missing_item_deduction_amount - float , Optional  
14. refund_amount - float , Optional  
15. extra_amount_due - float , Optional  
16. final_payment_status - string , Optional

I first thought booking dates and event dates were the same thing, but after thinking about real tent house operations, I realized items usually leave the shop before the actual function and return after the event ends.  

Because of this, availability checking should use the full item movement period instead of only the wedding or event date.  

For example, if a wedding happens on 18th November, chairs may leave the shop on 17th November and return on 20th November, so those chairs should not appear available during that entire period.


I realized the booking payment process is not only about taking advance payment and final payment. After the event finishes, the system also needs to handle deposit deductions for damaged or missing items and decide whether money should be refunded to the customer or additional payment is still pending.  

For example, if the remaining deposit amount is still positive after all deductions, the system should calculate a refund amount for the customer. If deductions become greater than the deposit amount, the system should store the extra amount still owed by the customer.  

The final_payment_status field will help the system identify whether the booking is fully settled, refund pending, or payment still due.

## D. Booking Item Information

This section stores item-wise details connected to bookings.

1. booking_item_id - string , Required 
2. booking_id - string , Required 
3. item_id - string , Required 
4. quantity_booked - integer , Required 
5. price_per_day - float , Required 
6. discount_percentage - float , Optional  
7. final_price_per_day - float , Required  
8. total_item_cost - float , Required 
9. quantity_returned - integer , Optional  
10. damaged_quantity - integer , Optional  
11. missing_quantity - integer , Optional  
12. item_return_status - string , Optional

### Why I separated this section:
One booking contains many different rental items, so storing all items inside the main booking record may become complex so i save items of each booking separately

I also moved return and damage tracking closer to booking items because one booking can contain many different items, and different items may return in different conditions.  

For example, all chairs may return safely while some tables may return damaged or some coolers may still be missing.

I realized damage information should not be stored separately in multiple places because that may create inconsistent records if one section gets updated and another does not.  

Because of this, item-wise damaged quantities are treated as the main damage record, while damage descriptions are only used for additional notes and explanations.

I realized item pricing may not always stay fixed because Rakesh ji sometimes gives discounts to regular customers or family connections.  

Because of this, the system should store both the original item price and the final negotiated item price used in that booking. This will help the program correctly calculate booking totals while still keeping a record of discounts.

### Example:
Booking B301 may contain:
- 200 chairs
- 100 plates
- 4 burners
- 1 sofa set

## E. Delivery, Return, and Damage Information

This section stores all information related to item delivery, return events, damaged items, missing items, and late returns.

I first thought one booking would have only one final return date, but after thinking about real tent house operations, I realized items may return in multiple parts on different days.  

For example, most chairs may return on time while a few remaining chairs may return two days later. Because of this, the system should support multiple return events instead of storing only one final return record for the whole booking.

1. record_id - string , Required  
2. booking_id - string , Required  
3. delivery_date - date , Required  
4. return_event_date - date , Required  
5. returned_item_id - string , Required  
6. returned_quantity - integer , Required  
7. return_status - string , Required  
8. late_return_days - integer , Optional  
9. delivery_status - string , Required  
10. damage_description - string , Required  
11. deduction_amount - float , Optional  
12. return_notes - string , Optional  

### Example:
For one wedding booking:
- 200 chairs were delivered
- 198 chairs returned on 20th November
- remaining 2 chairs returned on 22nd November
- 2 chairs were damaged during the event
- system calculated separate late return days for the delayed items

## F. Payment Information

This section stores all payment transactions connected to bookings because customers may pay in multiple parts during different stages of the event process.

1. payment_id - string , Required  
2. booking_id - string , Required  
3. payment_date - date , Required  
4. payment_amount - float , Required  
5. payment_method - string , Required  
6. payment_type - string , Required  
7. payment_notes - string , Optional

### Example:
One booking payment history may contain:
- ₹10,000 advance payment on booking date
- ₹20,000 payment during item delivery
- ₹15,000 final payment after event completion

Because of this, the system should store each payment separately instead of only maintaining one total paid amount.
# 3. How Your Groupings Connect To Each Other

All sections in this system are connected  

First, a customer contacts Sharma Tent House for a function like a wedding, engagement, birthday, or other events. After that, a booking is created for that customer. 
event<->booking record

Inside one booking, many different items can be added like chairs, tables, fans, burners, sound systems, and decoration items. Because of this
bokking records<-> item records 

The item section is important because before confirming any booking, the system must check whether enough items are available on those dates or not.
items<->available items  

After booking is confirm,  delivery information becomes connected because items are sent to the event location before the function starts.  
items<->deliverd items

Once the event finishes, return details become important because the system needs to know:
- which items came back,
- which items are still missing,
- and whether any item was damaged.
item<-> return items,damage items,missing items 

Customer details are connected with bookings
customer details<-> booking records

All these sections work together. If even one section is disconnected, the system may create booking mistakes, stock calculation errors, or payment confusion.

# 4. File Structure

I decided to use multiple JSON files instead of one large file because different types of information should stay separated and easier to update.

If everything is stored in one file, it may become difficult to search and update records during peak wedding season when many bookings happen together.

The files will connect using IDs like customer_id, booking_id, and item_id.

---

## customers.json

```json
[
  {
    "customer_id": "C101",
    "customer_name": "Amit Agarwal",
    "phone_number": "9876543210",
    "address": "Talwandi, Kota",
    "customer_notes": "Regular customer from past 5 years",
    "total_previous_bookings": 4
  },
  {
    "customer_id": "C102",
    "customer_name": "Rohit Mehta",
    "phone_number": "9829034567",
    "address": "Vigyan Nagar, Kota",
    "customer_notes": "Balance payment delayed once",
    "total_previous_bookings": 2
  }
]
```

# 5. Operations

1. rakesh ji  adds  new customer
 → system stores customer details 
 → system shows confirmation message.  

2. rakesh ji  creates a new booking
 → system checks item availability 
 → system confirms booking if particular items are  available.  

3. User tries to book more chairs than available stock → system blocks booking 
→ system shows enough quantity is not avaiable.  

4. User adds extra items to an existing booking
 → system recalculates total amount 
 → system shows updated bill.  

5. User removes items from booking
 → system reduce total amount 
 → system shoe message of updated amount, 

6. User changes booking dates 
→ system checks overlapping bookings 
→ system show msg of booking is confirmed or not

7. User cancels a booking 
→ system restores reserved inventory 
→ system marks booking as cancelled.  

8. User checks item availability for a specific date
 → system compares active bookings 
→ system shows available items.  

9. User give deposit payment 
→ system updates payment details
 → system shows remaining balance.  

10. User give final payment
 → system updates booking balance 
 → system marks payment completed.  

11. User marks booking items as delivered 
→ system updates delivery status
 → system stores delivery details.  

12. User checks today’s collections
 → system shows pending returns
→ system displays pickup schedules.  

13. User retrun item
 → system updates available stock 
 → system checks pending items.  

14. User return partail means half items → system keeps booking active → system shows missing quantity.  

15. User records damaged items → system calculates damage deduction → system updates damage records.  

16. User records missing items → system deducts amount from deposit → system updates refund amount.  

17. User closes booking → system verifies all items are returned → system marks booking completed.  

18. User searches customer history → system shows old bookings and payment history.  

19. User checks monthly damage report → system calculates total losses → system shows damage summary.  

---

# 6.  Things That Can Go Wrong

1. JSON file does not exist when the program starts → system automatically creates empty JSON files for first-time setup.


2. User enters negative quantity while booking → system rejects invalid input and asks again.  

3. Customer tries to book 250 chairs when only 220 are available → system blocks booking and shows remaining stock.  

4. Same LED wall gets booked for two functions on the same date → system prevents double booking.  

5. User enters invalid date format → system rejects the input and shows the correct date format example. 

6. User tries to return more items than originally booked → system rejects return entry.  

7. User closes booking before all items are returned → system prevents booking completion.  

8. Customer damages items whose cost becomes greater than deposit amount → system shows remaining pending payment.  

9. User creates duplicate customer using same phone number → system shows duplicate customer warning.  

10. Booking is modified after items are already delivered → system asks for confirmation before updating records.  

11. Customer returns items late after the function → system calculates late return charges automatically and updates the remaining balance..  

12. User tries deleting inventory item connected with active bookings → system blocks deletion request.  


13. User searches booking that does not exist → system shows “Booking Not Found” message.  

14. Customer cancels function after items already left the shop → system keeps cancellation pending for manual approval.  

15. User enters text instead of numeric quantity → system rejects invalid input and asks again.  

16. Multiple wedding bookings happen on the same day → system carefully checks stock before confirming new booking.  

17. Some items return damaged and some missing together → system calculates both damage charges and missing charges separately.  

18. Customer argues that deposit amount was different → system shows stored payment history and booking records.  


# 7. One Thing I Don’t Know Yet

One thing I still need to understand properly is how to manage item availability when many bookings overlap together during wedding season and some customers return items late.  

For example, if 200 chairs are booked for one wedding and another customer asks for chairs on nearby dates, the system should correctly calculate how many chairs are actually free at that time.  

To understand this better, I started thinking about real overlapping booking situations manually before designing the final logic.  

For example, if Sharma Tent House has 500 chairs in total and four different bookings already reserve chairs across overlapping dates, the system should calculate the total reserved quantity for each specific day before confirming a new booking.  

If 450 chairs are already reserved on 12th November across multiple active bookings, the system should understand that only 50 chairs are still free on that date even if total stock is 500.  

I think solving these examples manually first will help me design better availability checking logic and booking data structures before starting implementation.

I also realized I should test the availability logic using small manual examples before implementation.  

For example, if total chair quantity is 500 and existing bookings already reserve 200 chairs, 150 chairs, and 100 chairs on the same date, then the availability checking logic should return only 50 available chairs for that date.  

To verify the logic later in code, I would give the function the booking dates, reserved quantities, and total stock quantity as input, and then check whether the function correctly calculates the remaining available quantity.

