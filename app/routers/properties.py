from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies import get_current_admin
from app.models.property import Property
from app.models.user import User
from app.schemas.property import (
    PropertyCreate,
    PropertyUpdate,
    PropertyResponse,
)


router = APIRouter(
    prefix="/properties",
    tags=["Properties"],
)


@router.post(
    "",
    response_model=PropertyResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_property(
    property_data: PropertyCreate,
    db: AsyncSession = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    new_property = Property(
        title=property_data.title,
        description=property_data.description,
        price=property_data.price,
        city=property_data.city,
        address=property_data.address,
        rooms=property_data.rooms,
        area=property_data.area,
        property_type=property_data.property_type,
        deal_type=property_data.deal_type,
        is_active=True,
    )

    db.add(new_property)

    await db.commit()
    await db.refresh(new_property)

    return new_property

@router.get(
    "",
    response_model=list[PropertyResponse],
)
async def get_properties(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Property).where(Property.is_active == True)
    )

    properties = result.scalars().all()

    return properties

@router.get(
    "/{property_id}",
    response_model=PropertyResponse,
)
async def get_property(
    property_id: int,
    db: AsyncSession = Depends(get_db),
):
    property_obj = await db.get(Property, property_id)

    if property_obj is None or not property_obj.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found",
        )

    return property_obj

@router.patch(
    "/{property_id}",
    response_model=PropertyResponse,
)
async def update_property(
    property_id: int,
    property_data: PropertyUpdate,
    db: AsyncSession = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    property_obj = await db.get(Property, property_id)

    if property_obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found",
        )

    update_data = property_data.model_dump(
        exclude_unset=True
    )

    for field, value in update_data.items():
        setattr(property_obj, field, value)

    await db.commit()
    await db.refresh(property_obj)

    return property_obj

@router.delete(
    "/{property_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_property(
    property_id: int,
    db: AsyncSession = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    property_obj = await db.get(Property, property_id)

    if property_obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Property not found",
        )

    property_obj.is_active = False

    await db.commit()