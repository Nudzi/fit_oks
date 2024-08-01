# fit_oks

U ovom projektu se nalazi 10 testnih file-ova.

Testovi se pokrecu komandom: `pytest`, u terminalu.

10 testova:
- **testiranje admin stranice (test_admin_page):** ciscenje podataka u bazi, mijenjanje ukupne sume novca koji novi registrovani clan moze da ima na racunu. Provjerva da li se stara suma novca (1000$) kod novog korisnika aplikacije i nova suma novca (2000$) kod drugog novog korisnika aplikacije, razlikuju.
- **testiranje stranice za placanje racuna (test_bill_pay):** da li novi korisnik moze da izvrsi placanje duga sa svog racuna, i provjeravanje stanja racuna umanjenog za vrijednost placenog duga.
- **testiranje prebacivanja vrijednosti sa jednog racuna na drugi (test_correct_login_and_transfer_funds):** da li korisnik banke kada otvori novi racun u web aplikaciji, moze da prebaci sredstva sa osnovnog racuna na novootvoreni racun.
- **testiranje ispravnog logina (test_correct_login):** da li se korisnik banke moze logovat na web aplikaciju.
- **testiranje korisncke sluzbe (test_customer_care):** da li korisnik moze da posalje zahtjev korisniskom servisu.
- **testiranje zaboravljenih podataka (test_forgot_login_info):** da li korisnik moze da pristupi web stranici ako je zaboravio korisnicko ime i sifru.
- **testiranje unosa losih podatka za login (test_incorrect_login):** da li korisnik moze da pristupi web stranici ako je pogresan unos korisnickog imena i sifru.
- **testiranje novog korisnika (test_register):** da li je moguce da se registruje na web stranicu.
- **testiranje uzimanja kredita (test_request_loan):** da li korisnik moze da digne kredit na svom racunu i provjeri stanja racuna odobrenog kredita.
- **testiranje korisnickih podataka (test_update_contact_info):** da li korisnik web aplikacije moze da promijeni svoje podatke.
