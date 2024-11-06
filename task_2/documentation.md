# **BookMaster Application Documentation**

## **1. Introduction**

### **1.1 Purpose**

The purpose of this document is to provide a detailed description of the **BookMaster** online bookstore application. It outlines the system's architecture, features, functionalities, and requirements, serving as a guide for the development team, stakeholders, and any party involved in the project lifecycle.

### **1.2 Scope**

This documentation covers all aspects of the BookMaster application, including:

- Functional and non-functional requirements
- System architecture and design
- Data models and database design
- External interfaces and integrations
- Security considerations
- Performance requirements
- User interface design
- Future enhancements

### **1.3 Audience**

This document is intended for:

- Software Developers
- System Architects
- Quality Assurance Engineers
- Project Managers
- DevOps Engineers
- Stakeholders and Clients

## **2. Overall Description**

### **2.1 Product Perspective**

**BookMaster** is a standalone web-based application that operates as an online bookstore. It interfaces with external systems such as payment gateways and email services. The system is designed to be scalable, secure, and user-friendly, providing an efficient platform for purchasing books online.

### **2.2 Product Functions**

- User Registration and Authentication
- Book Catalog Browsing and Searching
- Shopping Cart Management
- Secure Checkout and Payment Processing
- Order Management
- User Profile Management
- Wishlist Functionality _(New Feature)_
- Search Autocomplete _(Enhancement)_
- Reviews and Ratings _(Planned Feature)_

### **2.3 User Classes and Characteristics**

- **Visitors:** Can browse the catalog and search for books without logging in.
- **Registered Users:** Can make purchases, manage profiles, view order history, and create wishlists.
- **Administrators:** Manage inventory, user accounts, orders, and system settings.

### **2.4 Operating Environment**

- **Client Side:**
  - Web Browsers: Chrome, Firefox, Safari, Edge
  - Devices: Desktop, Laptop, Tablet, Mobile (Responsive Design)
- **Server Side:**
  - Operating System: Linux (Ubuntu 20.04 LTS)
  - Web Server: Nginx
  - Application Server: Node.js (v14.x) with Express.js
  - Database Server: PostgreSQL (v12.x)
  - Programming Languages: JavaScript (ES6+), HTML5, CSS3
- **External Services:**
  - Payment Gateways: Stripe API
  - Email Services: SendGrid API
  - Cloud Hosting: AWS EC2 Instances
  - Content Delivery Network (CDN): Amazon CloudFront

### **2.5 Design and Implementation Constraints**

- Compliance with PCI DSS standards for payment processing.
- Adherence to GDPR for data privacy.
- Use of standard web technologies for maximum compatibility.
- System must be scalable to handle increased load.
- Responsive design for accessibility on various devices.

### **2.6 Assumptions and Dependencies**

- Users have access to the internet and a modern web browser.
- External services (payment gateway, email service) are operational.
- The database server is highly available and secure.
- Clients will provide necessary content (e.g., book descriptions, images).

## **3. System Features**

### **3.1 User Registration and Authentication**

#### **3.1.1 Description**

Provides secure registration and authentication mechanisms for users to access personalized features.

#### **3.1.2 Functional Requirements**

- **FR-1:** Users shall be able to register by providing a unique username, valid email address, and password.
- **FR-2:** The system shall send an account activation email upon registration.
- **FR-3:** Users shall be able to log in using their email/username and password.
- **FR-4:** The system shall provide functionality to reset passwords via email verification.
- **FR-5:** Users shall be able to update their passwords after logging in.

#### **3.1.3 Non-Functional Requirements**

- **NFR-1:** Passwords shall be hashed using a strong algorithm (e.g., bcrypt with a sufficient cost factor).
- **NFR-2:** Authentication responses shall be provided within 2 seconds.
- **NFR-3:** The system shall implement account lockout after 5 failed login attempts within 15 minutes.
- **NFR-4:** Registration and login pages shall be protected against automated bots using reCAPTCHA.

### **3.2 User Profile Management**

