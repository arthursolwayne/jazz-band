
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (D2) -> F2 (F2) -> A2 (A2) -> C3 (C3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),   # C3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: F7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Am7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),  # G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm (D, F, G, D)
# Bar 2 (1.5 - 2.25): D, F, G
# Bar 3 (2.25 - 3.0): D
# Bar 4 (3.0 - 3.75): D, F, G, D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.65),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.65, end=1.8),   # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.8, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=3.0),  # D (held)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.15),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.15, end=3.3),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.3, end=3.45),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.45, end=3.75), # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_shorter_intro.mid")
