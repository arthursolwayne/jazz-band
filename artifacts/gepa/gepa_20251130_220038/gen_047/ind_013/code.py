
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # Eb

    # Bar 3: F7 (F, Ab, C, E)
    pretty_midi.Note(velocity=95, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.625),  # E

    # Bar 4: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),  # Eb

    # Bar 5: F7 (F, Ab, C, E)
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.125),  # E

    # Bar 6: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),  # Eb

    # Bar 7: F7 (F, Ab, C, E)
    pretty_midi.Note(velocity=95, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.625),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody with one short motif, leave it hanging, come back and finish it
# Motif: F (65), Gb (66), E (69), F (65), leave on E, then return to resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # E (hanging)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.375, end=2.5),  # Gb
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Add hi-hat on every eighth note for the entire duration
for i in range(0, 6, 0.375):
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.375)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
