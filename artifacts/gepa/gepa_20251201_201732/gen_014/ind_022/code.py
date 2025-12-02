
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus): walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # D (chromatic)
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625),  # G (fifth)
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # A (chromatic)
]
bass.notes.extend(bass_notes)

# Piano (Diane): open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.0),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=2.0),  # Ab (E3)
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.0),  # C (G3)
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=2.0),  # D (A3)
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.5),  # Bb (E3)
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.5),  # D (G3)
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.5),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.5),  # Ab (E3)
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=3.0),  # Eb (F3)
    pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=3.0),  # G (G3)
    pretty_midi.Note(velocity=90, pitch=51, start=2.5, end=3.0),  # Bb (E3)
    pretty_midi.Note(velocity=90, pitch=57, start=2.5, end=3.0),  # D (A3)
]
piano.notes.extend(piano_notes)

# Sax (Dante): short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # A (E4)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # A (E4)
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Drums continue
# Bar 3 (3.0 - 4.5s)
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4 (4.5 - 6.0s)
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 2: Drums
# Bar 2 (1.5 - 3.0s) already covered in the first drum_notes section
# Bar 3 and 4 have been extended from the first bar

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
