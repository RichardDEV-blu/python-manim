from manim import *
import numpy as np


# ============================================================
# VERTICAL 9:16 — 1080p
# ============================================================

config.frame_height = 8.0
config.frame_width = 4.5

config.pixel_width = 1080
config.pixel_height = 1920

config.background_color = "#000000"
config.frame_rate = 60


# ============================================================
# COLORS
# ============================================================

COLOR_TEXT = "#F5F5F7"
COLOR_MUTED = "#8E95A8"
COLOR_GRID = "#2B2F3A"

COLOR_RUN = "#FFFFFF"
COLOR_WALK = "#F06A6A"
COLOR_SWIM = "#58C4DD"
COLOR_BENIGN = "#63D6A0"
COLOR_MALIGN = "#B57EF7"

COLOR_NUMBER = "#AAB0BF"
COLOR_BRACKET = "#555B70"


# ============================================================
# TYPOGRAPHY
# ============================================================

FONT = "Montserrat"


# ============================================================
# GLOBAL TIMING
# ============================================================

SPEED_FACTOR = 1.35

AMBIENT_ROTATION_RATE = 0.07 / SPEED_FACTOR


# ============================================================
# SAFE AREA
# ============================================================

SAFE_W = 3.90


# ============================================================
# POSITIONS
# ============================================================

CAPTION_Y = -2.58
EMBEDDING_Y = 0.10


# ============================================================
# SCENE
# ============================================================

