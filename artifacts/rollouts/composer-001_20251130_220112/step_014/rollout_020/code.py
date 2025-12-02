
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # Gb (chromatic)
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # G (3rd)
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),   # A (5th)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),   # Bb (7th)
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # B (chromatic)
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # C (octave)
    pretty_midi.Note(velocity=90, pitch=54, start=4.125, end=4.5),   # C# (chromatic)
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),   # B (chromatic)
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),  # Bb (7th)
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # B (chromatic)
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),   # A (5th)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.25),  # E
    # Bar 3: Bbm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # G
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=53, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif — F, Ab, Bb, G — played on beat 1 of bar 2, then left hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),   # G
    # Repeat the first two notes at the end to finish it
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),   # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
