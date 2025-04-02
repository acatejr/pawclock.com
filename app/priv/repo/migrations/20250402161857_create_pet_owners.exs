defmodule App.Repo.Migrations.CreatePetOwners do
  use Ecto.Migration

  def change do
    create table(:pet_owners) do
      add :first_name, :string
      add :last_name, :string
      add :email, :string

      timestamps(type: :utc_datetime)
    end

    create unique_index(:pet_owners, [:email])
  end
end
