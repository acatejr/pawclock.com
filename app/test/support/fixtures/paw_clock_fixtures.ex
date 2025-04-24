defmodule App.PawClockFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `App.PawClock` context.
  """

  @doc """
  Generate a pet.
  """
  def pet_fixture(attrs \\ %{}) do
    {:ok, pet} =
      attrs
      |> Enum.into(%{
        name: "some name",
        pet_type: :cat
      })
      |> App.PawClock.create_pet()

    pet
  end

  @doc """
  Generate a owner.
  """
  def owner_fixture(attrs \\ %{}) do
    {:ok, owner} =
      attrs
      |> Enum.into(%{
        first_name: "some first_name",
        last_name: "some last_name",
        phone: "some phone"
      })
      |> App.PawClock.create_owner()

    owner
  end
end
