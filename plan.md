# Sharma Tent House Management System

# 1. Three-Sentence Specification

THE program  I bulit will help Rakesh ji Owner of Sharma Tent House manage all bookings, rental items, customer details, payments, deliveries, returns, and damaged items from one computer system instead of maintaining everything in a handwritten ledger.  

the user of this system will be Rakesh ji and Ankit because both of them run tent house . they need only single computer program  

at the end of this project the system can do following things:-
correctly save all booking
stop overbooking mistakes
track avaliable item
calculate payments and damages properly
keep all information stored permanently 

# 2. The Information Your Program Must Remember

After carefully reading the full story, I understood that Sharma Tent House does not only rent chairs and tables. The business actually manages :- customers, event schedules, booking overlap, delivery timing, damaged items, deposits, missing items, and payment tracking together. Because of this, I divided the information into different groups instead of storing everything in one place.

---

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
4. item_type - string , Required 
5. total_quantity - integer ,Required 
6. available_quantity - integer , Required 
7. rental_price_per_day - float , Required 
8. damage_charge - float , Optional 
9. late_fee_per_day - float , Required
10. item_condition - string , Required

For example:
- Chairs are bulk items because only quantity matters.
- LED walls are unique items because exact unit tracking matters.
- Gas burners are limited-count items because only a few are available.

If one LED wall is already booked for a function in Mahaveer Nagar, the same LED wall cannot be booked again for another event on the same date.

---

## C. Booking Information

This section stores complete event booking details.


1. booking_id - string , Required 
2. customer_id  - string , Required 
3. event_name - string , Required 
4. event_location - string , Required 
5. booking_start_date - date , Required 
6. booking_end_date - date , Required 
7. booking_status - string , Required 
8. deposit_amount - float , Required 
9. total_amount - float , Required 
10. amount_paid - float , Required 
11. remaining_balance - float , Required 


- Booking dates are necessary because multiple events happen together during wedding season.
- Deposit amount is important because damages and missing items are adjusted from it.
- Booking status helps manage cancelled, completed, or active bookings.


## D. Booking Item Information

This section stores item-wise details connected to bookings.

1. booking_item_id - string , Required 
2. booking_id - string , Required 
3. item_id - string , Required 
4. quantity_booked - integer , Required 
5. price_per_day - float , Required 
6. total_item_cost - float , Required 

### Why I separated this section:
One booking contains many different rental items, so storing all items inside the main booking record may become complex so i save items of each booking separately

### Example:
Booking B301 may contain:
- 200 chairs
- 100 plates
- 4 burners
- 1 sofa set

## E. Delivery, Return, and Damage Information

This section stores all information related to item delivery, item returns, missing items, damaged items

1. record_id - string , Required 
2. booking_id - string , Required 
3. delivery_date - date , Required 
4. expected_return_date , date , Required 
5. actual_return_date - date , Required 
6. delivery_status - string , Required 
7. returned_quantity - integer , Required 
8. missing_quantity - integer , Required 
9. damaged_quantity - integer , Required 
10. damage_description - string , Required 
11. late_return_days - integer , Required 
12. deduction_amount - float , Optional 
13. return_notes - string , Optional 

### Example:
For one wedding booking:
- 200 chairs were delivered
- only 198 chairs returned
- 2 chairs were damaged
- return happened 1 day late

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

All these sections work together. If even one section is disconnected, the system may may cuases errors

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

##  Things That Can Go Wrong

1. JSON file does not exist when the program starts 

2. User enters negative quantity while booking → system rejects invalid input and asks again.  

3. Customer tries to book 250 chairs when only 220 are available → system blocks booking and shows remaining stock.  

4. Same LED wall gets booked for two functions on the same date → system prevents double booking.  

5. User enters invalid date format → system shows correct date format example.  

6. User tries to return more items than originally booked → system rejects return entry.  

7. User closes booking before all items are returned → system prevents booking completion.  

8. Customer damages items whose cost becomes greater than deposit amount → system shows remaining pending payment.  

9. User creates duplicate customer using same phone number → system shows duplicate customer warning.  

10. Booking is modified after items are already delivered → system asks for confirmation before updating records.  

11. Customer returns items late after function → system automatically adds late return charges.  

12. User tries deleting inventory item connected with active bookings → system blocks deletion request.  


14. User searches booking that does not exist → system shows “Booking Not Found” message.  

15. Customer cancels function after items already left the shop → system keeps cancellation pending for manual approval.  

16. User enters text instead of numeric quantity → system rejects invalid input and asks again.  

17. Multiple wedding bookings happen on the same day → system carefully checks stock before confirming new booking.  

18. Some items return damaged and some missing together → system calculates both damage charges and missing charges separately.  

19. Customer argues that deposit amount was different → system shows stored payment history and booking records.  


# 7. One Thing I Don’t Know Yet

One thing I still need to understand properly is how to manage item availability when many bookings overlap together during wedding season and some customers return items late.  

For example, if 200 chairs are booked for one wedding and another customer asks for chairs on nearby dates, the system should correctly calculate how many chairs are actually free at that time.  