#### **3.2.1 Description**

Allows users to manage their personal information and preferences.

#### **3.2.2 Functional Requirements**

- **FR-6:** Users shall be able to view and edit their personal information, including name, email, and contact details.
- **FR-7:** Users shall be able to upload and update their profile picture. _(Bug fix required)_
- **FR-8:** Users shall be able to manage their shipping addresses.
- **FR-9:** Users shall view their order history with details such as order date, items purchased, and order status.

#### **3.2.3 Non-Functional Requirements**

- **NFR-5:** Changes to profile information shall be saved within 1 second.
- **NFR-6:** The system shall validate all inputs for proper format and content.

### **3.3 Book Catalog Browsing**

#### **3.3.1 Description**

Enables users to explore and discover books through various browsing options.

#### **3.3.2 Functional Requirements**

- **FR-10:** Users shall be able to browse books by categories such as genre, author, bestseller lists, and new arrivals.
- **FR-11:** The system shall display book details including title, author, ISBN, price, availability, synopsis, and cover image.
- **FR-12:** Users shall be able to filter books based on criteria like price range, language, publication date, and rating.

#### **3.3.3 Non-Functional Requirements**

- **NFR-7:** Book catalog pages shall load within 3 seconds.
- **NFR-8:** The system shall support high-resolution images without significant performance degradation.

### **3.4 Search Functionality**

#### **3.4.1 Description**

Allows users to search for books using a robust search engine.

#### **3.4.2 Functional Requirements**

- **FR-13:** Users shall be able to search for books using keywords related to title, author, or ISBN.
- **FR-14:** The system shall provide search autocomplete suggestions as users type. _(Enhancement requested)_
- **FR-15:** Advanced search options shall be available for more precise results.

#### **3.4.3 Non-Functional Requirements**

- **NFR-9:** Search queries shall return results within 2 seconds.
- **NFR-10:** The search engine shall be capable of handling at least 100 queries per second.

### **3.5 Shopping Cart**

#### **3.5.1 Description**

Facilitates the collection of items the user intends to purchase.

#### **3.5.2 Functional Requirements**

- **FR-16:** Users shall be able to add books to the shopping cart from the product listing or detail pages.
- **FR-17:** Users shall be able to view the contents of their shopping cart at any time.
- **FR-18:** Users shall be able to modify quantities or remove items from the cart.
- **FR-19:** The system shall calculate and display the subtotal, tax, and total amounts.

#### **3.5.3 Non-Functional Requirements**

- **NFR-11:** The shopping cart shall be persistent, saving items even if the user logs out or closes the browser.
- **NFR-12:** Updates to the cart shall reflect immediately without requiring a page refresh (AJAX implementation).

### **3.6 Checkout Process**

#### **3.6.1 Description**

Manages the completion of purchases securely and efficiently.

#### **3.6.2 Functional Requirements**

- **FR-20:** The system shall guide users through a multi-step checkout process: Review Cart, Shipping Information, Payment Information, Order Confirmation.
- **FR-21:** Users shall be able to select or enter a shipping address.
- **FR-22:** The system shall process payments through an integrated payment gateway (e.g., Stripe).
- **FR-23:** An order confirmation shall be displayed upon successful payment, and an email receipt shall be sent.

#### **3.6.3 Non-Functional Requirements**

- **NFR-13:** All payment transactions shall occur over HTTPS with SSL encryption.
- **NFR-14:** Payment processing shall comply with PCI DSS regulations.
- **NFR-15:** The checkout process shall be optimized to prevent abandonment, with page loads under 2 seconds.

### **3.7 Order Management**

#### **3.7.1 Description**

Allows users to manage their orders post-purchase.

#### **3.7.2 Functional Requirements**

- **FR-24:** Users shall be able to view past orders with details including items purchased, prices, and shipping information.
- **FR-25:** The system shall allow users to track the shipping status of their orders.
- **FR-26:** Users shall be able to request returns or exchanges within a specified period.

#### **3.7.3 Non-Functional Requirements**

