
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # Hihat fill
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat fill
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Hihat fill
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line (F, C, G, D) with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=73, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano chords (Fmaj7, Bb7, Dm7, G7)
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax melody (F, G, Ab, Bb) - one short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=77, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=78, start=1.875, end=2.0625), # Ab
    pretty_midi.Note(velocity=100, pitch=79, start=2.0625, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=100, pitch=77, start=2.8125, end=3.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add some fills in bar 2
# Snare fill
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.0625, end=2.25),
]
for note in drum_notes:
    drums.notes.append(note)

# Hi-hat fill
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
