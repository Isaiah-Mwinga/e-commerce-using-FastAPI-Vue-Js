from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Computing(Base):
    __tablename__ = "computings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id, ondelete='CASCADE"))
    category = relationship("Category", back_populates="Computing")

    def __repr__(self):
        return f"Computing(id={self.id}, name={self.name}, category_id={self.category_id})"

        class Laptops(Computing):
            __tablename__ = "laptops"
            id = Column(Integer, ForeignKey("computings.id"), primary_key=True)
            brand = Column(String, index=True)
            model = Column(String, index=True)
            price = Column(Integer, index=True)
            quantity = Column(Integer, index=True)
            description = Column(String, index=True)

            def __repr__(self):
                return f"Laptops(id={self.id}, name={self.name}, category_id={self.category_id}, brand={self.brand}, model={self.model}, price={self.price}, quantity={self.quantity}, description={self.description})"

