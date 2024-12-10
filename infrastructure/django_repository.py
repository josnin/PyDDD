from domain.repositories import ProductCatalogRepository
from product_catalog import models as django_models
from domain import models

class DjangoProductRepository(ProductCatalogRepository):

    def get(self, entity_id) -> models.ProductCatalog:
        from_django_product = django_models.ProductCatalog.objects.get(id=entity_id)
        from_django_variant_items = django_models.VariantItem.objects.filter(product_id=entity_id)

        product_catalog = models.ProductCatalog(
            entity_id=from_django_product.id,
            name=from_django_product.name,
            description=from_django_product.description,
            status=from_django_product.status
            )

        for item in from_django_variant_items:
            product_catalog.add_variant(
                models.VariantItem(
                    item.id, 
                    item.option, 
                    item.value,
                    item.price,
                    item.stock
                )
            )

        return product_catalog