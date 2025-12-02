
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble
# Sax motif (Fm7 - Ab - G - Eb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.0),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus's walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.125),  # Gb
    pretty_midi.Note(velocity=90, pitch=45, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=2.375, end=2.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane's piano comping on 2 and 4 (F7 chords: F, A, C, Eb)
piano_notes = [
    # Bar 2 - 2nd beat (beat 2.0)
    pretty_midi.Note(velocity=95, pitch=53, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=95, pitch=57, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=95, pitch=50, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=95, pitch=51, start=2.0, end=2.125),  # Eb
    # Bar 3 - 2nd beat (beat 3.5)
    pretty_midi.Note(velocity=95, pitch=53, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=95, pitch=57, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=95, pitch=50, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=95, pitch=51, start=3.5, end=3.625),  # Eb
    # Bar 4 - 2nd beat (beat 5.0)
    pretty_midi.Note(velocity=95, pitch=53, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=95, pitch=57, start=5.0, end=5.125),  # C
    pretty_midi.Note(velocity=95, pitch=50, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=95, pitch=51, start=5.0, end=5.125),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full ensemble
# Sax motif (Fm7 - Ab - G - Eb) again for continuity
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=2.875, end=3.0),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus's walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.125),  # Gb
    pretty_midi.Note(velocity=90, pitch=45, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=3.25, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane's piano comping on 2 and 4 (F7 chords: F, A, C, Eb)
piano_notes = [
    # Bar 3 - 2nd beat (beat 3.5)
    pretty_midi.Note(velocity=95, pitch=53, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=95, pitch=57, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=95, pitch=50, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=95, pitch=51, start=3.5, end=3.625),  # Eb
    # Bar 4 - 2nd beat (beat 5.0)
    pretty_midi.Note(velocity=95, pitch=53, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=95, pitch=57, start=5.0, end=5.125),  # C
    pretty_midi.Note(velocity=95, pitch=50, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=95, pitch=51, start=5.0, end=5.125),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full ensemble
# Sax motif (Fm7 - Ab - G - Eb) again for continuity
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.625, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=3.875, end=4.0),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Marcus's walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=4.0, end=4.125),  # Gb
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.25),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=4.25, end=4.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=4.375, end=4.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane's piano comping on 2 and 4 (F7 chords: F, A, C, Eb)
piano_notes = [
    # Bar 4 - 2nd beat (beat 5.0)
    pretty_midi.Note(velocity=95, pitch=53, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=95, pitch=57, start=5.0, end=5.125),  # C
    pretty_midi.Note(velocity=95, pitch=50, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=95, pitch=51, start=5.0, end=5.125),  # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
