defmodule App.AccountTest do
  use App.DataCase

  alias App.Account

  describe "pet_owners" do
    alias App.Account.PetOwner

    import App.AccountFixtures

    @invalid_attrs %{first_name: nil, last_name: nil, email: nil}

    test "list_pet_owners/0 returns all pet_owners" do
      pet_owner = pet_owner_fixture()
      assert Account.list_pet_owners() == [pet_owner]
    end

    test "get_pet_owner!/1 returns the pet_owner with given id" do
      pet_owner = pet_owner_fixture()
      assert Account.get_pet_owner!(pet_owner.id) == pet_owner
    end

    test "create_pet_owner/1 with valid data creates a pet_owner" do
      valid_attrs = %{first_name: "some first_name", last_name: "some last_name", email: "some email"}

      assert {:ok, %PetOwner{} = pet_owner} = Account.create_pet_owner(valid_attrs)
      assert pet_owner.first_name == "some first_name"
      assert pet_owner.last_name == "some last_name"
      assert pet_owner.email == "some email"
    end

    test "create_pet_owner/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Account.create_pet_owner(@invalid_attrs)
    end

    test "update_pet_owner/2 with valid data updates the pet_owner" do
      pet_owner = pet_owner_fixture()
      update_attrs = %{first_name: "some updated first_name", last_name: "some updated last_name", email: "some updated email"}

      assert {:ok, %PetOwner{} = pet_owner} = Account.update_pet_owner(pet_owner, update_attrs)
      assert pet_owner.first_name == "some updated first_name"
      assert pet_owner.last_name == "some updated last_name"
      assert pet_owner.email == "some updated email"
    end

    test "update_pet_owner/2 with invalid data returns error changeset" do
      pet_owner = pet_owner_fixture()
      assert {:error, %Ecto.Changeset{}} = Account.update_pet_owner(pet_owner, @invalid_attrs)
      assert pet_owner == Account.get_pet_owner!(pet_owner.id)
    end

    test "delete_pet_owner/1 deletes the pet_owner" do
      pet_owner = pet_owner_fixture()
      assert {:ok, %PetOwner{}} = Account.delete_pet_owner(pet_owner)
      assert_raise Ecto.NoResultsError, fn -> Account.get_pet_owner!(pet_owner.id) end
    end

    test "change_pet_owner/1 returns a pet_owner changeset" do
      pet_owner = pet_owner_fixture()
      assert %Ecto.Changeset{} = Account.change_pet_owner(pet_owner)
    end
  end
end
