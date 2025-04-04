defmodule App.Repo.Migrations.CreateOwners do
  use Ecto.Migration

  def change do
    create table(:owners) do
      add :first_name, :string
      add :last_name, :string
      add :email, :string

      timestamps(type: :utc_datetime)
    end

    create unique_index(:owners, [:email])
  end
end