- **NFR-16:** Order history pages shall load within 2 seconds.
- **NFR-17:** Order data shall be retained for at least 2 years.

### **3.8 Wishlist Functionality** _(New Feature Requested)_

#### **3.8.1 Description**

Enables users to save books they are interested in purchasing later.

#### **3.8.2 Functional Requirements**

- **FR-27:** Users shall be able to add books to their wishlist from the product detail page.
- **FR-28:** Users shall be able to view, manage, and remove items from their wishlist.
- **FR-29:** The system shall notify users of promotions or price changes for items on their wishlist.

#### **3.8.3 Non-Functional Requirements**

- **NFR-18:** The wishlist shall support up to 100 items per user.
- **NFR-19:** Changes to the wishlist shall be reflected in real-time.

### **3.9 Reviews and Ratings** _(Planned Feature)_

#### **3.9.1 Description**

Allows users to provide feedback on books, enhancing community interaction.

#### **3.9.2 Functional Requirements**

- **FR-30:** Users shall be able to rate books on a scale of 1 to 5 stars.
- **FR-31:** Users shall be able to write and submit reviews.
- **FR-32:** The system shall display average ratings and reviews on book detail pages.
- **FR-33:** Administrators shall be able to moderate reviews for inappropriate content.

#### **3.9.3 Non-Functional Requirements**

- **NFR-20:** User-submitted reviews shall be processed within 5 seconds.
- **NFR-21:** The system shall implement anti-spam measures to prevent fraudulent reviews.

### **3.10 Administration Module**

#### **3.10.1 Description**

Provides tools for administrators to manage the system effectively.

#### **3.10.2 Functional Requirements**

- **FR-34:** Administrators shall be able to manage the book catalog (add, update, delete books).
- **FR-35:** Administrators shall be able to manage user accounts.
- **FR-36:** The system shall provide sales reports and analytics.
- **FR-37:** Administrators shall be able to configure system settings and promotional offers.

#### **3.10.3 Non-Functional Requirements**

- **NFR-22:** Administrative actions shall be logged for security auditing.
- **NFR-23:** The administration module shall be accessible only to authorized personnel.

### **3.11 Bug Fix: Profile Picture Update Issue**

#### **3.11.1 Description**

Resolve an issue preventing users from updating their profile picture.

#### **3.11.2 Functional Requirements**

- **FR-38:** Users shall be able to successfully upload and update their profile pictures.
- **FR-39:** The system shall validate the image file format and size before uploading.
- **FR-40:** An appropriate error message shall be displayed if the upload fails.

#### **3.11.3 Non-Functional Requirements**

- **NFR-24:** Supported image formats include JPEG, PNG, and GIF.
- **NFR-25:** Maximum allowed image size is 2MB.
- **NFR-26:** The profile picture update process shall complete within 3 seconds.

## **4. External Interface Requirements**

### **4.1 User Interfaces**

- **UI-1:** Responsive and intuitive web interface accessible from modern browsers.
- **UI-2:** Consistent design language and branding throughout the application.
- **UI-3:** Accessible design compliant with WCAG 2.1 Level AA standards.
- **UI-4:** Support for internationalization and localization (multi-language support).

### **4.2 Hardware Interfaces**

Not applicable. BookMaster is a web-based application with no direct hardware interfaces.

### **4.3 Software Interfaces**

- **SI-1:** Integration with Stripe API for payment processing.
- **SI-2:** Integration with SendGrid API for sending emails.
- **SI-3:** RESTful APIs for frontend-backend communication.
- **SI-4:** Integration with third-party book data sources (e.g., ISBNdb).

### **4.4 Communications Interfaces**

- **CI-1:** All communications between client and server shall use HTTPS.
- **CI-2:** WebSocket connections may be used for real-time features (e.g., notifications).

## **5. System Architecture**

### **5.1 Overview**

The system follows a modular, layered architecture to enhance scalability and maintainability, consisting of:

