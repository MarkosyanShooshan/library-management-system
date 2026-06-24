 Library Management System 

[Armenian] Սա Օբյեկտային Կողմնորոշված Ծրագրավորման (**OOP**) սկզբունքներով գրված պարզ համակարգ է Python
լեզվով, որը նախատեսված է գրադարանի գրքերը կառավարելու համար: Նախագիծը ցուցադրում է դասերի (Classes), 
օբյեկտների (Objects) և մեթոդների (Methods) ճիշտ համագործակցությունը, ինչպես նաև օբյեկտի վիճակի (state)
փոփոխությունը:

[English] This is a simple Library Management System built in Python, showcasing the core principles of 
Object-Oriented Programming (**OOP**). The project demonstrates how classes, objects, and methods interact
with each other to manage a book inventory, track availability states, and handle check-out/check-in 
operations.



Features

․Գրքերի ավելացում (Add Books): Հնարավորություն է տալիս գրադարանի ցուցակում ավելացնել նոր գրքեր 
(վերնագրով և հեղինակով):
․Հասանելիության վերահսկում (Availability Tracking): Յուրաքանչյուր գիրք ունի իր կարգավիճակը
(Available / Checked out):
․Գրքի հանձնում/վերցնում (Check-out & Check-in):Ծրագիրը վավերացնում է գործողությունները՝
թույլ չտալով վերցնել արդեն վերցված գիրքը կամ վերադարձնել գրադարանում արդեն առկա գիրքը:
․Գրացուցակի ցուցադրում (Inventory Display): Մեկ հրամանով ցուցադրում է գրադարանի բոլոր գրքերի
ամբողջական տեղեկատվությունը կոկիկ ձևավորմամբ:



OOP Կառուցվածքը / OOP Architecture
Նախագիծը բաղկացած է երկու հիմնական դասերից (Classes).

1. Book Class:
    Attributes:
    title` (վերնագիր),
    author` (հեղինակ),
    available` (հասանելիություն):
    
   Methods:
   display_info(),
   checkout()` (վերցնել գիրքը),
   checkin()` (վերադարձնել գիրքը):
   
2. Library Class:
   Attributes:
   books` (գրքերի ցուցակ):
   
   Methods:
   add_book()` (ավելացնել գիրք),
   display_books()` (ցուցադրել բոլոր գրքերը):
