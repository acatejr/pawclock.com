defmodule App.Repo.Migrations.Initial do
  use Ecto.Migration

  def change do
    create table(:owners) do
      add :first_name, :string
      add :last_name, :string
      add :email, :string
      timestamps(type: :utc_datetime)
    end

    create table(:pets) do
      add :name, :string
      timestamps(type: :utc_datetime)
    end

    create table(:owners_pets, primary_key: false) do
      add :owner_id, references(:owners, on_delete: :delete_all), null: false
      add :pet_id, references(:pets, on_delete: :delete_all), null: false
    end

    create unique_index(:owners_pets, [:owner_id, :pet_id])

  end
end

# defmodule App.Repo.Migrations.CreatePets do
#   use Ecto.Migration

#   def change do
#     create table(:pets) do
#       add :name, :string

#       timestamps(type: :utc_datetime)
#     end
#   end
# end

# defmodule App.Repo.Migrations.CreateOwners do
#   use Ecto.Migration

#   def change do
#     create table(:owners) do
#       add :first_name, :string
#       add :last_name, :string
#       add :email, :string

#       timestamps(type: :utc_datetime)
#     end

#     create unique_index(:owners, [:email])
#   end
# end

# defmodule App.Repo.Migrations.CreateOwnersPetsJoinTable do
#   use Ecto.Migration

#   def change do
#     create table(:owners_pets) do
#       add :owner_id, references(:owners, on_delete: :delete_all)
#       add :pet_id, references(:pets, on_delete: :delete_all)
#       # timestamps()
#     end

#     # Add unique index to prevent duplicate associations
#     create unique_index(:owners_pets, [:owner_id, :pet_id])

#   end
# end
