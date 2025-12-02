
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle dynamics, space, and rhythmic variation
drum_notes = [
    pretty_midi.Note(velocity=60, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif (bars 2-4)
# Start with a motive, leave it hanging, return to finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Bass line (bars 2-4)
# Chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=35, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=37, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=40, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=41, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=39, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=37, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=34, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=35, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=39, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=41, start=5.5, end=5.75),  # B
    pretty_midi.Note(velocity=90, pitch=40, start=5.75, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano (bars 2-4)
# 7th chords, comp on 2 and 4, with emotion
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),

    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.5),  # E7 (E, G#, B, D)
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=77, start=2.25, end=2.5),

    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # A7 (A, C#, E, G)
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.25),

    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.0),  # E7 again
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=4.0),

    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # A7 again
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.75),

    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.5),  # E7 one more time
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=77, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Use dynamic variation and space to create tension
drum_notes = []
for bar in range(2, 5):
    bar_start = bar * 1.5
    bar_end = bar_start + 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=70, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=70, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare2 = pretty_midi.Note(velocity=90, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    # Add with dynamic variation on some hits
    if bar == 2:
        kick1.velocity = 65
        snare1.velocity = 85
        hihat2.velocity = 75
    elif bar == 3:
        kick2.velocity = 75
        hihat4.velocity = 85
    elif bar == 4:
        snare2.velocity = 95
        hihat1.velocity = 70
    drum_notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