class WordEmbeddingsVertical(ThreeDScene):

    def construct(self):

        self.camera.background_color = "#000000"

        # ====================================================
        # CAMERA
        # ====================================================

        self.set_camera_orientation(
            phi=68 * DEGREES,
            theta=-45 * DEGREES,
            distance=10
        )

        # ====================================================
        # HELPERS
        # ====================================================

        def fit_width(mobject, max_width=SAFE_W):

            if mobject.width > max_width:
                mobject.scale(
                    max_width / mobject.width
                )

            return mobject


        def make_text(
            text,
            font_size,
            color,
            weight=BOLD,
            max_width=None
        ):

            obj = Text(
                text,
                font=FONT,
                font_size=font_size,
                color=color,
                weight=weight
            )

            # IMPORTANT:
            # Preserve Manim's native character spacing.
            # Only scale the complete text if necessary.
            if max_width is not None:
                fit_width(
                    obj,
                    max_width
                )

            return obj


        def make_caption(
            line1_text,
            line2_text,
            color=COLOR_MUTED
        ):

            line1 = make_text(
                line1_text,
                15,
                color,
                BOLD,
                max_width=SAFE_W
            )

            line2 = make_text(
                line2_text,
                15,
                color,
                BOLD,
                max_width=SAFE_W
            )

            group = VGroup(
                line1,
                line2
            ).arrange(
                DOWN,
                buff=0.045
            )

            group.move_to(
                np.array([
                    0,
                    CAPTION_Y,
                    0
                ])
            )

            return group


        # ====================================================
        # HEADER — 2D OVERLAY
        # ====================================================

        title = make_text(
            "FROM WORDS TO VECTORS",
            25,
            COLOR_TEXT,
            BOLD,
            max_width=SAFE_W
        )

        subtitle = make_text(
            "WORDS AS NUMERICAL REPRESENTATIONS",
            10,
            COLOR_MUTED,
            BOLD,
            max_width=SAFE_W
        )

        header = VGroup(
            title,
            subtitle
        ).arrange(
            DOWN,
            buff=0.07
        )

        header.to_edge(
            UP,
            buff=0.25
        )

        # Keep header completely 2D.
        self.add_fixed_in_frame_mobjects(
            header
        )

        self.play(
            FadeIn(header),
            run_time=1.0 * SPEED_FACTOR
        )


        # ====================================================
        # WORD DATA
        # ====================================================

        words = [
            ("RUN", COLOR_RUN),
            ("WALK", COLOR_WALK),
            ("SWIM", COLOR_SWIM),
            ("BENIGN", COLOR_BENIGN),
            ("MALIGN", COLOR_MALIGN),
        ]


        # ====================================================
        # ILLUSTRATIVE EMBEDDINGS
        # ====================================================

        embeddings = [

            [
                0.42,
                -0.17,
                0.83,
                -0.31,
                0.56,
                0.21
            ],

            [
                0.37,
                -0.12,
                0.76,
                -0.28,
                0.61,
                0.19
            ],

            [
                -0.21,
                0.68,
                0.41,
                -0.73,
                0.34,
                0.82
            ],

            [
                -0.64,
                0.27,
                -0.18,
                0.71,
                0.43,
                -0.52
            ],

            [
                -0.71,
                0.42,
                -0.31,
                0.86,
                0.57,
                -0.68
            ]

        ]


        # ====================================================
        # EMBEDDING CARD — 2D OVERLAY
        # ====================================================

        card = RoundedRectangle(
            width=3.90,
            height=2.55,
            corner_radius=0.15,
            stroke_color=COLOR_GRID,
            stroke_width=1.5,
            fill_color="#08090D",
            fill_opacity=0.96
        )

        card.move_to(
            np.array([
                0,
                EMBEDDING_Y,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            card
        )

        self.play(
            FadeIn(card),
            run_time=0.8 * SPEED_FACTOR
        )


        # ====================================================
        # CURRENT WORD — 2D OVERLAY
        # ====================================================

        current_word = make_text(
            "RUN",
            30,
            COLOR_RUN,
            BOLD
        )

        current_word.move_to(
            np.array([
                0,
                1.02,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            current_word
        )


        # ====================================================
        # EMBEDDING LABEL — 2D OVERLAY
        # ====================================================

        embedding_label = make_text(
            "EMBEDDING",
            11,
            COLOR_MUTED,
            BOLD
        )

        embedding_label.move_to(
            np.array([
                0,
                0.56,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            embedding_label
        )


        # ====================================================
        # VALUE TRACKERS
        # ====================================================

        value_trackers = [
            ValueTracker(value)
            for value in embeddings[0]
        ]


        # ====================================================
        # EMBEDDING NUMBER POSITIONS
        # ====================================================

        number_x_positions = np.array([
            -1.43,
            -0.86,
            -0.29,
             0.29,
             0.86,
             1.43
        ])

        number_y = 0.00


        # ====================================================
        # NUMBER CREATOR — 2D OVERLAY
        # ====================================================

        def create_number(
            value,
            x
        ):

            number = Text(
                f"{value:+.2f}",
                font=FONT,
                font_size=11,
                color=COLOR_NUMBER,
                weight=BOLD
            )

            number.move_to(
                np.array([
                    x,
                    number_y,
                    0
                ])
            )

            return number


        # ====================================================
        # CURRENT EMBEDDING NUMBERS
        # ====================================================

        current_numbers = VGroup()

        for tracker, x in zip(
            value_trackers,
            number_x_positions
        ):

            number = create_number(
                tracker.get_value(),
                x
            )

            current_numbers.add(
                number
            )


        # ====================================================
        # NUMBER UPDATERS
        # ====================================================

        for number, tracker, x in zip(
            current_numbers,
            value_trackers,
            number_x_positions
        ):

            def update_number(
                mob,
                t=tracker,
                xpos=x
            ):

                updated = create_number(
                    t.get_value(),
                    xpos
                )

                mob.become(
                    updated
                )

            number.add_updater(
                update_number
            )


        self.add_fixed_in_frame_mobjects(
            current_numbers
        )


        # ====================================================
        # BRACKETS — 2D OVERLAY
        # ====================================================

        left_bracket = make_text(
            "[",
            20,
            COLOR_BRACKET,
            BOLD
        )

        right_bracket = make_text(
            "]",
            20,
            COLOR_BRACKET,
            BOLD
        )

        left_bracket.move_to(
            np.array([
                -1.70,
                number_y,
                0
            ])
        )

        right_bracket.move_to(
            np.array([
                1.70,
                number_y,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            left_bracket,
            right_bracket
        )


        # ====================================================
        # DIMENSION TEXT — 2D OVERLAY
        # ====================================================

        dimension_text = make_text(
            "6 shown · hundreds or thousands in reality",
            9,
            COLOR_MUTED,
            BOLD,
            max_width=3.30
        )

        dimension_text.move_to(
            np.array([
                0,
                -0.52,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            dimension_text
        )


        # ====================================================
        # INITIAL CAPTION — 2D OVERLAY
        # ====================================================

        caption = make_caption(
            "A word becomes a vector",
            "of numbers",
            COLOR_MUTED
        )

        self.add_fixed_in_frame_mobjects(
            caption
        )


        # ====================================================
        # INITIAL APPEARANCE
        # ====================================================

        self.play(
            FadeIn(current_word),
            FadeIn(embedding_label),
            FadeIn(left_bracket),
            FadeIn(right_bracket),
            FadeIn(current_numbers),
            FadeIn(dimension_text),
            FadeIn(caption),

            run_time=1.5 * SPEED_FACTOR
        )

        self.wait(
            1.4 * SPEED_FACTOR
        )


        # ====================================================
        # CHANGE EMBEDDING
        # ====================================================

        def change_embedding(
            index,
            line1,
            line2
        ):

            nonlocal current_word
            nonlocal caption

            # ------------------------------------------------
            # NEW WORD — 2D
            # ------------------------------------------------

            new_word = make_text(
                words[index][0],
                30,
                words[index][1],
                BOLD
            )

            new_word.move_to(
                current_word.get_center()
            )


            # ------------------------------------------------
            # NEW CAPTION — 2D
            # ------------------------------------------------

            new_caption = make_caption(
                line1,
                line2,
                words[index][1]
            )


            # ------------------------------------------------
            # REGISTER AS FIXED 2D OBJECTS
            # ------------------------------------------------

            self.add_fixed_in_frame_mobjects(
                new_word,
                new_caption
            )


            # ------------------------------------------------
            # CROSSFADE
            # ------------------------------------------------

            self.play(
                FadeOut(
                    current_word
                ),
                FadeOut(
                    caption
                ),
                FadeIn(
                    new_word
                ),
                FadeIn(
                    new_caption
                ),

                run_time=0.75 * SPEED_FACTOR
            )


            # ------------------------------------------------
            # REMOVE OLD OBJECTS
            # ------------------------------------------------

            self.remove(
                current_word,
                caption
            )

            current_word = new_word
            caption = new_caption


            # ------------------------------------------------
            # ANIMATE EMBEDDING VALUES
            # ------------------------------------------------

            self.play(
                *[
                    tracker.animate.set_value(target)
                    for tracker, target in zip(
                        value_trackers,
                        embeddings[index]
                    )
                ],
                run_time=1.45 * SPEED_FACTOR
            )

            self.wait(
                0.65 * SPEED_FACTOR
            )


        # ====================================================
        # RUN → WALK
        # ====================================================

        change_embedding(
            1,
            "WALK has a different",
            "numerical representation"
        )


        # ====================================================
        # WALK → SWIM
        # ====================================================

        change_embedding(
            2,
            "Change the token, and",
            "the vector changes"
        )


        # ====================================================
        # SWIM → BENIGN
        # ====================================================

        change_embedding(
            3,
            "BENIGN is represented",
            "in the same space"
        )


        # ====================================================
        # BENIGN → MALIGN
        # ====================================================

        change_embedding(
            4,
            "MALIGN becomes another",
            "point in that space"
        )


        # ====================================================
        # EMPHASIZE MALIGN
        # ====================================================

        self.play(
            current_word.animate.scale(
                1.10
            ),
            run_time=0.5 * SPEED_FACTOR
        )

        self.wait(
            0.7 * SPEED_FACTOR
        )


        # ====================================================
        # REMOVE 2D CONTENT
        # ====================================================

        self.play(
            FadeOut(header),
            FadeOut(embedding_label),
            FadeOut(left_bracket),
            FadeOut(right_bracket),
            FadeOut(current_numbers),
            FadeOut(dimension_text),
            FadeOut(card),
            FadeOut(caption),
            FadeOut(current_word),

            run_time=1.2 * SPEED_FACTOR
        )


        self.remove(
            header,
            embedding_label,
            left_bracket,
            right_bracket,
            current_numbers,
            dimension_text,
            card,
            caption,
            current_word
        )


        # ====================================================
        # 3D AXES
        # ====================================================

        axes = ThreeDAxes(
            x_range=[-2.2, 2.2, 1],
            y_range=[-2.2, 2.2, 1],
            z_range=[-2.2, 2.2, 1],

            x_length=3.5,
            y_length=3.5,
            z_length=3.5,

            axis_config={
                "stroke_color": "#555B70",
                "stroke_width": 1.2,
                "stroke_opacity": 0.6,
                "include_tip": False,
            }
        )

        axes.shift(
            np.array([
                0,
                -0.35,
                0
            ])
        )


        # ====================================================
        # MALIGN POINT
        # ====================================================

        origin = axes.c2p(
            0,
            0,
            0
        )

        malign_point = axes.c2p(
            -1.25,
            1.15,
            1.30
        )


        # ====================================================
        # VECTOR
        # ====================================================

        malign_vector = Arrow3D(
            start=origin,
            end=malign_point,
            color=COLOR_MALIGN,
            thickness=0.045,
            height=0.22,
            base_radius=0.065
        )


        # ====================================================
        # POINT
        # ====================================================

        malign_dot = Dot3D(
            point=malign_point,
            radius=0.075,
            color=COLOR_MALIGN
        )


        # ====================================================
        # FINAL TITLE — PURE 2D OVERLAY
        # ====================================================

        # IMPORTANT:
        # This is deliberately kept as a normal Text object.
        # It is NOT rotated, converted to 3D, or attached to
        # the 3D coordinate system.

        malign_label = Text(
            "MALIGN",
            font=FONT,
            font_size=22,
            weight=BOLD,
            color=COLOR_MALIGN
        )

        malign_label.move_to(
            np.array([
                0,
                3.45,
                0
            ])
        )

        # Fixed to the camera frame.
        # Therefore the 3D camera rotation cannot distort
        # the text geometry or its native character spacing.
        self.add_fixed_in_frame_mobjects(
            malign_label
        )


        # ====================================================
        # FINAL CAPTION — PURE 2D OVERLAY
        # ====================================================

        final_caption = Text(
            "We can visualize the embedding as a point in 3D",
            font=FONT,
            font_size=13,
            weight=BOLD,
            color=COLOR_MUTED
        )

        fit_width(
            final_caption,
            SAFE_W
        )

        final_caption.move_to(
            np.array([
                0,
                -3.05,
                0
            ])
        )

        self.add_fixed_in_frame_mobjects(
            final_caption
        )


        # ====================================================
        # CREATE 3D SPACE
        # ====================================================

        self.play(
            Create(axes),
            run_time=1.4 * SPEED_FACTOR
        )

        self.begin_ambient_camera_rotation(
            rate=AMBIENT_ROTATION_RATE
        )


        # ====================================================
        # REVEAL VECTOR
        # ====================================================

        self.play(
            GrowFromPoint(
                malign_vector,
                origin
            ),

            FadeIn(
                malign_dot,
                scale=0.3
            ),

            FadeIn(
                malign_label
            ),

            FadeIn(
                final_caption
            ),

            run_time=1.8 * SPEED_FACTOR
        )


        # ====================================================
        # FINAL RING
        # ====================================================

        self.wait(
            1.0 * SPEED_FACTOR
        )

        ring = Circle(
            radius=0.18,
            color=COLOR_MALIGN,
            stroke_width=3
        )

        ring.rotate(
            90 * DEGREES,
            axis=RIGHT
        )

        ring.move_to(
            malign_point
        )

        self.play(
            Create(ring),
            run_time=0.7 * SPEED_FACTOR
        )

        self.play(
            ring.animate
                .scale(1.8)
                .set_opacity(0),
            run_time=1.4 * SPEED_FACTOR
        )


        # ====================================================
        # END
        # ====================================================

        self.wait(
            2.8 * SPEED_FACTOR
        )

        self.stop_ambient_camera_rotation()

        # self.interactive_embed()