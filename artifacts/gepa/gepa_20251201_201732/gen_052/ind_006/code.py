
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Bass: D2 (MIDI 38), F2 (MIDI 41), A2 (MIDI 45), C3 (MIDI 48)
# Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F2 on 2
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # A2 on 3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 (D, F, A, C) open voicing, resolve on 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D3
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=1.875),  # A3
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # C4
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # D3
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.25), # F3
    pretty_midi.Note(velocity=100, pitch=56, start=1.875, end=2.25), # A3
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.25), # C4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # D3
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625), # F#3
    pretty_midi.Note(velocity=100, pitch=56, start=2.25, end=2.625), # A3
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # C4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D3
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),  # F3
    pretty_midi.Note(velocity=100, pitch=56, start=2.625, end=3.0),  # A3
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # C4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dm melody, one short motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),   # E4
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=1.875), # D4
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # E4
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),   # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # E4
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=2.75), # D4
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),   # E4
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 2) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
