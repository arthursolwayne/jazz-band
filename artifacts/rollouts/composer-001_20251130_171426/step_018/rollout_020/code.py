
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
drum_note_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_note_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75)
drum_note_3 = pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75)
drum_note_4 = pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125)
drum_note_5 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4, drum_note_5])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # D (F7)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # D (F7)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # D (F7)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),   # Hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),   # Hihat on 3-4

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),   # Hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),   # Hihat on 3-4

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),   # Hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),   # Hihat on 3-4
]
drums.notes.extend(drum_notes)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # C

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # C

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
