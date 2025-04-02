defmodule App.AccountFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `App.Account` context.
  """

  @doc """
  Generate a unique pet_owner email.
  """
  def unique_pet_owner_email, do: "some email#{System.unique_integer([:positive])}"

  @doc """
  Generate a pet_owner.
  """
  def pet_owner_fixture(attrs \\ %{}) do
    {:ok, pet_owner} =
      attrs
      |> Enum.into(%{
        email: unique_pet_owner_email(),
        first_name: "some first_name",
        last_name: "some last_name"
      })
      |> App.Account.create_pet_owner()

    pet_owner
  end
end
