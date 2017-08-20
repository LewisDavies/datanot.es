Title: Create A Sample Database On A Mac
Slug: sql/create-a-sample-database-on-a-mac
Category: SQL
Tags: CREATE, DATABASE, psql, pg_restore
Date: 2017-08-11
Modified: 2017-08-11

#### Download Postgres.app
[Postgres.app](https://postgresapp.com/) makes it simple to set up a PostgreSQL database on a Mac. Simply download it, add it to your Applications, then run it.

#### Add command line tools to your PATH
We need to run a few commands to set up our sample database. (The docs have full details)[https://postgresapp.com/documentation/cli-tools.html], but here's how to add the relevant directory to your `$PATH`.

Open up a new terminal — you should be in your home directory — and type `nano .bash_profile`. Add the following lines at the end of your profile:

`PATH="$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin"
export PATH`

Save and exit (Ctrl-O and Ctrl-X), then run `source .bash_profile`.

#### Download the sample database files
For the next couple of steps, I used the guide from [postgresqltutorial.com](http://www.postgresqltutorial.com/postgresql-sample-database/). Download the sample database from the linked page. Extract the data and `dvdrental.tar` should apppear in the same directory.

#### Create a new database and load sample data
Head back to your terminal and run `psql`. To create our sample database, run `CREATE DATABASE dvdrental;` in this window. Next, load the sample data with `pg_restore -U postgres -d dvdrental /path/to/your/files/dvdrental.tar`.

#### Connect to the database
This part is optional, but you'll probably want to take a peek at your data once it's loaded and a client program will make this easy. I'd recommend trying [Postico](https://eggerapps.at/postico/), which is made by the same people who make Postgres.app. It's got a great, minimal interface and is easy to use. You're now ready to make your own tutorials!
