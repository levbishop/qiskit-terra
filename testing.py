import warnings
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

logger.info("hello")
logger.warning(warnings.formatwarning("goodbye", PendingDeprecationWarning, __file__, 9))
print(f"hhh {warnings.formatwarning('goodbye', PendingDeprecationWarning, __file__, 1)} hhh")

logging.captureWarnings(True)
with warnings.catch_warnings(record=True) as ww:
    warnings.filterwarnings('ignore')
    warnings.warn("wow")
print(f"xxx {ww} xxx")
warnings.filterwarnings('once')
for x in range(3):
    warnings.warn(f"oop{x}", PendingDeprecationWarning)

warnings.filterwarnings('always')
for x in range(3):
    warnings.warn(f"oop2-{x%2}", PendingDeprecationWarning)
