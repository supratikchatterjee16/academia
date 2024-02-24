# Database Security

Databases often store confidential and personal information, so it needs to be secured.

First level is with logins. 2 ways of doing so is SSO based and Basic Login based.

Second level is through GRANTs, REVOKEs, and DENYs. This can be done over a group or at the user level.

Third level is by creating views to deny access to columns.

Fourth level is by encrypting data stored. It can be done via a DBMS or External cryptographic resoures.

Points to consider :
1. Level of risk
2. Usage pattern
3. Sensitivity of data
4. Encryption handling
5. Encryption options

Triggers can be used for DBMS based encryptions.