- **Presentation Layer:** Client-side code (HTML, CSS, JavaScript) rendered in the user's browser.
- **Application Layer:** Server-side code handling business logic, built with Node.js and Express.js.
- **Data Layer:** Database using PostgreSQL, handling data storage and retrieval.
- **Integration Layer:** Interfaces with external services (payment gateway, email services).

### **5.2 Architectural Components**

- **Frontend Framework:** React.js for building interactive user interfaces.
- **Backend Framework:** Express.js for server-side application logic.
- **Database:** PostgreSQL with Sequelize ORM for data modeling.
- **Caching:** Redis for session management and caching frequently accessed data.
- **APIs:** RESTful APIs adhering to standard HTTP methods and status codes.
- **Authentication:** JSON Web Tokens (JWT) for stateless authentication.

### **5.3 Deployment Architecture**

- **Hosting:** AWS EC2 instances for application servers.
- **Load Balancing:** AWS Elastic Load Balancing (ELB) to distribute incoming traffic.
- **Scalability:** Auto-scaling groups to adjust resources based on demand.
- **Data Storage:** Amazon RDS for the PostgreSQL database.
- **Static Assets:** Amazon S3 and CloudFront for serving static content.

## **6. Data Model and Database Design**

### **6.1 Entity-Relationship Diagram (ERD)**

_(An ERD should be included here, displaying entities such as Users, Books, Orders, Wishlist, Reviews, etc., along with their relationships.)_

### **6.2 Database Tables**

#### **Users**

- **Fields:**
  - UserID (PK, UUID)
  - Username (Unique)
  - Email (Unique)
  - PasswordHash
  - FirstName
  - LastName
  - ProfilePictureURL
  - CreatedAt
  - UpdatedAt

#### **Books**

- **Fields:**
  - BookID (PK, UUID)
  - Title
  - AuthorID (FK)
  - ISBN (Unique)
  - Description
  - Price
  - StockQuantity
  - CategoryID (FK)
  - CoverImageURL
  - AverageRating
  - CreatedAt
  - UpdatedAt

#### **Authors**

- **Fields:**
  - AuthorID (PK, UUID)
  - Name
  - Biography
  - CreatedAt
  - UpdatedAt

#### **Categories**

- **Fields:**
  - CategoryID (PK, UUID)
  - CategoryName
  - ParentCategoryID (FK, Nullable)
  - CreatedAt
  - UpdatedAt

#### **Orders**

- **Fields:**
  - OrderID (PK, UUID)
  - UserID (FK)
  - OrderDate
  - TotalAmount
  - PaymentStatus
  - ShippingAddressID (FK)
  - CreatedAt
  - UpdatedAt

#### **OrderItems**

- **Fields:**
  - OrderItemID (PK, UUID)
  - OrderID (FK)
  - BookID (FK)
  - Quantity
  - UnitPrice
  - CreatedAt
  - UpdatedAt

#### **Wishlists**

- **Fields:**
  - WishlistID (PK, UUID)
  - UserID (FK)
  - CreatedAt
  - UpdatedAt

#### **WishlistItems**

- **Fields:**
  - WishlistItemID (PK, UUID)
  - WishlistID (FK)
  - BookID (FK)
  - AddedAt

#### **Reviews**

- **Fields:**
  - ReviewID (PK, UUID)
  - BookID (FK)
  - UserID (FK)
  - Rating
  - ReviewText
  - ReviewDate
  - CreatedAt
  - UpdatedAt

#### **Addresses**

- **Fields:**
  - AddressID (PK, UUID)
  - UserID (FK)
  - AddressLine1
  - AddressLine2
  - City
  - State
  - ZipCode
  - Country
  - CreatedAt
  - UpdatedAt

## **7. Security Considerations**

### **7.1 Authentication and Authorization**

- **Use JWTs** for stateless authentication.
- **Role-Based Access Control (RBAC):** Differentiate access levels between users and administrators.
- **Secure Storage of Credentials:** Passwords are hashed using bcrypt with a salt.

### **7.2 Data Protection**

