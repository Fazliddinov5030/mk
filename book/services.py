from django.conf import settings
from django.db.models import Q
from courses.models import Course

try:
    from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
    POSTGRES_SEARCH_AVAILABLE = True
except ImportError:
    POSTGRES_SEARCH_AVAILABLE = False


class SearchEngine:
    @staticmethod
    def full_text_search(query_string):
        """Return search results using the best available backend."""
        db_engine = settings.DATABASES.get('default', {}).get('ENGINE', '')
        use_postgres = POSTGRES_SEARCH_AVAILABLE and 'postgresql' in db_engine

        if use_postgres:
            search_vector = SearchVector('title', weight='A') + SearchVector('description', weight='B')
            search_query = SearchQuery(query_string)
            return Course.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).select_related('instructor').order_by('-rank')

        return Course.objects.filter(
            Q(title__icontains=query_string) | Q(description__icontains=query_string)
        ).select_related('instructor').order_by('-title__icontains', 'title')