from collections import defaultdict

def popular_creater(creators, ids, views):
    creator_views = defaultdict(int)
    creator_videos = defaultdict(list)
    
    for creator, video_id, view in zip(creators, ids, views):
        creator_views[creator] += view
        creator_videos[creator].append((view, video_id))
    
    max_views = max(creator_views.values())
    
    answer = [[creator, video_id] for creator in creator_views for views in creator_videos[creator] if sum(views) == max_views for view, video_id in views if view == max_views]
    
    return answer