- **Encryption:** SSL/TLS for data in transit; sensitive data encrypted at rest.
- **Data Privacy:** Compliance with GDPR regulations.
- **Regular Audits:** Security audits and penetration testing to identify vulnerabilities.

### **7.3 Input Validation**

- Sanitize all user inputs to prevent SQL Injection, XSS, and other injection attacks.
- Use parameterized queries and prepared statements with ORM.

### **7.4 Session Management**

- Implement secure session cookies with HttpOnly and Secure flags.
- Monitor for session hijacking and implement session timeouts.

## **8. Performance Requirements**

- **PR-1:** The system shall support at least 10,000 concurrent users.
- **PR-2:** Average server response time shall be less than 500ms under normal load.
- **PR-3:** The system shall handle spike traffic with up to 20,000 requests per minute without significant performance degradation.
- **PR-4:** Database read and write operations shall complete within 200ms.

## **9. Error Handling and Logging**

- **EH-1:** Implement comprehensive logging for debugging and auditing purposes.
- **EH-2:** User-facing errors shall be presented in a user-friendly manner without exposing sensitive information.
- **EH-3:** Critical system errors shall trigger alerts to the development team via email or messaging systems.

## **10. Quality Attributes**

### **10.1 Scalability**

- Design the application to scale horizontally with additional servers.
- Use microservices architecture where appropriate.

### **10.2 Reliability and Availability**

- Aim for 99.9% uptime.
- Implement redundancy and failover mechanisms.

### **10.3 Maintainability**

- Modular codebase with clear separation of concerns.
- Use of coding standards and best practices.
- Comprehensive documentation and inline code comments.

### **10.4 Usability**

- Conduct usability testing with real users.
- Ensure the interface is intuitive and accessible.

### **10.5 Portability**

- Use containerization (e.g., Docker) to enable easy deployment across different environments.

## **11. Development and Testing**

### **11.1 Development Practices**

- **Agile Methodology:** Employ Scrum framework with sprints.
- **Version Control:** Use Git with a branching strategy (e.g., GitFlow).
- **Code Reviews:** Mandatory peer reviews before code is merged.

### **11.2 Testing Strategy**

- **Unit Testing:** Ensure individual components function correctly.
- **Integration Testing:** Test interactions between different components.
- **System Testing:** Validate the system as a whole against requirements.
- **Performance Testing:** Conduct load and stress testing.
- **Security Testing:** Perform vulnerability assessments and penetration testing.
- **Automated Testing:** Implement CI/CD pipelines with automated test suites.

## **12. Deployment and Maintenance**

### **12.1 Deployment Strategy**

- **Continuous Integration/Continuous Deployment (CI/CD):** Use tools like Jenkins or GitHub Actions.
- **Staging Environment:** Deploy to a staging environment before production.
- **Blue-Green Deployment:** To minimize downtime during releases.

### **12.2 Maintenance Plan**

- **Regular Updates:** Apply security patches and updates regularly.
- **Monitoring and Alerting:** Use tools like New Relic or AWS CloudWatch.
- **Customer Support:** Provide channels for users to report issues.

## **13. Future Enhancements**

- **Mobile Application Development:** Native apps for iOS and Android platforms.
- **Personalized Recommendations:** Use machine learning to suggest books to users.
- **Social Features:** Enable users to follow authors or other users.
- **Gift Cards and Coupons:** Implement support for promotions.

## **14. Appendices**

### **14.1 Glossary**

- **SKU:** Stock Keeping Unit, a unique identifier for each distinct product.
- **PCI DSS:** Payment Card Industry Data Security Standard.
- **GDPR:** General Data Protection Regulation.
- **JWT:** JSON Web Token.

### **14.2 References**

- Stripe API Documentation: [https://stripe.com/docs/api](https://stripe.com/docs/api)
- SendGrid API Documentation: [https://docs.sendgrid.com/](https://docs.sendgrid.com/)
- OWASP Security Guidelines: [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
- GDPR Compliance: [https://gdpr.eu/](https://gdpr.eu/)
