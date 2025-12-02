
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
# F7 = F, A, C, E
# Bass line in F7: F, G#, A, Bb, B, C#, D, Eb, E, F#, G, Ab, A, Bb, B, C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.625),    # F
    pretty_midi.Note(velocity=80, pitch=73, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),   # Bb

    pretty_midi.Note(velocity=80, pitch=72, start=2.0, end=2.125),   # B
    pretty_midi.Note(velocity=80, pitch=74, start=2.125, end=2.25),  # C#
    pretty_midi.Note(velocity=80, pitch=73, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=2.375, end=2.5),   # Eb

    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=2.625),   # E
    pretty_midi.Note(velocity=80, pitch=75, start=2.625, end=2.75),  # F#
    pretty_midi.Note(velocity=80, pitch=74, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.875, end=3.0),   # Ab

    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.125),   # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.5),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, E
# Comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2
    pretty_midi.Note(velocity=85, pitch=71, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=85, pitch=74, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=85, pitch=76, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=85, pitch=78, start=1.875, end=2.0),   # E

    # Bar 3: F7 on 2
    pretty_midi.Note(velocity=85, pitch=71, start=2.875, end=3.0),   # F
    pretty_midi.Note(velocity=85, pitch=74, start=2.875, end=3.0),   # A
    pretty_midi.Note(velocity=85, pitch=76, start=2.875, end=3.0),   # C
    pretty_midi.Note(velocity=85, pitch=78, start=2.875, end=3.0),   # E

    # Bar 4: F7 on 2
    pretty_midi.Note(velocity=85, pitch=71, start=3.875, end=4.0),   # F
    pretty_midi.Note(velocity=85, pitch=74, start=3.875, end=4.0),   # A
    pretty_midi.Note(velocity=85, pitch=76, start=3.875, end=4.0),   # C
    pretty_midi.Note(velocity=85, pitch=78, start=3.875, end=4.0),   # E
]
piano.notes.extend(piano_notes)

# Sax: Motif in F, one short phrase, leave it hanging, come back and finish
# F, Bb, C, F (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),   # F (hanging)
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    hihat = [
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.0, end=start_time + 0.1875),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.1875, end=start_time + 0.375),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.375, end=start_time + 0.5625),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.5625, end=start_time + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.75, end=start_time + 0.9375),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 0.9375, end=start_time + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.125, end=start_time + 1.3125),
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + 1.3125, end=start_time + 1.5)
    ]
    # Add all notes
    drums.notes.extend([kick1, kick3, snare2, snare4])
    drums.notes.extend(hihat)

# Add for bar 2 (1.5s)
add_drums(1.5)
# Add for bar 3 (2.5s)
add_drums(2.5)
# Add for bar 4 (3.5s)
add_drums(3.5)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
