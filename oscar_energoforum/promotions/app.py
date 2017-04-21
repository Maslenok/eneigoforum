from oscar.apps.promotions.app import PromotionsApplication as CorePromotionApplication
from oscar_energoforum.promotions.views import HomeView
class PromotionsApplication(CorePromotionApplication):
    home_view = HomeView
application = PromotionsApplication()