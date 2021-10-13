from payment_card import PaymentCard

def main():
    #write your code below this line
    paul = PaymentCard(20)
    matt = PaymentCard(30)

    paul.eat_heartily()
    matt.eat_affordably()

    print("Paul: " + str(paul))
    print("Matt: " + str(matt))

    paul.eat_affordably()
    paul.eat_affordably()
    matt.add_money(50)

    print("Paul: " + str(paul))
    print("Matt: " + str(matt))

if __name__ == '__main__':
    main()
