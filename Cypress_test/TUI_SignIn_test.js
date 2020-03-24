// / <reference types = "Cypress"./>

describe('TUI Sign In test', () => {
    beforeEach(() => {
        cy.visit("https://www.tui.pl/mytui/logowanie");
      });
      
    it('Submit empty form test', () => {
        cy.get('#email')
            .clear()
            .should('be.empty');

        cy.get('#pass')
            .clear()
            .should('be.empty');

        cy.get('button[type="submit"]').click();

        cy.get ('form-message')
            .contains("Wpisz poprawny adres e-mail.")
            .should('be.visible');

        cy.get ('form-message')
            .contains("Wpisz hasło.")
            .should('be.visible');
    });

    it('Submit empty password', () => {
        cy.get('#email')
            .clear()
            .type('agnieszka@gmail.com');

        cy.get('#pass')
            .clear()
            .should('be.empty');

        cy.get('button[type="submit"]').click();

        cy.get ('form-message')
            .contains("Wpisz hasło.")
            .should('be.visible');
    });

});