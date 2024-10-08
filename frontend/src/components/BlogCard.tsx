import { Card, CardBody, CardFooter } from '@chakra-ui/card';
import { Image, Stack, Heading, ButtonGroup, Button, LinkOverlay, Box } from '@chakra-ui/react';

import { ArticleResponseT } from '../types';

interface GridPostItemProps {
    post: ArticleResponseT;
    isLoggedIn: boolean;
    onDelete: (id: number) => void;
}

export const BlogCard = ({ post, isLoggedIn, onDelete }: GridPostItemProps) => {
    const { id, color, title, thumbnail } = post;

    const controls = () => (
        <CardFooter>
            <ButtonGroup spacing="2">
                {/* Here we use link to deletePost function from the parent component with onDelete link */}
                <Button variant="solid" colorScheme="blue" onClick={() => onDelete(post.id)}>
                    Delete
                </Button>
            </ButtonGroup>
        </CardFooter>
    );

    return (
        <Card maxW="sm">
            <CardBody>
                <Box id="thumbnail" style={{ backgroundColor: color }}>
                    <Image src={thumbnail} alt={title} borderRadius="lg" />
                </Box>
                <Stack mt="6" spacing="3">
                    <LinkOverlay href={`posts/${id}`} style={{ color: 'inherit' }}>
                        <Heading size="md">{title}</Heading>
                    </LinkOverlay>
                </Stack>
            </CardBody>

            {isLoggedIn ? controls() : ''}
        </Card>
    );
};
