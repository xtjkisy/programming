import time
import sqlite3

class BankingSystem:
    def __init__(self):
        # Connect to the SQLite database
        self.connection = sqlite3.connect('/home/xtjkisy/ATM.db')
        self.cursor = self.connection.cursor()
        self.user_data_list = self.load_user_data()

    def load_user_data(self):
        try:
            self.cursor.execute("SELECT * FROM clients")
            rows = self.cursor.fetchall()

            user_data_list = []
            for row in rows:
                user_data_list.append({
                    'login': row[1],
                    'password': row[2],
                    'name': row[3],
                    'surname': row[4],
                    'age': row[5],
                    'balance': row[6]
                })

            return user_data_list
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return []

    def save_user_data(self):
        try:
            self.cursor.execute("DELETE FROM clients")  # Clear existing data
            for user_data in self.user_data_list:
                self.cursor.execute(
                    "INSERT INTO clients (login, password, name, surname, age, balance) VALUES (?, ?, ?, ?, ?, ?)",
                    (user_data['login'], user_data['password'], user_data['name'],
                     user_data['surname'], user_data['age'], user_data['balance'])
                )
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")

    def authenticate_user(self):
        attempts = 0
        while attempts < 3:
            try:
                login = self.input_taker('', 'Write your login: ')
                password = self.input_taker('', 'Write your password: ')

                for user_data in self.user_data_list:
                    if login == user_data.get('login') and password == user_data.get('password'):
                        self.current_user_data = user_data
                        return True
                print(f'Incorrect login or password. {2 - attempts} attempts remaining.')
                attempts += 1
            except ValueError:
                print("Invalid input. Please enter a valid value.")

        print("Your card will not be returned.")
        return False

    def input_taker(self, typ, text):
        while True:
            try:
                inp = input(text)
                if typ == 'int':
                    return int(inp)
                else:
                    return inp
            except ValueError:
                print("Invalid input. Please enter a valid value.")

    def action_picker(self):
        attempts = 0
        while attempts < 3:
            try:
                print('Choose action:\n 1- Check balance\n 2- Withdraw\n 3- Deposit\n 4- Transfer\n 5- Close')
                action = self.input_taker(typ='', text='>>> ')
                return action
            except ValueError:
                print("Invalid input. Please enter a valid action.")
                attempts += 1

        print("Your card will not be returned.")
        return None

    def transfer_money(self):
        try:
            recipient_login = self.input_taker('', 'Enter the recipient\'s login: ')

            # Check if the recipient exists in the user data list
            recipient_data = next((user for user in self.user_data_list if user['login'] == recipient_login), None)

            if recipient_data is None:
                print("Woosong Bank doesn't have a client with this login. Please check and try again.")
                return

            transfer_amount = self.input_taker('int', 'Enter the amount to transfer: ')

            if transfer_amount > self.current_user_data["balance"]:
                print("Not enough money in your account.")
            else:
                self.current_user_data["balance"] -= transfer_amount
                recipient_data["balance"] += transfer_amount
                print(f'Transfer successful! Your latest balance is {self.current_user_data["balance"]}')

            return self.func()

        except ValueError:
            print("Invalid input. Please enter a valid value.")

    def main(self):
        try:
            print('Insert your card')
            time.sleep(5)
            print('Card read Successfully!')
            time.sleep(3)
            print('Hello from Woosong Bank')

            # Load user data from file or create new data if the file doesn't exist
            self.user_data_list = self.load_user_data()
            if not self.user_data_list:
                print("No user data found. Exiting.")
                return

            # Authenticate the user
            if not self.authenticate_user():
                print("Authentication failed. Exiting.")
                return

            done = True
            while done:
                try:
                    action = self.action_picker()

                    if action == '1':
                        print(f'Hello, {self.current_user_data["login"]}, you have {self.current_user_data["balance"]}c in your balance')
                        time.sleep(3)
                        done = self.func()

                    elif action == '2':
                        print(f'Your latest balance is {self.current_user_data["balance"]}')
                        money2with = self.input_taker('int', 'Write amount: ')

                        if money2with > self.current_user_data["balance"]:
                            print("Not enough money in your card.")
                        else:
                            self.current_user_data["balance"] -= money2with
                            print(f'Your latest balance is {self.current_user_data["balance"]}')

                        done = self.func()

                    elif action == '3':
                        add = self.input_taker('int', 'Write amount: ')
                        self.current_user_data["balance"] += add
                        print(f'Your latest balance is {self.current_user_data["balance"]}')
                        done = self.func()

                    elif action == '4':
                        self.transfer_money()
                        done = self.func()

                    elif action == '5':
                        print("Good bye!")
                        return

                    else:
                        print("Invalid input. Please enter a valid action.")

                except ValueError:
                    print("Invalid input. Please enter a valid value.")

            # Save user data after finishing the transactions
            self.save_user_data()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def func(self):
        while True:
            try:
                ask = input('Do you want to continue? yes/no: ')
                time.sleep(2)
                if ask.lower() == 'yes':
                    return True
                elif ask.lower() == 'no':
                    print("Good bye!")
                    return False
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    return self.func()
            except ValueError:
                print("Invalid input. Please enter a valid value.")

    def __del__(self):
        # Close the SQLite connection when the object is deleted
        self.connection.close()

if __name__ == '__main__':
    banking_system = BankingSystem()
    banking_system.main()
