
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # F (D2, 38)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # G (E2, 41) - chromatic approach to F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    # C (F2, 43)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    # E (D#2, 40) - chromatic approach to F
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F-A-C-E) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Bbmaj7 (Bb-D-F-A) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # A
]
piano.notes.extend(piano_notes)

# Bar 4: D7 (D-F#-A-C) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=6.0),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Dante: Your motif (1.5 - 3.0s)
# Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=68, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Same pattern repeated with slight variation in timing
for i in range(2):
    for note in drum_notes:
        note.start += 1.5 + (i * 1.5)
        note.end += 1.5 + (i * 1.5)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
